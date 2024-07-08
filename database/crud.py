import sqlite3


def database_connection(file: str) -> sqlite3.Connection:
    """
    This function creates a connection to a SQLite database.
    :param file: loction of the SQLite database file
    :return: sqlite3.Connection object
    """
    return sqlite3.connect(file)


def get_known_course_dates(connection: sqlite3.Connection) -> list:
    """
    This function checks if database file is available. If not, file will be created.
    If file exists, all data will be fetched from the database and returned.
    :param connection: sqlite3.Connection object
    :return: list of tuples (course_name, course_date, course_location)
    """
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM course_dates")
        return cursor.fetchall()
    except sqlite3.OperationalError:
        cursor.execute("CREATE TABLE course_dates (course_name TEXT, course_date TEXT, course_location TEXT)")
        return []


def match_course_dates(
        sql_result: list,
        course_dates: list,
        db_connection: sqlite3.Connection,
        course_name: str,
        location: str,
) -> bool:
    """
    This function checks if there are any new course dates in the input list that are not already in the database.
    If new dates are found, they will be inserted into the database.
    :param sql_result: list of tuples (course_name, course_date, course_location)
    :param course_dates: list of available course dates
    :param db_connection: sqlite3.Connection object
    :param course_name: name of the course
    :param location: location of the course
    :return: bool indicating whether courses already exist in the database
    """
    known_dates = [course_date[1] for course_date in sql_result]
    return_value = True
    for course_date in course_dates:
        if course_date not in known_dates:
            _ = insert_course_dates(
                db_connection,
                [(course_name, course_date, location)]
            )
            return_value = False
    return return_value


def insert_course_dates(connection: sqlite3.Connection, course_dates: list) -> bool:
    """
    Helper function to insert course dates into the database.
    :param connection: sqlite3.Connection object
    :param course_dates: list of tuples (course_name, course_date, course_location)
    :return: bool indicating whether the insert operation was successful
    """
    cursor = connection.cursor()
    for course_date in course_dates:
        cursor.execute("INSERT INTO course_dates VALUES (?,?,?)", course_date)
    connection.commit()
    return True
