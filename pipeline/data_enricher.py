import pandas as pd
import requests
import json
from pandas import json_normalize



api_url_product = 'https://fakestoreapi.com/products'
api_url_users = 'https://fakestoreapi.com/products'

response_product = requests.get(api_url_product)
response_users = requests.get(api_url_users)

product = response_product.json()
users = response_users.json()

df_read = pd.DataFrame(product)
print(df_read)
print(df_read.head())


df_read_users = pd.DataFrame(users)
print(df_read_users)
print(df_read_users.head())