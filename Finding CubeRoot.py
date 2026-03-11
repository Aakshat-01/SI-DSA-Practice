# Finding CubeRoot
# Find the cube root of the given number. Assume that all the input test cases will be a perfect cube.
# Note: Do not use any inbuilt functions / libraries for your main logic.

def solve(n):
    sign=-1 if n<0 else 1
    n=abs(n)
    l,h=1,n
    while(l<=h):
        m=(l+h)//2
        if m*m*m==n:
            return sign*m
        elif m*m*m>n:
            h=m-1
        else:
            l=m+1

n=int(input())
for _ in range(n):
    num=int(input())
    print(solve(num))