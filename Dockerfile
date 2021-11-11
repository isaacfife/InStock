FROM python:3.10-slim
ADD https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz /tmp/
RUN tar -xf /tmp/geckodriver-v0.30.0-linux64.tar.gz -C /usr/local/bin
