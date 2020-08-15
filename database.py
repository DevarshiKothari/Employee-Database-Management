import sqlite3 as sq


table_creation = "CREATE TABLE IF NOT EXISTS Employees (id INTEGER PRIMARY KEY, name TEXT, age TEXT, pay TEXT);"
        

insertion = '''INSERT INTO Employees (name,age,pay) VALUES (?,?,?);'''

select_all = '''SELECT * FROM Employees;'''

select_for_single_value = '''SELECT * From Employees WHERE name=(?);'''

for_updation = '''UPDATE Employees SET pay=(?) WHERE name=(?);'''

deletion = '''DELETE FROM Employees WHERE name=(?);'''

selection_of_one = '''SELECT * FROM Employees WHERE name=(?);'''

visualize_employees_pay = "SELECT name,AVG(pay) FROM Employees GROUP BY name;"

def connect():
    return sq.connect('employees_database.db')


def create_table(connection):
    with connection:
        connection.execute(table_creation)


def table_content_view(connection):
    with connection:
        return connection.execute(select_all).fetchall()


def select_single_value(connection,name):
    with connection:
        return connection.execute(selection_of_one,(name,)).fetchall()


def insert_in_table(connection,name,age,pay):
    with connection:
        connection.execute(insertion,(name,age,pay))


def value_update(connection,pay,name):
    with connection:
        connection.execute(for_updation,(pay,name))


def row_delete(connection,name):
    with connection:
        connection.execute(deletion,(name,))


def visualize_data(connection):
    with connection:
        return connection.execute(visualize_employees_pay).fetchall()