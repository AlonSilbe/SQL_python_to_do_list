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
#print each row
    for row in rows:
        print(row)
    menu()
    
def add():
    num=input('Please enter how many things you have to do.')
    numz=int(num)
    i=int(1)

#creates the file for the list and a variable resmebling the file in the code
    conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
#Creates the table for the todo list in the file
    conn.execute("CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY ,category char(50), theitem char(100))")
#insert users inputs into table
    while i<=numz:
        category=input('Please enter what category of what you want to do')
        item=input('pleses enter the item you want to buy or the activite you want to do')
        conn.execute("INSERT INTO todo (category, theitem) VALUES ('{}','{}')".format(category,item))
        i=i+1
    conn.commit()
    menu()

def dele():
        conn = sqlite3.connect('todo.db')
        conn.execute("DELETE FROM todo")
        conn.commit()
        print('All values have been deleted')
        menu()
        
#menu function based on function from teachyourselfpython.com
def menu():
    print("Choose what you want to do to the list")
    print()
    
    #creates the file for the list and a variable resmebling the file in the code
    conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
    choice = input("""
                      A: Add assignments to the todo list
                      B: deltete all values in the table
                      C: print the DB
                    

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        add()
    elif choice == "B" or choice =="b":
        dele()
    elif choice == "C" or choice =="c":
        select_all(conn)
    #elif choice=="Q" or choice=="q":
     #   sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()
        
def main():
    print('Hello welcome to todo list DB program')
    menu()

#the program is initiated, so to speak, here
main()


