# Enclosing Substring
# Given 2 strings A and B, find the smallest substring of B having all the characters of A, in any order.


def check(cntA,cntB):
    for i in range(26):
        if cntA[i]<cntB[i]:
            return False
    return True

def solve(a,b):
    m=len(a)
    n=len(b)
    cntB=[0]*26
    for i in a:
        cntB[ord(i)-ord('a')]+=1
    p1=p2=0
    cntA=[0]*26
    ans=float("inf")
    while p2<n:
        cntA[ord(b[p2])-ord('a')]+=1
        while(check(cntA,cntB)):
            ans=min(ans,p2-p1+1)
            cntA[ord(b[p1])-ord('a')]-=1
            p1+=1
        p2+=1
    return ans if ans != float("inf") else -1

t=int(input())
for _ in range(t):
    a,b=input().split()
    print(solve(a,b))