# First Repeating Character - 1
# Given a string of characters, find the first repeating character.



t=int(input())
for _ in range(t):
    s=input()
    r="."
    for c in s:
        if s.count(c)>1:
            r=c
            break
    print(r)