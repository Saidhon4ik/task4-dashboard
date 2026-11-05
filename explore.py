import pandas as pd
import yaml

store = "STORE1"

users = pd.read_csv(f"data/{store}/users.csv")
orders = pd.read_parquet(f"data/{store}/orders.parquet")
with open(f"data/{store}/books.yaml", encoding="utf-8") as f:
    books = pd.DataFrame(yaml.safe_load(f))

print(users.shape, orders.shape, books.shape)
print(books.columns.tolist())
print(orders.head())