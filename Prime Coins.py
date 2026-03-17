# Prime Coins
# Santa and Banta are playing a game of coins. They have a pile containing N coins. Players take alternate turns,
# removing some coins from the pile. On each turn, a player can remove either one 
# coin or coins equal to some prime power (i.e. px coins, where p - prime number and x - positive integer). 
# The game ends when the pile becomes empty. The player who can not make a move in his turn loses.

# Given the pile size, and assuming Santa always plays the first move, your task is to find out who will win the game, 
# provided that both the players play optimally.


t=int(input())
for _ in range(t):
    n=int(input())
    if n%6==0:
        print("Banta")
    else:
        print("Santa")