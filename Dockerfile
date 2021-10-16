FROM python:3
RUN apt-get -y install google-chrome-stable
RUN pip3 install apify-client
RUN pip3 install selenium
RUN pip3 install webdriver-manager
COPY ./* ./
CMD [ "python3", "main.py" ]
