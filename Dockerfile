FROM python:3.11-slim-buster

# Define arguments and environment variables
ARG AIRFLOW_USER_HOME=/opt/airflow
ENV PYTHONPATH="${AIRFLOW_USER_HOME}:${PYTHONPATH}" \
    AIRFLOW_HOME=${AIRFLOW_USER_HOME} \
    APP_HOME=/usr/src/app

# Update and install necessary packages, then clean up to reduce image size
RUN apt-get update && \
    apt-get install -y netcat vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR $APP_HOME

# Copy all necessary files and directories
COPY . $APP_HOME/

# Install Python dependencies
RUN pip3 install pipenv && \
    pipenv install --dev --system --deploy && \
    chmod +x entrypoint.sh \

EXPOSE 8080

ENTRYPOINT ["./entrypoint.sh"]
