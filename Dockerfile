FROM python:3.11-slim-buster

WORKDIR /root/airflow
ENV PYTHONPATH "${PYTHONPATH}:${WORKDIR}"

RUN apt-get update && \
    apt-get install -y netcat vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install pipenv

COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev --system --deploy

COPY . .

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
