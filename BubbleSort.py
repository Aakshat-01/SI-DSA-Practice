# Bubble Sort 
# Implement Bubble Sort and print the total number of swaps involved to sort the array.


t=int(input())
def bubbleSort(arr,n):
    c=0
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                c+=1
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return c
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    print(bubbleSort(l,n))