#In this program you will create a todo list
import sqlite3

#function for printing the tabel in the end
def select_all(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM todo")

#Create a list containing all the values in the database
    rows = cur.fetchall()
    print(rows)
#print each row
    for row in rows:
        print(row)
 
print("Hi user! Ceate a todo list database...")

num=input('Please enter how many things you have to do.')
numz=int(num)
i=int(1)

#creates the file for the list and a variable resmebling the file in the code
conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
#Creates the table for the todo list in the file
conn.execute("CREATE TABLE IF NOT EXISTS todo (category char(50), theitem char(100),id INTEGER PRIMARY KEY )")
#insert users inputs into table
while i<=numz:
    category=input('Please enter what category of what you want to do')
    item=input('pleses enter the item you want to buy or the activite you want to do')
    conn.execute("INSERT INTO todo (category, theitem) VALUES ('{}','{}')".format(category,item))
    i=i+1
conn.commit()


print("Database todo.db created")
select_all(conn)


ans=int(input('want to delete? if yes enter 1 if no enter 0'))
if ans==1:
    conn = sqlite3.connect('todo.db')
    conn.execute("DELETE FROM todo")
    conn.commit()
