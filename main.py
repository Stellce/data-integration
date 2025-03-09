import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient
from datetime import datetime
import schedule
import time

def generate_report():
    psql_eng = create_engine("postgresql://postgres:zaq1%40WSX@localhost:5432/postgres")
    postgres_data = pd.read_sql("select * from orders", psql_eng)

    mongo_client = MongoClient("mongodb://localhost:27017/")
    db = mongo_client["mongo_db"]
    mongo_data = db["mongo_db"]
    data = mongo_data.find()
    mongo_data = pd.DataFrame(data)
    mongo_data.drop('_id', axis=1, inplace=True)

    excel = pd.read_excel("excel_data.xlsx")
    excel_data = pd.DataFrame(excel)
    excel_data.columns = excel_data.columns.str.lower()

    combined_data = pd.merge(postgres_data, excel_data, on="product", how="left")
    mongo_data_expanded = mongo_data.explode("products").rename(columns={"products": "product"})
    final_data = pd.merge(combined_data, mongo_data_expanded, on="product", how="left")
    final_data.to_excel("report.xlsx", index=False)
    print(f"report generated at: {datetime.now()}")

generate_report()
schedule.every().minute.do(generate_report)

while True:
    schedule.run_pending()
    time.sleep(1)