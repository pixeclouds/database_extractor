import sqlite3
from datetime import date
import json
import sys

try:
    # user command line arguments
    database = sys.argv[1]
    tables = sys.argv[2:]

    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # get a list of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    
    #  extract all tables if no table is specified
    tables = tables if tables else [tab[0] for tab in cursor.fetchall()]

    print("Starting extraction...")

    # data dictionary
    data = {}

    # iterate through each table and add its data to the dictionary
    for table in tables:
        # select table
        cursor.execute(f"SELECT * FROM {table}")

        # get the columns
        columns = [description[0] for description in cursor.description]
        
        # get the rows 
        rows = cursor.fetchall()

        # add the table data to the dictionary
        data[table] = {
            "columns": columns,
            "rows": [[cell for cell in row] for row in rows]
        }

    # Close database connection
    conn.close()

    # data backup version 
    version = date.today()

    # extracted data file
    output = f"{database}-version-{version}.json"
    
    # write the dictionary to a JSON file
    with open(f'{output}', 'w') as output_file:
        json.dump(data, output_file)

    # command line messages
    print("Message: Completed")
    print(f"No of tables extracted: {len(tables)}")
    print(f'Data extract into: "{output}"')
    
except sqlite3.Error as e:
    print("Error:", e)
