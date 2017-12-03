from tachyonic.netrino_api.functions import *
from tachyonic.netrino_api.netrino_celery import *
import warnings
import re
import napalm
from easysnmp import Session
from pyipcalc import *
from datetime import datetime

warnings.simplefilter("ignore", DeprecationWarning)


@app.task
def confDevice(host, user, snippet=None, srid=None, activate=False, deactivate=False):
    db = Mysql(host=mysql.get('host'),
               database=mysql.get('database'),
               username=mysql.get('username'),
               password=mysql.get('password'))
    if snippet and srid:
        filename = "/tmp/" + srid + ".conf"
        f = open(filename, "w")
        f.write(snippet)
        f.close()
    sql = 'SELECT os FROM device where id=%s'
    result = db.execute(sql, (ip_to_int(host),))
    if len(result) > 0:
        os = result[0]['os'].lower()
        if os == 'ios' and not re.search(r'\nend$', snippet):
            f = open(filename, "a")
            f.write('\nend')
            f.close()
        driver = napalm.get_network_driver(os)
        private_key = str("%s/%s.key" % (ssh_key_loc, user))
        device = driver(hostname=host, username=user, password='', optional_args={
            "allow_agent": True, "key_file": private_key})
        now = datetime.strftime(datetime.now(), '%Y-%d-%m %H:%M')
        try:
            device.open()
            device.load_merge_candidate(filename=filename)
            device.commit_config()
            if srid:
                sql = 'UPDATE service_requests SET status='
                if activate:
                    sql += '"ACTIVE"'
                    sql += ',result=CONCAT(IFNULL(result,""),%s)'
                    vals = ['\n\n--\n' + now + '\n' + snippet]
                elif deactivate:
                    sql += '"INACTIVE"'
                    sql += ',result=CONCAT(IFNULL(result,""),%s)'
                    vals = ['\n\n--\n' + now + '\n' + snippet]
                else:
                    sql += '"SUCCESS"'
                    vals = [[now + '\nService Request deployed']]
                vals.append(srid)
                sql += ' WHERE id=%s'
                db.execute(sql, tuple(vals))
                db.commit()
        except Exception as e:
            print(str(e))
            if srid:
                sql = 'UPDATE service_requests SET result=CONCAT(IFNULL(result,""),%s),status="UNKNOWN" where id=%s'
                db.execute(sql, ('\n\n--\n' + now + '\n' + str(e), srid))
                db.commit()
        device.close()
    else:
        if srid:
            now = datetime.strftime(datetime.now(), '%Y-%d-%m %H:%M')
            sql = 'UPDATE service_requests SET result=CONCAT(IFNULL(result,""),%s),status="FAILED" where id=%s'
            db.execute(sql, ('\n\n--\n' + now + '\n' + 'UNKNOWN DEVICE', srid))
            db.commit()
        return "Unknown Device"


@app.task
def addDevice(host, user, srid=None, community=None):
    db = Mysql(host=mysql.get('host'),
               database=mysql.get('database'),
               username=mysql.get('username'),
               password=mysql.get('password'))
    intIP = ip_to_int(host)
    session = Session(hostname=host, community=community, version=2)
    now = datetime.strftime(datetime.now(), '%Y-%d-%m %H:%M')
    try:
        # getting system.sysDescr.0
        sysdescription = session.get('1.3.6.1.2.1.1.1.0')
    except Exception as e:
        print(str(e))
        if srid:
            sql = 'UPDATE service_requests SET result="%s",status="UNKNOWN" where id=%s'
            db.execute(sql, (now + '\n' + str(e), srid))
            db.commit()
        sys.exit(0)

    isCisco = re.match(
        'Cisco ([^,]+) Software.*Version ([^,]+)', sysdescription.value)

    if isCisco:
        vendor = "Cisco"
        os = isCisco.group(1)
        os_ver = isCisco.group(2)
    else:
        isJunOS = re.search('JUNOS ([^ ]+)', sysdescription.value)
        if isJunOS:
            vendor = "Juniper"
            os = "Junos"
            os_ver = isJunOS.group(1)
        else:
            vendor = "Unkown"
            os = ""
            os_ver = ""

    hostnamereq = session.get('.1.3.6.1.2.1.1.5.0')
    hostname = hostnamereq.value

    sql = 'INSERT INTO device (id, snmp_comm, name, vendor, os, os_ver) VALUES (%s, %s, %s, %s, %s, %s)'
    sql += ' ON DUPLICATE KEY UPDATE'
    sql += ' snmp_comm=%s,'
    sql += ' name=%s,'
    sql += ' vendor=%s,'
    sql += ' os=%s,'
    sql += ' os_ver=%s,'
    sql += ' last_discover=%s'
    result = db.execute(sql, (intIP, community, hostname, vendor, os, os_ver,
                              community, hostname, vendor, os, os_ver, now))
    db.commit()

    if os:
        driver = napalm.get_network_driver(os)
        private_key = "%s/%s.key" % (ssh_key_loc, user)
        device = driver(hostname=host, username=user, password='', optional_args={
            "allow_agent": True, "key_file": private_key})
        try:
            device.open()
        except Exception as e:
            print(str(e))
            return ("Unable to connect to " + host)
        try:
            portresult = device.get_interfaces()
            if portresult:
                db.execute(
                    'UPDATE device_port SET present=0,alias=%s,prefix_len=%s where id="%s"', (None, None, intIP))
                db.commit()
            for port in portresult:
                sql = 'INSERT INTO device_port (id,port,descr,mac,present,igroup) VALUES (%s,%s,%s,%s,%s,NULL)'
                sql += ' ON DUPLICATE KEY UPDATE'
                sql += ' id=VALUES(id),'
                sql += ' port=VALUES(port),'
                sql += ' descr=VALUES(descr),'
                sql += ' mac=VALUES(mac),'
                sql += ' present=1'
                result = db.execute(sql, (intIP, port, portresult[port][
                    'description'], portresult[port]['mac_address'], True))
                db.commit()
        except Exception as e:
            print(str(e))
        try:
            ipresult = device.get_interfaces_ip()
            for port in ipresult:
                sql = 'INSERT INTO device_port (id,port,alias,prefix_len) VALUES (%s,%s,%s,%s)'
                sql += ' ON DUPLICATE KEY UPDATE'
                sql += ' id=VALUES(id),'
                sql += ' port=VALUES(port),'
                sql += ' alias=VALUES(alias),'
                sql += ' prefix_len=VALUES(prefix_len)'
                ips = ipresult[port]['ipv4']
                for ip in ips:
                    pl = ipresult[port]['ipv4'][ip]['prefix_length']
                    iprefix = '/' + str(pl)
                    result = db.execute(sql, (intIP, port, ip, pl))
                    db.commit()
            if srid:
                sql = 'UPDATE service_requests SET status="SUCCESS" where id=%s'
                db.execute(sql, (srid,))
                db.commit()
                # updateSupernets(intIP)
        except Exception as e:
            print(str(e))
        device.close()
        return result
    else:
        if srid:
            now = datetime.strftime(datetime.now(), '%Y-%d-%m %H:%M')
            sql = 'UPDATE service_requests SET status="FAILURE",result="%s\nDevice not supported" where id=%s'
            db.execute(sql, (now, srid))
            db.commit()
        return "Device not supported"
