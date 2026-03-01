# Reverse Bits 
# Given a number, reverse the bits in the binary representation (consider 32-bit unsigned data) of the number, 
# and print the new number formed.


t=int(input())
for _ in range(t):
    n=int(input())
    rev=0
    for i in range(32):
        bit=n&1
        rev=rev<<1
        rev=rev | bit
        n=n>>1
    print(rev)