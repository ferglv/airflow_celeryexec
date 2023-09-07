FROM python:3.11-slim-buster

WORKDIR /root/airflow
ENV PYTHONPATH "${PYTHONPATH}:${WORKDIR}"

RUN apt-get update && \
    apt-get install -y netcat vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install pipenv && \
    pipenv install --dev --system --deploy

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
