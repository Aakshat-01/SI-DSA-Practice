# Equal 0s and 1s
# You are given an array of 0's and 1's. Find the length of the longest subarray which has an equal number of 0's and 1's.


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr=[-1 if x==0 else 1 for x in arr]
    pp=[0]*n
    pp[0]=arr[0]
    hm={0:-1}
    ans=0
    for i in range(0,n):
        pp[i]=pp[i-1]+arr[i]
        if pp[i] in hm:
            ans=max(ans,i-hm[pp[i]])
        else:
            hm[pp[i]]=i 
    print(ans)
