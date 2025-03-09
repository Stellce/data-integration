# Data Integration: SQL - NoSQL - Excel

## Overview
This project integrates data from three different sources: a SQL database (PostgreSQL), a NoSQL database (MongoDB), and an Excel file. The goal is to merge sales, inventory, and analytical data into a unified report that is automatically updated at regular intervals.

## Features
- Extracts data from a PostgreSQL database containing sales records.
- Fetches inventory data from MongoDB.
- Reads analytical data from an Excel file.
- Merges all data sources into a single dataset.
- Generates an Excel report with integrated data.
- Automates the process using scheduled tasks.

## Technologies Used
- **Python**: Data processing and automation.
- **Pandas**: Data manipulation and merging.
- **SQLAlchemy**: PostgreSQL database connection.
- **PyMongo**: MongoDB interaction.
- **Schedule**: Task scheduling for automation.
- **OpenPyXL**: Exporting data to Excel.

## Installation
### Prerequisites
Ensure you have Python installed along with the required dependencies:

```bash
pip install pandas sqlalchemy psycopg2 pymongo schedule openpyxl
```

### Database Setup
1. **PostgreSQL**:
   - Create a database named `postgres`.
   - Ensure it contains a table `orders` with sales data.
   - Update the connection string in `generate_report()`.

2. **MongoDB**:
   - Create a database named `mongo_db`.
   - Store inventory data in a collection named `mongo_db`.

3. **Excel File**:
   - Ensure `excel_data.xlsx` contains analytical data.
   - `report.xlsx` is a mock file to present data integration result which will be updated through script running.

## Usage
Run the script to generate and update the report automatically:

```bash
python main.py
```

The script will:
- Extract data from PostgreSQL.
- Retrieve inventory data from MongoDB.
- Read analytical data from the Excel file.
- Merge the datasets.
- Generate `report.xlsx`.
- Schedule updates to run every minute.
