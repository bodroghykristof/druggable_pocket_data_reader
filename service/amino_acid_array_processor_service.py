from queries import array_processor_queries
import time


def process_amino_acid_arrays():
    """
    count_all = count_pockets_where_score_higher_than_0.5()
    for i in range count_all:
        pocket = fetch using i as offset and 1 as limit - use the same ordering and filter!
        timestamp_of_pocket = pocket.get_timestamp()
        sibling_pockets = []
        sibling_timestamps = []
         for j in range timestamp_of_pocket +- 100:
            pockets_of_timestamp = fetch in j time with drug score higher than 0.5
            best_match_similarity = - infinity
            current_sibling_pocket = None
            for pocket_to_compare in pockets_of_timestamp:
                similarity = calculate_similarity(pocket, pocket_to_compare)
                if similarity > best_match_similarity:
                    best_match_similarity = similarity
                    current_sibling_pocket = pocket_to_compare
            if best_match_similarity > 0.75:
                sibling_pockets.add(current_sibling_pocket)
                sibling_timestamps.add(j)
        pocket.set_sibling_pockets(sibling_pockets)
        pocket.set_sibling_timestamps(sibling_timestamps)
        save pocket
    """

    start_time = time.time()
    drug_score_limit = 0.5
    intersection_limit_lower = 0.5
    intersection_limit_higher = 0.75
    experiment_size = 10  # 1000 or 1200
    investigated_radius = 100
    number_of_pockets = array_processor_queries.count_pockets_with_high_drug_score(drug_score_limit)

    for pocket_number in range(number_of_pockets):

        pocket = array_processor_queries.fetch_one_pocket_with_high_drug_score(drug_score_limit, pocket_number)
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

        array_processor_queries.save_sibling_arrays_by_id(pocket['id'], sibling_pocket_ids_50,
                                                          sibling_snapshots_50, sibling_pocket_ids_75,
                                                          sibling_snapshots_75)

    print("Time Elapsed: " + str(time.time() - start_time))


def process_pockets_of_snapshots(drug_score_limit, intersection_limit_lower, intersection_limit_higher, moment, pocket,
                                 sibling_pocket_ids_50,
                                 sibling_snapshots_50, sibling_pocket_ids_75, sibling_snapshots_75):
    pockets_of_snapshot = array_processor_queries.get_pockets_by_snapshot_with_high_drug_score(
        moment, drug_score_limit)
    current_best_match, highest_intersection = get_best_match_for_snapshot(pocket, pockets_of_snapshot)

    if highest_intersection > intersection_limit_lower:
        sibling_pocket_ids_50.append(current_best_match['id'])
        sibling_snapshots_50.append(moment)

    if highest_intersection > intersection_limit_higher:
        sibling_pocket_ids_75.append(current_best_match['id'])
        sibling_snapshots_75.append(moment)


def get_best_match_for_snapshot(pocket, pockets_of_snapshot):
    highest_intersection = 0
    current_best_match = None

    for pocket_to_compare in pockets_of_snapshot:
        intersection = calculate_intersection_percentage(pocket['amino_acids'], pocket_to_compare['amino_acids'])

        if intersection > highest_intersection:
            highest_intersection = intersection
            current_best_match = pocket_to_compare

    return current_best_match, highest_intersection


def calculate_intersection_percentage(list_one, list_two):
    max_of_sizes = max(len(list_one), len(list_two))
    intersection_size = len(set(list_one).intersection(list_two))
    return intersection_size / max_of_sizes
