import pandas as pd
import requests

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