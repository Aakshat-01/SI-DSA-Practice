# A power B 
# Given 2 numbers - A and B, evaluate AB.

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    m=1000000007
    pow=1
    while(b!=0):
        if((b&1)==1):
            pow=(pow*a)%m
        a=(a*a)%m
        b=b>>1
    print(pow)