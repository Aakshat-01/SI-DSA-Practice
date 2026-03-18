# Collecting Water
# You are given the heights of N buildings. All the buildings are of width 1 and are adjacent to each other with 
# no empty space in between. Assume that it is raining heavily, and as such water will be accumulated on top of 
# certain buildings. Your task is to find the total amount of water accumulated.


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    lm=[float("-inf")]*n
    rm=[float("-inf")]*n
    lm[0]=arr[0]
    for i in range(1,n):
        lm[i]=max(lm[i-1],arr[i])
    rm[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        rm[i]=max(rm[i+1],arr[i])
    ans=0
    for i in range(1,n-1):
        ans+=min(lm[i],rm[i])-arr[i]
    print(ans)

