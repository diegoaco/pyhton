''' Easy way to use SQL in Python '''

import pandas as pd
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

# Import data in csv form:
data = pd.read_csv("/Users/diego/Downloads/Stori_Data_Challenge_2021.csv", delimiter = ",")   
# Convert it to a dataframe and remove NaN rows:
df = pd.DataFrame(data).dropna()

# If we want to change the date format of some columns:
df['activated_date'] = pd.to_datetime(df['activated_date'])
df['activated_date'] = df['activated_date'].dt.strftime('%Y-%m') # Remove the day information

df['last_payment_date'] = pd.to_datetime(df['last_payment_date']).dt.date

# Usual SQL querry:
table2 = pysqldf("SELECT REPLACE(cust_id, 'C', '') AS cust_id, activated_date, last_payment_date, \
              cash_advance, credit_limit,\
              100*(cash_advance/credit_limit) as percentage \
              FROM df \
              WHERE activated_date LIKE '2020%' \
              AND last_payment_date LIKE '2020%';")

print(table2)
