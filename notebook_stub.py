import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("seaborn-v0_8")

Load data
df = pd.read_csv("data/sample_sales.csv", parse_dates=["order_date"])
df["revenue"] = df["quantity"] * df["price"]
df["year_month"] = df["order_date"].dt.to_period("M").astype(str)

Aggregations
monthly_rev = df.groupby("year_month", as_index=False)["revenue"].sum()
top_products = df.groupby("product", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)

Print outputs (so reviewers see results)
print("\nMonthly revenue:")
print(monthly_rev)
print("\nTop products by revenue:")
print(top_products.head(5))
