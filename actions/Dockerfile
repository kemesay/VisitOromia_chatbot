
FROM rasa/rasa-sdk:3.6.1
WORKDIR /app
COPY ./requirements.txt ./requirements.txt 
USER root
RUN /bin/bash -o pipefail -c pip install requirements.txt
COPY . /app/actions
# EXPOSE 5055
USER 1001
