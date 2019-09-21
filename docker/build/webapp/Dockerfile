FROM php:7.2-apache

# Apache
RUN a2enmod ssl rewrite

## Basic tools
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y bash \
            curl \
            wget \
            ca-certificates \
            vim \
            git \
            nano \
            cron

## PHP
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libxrender1 libfontconfig \
        libicu-dev \
        mariadb-client \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install pdo_mysql gd mbstring bcmath zip intl opcache \
    && docker-php-ext-enable intl opcache

# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Timezone
RUN echo "Europe/Paris" >/etc/timezone && \
ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime && \
dpkg-reconfigure -f noninteractive tzdata

WORKDIR /var/www
