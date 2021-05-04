"""
Holds and returns connections to data files, the database and csv containing sudokus
"""
import sqlite3
import os

DATABASE_PATH = 'src//data//sudokus.db'
CSV_PATH = 'src//data//sudokus.csv'

def get_database_connection():
    return sqlite3.connect(DATABASE_PATH)

def database_exists():
    return os.path.isfile(DATABASE_PATH)

def get_csv_path():
    return CSV_PATH
