import requests
import pandas as pd

base_url = 'https://fakestoreapi.com/)'

response = requests.get(base_url)

response.status_code = 200

data = response.json