from itertools import combinations

def generate_team_combination(players:[int], team_size:int, current_combination:[int]=[]):
    if team_size == 0:
        print(" ".join(map(str, current_combination)))
        return
    if len(players) < team_size:
        return
    for i in range(len(players)):
        new_combination = current_combination + [players[i]]
        generate_team_combination(players[i+1: ], team_size - 1, new_combination)


def main():
    n = int(input())
    players = list(map(int, input().split()))
    if n > 12:
        generate_team_combination(players, 12)


main()