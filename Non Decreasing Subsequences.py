# Non Decreasing Subsequences
# You are given an array of integers of size N. Find the total number of non-decreasing subsequences present in the array.




# def solve(arr,idx,n,prev):
#     if idx==n:
#         return 1
#     cnt=0
#     if arr[idx]>=prev:
#         cnt+=solve(arr,idx+1,n,arr[idx])
#     cnt+=solve(arr,idx+1,n,prev)
#     return cnt


# def solve(arr,n):
#     cnt=0
#     for i in range(2**n):
#         l=[]
#         temp=-float("inf")
#         flag=True
#         for j in range(n):
#             if ((i>>j)&1)==1:
#                 if temp>arr[j]:
#                     flag=False
#                     break
#                 else:
#                     temp=arr[j]
#         if flag==True:
#             cnt+=1
#     return cnt
    
int_min=-float("inf")
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(solve(arr,0,n))
