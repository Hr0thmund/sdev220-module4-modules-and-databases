import csv, sqlite3

# I'm doing some things different from the book example text here.
# I'm using a with statement for automatic resource cleanup.
# I think "db" is a more meaningful name handle for the database than "conn",
# and "cursor" is slightly more readable than "curs"
with sqlite3.connect('books.db') as db:
    cursor = db.cursor()

    cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            title TEXT,
            author AUTHOR,
            year INTEGER
            )
    ''')

    with open('books2.csv', 'rt') as file:
        reader = csv.DictReader(file)
        for row in reader:
            insert_statement = "INSERT INTO books (title, author, year) VALUES (?, ?, ?)"
            cursor.execute(insert_statement, (row['title'], row['author'], row['year']))
        db.commit()

        cursor.execute("SELECT title FROM books ORDER BY title ASC")
        rows = cursor.fetchall()
        print(rows)
