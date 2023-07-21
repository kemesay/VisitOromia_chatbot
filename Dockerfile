FROM rasa/rasa:2.8.0
WORKDIR '/app'
COPY . /app
USER root
# WORKDIR /app
# COPY . /app
COPY ./data /app/data
COPY ./models /app/models
RUN mkdir /app/certs
COPY /root@ip-172-31-12-104:/home/ubuntu/server.p12 /app/certs/server.p12
RUN  rasa train
VOLUME /app
VOLUME /app/data
VOLUME /app/models

ENV SSL_CERTIFICATE_PATH="/app/certs/server.p12"
ENV SSL_CERTIFICATE_KEY_PATH="/app/certs/server.p12"
ENV SSL_CERTIFICATE_PASSWORD="Coop#4321"  
# If the certificate is password-protected, provide the password here

CMD ["run","-m","/app/models","--enable-api","--cors","*","--debug" ,"--endpoints", "endpoints.yml", "--log-file", "out.log", "--debug"]