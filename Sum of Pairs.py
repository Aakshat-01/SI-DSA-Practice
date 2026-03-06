# Sum of Pairs 
# Given an array of integers and a number K, check if there exist a pair of indices i,j s.t. a[i] + a[j] = K and i!=j.


t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    found=False
    l,r=0,n-1
    while(l<r):
        s=arr[l]+arr[r]
        if s==k:
            found=True
            break
        elif s<k:
            l+=1
        else:
            r-=1
    if found:
        print("True")
    else:
        print("False")