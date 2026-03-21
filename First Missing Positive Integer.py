# First Missing Positive Integer
# You are given an array of integers of size N. Find the first positive integer that is missing from the array.
# Note: 
#  Try solving in O(N) time without using any additional space, except the input array.


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr=[x for x in arr if x>0]
    arr=list(set(arr))
    arr.sort()
    n=len(arr)
    l,h=0,n-1
    ans=n+1
    while(l<=h):
        mid=(l+h)//2
        if mid+1 == arr[mid]:
            l=mid+1
        else:
            ans=mid+1
            h=mid-1
    print(ans)
        