# Rearrange Sequence - 3 
# You are given an array of size N containing integers. Find the size of the largest subarray that can be rearranged to form a contiguous sequence.
# A contiguous sequence means that the difference of adjacent elements should be 0 or 1.



def solve(arr,n):
    ans=0
    for i in range(n):
        mini,maxi=float("inf"),-float("inf")
        s=set()
        for j in range(i,n):
            mini=min(arr[j],mini)
            maxi=max(arr[j],maxi)
            s.add(arr[j])
            if maxi-mini<=len(s)-1:
                ans=max(ans,j-i+1)
    return ans

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(solve(arr,n))