# Product of 2 Matrices 
# Given 2 matrices, find their product.



t=int(input())
for _ in range(t):
    n1,m1=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(n1)]
    n2,m2=map(int,input().split())
    b=[list(map(int,input().split())) for _ in range(n2)]
    c=[[0]*m2 for _ in range(n1)]
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                c[i][j]+=a[i][k]*b[k][j]
    for r in c:
        print(*r)