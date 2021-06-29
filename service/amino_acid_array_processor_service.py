from queries import array_processor_queries


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
    drug_score_limit = 0.5
    number_of_snapshots = 10
    number_of_pockets = array_processor_queries.count_pockets_with_high_drug_score(drug_score_limit)
    for pocket_number in range(number_of_pockets):
        pocket = array_processor_queries.fetch_one_pocket_with_high_drug_score(drug_score_limit, pocket_number)
        snapshot = pocket['snapshot']
        sibling_pockets = []
        sibling_snapshots = []
        for moment in range(max(snapshot - 100, 1), min(number_of_snapshots + 1, snapshot + 100)): # add condition for end of 1000s
            pockets_of_snapshot = array_processor_queries.get_pockets_by_snapshot_with_high_drug_score_and_not_with_id(
                moment, drug_score_limit, pocket['id'])
            best_similarity = 0
            current_best_match = None
            for pocket_to_compare in pockets_of_snapshot:
                print('Comparing ' + str(pocket['id']) + ' with ' + str(pocket_to_compare['id']))
