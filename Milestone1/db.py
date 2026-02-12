import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Asuccessfullperson#78",
        database="policynav"
    )
