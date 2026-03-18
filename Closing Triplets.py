# Closing Triplets
# Given three arrays A, B, and C, choose a triplet a, b, c such that a, b, and c belong to the arrays A, B, and C 
# respectively, such that the absolute difference between the maximum and minimum element of the chosen triplet is
#  minimized, i.e., minimize |max(a,b,c)-min(a,b,c)|.


def triplets(a,b,c,n1,n2,n3):
    p1=p2=p3=ans=0
    res=float("inf")
    while(p1<n1 and p2<n2 and p3<n3):
        k1,k2,k3=a[p1],b[p2],c[p3]
        maxi=max(k1,k2,k3)
        mini=min(k1,k2,k3)
        ans=maxi-mini
        res=min(ans,res)
        if mini==k1:
            p1+=1
        elif mini==k2:
            p2+=1
        else:
            p3+=1
    return res

t=int(input())
for _ in range(t):
    n1=int(input())
    A=list(map(int,input().split()))
    n2=int(input())
    B=list(map(int,input().split()))
    n3=int(input())
    C=list(map(int,input().split()))
    A.sort()
    B.sort()
    C.sort()
    print(triplets(A,B,C,n1,n2,n3))

