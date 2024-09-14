import sqlite3
# Connect to a database (or create one if it doesn't exist)
connection = sqlite3.connect('example.db')
# Create a cursor object to interact with the database
cursor = connection.cursor()
cursor.execute('''CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT,  subject TEXT , age INT ,grade REAL)''')
cursor.execute("INSERT INTO students (id,name,subject,age,grade) VALUES (101,'Alice','computers',22,85.5)")
cursor.execute("INSERT INTO students (id,name,subject,age,grade) VALUES (102,'Geethika','Da',25,92.6)")
cursor.execute("INSERT INTO students (id,name,subject,age,grade) VALUES (103,'Chinnu','DMT',26, 75.9)")
cursor.execute("INSERT INTO students (id,name,subject,age,grade) VALUES (104,'sai','PDM',24, 88.3)")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
  print(row)
# Save (commit) the changes
connection.commit()
try:
   cursor.execute("SELECT * FROM non_existing_table")
except sqlite3.OperationalError as e:
  print(f"An error occurred: {e}")
cursor.execute("INSERT INTO students (id,name,subject,age, grade) VALUES (?,?,?,?,?)", (110,'Bob','ADSD',27, 92.3))
#closing connection
connection.close()
