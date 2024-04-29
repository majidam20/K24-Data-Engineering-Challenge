### Import Libraries
import os
import sys
import random
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2

pd.options.display.max_rows = None
pd.set_option('display.max_columns', 500)
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(threshold=np.inf)

os.environ['PYTHONHASHSEED'] = '0'
np.random.seed(42)
random.seed(12345)

###+++ 2) Store Data into Database

# Define the database connection parameters
db_params = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': '1333'
}

dfcleaned = pd.read_csv("sales_data_cleaned.csv", sep=",")


# Create a connection to the PostgreSQL server
conn = psycopg2.connect(
    host=db_params['host'],
    database=db_params['database'],
    user=db_params['user'],
    password=db_params['password']
)


# Create a cursor object
cur = conn.cursor()

# Set automatic commit to be true, so that each action is committed without having to call conn.committ() after each command
conn.set_session(autocommit=True)

# Create the 'soccer' database
dbname = pd.read_sql_query("SELECT datname FROM pg_catalog.pg_database where datname = 'sales_data_cleaned' ORDER BY 1;", con=conn)

if len(dbname)== 0:
    # Create the 'soccer' database
    cur.execute("CREATE DATABASE sales_data_cleaned")

    # Commit the changes and close the connection to the default database
    conn.commit()
    cur.close()

conn.close()

# Connect to the 'soccer' database
db_params['database'] = 'sales_data_cleaned'
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}/{db_params["database"]}')

dfcleaned.to_sql('sales_data_cleaned', engine, if_exists='replace', index=False)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++