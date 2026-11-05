import pandas as pd
import yaml

from clean import add_price_columns

store = "STORE1"

users = pd.read_csv(f"data/{store}/users.csv")
orders = pd.read_parquet(f"data/{store}/orders.parquet")
with open(f"data/{store}/books.yaml", encoding="utf-8") as f:
    books = pd.DataFrame(yaml.safe_load(f))

orders = add_price_columns(orders)

print(orders[["unit_price", "currency", "amount"]].head(8))
print(orders["currency"].value_counts())
print(orders["amount"].min(), orders["amount"].max())
print(orders["amount"].isna().sum())