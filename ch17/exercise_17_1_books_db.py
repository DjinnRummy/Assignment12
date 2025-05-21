import sqlite3

# Connect to the books database
connection = sqlite3.connect('books.db')
cursor = connection.cursor()

# 1. Select all authors’ last names from the authors table in descending order
print("Authors (descending):")
for row in cursor.execute('SELECT last FROM authors ORDER BY last DESC'):
    print(row[0])

print("\nTitles (ascending):")
# 2. Select all book titles from the titles table in ascending order
for row in cursor.execute('SELECT title FROM titles ORDER BY title ASC'):
    print(row[0])

print("\nBooks for a specific author (ordered by title):")
# 3. INNER JOIN for a specific author
for row in cursor.execute("""
    SELECT titles.title, titles.copyright, titles.isbn
    FROM titles
    INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn
    INNER JOIN authors ON authors.id = author_ISBN.id
    WHERE authors.last = 'PLACEHOLDER_LAST' AND authors.first = 'PLACEHOLDER_FIRST'
    ORDER BY titles.title
"""):
    print(row)

# 4. Insert a new author (replace placeholders)
cursor.execute("""
    INSERT INTO authors (first, last) VALUES ('NewFirstName', 'NewLastName')
""")

# 5. Insert a new title and link it to an author
cursor.execute("""
    INSERT INTO titles (isbn, title, edition, copyright)
    VALUES ('9999999999', 'New Book Title', 1, '2025')
""")
cursor.execute("""
    INSERT INTO author_ISBN (id, isbn) VALUES (1, '9999999999')
""")

# Commit changes and close
connection.commit()
connection.close()
