FROM python:3
RUN apt-get -y update
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb
RUN pip3 install apify-client
RUN pip3 install selenium
RUN pip3 install webdriver-manager
RUN pip3 install googletrans==4.0.0rc1
COPY ./* ./
CMD [ "python3", "main.py" ]
