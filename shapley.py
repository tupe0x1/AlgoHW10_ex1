import itertools
import collections
import math
import random

def _random_permutation(iterable):
    items = list(iterable)
    random.shuffle(items)
    return tuple(items)

def calc_values_partial(all_players: str, map_subset_to_cost: dict, percentage: float):
    if not (0 < percentage <= 1):
        raise ValueError("percentage must be between 0 and 1")

    map_player_to_sum_of_marginal_costs = collections.defaultdict(float)

    # Generate all permutations
    total_permutations = math.factorial(len(all_players))

    # Number of permutations to sample
    num_samples = math.ceil(percentage * total_permutations)

    # Randomly sample permutations
    sampled_permutations = [ _random_permutation(all_players) for _ in range(num_samples)  ]

    for permutation in sampled_permutations:
        current_cost = 0
        current_subset = ""

        for player in permutation:
            current_subset += player
            new_cost = map_subset_to_cost[''.join(sorted(current_subset))]
            marginal_cost = new_cost - current_cost

            map_player_to_sum_of_marginal_costs[player] += marginal_cost
            current_cost = new_cost

    # Average over sampled permutations
    for player, cost in map_player_to_sum_of_marginal_costs.items():
        map_player_to_sum_of_marginal_costs[player] = cost / num_samples

    return map_player_to_sum_of_marginal_costs


def calc_values_full(all_players: str, map_subset_to_cost: dict):
    map_player_to_sum_of_marginal_costs = collections.defaultdict(float)
    num_permutations = 0
    for permutation in itertools.permutations(all_players):
        current_cost = 0
        current_subset = ""
        for player in permutation:
            current_subset += player
            new_cost = map_subset_to_cost[''.join(sorted(current_subset))]
            marginal_cost = new_cost - current_cost
            map_player_to_sum_of_marginal_costs[player] += marginal_cost
            current_cost = new_cost
        num_permutations += 1

    for player, cost in map_player_to_sum_of_marginal_costs.items():
        map_player_to_sum_of_marginal_costs[player] = cost / num_permutations

    return map_player_to_sum_of_marginal_costs