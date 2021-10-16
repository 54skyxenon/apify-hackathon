FROM python:3
RUN cat /etc/*-release
RUN apt-get update
RUN apt-get install -y firefox
RUN pip3 install apify-client
RUN pip3 install selenium
RUN pip3 install webdriver-manager
COPY ./* ./
CMD [ "python3", "main.py" ]
