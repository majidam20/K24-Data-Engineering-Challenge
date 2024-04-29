FROM python:3


RUN mkdir /outputs

COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt


COPY sales_data_cleaned.py ./


CMD [ "python", "sales_data_cleaned.py" ]







