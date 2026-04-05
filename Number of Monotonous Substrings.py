# Number of Monotonous Substrings 
# Given a string S, print the number of monotonous substrings of S. Since the answer may be too large, 
# print answer modulo 1e9 + 7. A string is monotonous if all the characters of the string are the same.


t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    cnt,ans=1,0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            cnt+=1
        else:
            ans+=(cnt*(cnt+1)//2)
            cnt=1
    ans+=(cnt*(cnt+1)//2)
    print(ans%(10**9+7))