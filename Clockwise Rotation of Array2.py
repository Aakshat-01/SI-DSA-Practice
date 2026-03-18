# Clockwise Rotation of Array


def reverse(l,h,arr):
    while(l<h):
        arr[l],arr[h]=arr[h],arr[l]
        l+=1
        h-=1

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    k=k%n
    reverse(0,n-1,arr)
    reverse(0,k-1,arr)
    reverse(k,n-1,arr)
    print(*arr)