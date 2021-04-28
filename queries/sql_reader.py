from sys_sql_io.sql_connection_handler import connection_handler
import traceback
import util.logger as logger


@connection_handler
def atoms_exist_in_table(cursor):
    query = "SELECT COUNT(*) FROM atom as count"
    try:
        cursor.execute(query)
        return cursor.fetchone()['count'] > 0
    except:
        logger.error(traceback.format_exc())


@connection_handler
def processed_snapshots(cursor):
    query = "SELECT DISTINCT snapshot FROM pocket"
    try:
        cursor.execute(query)
        return [record['snapshot'] for record in cursor.fetchall()]
    except:
        logger.error(traceback.format_exc())
