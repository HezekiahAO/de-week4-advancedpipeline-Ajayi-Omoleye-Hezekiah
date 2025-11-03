import requests
import pandas as pd

class Api_client:
    def __init__(self, base_url) -> None:
        self.base_url = base_url

    # @property
    def get_all_products(self, endpoint):
        self.endpoint = endpoint or '/products'
        product_response = requests.get(self.base_url + endpoint)
        self.product_data = product_response.json()

        return self.product_data
    

    # @property
    def get_all_users(self, endpoint):
        
        self.endpoint = endpoint or '/users'

        user_response = requests.get(self.base_url + self.endpoint)

        self.user_data = user_response.json()

        return self.user_data


    def piginate_products(self, endpoint):
        pass
    
    def piginate_users(self, endpoint):
        pass
                                                            # Working in a modular approach where i finish one project then test that project, before integrating it into the pipeline

if __name__ == "__main__":
    main = Api_client(base_url = 'https://fakestoreapi.com')
    print(main.get_all_products('/products'))
    print(main.get_all_users('/users'))

# Pigination