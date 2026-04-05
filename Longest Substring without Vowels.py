# Longest Substring without Vowels
# Given a string S consisting of only lowercase characters, 
# find the length of the longest substring that does not contain any vowel.


t=int(input())
for _ in range(t):
    s=input()
    res=ans=0
    for i in range(len(s)):
        if s[i] not in "aeiou":
            ans+=1
        else:
            res=max(res,ans)
            ans=0
    res=max(res,ans)
    print(res)