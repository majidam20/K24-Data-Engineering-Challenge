# Solutions of Data Engineering Challenge

## Problem Statement

Imagine you are working with a large dataset in a CSV file that contains information about sales transactions for the last month.
Pricing team has provided `sales_data.csv` CSV file that contains all the information.
Each row in the CSV file represents a single transaction, and the columns include information such as 
"TransactionID," "ProductID," "Quantity,", "SalePrice" and "PurchasePrice"

My solutions are as follows:
### 1) Clean and Analyse the Dataset

* Created a Jupyter Notebook `data_analysis.ipynb` where I cleaned the dataset and analyzed the relation between Sale Price and Quantity for some products.

* Saved the cleaned dataset into `sales_data_cleaned.csv`.

### 2) Stored Data into Database

* I Prepared a docker compose file to run PostgreSQL. So, I created a docker file and install and run python file in the docker image. Moreover, I created a docker-compose.yml file and install and run postgres database.


* Finaly, to run docker run the following command in CMD:

	`docker-compose up --build -d`


* I Implemented a Python script `transfer_sales_data.py` to read `sales_data_cleaned.csv` and store the data into a table in the PostgreSQL database.


### 3) Implemented Process Data Python Function

I Implemented a Python function (`process_data()`) which performs the following transformations on the data:
* Calculate the total profit for each transaction by multiplying the "Quantity" and ("SalePrice" - "PurchasePrice") columns.
* Calculate the total profit for each product.
* Identify the top 2 selling products based on the **total quantity**.

The Python function `process_data() -> tuple[dict[int, float], dict[int, float], list[int]]`
that reads the data from database and returns a tuple containing:

* A dictionary where the keys are transaction IDs, and values are the total profit for each transaction.
* A dictionary where the keys are product IDs, and values are the total profit for each product.
* The product IDs of the 2 top-selling products.

Also, I stored the result in a file of your choice. For example: result.json

* The app.py contains the implementation of the process_data() function and any other necessary codes.

