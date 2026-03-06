# Sort 0s and 1s 
# You are given an array of 0's and 1's. Sort the array in ascending order and print it.
# Note: 
# Solve using two-pointer technique.


def solve(arr,n):
    l,r=0,n-1
    while(l<r):
        if arr[l]==1 and arr[r]==0:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
        elif arr[l]==0:
            l+=1
        else:
            r-=1


t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    solve(l,n)
    print(*l)