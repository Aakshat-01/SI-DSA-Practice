# Finding Frequency
# Given an array, you have to find the frequency of a number X.


def floorBS(arr,n,x):
    l,h,p1=0,n-1,0
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]==x:
            p1=mid
            h=mid-1
        elif arr[mid]<x:
            l=mid+1
        else:
            h=mid-1
    return p1

def ceilBS(arr,n,x):
    l,h,p2=0,n-1,-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]==x:
            p2=mid
            l=mid+1
        elif arr[mid]<x:
            l=mid+1
        else:
            h=mid-1
    return p2

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
q=int(input())
for _ in range(q):
    num=int(input())
    p1=floorBS(arr,n,num)
    p2=ceilBS(arr,n,num)
    print(p2-p1+1)




