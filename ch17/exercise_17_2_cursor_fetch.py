import sqlite3

# Connect to the books database
connection = sqlite3.connect('books.db')
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
