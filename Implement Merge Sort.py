# Implement Merge Sort 
# Given an array of size N, implement Merge sort.


def mergeSort(arr,l,h):
    if l>=h:
        return 
    mid=(l+h)//2
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,h)
    merge(arr,l,mid,h)
    print(*arr)


def merge(arr,l,mid,h):
    p1,p2=l,mid+1
    temp=[]
    while(p1<=mid and p2<=h):
        if arr[p1]<=arr[p2]:
            temp.append(arr[p1])
            p1+=1
        else:
            temp.append(arr[p2])
            p2+=1
    while p1<=mid:
        temp.append(arr[p1])
        p1+=1
    while p2<=h:
        temp.append(arr[p2])
        p2+=1
    for i in range(len(temp)):
        arr[l+i]=temp[i]
n=int(input())
arr=list(map(int,input().split()))
mergeSort(arr,0,n-1)
