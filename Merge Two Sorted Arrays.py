# Merge Two Sorted Arrays 
# You are given two sorted integer arrays A and B of size N and M respectively. 
# Print the entire data in sorted order.


def solve(a,b,n,m):
    p1,p2=0,0
    while(p1<n and p2<m):
        if a[p1]<b[p2]:
            print(a[p1],end=" ")
            p1+=1
        else:
            print(b[p2],end=" ")
            p2+=1
    while(p1<n):
        print(a[p1],end=" ")
        p1+=1
    while(p2<m):
        print(b[p2],end=" ")
        p2+=1

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
solve(a,b,n,m)