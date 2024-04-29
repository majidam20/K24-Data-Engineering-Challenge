FROM python:3


RUN mkdir /outputs

COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt


COPY transfer_sales_data.py ./


CMD [ "python", "transfer_sales_data.py" ]







