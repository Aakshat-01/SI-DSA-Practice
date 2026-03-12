# Finding the Floor 
# Given an array, you have to find the floor of a number x. 
# The floor of a number x is nothing but the largest number in the array less than or equal to x.


def floor(arr,n,x):
    l,h,ans=0,n-1,-2147483648
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]<=x:
            ans=arr[mid]
            l=mid+1
        else:
            h=mid-1
    return ans

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
q=int(input())
for _ in range(q):
    num=int(input())
    print(floor(arr,n,num))