"""This file is responsible for reading and writing data from/to the SQL database serving
amino_acid_array_processor module of the application."""

from util.sql_connection_handler import connection_handler
import traceback
import util.logger as logger


@connection_handler
def count_pockets_with_high_drug_score(cursor, score):
    """Count pockets with higher druggability score than lower limit defined by parameter 'score'."""

    query = "select count(*) from pocket as count where druggability_score > %(score)s"
    try:
        cursor.execute(query, {'score': score})
        return cursor.fetchone()['count']
    except:
        logger.error(traceback.format_exc())


@connection_handler
def fetch_one_pocket_with_high_drug_score(cursor, score, offset):
    """Get the next pocket ('offset'th) with druggability score higher than defined by lower limit 'score'."""

    query = """
        select id, snapshot, amino_acids
        from pocket
        where druggability_score > %(score)s
        order by id
        limit 1 offset %(offset)s"""
    try:
        cursor.execute(query, {'score': score, 'offset': offset})
        return cursor.fetchone()
    except:
        logger.error(traceback.format_exc())


@connection_handler
def get_pockets_by_snapshot_with_high_drug_score(cursor, moment, score):
    """Get all pockets registered in the given snapshot with druggability score higher
    than defined by lower limit 'score'."""

    query = """
         select id, snapshot, amino_acids
         from pocket
         where druggability_score > %(score)s and snapshot = %(moment)s
         order by id"""
    try:
        cursor.execute(query, {'score': score, 'moment': moment})
        return cursor.fetchall()
    except:
        logger.error(traceback.format_exc())


@connection_handler
def save_sibling_arrays_by_id(cursor, pocket_id, sibling_pocket_ids_50,
                              sibling_snapshots_50, sibling_pocket_ids_75,
                              sibling_snapshots_75):
    """Save created sibling amino acid and snapshot arrays fot the given pocket defined by parameter 'pocket_id'
    into corresponding columns of table 'pocket'."""

    query = """
         update pocket
         set sibling_pockets_50 = %(sibling_pocket_ids_50)s, sibling_snapshots_50 = %(sibling_snapshots_50)s, sibling_pockets_75 = %(sibling_pocket_ids_75)s, sibling_snapshots_75 = %(sibling_snapshots_75)s
         where id = %(pocket_id)s"""
    try:
        cursor.execute(query, {'pocket_id': pocket_id,
                               'sibling_pocket_ids_50': sibling_pocket_ids_50,
                               'sibling_snapshots_50': sibling_snapshots_50,
                               'sibling_pocket_ids_75': sibling_pocket_ids_75,
                               'sibling_snapshots_75': sibling_snapshots_75})
    except:
        logger.error(traceback.format_exc())
