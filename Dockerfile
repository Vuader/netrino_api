FROM tachyonic

RUN apt-get --assume-yes install libsnmp-dev
RUN pip3 install pyipcalc
RUN pip3 install celery
RUN pip3 install napalm
RUN pip3 install easysnmp

WORKDIR /root
ADD https://api.github.com/repos/TachyonicProject/netrino_common/git/refs/heads/development /root/netrino_common.json
RUN git clone -b development https://github.com/TachyonicProject/netrino_common.git
WORKDIR /root/netrino_common
RUN pip3 install .

COPY db.sql /root/
COPY tachyonic/netrino_api /usr/local/lib/python3.5/dist-packages/tachyonic/netrino_api
COPY tachyonic/netrino_api/resources/netrino-celery.cfg /etc
COPY 000-default.conf /etc/apache2/sites-available/

WORKDIR /var/www
RUN mkdir netrino_api

RUN chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \
             && service mysql start; service mysql start \
             && mysql -ppassword tachyon < /root/db.sql \
             && tachyonic -s tachyonic.netrino_api netrino_api
RUN chown -R www-data:www-data netrino_api/tmp
RUN ln -s /var/www/tachyonic_api/policy.json /var/www/netrino_api/policy.json
RUN echo "netrino_api = http://localhost/netrino" >> /var/www/tachyonic_api/settings.cfg
RUN echo "[endpoints]" >> /var/www/tachyonic_ui/settings.cfg
RUN echo "netrino_api = http://localhost/netrino" >> /var/www/tachyonic_ui/settings.cfg
RUN sed -i -e 's/\(modules.*\)/\1, tachyonic.netrino_ui/' /var/www/tachyonic_ui/settings.cfg
RUN apt-get --assume-yes install vim screen
EXPOSE 80
CMD service apache2 start && (chown -R mysql:mysql /var/lib/mysql /var/run/mysqld && service mysql start) && bash
