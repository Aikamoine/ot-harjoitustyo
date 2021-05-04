"""
Holds and returns connections to data files, the database and csv containing sudokus
"""
import sqlite3
import os

database_path = 'src//data//sudokus.db'
csv_path = 'src//data//sudokus.csv'

def get_database_connection():
    return sqlite3.connect(database_path)

def database_exists():
    return os.path.isfile(database_path)
    
def get_csv_path():
    return csv_path
