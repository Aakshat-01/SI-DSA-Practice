# Guess the Problem - 1 
# Understand the problem statement from the given sample input and output.


t=int(input())
for _ in range(t):
    a,b=map(str,input().split())
    c=""
    for i in range(len(b)):
        if b[i] not in a:
            c+=b[i]
    print(c)