FROM rasa/rasa:2.6.2-full

# WORKDIR /rasa-app

USER root
ADD ./models /app/models/
ADD ./config.yml /app/
ADD ./actions /app/actions/
ADD ./data /app/data/
ADD ./domain.yml /app/
ADD ./config.yml /app/
ADD ./endpoints.yml /app/
ADD ./Dockerfile /app/
ADD ./docker-compose.yml /app/

# COPY . .
