import database as db
import charts
import matplotlib.pyplot as plt


prompt = '''WELCOME,
PLEASE SELECT THE FOLLOWING OPTIONS AS PER YOUR NEED
1. VIEW_TABLE 
2. SELECT PARTICULAR ITEM
3. INSERTION
4. UPDATION
5. DELETION
6. Visual Representation of Employees Pay
7. EXIT

YOUR SELECTION : '''


def menu():
    connection = db.connect()
    db.create_table(connection)
    while (choice := input(prompt)) != '7':
        if choice=='1':

            contents = db.table_content_view(connection)
            #print('The Table Contents Are :')
            print('Id Name   Age  Pay')
            for content in contents:
                print(f'{content[0]} {content[1]} {content[2]} {content[3]}')
            print('\n')

        elif choice=='2':
            name = input('Please provide the employees Name : ')

            names = db.select_single_value(connection,name)
            print('Id Name   Age  Pay')
            for same_name in names:
                print(f'{same_name[0]} {same_name[1]} {same_name[2]} {same_name[3]}')
            print('\n')

        elif choice=='3':
            name = input('New Employees Name : ')
            age = input('His/Her age : ')
            pay = input('His/Her pay :')

            db.insert_in_table(connection,name,age,pay)

        elif choice=='4':
            name = input('Name of employee : ')
            pay = input('His/Her new pay : ')

            db.value_update(connection,name,pay)

        elif choice=='5':
            name = input('Employees name to be deleted : ')

            db.row_delete(connection,name)

        elif choice=='6':

            chart_data = db.visualize_data(connection)
            charts.return_chart(chart_data)
            plt.show()


menu()