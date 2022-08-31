import mysql.connector


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def get_student_tc_info(name):
    """This function will help to get the complete details about a student's
    Transfer from an institution.
    """


def set_student_tc_info(id, name, father_name, mother_name, nationality, conduct, remark):
    """This function will help to set the complete details about a student's
    Transfer in an institution.
    """


def get_connection_credentials():
    """
    This function will help with creating connection credentials for connecting with mysql.
    :return: jdbc connection.
    """
    config = {
        'user': 'root',
        'password': 'Root@123',
        'host': '127.0.0.1',
        'database': 'student',
        'raise_on_warnings': True
    }
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    try:
        cursor.execute(
            "SELECT name from transfer_certificate")

        for (name) in cursor:
            print("Hello {}".format(
                name))

    except mysql.connector.Error as err:
        print("cursor execute failed : {}".format(err))
        exit(1)

    cnx.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Harshini')
    get_connection_credentials()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
