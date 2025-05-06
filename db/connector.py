import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os


load_dotenv()


def get_connection(database: str = "sakila") -> mysql.connector.connection_cext.CMySQLConnection | None:
    """
    Establishes a connection to the Sakila database.

    :param database: Name of the database (default is 'sakila')
    :return: Connection object or None if an error occurs
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("host_read"),
            user=os.getenv("user_read"),
            password=os.getenv("password_read"),
            database=database
        )
        return connection
    except Error as e:
        print(f"[Connection error to sakila] {e}")
        return None


def get_log_connection(database: str = "group_111124_fp_GolubenkoA") -> mysql.connector.connection_cext.CMySQLConnection | None:
    """
    Establishes a connection to the logging database.

    :param database: Name of the logging database (default is 'group_111124_fp_GolubenkoA')
    :return: Connection object or None if an error occurs
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("host_write"),
            user=os.getenv("user_write"),
            password=os.getenv("password_write"),
            database=database
        )
        return connection
    except Error as e:
        print(f"[Connection error to log database] {e}")
        return None
