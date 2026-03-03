# Flip Bits
# You are given two numbers A and B. 
# Write a program to count the number of bits to be flipped to change the number A to the number B. 
# Flipping a bit of a number means changing a bit from 1 to 0 or vice versa.


t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    x=a^b
    c=0
    while x>0:
        x=x&(x-1)
        c+=1
    print(c)