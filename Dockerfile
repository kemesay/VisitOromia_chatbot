FROM rasa/rasa:3.6.2
WORKDIR '/app'
COPY . /app
USER root
# WORKDIR /app
# COPY . /app
COPY ./data /app/data
COPY ./models /app/models
# COPY ./data /app/data
# COPY ./models /app/models

RUN mkdir /app/certs
COPY server.p12 /app/certs/server.p12
RUN  rasa train
VOLUME /app
VOLUME /app/data
VOLUME /app/models

ENV SSL_CERTIFICATE_PATH="/app/certs/server.p12"
ENV SSL_CERTIFICATE_KEY_PATH="/app/certs/server.p12"
ENV SSL_CERTIFICATE_PASSWORD="Coop#4321"
ENV PORT=8443  
# Use the desired port, e.g., 443 or 8443

# If the certificate is password-protected, provide the password here

# CMD ["run","-m","/app/models","--enable-api","--cors","*","--debug" ,"--endpoints", "endpoints.yml", "--log-file", "out.log", "--debug"]

CMD [ "run" ]




# version: '3'doc
# services:
#     rasa:
#       container_name: "rasa_server"
#       user: root
#       build: 
#         context:  .
#       volumes:
#       - "./:/app"
#       ports: 
#         - "5005:5005"
#     action_server:
#       container_name: "action_server"
#       build:
#         context: actions
#       volumes:
#         - ./actions:/app/actions
#         - ./data:/app/data
#       ports:
#         - 5055:5055
    
    # rasa-shell:
    # image: rasa/rasa:2.8.1-full
    # command: shell --endpoints http://rasa:5005
    # ports:
    #   - "8000:8000"



    # FROM rasa/rasa-sdk:3.6.1
# WORKDIR /app
# COPY requirements.txt requirements.txt
# USER root
# RUN pip install --verbose -r requirements.txt
# EXPOSE 5055
# USER 1001
