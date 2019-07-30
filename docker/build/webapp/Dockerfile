FROM debian:latest 
MAINTAINER Mikael Koutero "mkoutero@kernix.com"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y
RUN apt-get install -y apache2 libapache2-mod-wsgi
RUN apt-get install -y tzdata
RUN apt-get install -y git curl php7.0 libapache2-mod-php php-cli php-common 
# php-mbstring php-gd php-intl php-xml php-zip
RUN apt-get clean \
 	&& apt-get autoremove \
	&& rm -rf /var/lib/apt/lists/*



# Create and config webapp
RUN mkdir -p /var/www/epex-chatbot.com/public_html
RUN chown -R $USER:$USER /var/www/epex-chatbot.com/public_html
RUN chmod -R 755 /var/www


RUN a2enmod rewrite
RUN chown -R www-data:www-data /var/www
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_RUN_DIR /var/www

COPY ./dist /var/www/epex-chatbot.com/public_html/dist
COPY ./static /var/www/epex-chatbot.com/public_html/static
COPY ./index.html /var/www/epex-chatbot.com/public_html/index.html

# Disable the default test site
RUN a2dissite 000-default.conf

COPY ./docker/webapp/httpd-webapp.conf /etc/apache2/sites-available/epex-chatbot.com.conf
RUN a2ensite epex-chatbot.com.conf


RUN service apache2 restart

EXPOSE 80

CMD ["/usr/sbin/apache2", "-D",  "FOREGROUND"]
