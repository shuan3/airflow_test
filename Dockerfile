FROM apache/airflow:2.7.3
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow
#FROM apache/airflow:2.6.1 ADD requirements.txt . RUN pip install apache-airflow==${AIRFLOW_VERSION} -r requirements.txt
FROM python:3.8


WORKDIR /airflow

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}"--upgrade pip
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r requirements.txt
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" dag-factory

# Copy application code
# COPY . .

# CMD ["python", "your_app.py"]

# USER root

# Install gosu
RUN apt-get update && apt-get install -y gosu && rm -rf /var/lib/apt/lists/*
# # Add 'airflow' user
# RUN useradd -ms /bin/bash airflow

# # Switch to the 'airflow' user
# USER airflow
