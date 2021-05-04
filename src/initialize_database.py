"""
First-time setup for the database
"""
import csv
from repositories.sudoku_formatter import SudokuFormatter
from connections import get_database_connection
from connections import get_csv_path

connection = get_database_connection()
cursor = connection.cursor()

def drop_tables(connection):
    """Deletes existing database tables, in case initialization is run more than once

    Args:
        connection (sqlite3 database connetion): connection to the database
    """

    cursor.execute('''
        drop table if exists sudokus;
    ''')

    cursor.execute('''
        drop table if exists savedgames;
    ''')

    connection.commit()

def create_tables(connection):
    """Creates database tables for sudoku puzzles and saved games

    Args:
        connection (sqlite3 database connetion): connection to the database
    """

    cursor.execute('''
        create table sudokus (
            puzzle text,
            solution text,
            difficulty text
        );
    ''')

    cursor.execute('''
        create table savedgames (
            savename text primary key,
            puzzle text,
            solution text
        );
    ''')

    connection.commit()

def add_sudokus_to_database(csv_path):
    """Reads csv from given path and saves the puzzles in the database

    Args:
        csv_path (string): path to the csv file containing puzzles
    """

    formatter = SudokuFormatter()
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        
        for row in csv_reader:
            sudoku_data = formatter.dots_to_zeros(row)
            add_to_database(sudoku_data)

def add_to_database(sudokudata):
    """Adds one sudoku, along with its solution and difficulty into database

    Args:
        sudoku_data (array of strings): sudoku's puzzle, solution and difficulty

    Returns:
        [bool]: True if addition is succesful, False otherwise
    """
    try:
        cursor.execute(
            '''INSERT INTO sudokus VALUES(?,?,?)''',
            (sudokudata[0], sudokudata[1], sudokudata[2]))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def initilize_database():
    """
    Runs the initialization routine
    """
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

    csv_path = get_csv_path()
    add_sudokus_to_database(csv_path)

if __name__ == '__main__':
    initilize_database()
