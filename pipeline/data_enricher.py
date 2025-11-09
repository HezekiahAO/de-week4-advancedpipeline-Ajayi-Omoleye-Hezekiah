import pandas as pd


class DataEnricher:
    def __init__(self, products: list[dict], users: list[dict]):
        self.products_raw = products
        self.users_raw = users

        # Convert to DataFrames
        self.products_df = pd.DataFrame(products)
        self.users_df = pd.DataFrame(users)

    def enrich(self):
        # Merge products with user data
        enriched_df = self.products_df.merge(
            self.users_df,
            how="left",
            left_on="seller_id",   # or whatever your key is
            right_on="user_id",
            suffixes=("", "_user"),
        )

        # Compute revenue inside enrich()
        def compute_revenue(row):
            rating = row.get("rating", {})
            rating_count = rating.get("count", 0) if isinstance(rating, dict) else 0
            price = row.get("price", 0)
            return price * rating_count

        enriched_df["revenue"] = enriched_df.apply(compute_revenue, axis=1)
        return enriched_df

    def to_csv(self, path: str):
        enriched_df = self.enrich()
        enriched_df.to_csv(path, index=False)
        print(f"Enriched data saved to {path}")
