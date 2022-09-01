import mysql.connector
import pandas as pd
from mysql.connector import errorcode


# This script will help to build a transfer certificate database for a school.

DB_NAME = "student"
TABLES = {'transfer_certificate': (
    "CREATE TABLE if not exists `transfer_certificate` "
    "("
    "id              INT unsigned NOT NULL AUTO_INCREMENT,"
    "name            VARCHAR(150) NOT NULL,"
    "father_name     VARCHAR(150) NULL,"
    "mother_name     VARCHAR(150) NULL,"
    "nationality     VARCHAR(150) NULL,"
    "conduct         VARCHAR(150) NOT NULL,"
    "remark          VARCHAR(1500) NULL,"
    "PRIMARY KEY     (`id`)"
    ") ENGINE=InnoDB")}


def create_database(cursor):
    try:
        print("Creating Database '{}': ".format(DB_NAME), end='')
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {}".format(DB_NAME))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print("Database already exists, skipping database creation.")
        else:
            print("Failed creating database: {}".format(err))
            print(err.msg)
            exit(1)
    else:
        print("Database created successfully".format(DB_NAME))

    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print(err)
        exit(1)


def create_table(cursor):
    """
    This function will help with creating the MySql table that will be used for
    populating the student transfer certificate information.

    param config: MySql config credentials needed for creating tables.
    :return: none
    """
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table '{}': ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table already exists, skipping table creation.")
            else:
                print(err.msg)
                exit(1)
        else:
            print("Table created successfully.")

    # def get_student_tc_info(name):
    """This function will help to get the complete details about a student's
    Transfer from an institution.
    """


def set_student_tc_info(student_info, cursor):
    """This function will help to set the complete details about a student's
    Transfer in an institution.
    """

    add_student = ("INSERT INTO transfer_certificate "
                   "(name, id, conduct) "
                   "VALUES (%s, %s, %s")
    try:
        print("Inserting data into 'transfer_certificate' table.")
        cursor.execute(add_student, student_info)
    except mysql.connector.Error as err:
        print("Insertion of data into 'transfer_certificate' table failed, quitting.")
        print(err.msg)
        exit(1)


def get_config_credentials():
    """
    This function will help with creating config credentials for connecting with mysql.
    :return: jdbc connection config information.
    """
    config = {
        'user': 'root',
        'password': 'Root@123',
        'host': '127.0.0.1',
        'database': 'information_schema',
        'raise_on_warnings': True
    }

    return config


def create_connection(config):
    cnx = mysql.connector.connect(**config)
    return cnx


def create_cursor(cnx):
    cursor = cnx.cursor()
    return cursor


def close_connection(cnx):
    cnx.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    configuration = get_config_credentials()
    connection = create_connection(configuration)
    crs = create_cursor(connection)
    create_database(crs)
    configuration['database'] = DB_NAME
    crs = create_cursor(connection)
    create_table(crs)
    close_connection(connection)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
