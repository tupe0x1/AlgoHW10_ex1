import itertools

def _powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))

def create_shapley_map(players_costs: dict):
    all_players = players_costs.keys()
    map_subset_to_cost = {
        "".join(sorted(subset)): max([players_costs[player] for player in subset])
        for subset in _powerset(all_players)
        if len(subset) > 0
    }
    map_subset_to_cost[""] = 0
    return ''.join(all_players), map_subset_to_cost