# Quadruples of XOR
# You are given 4 arrays of integers: A, B, C, and D. You have to find the number of quadruples (i, j, k, l) 
# such that A[i]^B[j]^C[k]^D[l] = 0, where ^ is the bitwise XOR operator.


t=int(input())
for _ in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    C=list(map(int,input().split()))
    D=list(map(int,input().split()))
    f={}
    for a in A:
        for b in B:
            f[a^b]=f.get(a^b,0)+1
    ans=0
    for c in C:
        for d in D:
            x=c^d
            ans+=f.get(x,0)
    print(ans)