import pandas as pd


class DataEnricher:

    def _init__(self, products: list[dict], users: list[dict]):
        self.products_raw = products
        self.user_raw = users

    # Converter
        self.products_df = pd.DataFrame(products)
        self.user_df = pd.DataFrame(users)

    def enricher(self):
        enriched_df = self.products_df.merge(
            self.user_df,
            how="left",
            left_on="seller__id",
            right_on= "user_id",
            suffixes= ("", "_user")
        )

