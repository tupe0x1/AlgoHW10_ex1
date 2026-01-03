import itertools
import math
import random
import airport
import shapley

def show(map_player_to_shapley_value):
    """
    Print the Shapley values to screen.
    """
    keys = list(map_player_to_shapley_value.keys())
    keys = sorted(keys)
    for player in keys:
        print("Shapley value of {} is {}".format(player, map_player_to_shapley_value[player]))

def calc_diff(res1: dict, res2: dict):
    print("diffs")
    total = sum(res1.values())
    for key in res1.keys():
        print("plyer {} diff precent: {}%".format(key, (abs(res1[key] - res2[key]) / total) *100))

def two_players():
    print("---- 2 players ----")
    players = ["a", "b"]
    players_path_costs = {
        "": 0,
        "a": 10, "b": 5,
        "ab": 10
    }
    sample_amount = 0.51
    res = shapley.calc_values_partial(''.join(players), players_path_costs, sample_amount)
    show(res)

def three_players_a():
    print("---- 3 players a ----")
    players = ["a", "b", "c"]
    players_path_costs = {
        "": 0,
        "a": 10, "b": 15, "c": 25,
        "ab": 20, "ac": 25, "bc": 30,
        "abc": 37
    }
    sample_amount = 0.9
    res = shapley.calc_values_partial(''.join(players), players_path_costs, sample_amount)
    show(res)
    print("real")
    res = shapley.calc_values_full(''.join(players), players_path_costs)
    show(res)
def three_players_b():
    print("---- 3 players b ----")
    players = ["a", "b", "c"]
    players_path_costs = {
        "": 0,
        "a": 10, "b": 15, "c": 0,
        "ab": 20, "ac": 10, "bc": 15,
        "abc": 20
    }
    sample_amount = 0.9
    res = shapley.calc_values_partial(''.join(players), players_path_costs, sample_amount)
    show(res)
    print("real")
    res = shapley.calc_values_full(''.join(players), players_path_costs)
    show(res)

def airport_shapley(amount = 10):
    costs = [random.randint(1, 1000) for i in range(amount)]
    costs.sort()
    cost_map = {}
    for p in range(amount):
        cost_map[f'{p}'] = costs[p]

    print("---- airport shapley ----")
    (p, m) = airport.create_shapley_map(cost_map)
    total_permutations = math.factorial(amount)
    print(f"{math.sqrt(total_permutations)}/{total_permutations} airport shapley values")
    res = shapley.calc_values_partial(''.join(p), m, math.sqrt(total_permutations)/total_permutations)
    show(res)

if __name__ == "__main__":
    two_players()
    three_players_a()
    three_players_b()
    airport_shapley()
    airport_shapley(20)

