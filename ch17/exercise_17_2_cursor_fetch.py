'''This program covers exercise 17.2 in the course textbook
Name: Tierra Gipson'''

import sqlite3
import os

# Get the current script directory
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "books.db")
# Connect to the books database
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Execute a query to select all from titles
cursor.execute('SELECT * FROM titles')

# Print column headers using cursor.description
headers = [desc[0] for desc in cursor.description]
print(' | '.join(headers))
print('-' * 50)

# Fetch all data and print in rows
for row in cursor.fetchall():
    print(' | '.join(str(item) for item in row))

# Close the connection
connection.close()
