# Pair with Difference K 
# You are given an integer array and an integer K. 
# You have to tell if there exists a pair of integers in the given array such that ar[i]-ar[j]=K and i≠j.



t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    f="false"
    s=set()
    for x in arr:
        if (x-k) in s or (x+k) in s:
            f="true"
            break
        s.add(x)
    print(f)