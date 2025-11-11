import pandas as pd
import requests
import json
from pandas import json_normalize

api_url_products = 'https://fakestoreapi.com/products'
api_url_users = 'https://fakestoreapi.com/users'

response_products = requests.get(api_url_products)
response_users = requests.get(api_url_users)

# Ensure HTTP requests succeeded (will raise HTTPError on bad status)
response_products.raise_for_status()
response_users.raise_for_status()

# Call the .json() method to get parsed JSON data (not the method object)
products = response_products.json()
users = response_users.json()

df_read_products = pd.DataFrame(products)
df_read_users = pd.DataFrame(users)

print(df_read_products.head())
print(df_read_users.head())

df_products = pd.json_normalize(products)  # Normalize nested JSON data for products
df_users = pd.json_normalize(users)
print(df_read_products.head())
print(df_read_users.head())


# LEFT JOIN: keep all products, add matching seller info
# Products and Users both have 'id' columns. We join on matching IDs.
# This is a simple positional join since there's no actual seller_id field.
left_join_product = pd.merge(
    df_read_products, 
    df_read_users, 
    left_on='id', 
    right_on='id', 
    how='left', 
    suffixes=('_product', '_user')
)
print("Merged result:")
print(left_join_product.head())



