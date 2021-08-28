"""This file is responsible for reading data from the SQL database serving
data_reader module of the application."""


from util.sql_connection_handler import connection_handler
import traceback
import util.logger as logger


@connection_handler
def atoms_exist_in_table(cursor):
    """Returns whether atoms have already been parsed and persisted into the database.
    This is important because if we do not read all data at once but in separate parts
    then reading atoms should be done only on the first running."""

    query = "SELECT COUNT(*) FROM atom as count"
    try:
        cursor.execute(query)
        return cursor.fetchone()['count'] > 0
    except:
        logger.error(traceback.format_exc())


@connection_handler
def processed_snapshots(cursor):
    """Fetches already processed snapshots for data_reader module."""

    query = "SELECT DISTINCT snapshot FROM pocket"
    try:
        cursor.execute(query)
        return [record['snapshot'] for record in cursor.fetchall()]
    except:
        logger.error(traceback.format_exc())
