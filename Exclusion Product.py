# Exclusion Product
# You are given an array of integers of size N. Create a new array such that 
# the element at an index i in the new array is the product of all the elements of the original array 
# except the element present at index i.

m = 10**9 + 7
def solve(arr, n):
    p = [0]*n
    ss = [0]*n
    b = [0]*n
    p[0] = arr[0]
    for i in range(1, n):
        p[i] = (p[i-1]*arr[i]) % m
    ss[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        ss[i] = (ss[i+1]*arr[i]) % m
    b[0] = ss[1]
    b[n-1] = p[n-2]
    for i in range(1, n-1):
        b[i] = (p[i-1]*ss[i+1]) % m
    return b

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    b = solve(arr, n)
    print(*b)
