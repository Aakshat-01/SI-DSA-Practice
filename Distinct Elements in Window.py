# Distinct Elements in Window
# Given an array of integers and a window size K, 
# find the number of distinct elements in every window of size K of the given array.


def solve(arr,k,n):
    hm={}
    for i in range(k):
        hm[arr[i]]=hm.get(arr[i],0)+1
    res=[len(hm)]
    for i in range(k,n):
        hm[arr[i-k]]-=1
        if hm[arr[i-k]]==0:
            del hm[arr[i-k]]
        hm[arr[i]]=hm.get(arr[i],0)+1
        res.append(len(hm))
    return res

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    ans=solve(arr,k,n)
    print(*ans)