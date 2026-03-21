# Toggle 01
# Consider an array of 0's of size N. You are given Q queries of the following types:
# 1 idx: Toggle the element present at the given index. If the element is 0, make it 1 and vice versa.
# 2 idx: Print the distance of the nearest 1 from the given index.


t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    arr=[0]*n
    for _ in range(q):
        k,i=map(int,input().split())
        if k==1:
            arr[i]=1-arr[i]
        else:
            ans=float("inf")
            for j in range(n):
                if arr[j]==1:
                    ans=min(ans,abs(j-i))
            if ans==float("inf"):
                print("-1")
            else:
                print(ans)