FROM python:3.6

COPY requirements.txt /
RUN apt-get update && apt-get install -y cyrus-sasl2-doc libsasl2-2 libsasl2-dev libsasl2-modules libsasl2-modules-db libsasl2-modules-gssapi-heimdal libsasl2-modules-sql libsasl2-modules-ldap libsasl2-modules-otp sasl2-bin \
    && pip install -r /requirements.txt


COPY ./ /rollrate 
WORKDIR /rollrate
ENV PYTHONPATH $PYTHONPATH:/rollrate
CMD gunicorn -b 0.0.0.0:8000 -w 4 "app:create_app()" -t 1200
#CMD flask run --host=0.0.0.0 -p 8000