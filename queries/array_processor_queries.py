from sys_sql_io.sql_connection_handler import connection_handler
import traceback
import util.logger as logger


@connection_handler
def count_pockets_with_high_drug_score(cursor, score):
    query = "select count(*) from pocket as count where druggability_score > %(score)s"
    try:
        cursor.execute(query, {'score': score})
        return cursor.fetchone()['count']
    except:
        logger.error(traceback.format_exc())


@connection_handler
def fetch_one_pocket_with_high_drug_score(cursor, score, offset):
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
def get_pockets_by_snapshot_with_high_drug_score_and_not_with_id(cursor, moment, score, id):
    query = """
         select id, snapshot, amino_acids
         from pocket
         where druggability_score > %(score)s and snapshot = %(moment)s and id != %(id)s
         order by id"""
    try:
        cursor.execute(query, {'score': score, 'moment': moment, 'id': id})
        return cursor.fetchall()
    except:
        logger.error(traceback.format_exc())


@connection_handler
def save_sibling_arrays_by_id(cursor, pocket_id, sibling_pocket_ids, sibling_snapshots):
    query = """
         update pocket
         set sibling_pockets = %(sibling_pocket_ids)s, sibling_timestamps = %(sibling_snapshots)s
         where id = %(pocket_id)s"""
    try:
        cursor.execute(query, {'pocket_id': pocket_id,
                               'sibling_pocket_ids': sibling_pocket_ids,
                               'sibling_snapshots': sibling_snapshots})
    except:
        logger.error(traceback.format_exc())
