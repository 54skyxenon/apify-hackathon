FROM python:3
RUN pip3 install apify-client
RUN pip3 install selenium
COPY ./* ./
CMD [ "python3", "main.py" ]
