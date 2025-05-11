import sqlite3
import pandas as pd

with sqlite3.connect("../db/lesson.db") as conn:
    # SQL JOIN
    sql = """
    SELECT 
        li.line_item_id,
        li.quantity,
        p.product_id,
        p.product_name,
        p.price
    FROM line_items li
    JOIN products p ON li.product_id = p.product_id;
    """
    
    df = pd.read_sql_query(sql, conn)
    print("First 5 rows of raw data:")
    print(df.head())

    df["total"] = df["quantity"] * df["price"]
    print("\nWith total column:")
    print(df.head())
 
    summary = df.groupby("product_id").agg({
        "line_item_id": "count",
        "total": "sum",
        "product_name": "first"
    }).reset_index()

    summary.columns = ["product_id", "order_count", "total_sales", "product_name"]

    summary.sort_values("product_name", inplace=True)

    summary.to_csv("order_summary.csv", index=False)
    print("\nSummary saved to order_summary.csv:")
    print(summary.head())
