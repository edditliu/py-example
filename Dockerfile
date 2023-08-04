FROM ubuntu:20.04

RUN apt update && apt install -y python3 python3-pip libpq-dev postgresql-client && pip install psycopg2
WORKDIR /usr/local/eddie/pg_example
COPY postgres_example_docker.py ./
COPY new_example_docker.py ./
CMD [ "sleep", "infinity" ]
