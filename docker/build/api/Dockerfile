FROM python:3.6
MAINTAINER Yann ZHAO "rzhao@kernix.com"


# Copy python elements
RUN mkdir -p /var/www/app
ADD ./app /var/www/app
COPY ./app/requirements.txt /var/www/app/requirements.txt
COPY ./app/setup.py /var/www/app/setup.py
COPY ./README.md /var/www/app/README.md
COPY ./INSTALL.md /var/www/app/INSTALL.md

WORKDIR /
RUN pip install -r /var/www/app/requirements.txt
RUN pip install -e /var/www/app/

EXPOSE 8080

WORKDIR /var/www/app/routes/

ENTRYPOINT ["python3"]
CMD ["routes.py"]
