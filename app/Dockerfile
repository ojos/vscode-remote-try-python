# Dockerfile
FROM python:3.7-slim-stretch

# Do not stdout/stderr buffer
ENV PYTHONUNBUFFERED 1

# Create application directory
RUN mkdir -p /var/app
WORKDIR /var/app

# Install dependent packages
RUN apt update
RUN apt -y install gcc \
                    git \
                    libmariadbclient-dev-compat

# Install python packages
COPY requirements.txt /var/app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Delete dependent packages
# RUN apt -y remove gcc

ADD . /var/app