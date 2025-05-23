'''This is exercise 17.1 from the textbooks
name: Tierra Gipson '''

import sqlite3
import os

# Get the current script directory
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "books.db")

# Connect to the books database
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# 1. Select all authors’ last names from the authors table in descending order
print("Authors (descending):")
for row in cursor.execute('SELECT last FROM authors ORDER BY last DESC'):
    print(row[0])

# 2. Select all book titles from the titles table in ascending order
print("\nTitles (ascending):")
for row in cursor.execute('SELECT title FROM titles ORDER BY title ASC'):
    print(row[0])

# 3. INNER JOIN for a real author in the database
print("\nBooks for author 'Deitel':")
for row in cursor.execute("""
    SELECT titles.title, titles.copyright, titles.isbn
    FROM titles
    INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn
    INNER JOIN authors ON authors.id = author_ISBN.id
    WHERE authors.last = 'Deitel'
    ORDER BY titles.title
"""):
    print(row)

# 4. Insert a new author
cursor.execute("""
    INSERT OR IGNORE INTO authors (first, last) VALUES ('Alexis', 'Rivera')
""")

# 5. Insert a new title
cursor.execute("""
    INSERT OR IGNORE INTO titles (isbn, title, edition, copyright)
    VALUES ('9999999999', 'How to Train Your Compiler', 1, '2025')
""")

# 6. Retrieve the ID of the new author
cursor.execute("""
    SELECT id FROM authors WHERE first = 'Alexis' AND last = 'Rivera'
""")
result = cursor.fetchone()
if result:
    author_id = result[0]
    try:
        # 7. Link the new author and new book
        cursor.execute("""
            INSERT INTO author_ISBN (id, isbn) VALUES (?, ?)
        """, (author_id, '9999999999'))
        print("\nInserted author_ISBN relationship.")
    except sqlite3.IntegrityError:
        print("Relationship between author and book already exists — skipping insert.")
else:
    print("Author not found, skipping relationship insert.")

# Commit and close
connection.commit()
connection.close()

