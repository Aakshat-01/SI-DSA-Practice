# Print Right Angled Triangle Pattern
# Print a mirror image of a right-angled triangle using '*'. See examples for more details.


t=int(input())
tc=1
for _ in range(t):
    n=int(input())
    print(f"Case #{tc}:")
    tc+=1
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*i)