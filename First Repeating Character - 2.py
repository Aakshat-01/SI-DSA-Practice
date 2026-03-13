# First Repeating Character - 2
# Given a string of characters, find the first repeating character.


t=int(input())
for _ in range(t):
    s=input()
    d={}
    r="."
    for c in s:
        d[c]=d.get(c,0)+1
        if d[c]>1:
            r=c
            break
    print(r)