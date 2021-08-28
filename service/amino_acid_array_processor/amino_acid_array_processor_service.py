from sql.amino_acid_array_processor import amino_acid_array_processor_queries
import util.logger as logger
import time


def process_amino_acid_arrays():
    """This is the entry point of the amino_acid_array_processor module of the application. This function
    fetches formerly read and processed pockets, selects those which have a good potential of being useful in
    drug discovery and attempts to find best matching sibling pockets their corresponding snapshots for each of them.

    In this module we investigate a +- 'investigated radius' nanoseconds environment of a given pocket (also limited by
    start and end of simulations). For each snapshot we traverse the pockets in that snapshot and select the pocket
    most similar to the investigated one. If the similarity (defined by the ratio of common amino acids present in the
    pockets) is high enough we put this pocket into a wider (sibling_pocket_ids_75) and/or a narrower
    (sibling_pocket_ids_50) set of pockets belonging to the investigated one. We also put the snapshot ID of the
    matching pocket into sibling_snapshots_50 and sibling_snapshots_75 arrays. We save these for arrays into
    corresponding columns of table 'pocket' of the database.
    """

    start_time = time.time()
    drug_score_limit = 0.5
    intersection_limit_lower = 0.5
    intersection_limit_higher = 0.75
    experiment_size = 10  # 1000 or 1200
    investigated_radius = 100
    number_of_pockets = amino_acid_array_processor_queries.count_pockets_with_high_drug_score(drug_score_limit)

    for pocket_number in range(number_of_pockets):

        pocket = amino_acid_array_processor_queries.fetch_one_pocket_with_high_drug_score(drug_score_limit, pocket_number)
        snapshot = pocket['snapshot']
        sibling_pocket_ids_50 = []
        sibling_snapshots_50 = []
        sibling_pocket_ids_75 = []
        sibling_snapshots_75 = []
        lower_index = max(snapshot - investigated_radius, ((snapshot - 1) // experiment_size) * experiment_size + 1)
        higher_index = min(snapshot + investigated_radius, (((snapshot - 1) // experiment_size + 1) * experiment_size))

        for moment in range(lower_index, higher_index + 1):
            if moment != snapshot:
                process_pockets_of_snapshots(drug_score_limit, intersection_limit_lower, intersection_limit_higher,
                                             moment, pocket,
                                             sibling_pocket_ids_50,
                                             sibling_snapshots_50, sibling_pocket_ids_75, sibling_snapshots_75)

        amino_acid_array_processor_queries.save_sibling_arrays_by_id(pocket['id'], sibling_pocket_ids_50,
                                                                     sibling_snapshots_50, sibling_pocket_ids_75,
                                                                     sibling_snapshots_75)
        logger.info(f'Processed pocket number: {pocket_number+1} of {number_of_pockets}')

    logger.info("Time Elapsed: " + str(time.time() - start_time))


def process_pockets_of_snapshots(drug_score_limit, intersection_limit_lower, intersection_limit_higher, moment, pocket,
                                 sibling_pocket_ids_50,
                                 sibling_snapshots_50, sibling_pocket_ids_75, sibling_snapshots_75):
    """Processes all pockets of the currently investigated snapshot and appends best matches and their snapshots
    to the accumulating lists."""

    pockets_of_snapshot = amino_acid_array_processor_queries.get_pockets_by_snapshot_with_high_drug_score(
        moment, drug_score_limit)
    current_best_match, highest_intersection = get_best_match_for_snapshot(pocket, pockets_of_snapshot)

    if highest_intersection > intersection_limit_lower:
        sibling_pocket_ids_50.append(current_best_match['id'])
        sibling_snapshots_50.append(moment)

    if highest_intersection > intersection_limit_higher:
        sibling_pocket_ids_75.append(current_best_match['id'])
        sibling_snapshots_75.append(moment)


def get_best_match_for_snapshot(pocket, pockets_of_snapshot):
    """Returns the best match for parameter 'pocket' from list of pockets 'pockets_of_snapshot' collected from the
    currently investigated snapshot along with the quantified similarity."""

    highest_intersection = 0
    current_best_match = None

    for pocket_to_compare in pockets_of_snapshot:
        intersection = calculate_intersection_percentage(pocket['amino_acids'], pocket_to_compare['amino_acids'])

        if intersection > highest_intersection:
            highest_intersection = intersection
            current_best_match = pocket_to_compare

    return current_best_match, highest_intersection


def calculate_intersection_percentage(list_one, list_two):
    """This function is used to quantify the similarity of the pockets based on the amino acids residing within them."""

    max_of_sizes = max(len(list_one), len(list_two))
    intersection_size = len(set(list_one).intersection(list_two))
    return intersection_size / max_of_sizes
