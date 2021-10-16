FROM python:3
RUN pip3 install lxml
RUN pip3 install apify-client
COPY ./* ./
CMD [ "python3", "example.py" ]
