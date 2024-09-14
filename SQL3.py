# Connect to a database (or create one if it doesn't exist)
connection = sqlite3.connect('example.db')
# Create a cursor object to interact with the database
cursor = connection.cursor()
cursor.execute('''CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, grade REAL)''')
cursor.execute("INSERT INTO students (name, grade) VALUES ('Alice', 85.5)")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
  print(row)
# Save (commit) the changes
connection.commit()
#closing connection
connection.close()
try:
   cursor.execute("SELECT * FROM non_existing_table")
except sqlite3.OperationalError as e:
  print(f"An error occurred: {e}")
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ('Bob', 92.3))
