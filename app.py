### Import Libraries
import os
import sys
import random
import pandas as pd
import numpy as np
import sqlalchemy as db


pd.options.display.max_rows = None
pd.set_option('display.max_columns', 500)
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(threshold=np.inf)

os.environ['PYTHONHASHSEED'] = '0'
np.random.seed(42)
random.seed(12345)

def process_data():

    dfcleaned = pd.read_csv("sales_data_cleaned.csv", sep=",")

    dfcleaned ["total profit"] = dfcleaned["Quantity"] * dfcleaned["SalePrice"] - dfcleaned["PurchasePrice"]

    dfcleanedTP = dfcleaned.groupby(by=["ProductID"])["total profit"].sum().to_frame().reset_index()

    dfcleaned["ProductID"] = dfcleaned["ProductID"].astype(np.int64)
    #the top 2 selling products based on the total quantity
    print(dfcleaned.groupby(by=["ProductID"])["Quantity"].sum().to_frame().reset_index().sort_values("Quantity", ascending=False)[:2])

process_data()

def process_data():
    # Define the database connection parameters
    db_params = {
        'host': 'localhost',
        'database': 'postgres',
        'user': 'postgres',
        'password': '1333'
    }

    engine = db.create_engine('postgresql+psycopg2://postgres:1333@localhost/sales_data_cleaned')

    connection = engine.connect()
    metadata = db.MetaData()
    sales_data_cleaned = db.Table('sales_data_cleaned', metadata, autoload_with=engine)

    query = db.select(sales_data_cleaned)
    data = connection.execute(query)
    data = data.fetchall()
    dfdata = pd.DataFrame(data)

    dfdata["total profit"] = dfdata["Quantity"] * dfdata["SalePrice"] - dfdata["PurchasePrice"]
    dfdataTID = dfdata.groupby(by=["TransactionID"])["total profit"].sum().round(2)
    dfdataTID = dfdataTID.to_frame().reset_index()
    dfdataTID["TransactionID"] = dfdataTID["TransactionID"].astype(np.int64)


    dfdata["total profit"] = dfdata["Quantity"] * dfdata["SalePrice"] - dfdata["PurchasePrice"]
    dfdataPID = dfdata.groupby(by=["ProductID"])["total profit"].sum()
    dfdataPID = dfdataPID.to_frame().reset_index()
    dfdataPID["ProductID"] = dfdataPID["ProductID"].astype(np.int64)

    # the top 2 selling TransactionID based on the total quantity
    firstOutput = dfdataTID.sort_values("total profit", ascending=False)[:2].to_dict().items()

    # the top 2 selling products based on the total quantity
    secondOutput = dfdataPID.sort_values("total profit", ascending=False)[:2].to_dict().items()

    # the top 2 selling productID
    thirdOutput = dfdataPID.sort_values("total profit", ascending=False).iloc[:2, 0].tolist()

    return tuple([firstOutput, secondOutput, thirdOutput])

with open('result.json', 'w') as f:
    print('Filename:', process_data(), file=f)

print ("\n Task3: Implemented Process Data Python Function \n")

print(process_data())