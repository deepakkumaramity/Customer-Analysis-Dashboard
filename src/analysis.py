import pandas as pd

def load_data():
    df = pd.read_csv("data/sales.csv")
    return df

def calculate_revenue(df):
    df["revenue"] = df["price"] * df["quantity"]
    return df

def customer_revenue(df):
    return df.groupby("customer_id")["revenue"].sum().reset_index()

def top_customers(df):
    return df.groupby("customer_id")["revenue"].sum().sort_values(ascending=False).head(5)

def repeat_customers(df):
    return df.groupby("customer_id").size().reset_index(name="orders").query("orders > 1")
