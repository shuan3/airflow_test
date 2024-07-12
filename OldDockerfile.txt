FROM python:3.8.0

ARG AIRFLOW_VERSION=2.7.3
ARG AIRFLOW_HOME=/usr/local/airflow
ENV SLUGIFY_USES_TEXT_UNIDECODE=yes



FROM apache/airflow:2.7.3
COPY /scripts/entrypoint.sh /scripts/entrypoint.sh
COPY requirements.txt /
# COPY . /
COPY . ${AIRFLOW_HOME}/
# RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# RUN chmod +x /scripts/entrypoint.sh

USER airflow
# RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -e .

# RUN set -ex \
#     && buildDeps=' \
#     freetds-dev \
#     python3-dev \
#     libkrb5-dev \
#     libsasl2-dev \
#     libssl-dev \
#     libffi-dev \
#     libpq-dev \
#     git \
#     ' \
#     && apt-get update -yqq \
#     && apt-get upgrade -yqq \
#     && apt-get install -yqq --no-install-recommends \
#     $buildDeps \
#     freetds-bin \
#     build-essential \
#     python3-pip \
#     && useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \
#     && pip install -U pip setuptools wheel \
#     && apt-get clean \
#     && rm -rf \
#     /var/lib/apt/lists/* \
#     /tmp/* \
#     /var/tmp/* \
#     /usr/share/man \
#     /usr/share/doc \
#     /usr/share/doc-base

# RUN pip install apache-airflow[http]==${AIRFLOW_VERSION}
# ADD . /




# ENTRYPOINT ["/scripts/entrypoint.sh"]
