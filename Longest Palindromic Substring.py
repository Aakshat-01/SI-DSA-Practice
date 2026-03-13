# Longest Palindromic Substring
# Given a string, find the length of the Longest Palindromic Substring (LPS).


def solve(s,n):
    res=0
    for i in range(n):
        p1,p2=i-1,i+1
        ans=1
        while(p1>=0 and p2<n and s[p1]==s[p2]):
            p1-=1
            p2+=1
            ans+=2
        res=max(res,ans)

        p1,p2=i,i+1
        ans=0
        while(p1>=0 and p2<n and s[p1]==s[p2]):
            p1-=1
            p2+=1
            ans+=2
        res=max(res,ans)
    return res

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    print(solve(s,n))