import sqlite3
import pandas as pd

def create_db_from_csv():
    try:
        # 1. Load the CSV file using Pandas
        df = pd.read_sql_query = pd.read_csv("data.csv")
        
        # 2. Clean the data (Optional but good practice)
        df.columns = df.columns.str.strip() # Removes accidental spaces in headers
        
        # 3. Connect to SQLite
        conn = sqlite3.connect("office_data.db")
        
        # 4. Export DataFrame to SQL
        # 'replace' means it will overwrite the table if it already exists
        df.to_sql("sales", conn, if_exists="replace", index=False)
        
        conn.close()
        print("✅ Success! 'office_data.db' created from CSV.")
        print(f"📊 Imported {len(df)} rows into the 'sales' table.")
        
    except FileNotFoundError:
        print("❌ Error: 'data.csv' not found. Please create the file first.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    create_db_from_csv()