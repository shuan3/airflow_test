FROM apache/airflow:2.7.3
ARG AIRFLOW_HOME=/usr/local/airflow
COPY /scripts/entrypoint.sh /scripts/entrypoint.sh
COPY requirements.txt /
COPY . ${AIRFLOW_HOME}/
USER root

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         openjdk-17-jre-headless \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow
# ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
# RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" apache-airflow-providers-apache-spark==2.1.3
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt
# RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -e .