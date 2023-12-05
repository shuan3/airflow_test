FROM python:3.8

WORKDIR /airflow

# Install dependencies
COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirement.txt
# RUN pip install dag-factory

# Copy application code
# COPY . .

# CMD ["python", "your_app.py"]