# Clockwise Rotation of Array
# Given an array, rotate it by K times in a clockwise direction.


t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    k=k%n
    new=[0]*n
    new[0:k]=arr[n-k:]
    new[k:]=arr[:n-k]
    print(*new)