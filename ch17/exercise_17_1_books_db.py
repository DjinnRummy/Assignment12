'''This is exercise 17.1 from the textbooks
name: Tierra Gipson '''

import sqlite3

# Connect to the books database (relative path)
connection = sqlite3.connect("books.db")
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

# 4. Insert a new author from textbook-style names
cursor.execute("""
    INSERT INTO authors (first, last) VALUES ('Harvey', 'Quirk')
""")

# 5. Insert a new real-ish title
cursor.execute("""
    INSERT INTO titles (isbn, title, edition, copyright)
    VALUES ('0143141592', 'Advanced Java Concepts', 1, '2024')
""")

# 6. Retrieve the ID of the new author
cursor.execute("""
    SELECT id FROM authors WHERE first = 'Harvey' AND last = 'Quirk'
""")
author_id = cursor.fetchone()[0]

# 7. Link the new author and new book
cursor.execute("""
    INSERT INTO author_ISBN (id, isbn) VALUES (?, ?)
""", (author_id, '0143141592'))

# Commit and close
connection.commit()
connection.close()
