# Protective Villagers 
# In a remote village, there is a new long marketplace with N stalls, all lined up along a straight path at positions 
# x1, x2, x3,..., xN. A group of villagers, represented by C individuals, are highly protective of their personal space 
# and tend to get into disputes when placed too close to one another. To maintain peace, the village leader wants to 
# allocate the villagers to these stalls in a way that maximizes the minimum distance between any two of them.

# Input Format
# The first line of input contains T - the number of test cases. It is followed by 2T lines, the first line contains 2 
# space-separated integers - N and C. The second contains N integers, where ith integer denotes xi, the location of the 
# ith stall.

# Output Format
# For each test case, print the largest minimum distance possible, separated by a new line.


def solve(arr, n, c):
    arr.sort()
    l=0
    h=arr[-1]-arr[0]
    ans=0
    while(l<=h):
        mid=(l+h)//2
        if(check(arr,n,mid,c)):
            ans=mid
            l=mid+1
        else:
            h=mid-1
    return ans

def check(arr,n,mid,c):
    cnt=1
    l=arr[0]
    for i in range(1,n):
        if(arr[i]-l>=mid):
            cnt+=1
            l=arr[i]
    return cnt>=c

t=int(input())
for _ in range(t):
    n,c=map(int,input().split())
    arr=list(map(int,input().split()))
    print(solve(arr,n,c))

    