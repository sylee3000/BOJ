import math, sys
input = sys.stdin.readline

N, game = input().split()
game_p = 2 if game == 'Y' else 3 if game == 'F' else 4

player = {}

for _ in range(int(N)):
    player_name = input()
    if player_name not in player.keys():
        player[player_name] = 1

print(len(player) // (game_p - 1))