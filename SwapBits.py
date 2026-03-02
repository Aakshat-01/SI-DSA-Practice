# Swap Bits 
# Given a number, swap the adjacent bits in the binary representation of the number, 
# and print the new number formed after swapping.


t=int(input())
for _ in range(t):
    n=int(input())
    ans=p=0
    for _ in range(16):
        bit1=(n>>p)&1
        bit2=(n>>(p+1))&1
        ans+=(bit1<<(p+1))
        ans+=(bit2<<(p))
        p+=2
    print(ans)