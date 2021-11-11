FROM python:3.10-slim
RUN apt-get update; \
    apt-get install -y firefox-esr; \
    rm -rf /var/lib/apt/lists/*;
RUN pip install requests selenium
ADD https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz /tmp/
RUN tar -xf /tmp/geckodriver-v0.30.0-linux64.tar.gz -C /usr/local/bin/geckodriver
RUN chmod +x /usr/local/bin/geckodriver
RUN rm /tmp/geckodriver-v0.30.0-linux64.tar.gz
