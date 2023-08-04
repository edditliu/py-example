FROM ubuntu:20.04

RUN apt update && apt install -y python3 python3-pip libpq-dev postgresql-client && pip install psycopg2 flask
RUN pip install pyyaml && apt -y install curl
WORKDIR /usr/local/eddie/pg_example
COPY new_example.py ./
COPY conf/manager-docker.yaml postgresql/conf/manager.yaml

CMD [ "python3", "new_example.py" ]
