# Cabinets Partitioning
# You are given a job that has been divided into N tasks. The task cannot be divided any further. 
# Each of the N tasks takes Si number of seconds to complete. Your job will be completed when all your tasks are completed. 
# You have K workers at your disposal to help you complete the tasks. But as per the nature of the job, 
# a worker can only be allocated continuous tasks. A worker can work only on a single task at any given point in time
# However, the workers can work in parallel on different tasks. You have to find the minimum possible time in which 
# you can complete the job.

# Input Format
# The first line of input contains T - the number of test cases. It's followed by 2T lines. 
# The first line of each test case contains N and K - the number of tasks and available workers for the current job, 
# separated by space. The next line contains N positive integers - denoting the time taken to complete the ith task.

# Output Format
# For each test case, print the minimum possible time in which you can complete the job, separated by a new line.


def solve(arr, n, k):
    l=max(arr)
    h=sum(arr)
    ans=float("inf")
    while(l<=h):
        mid=(l+h)//2
        if(check(arr,n,mid,k)):
            ans=mid
            h=mid-1
        else:
            l=mid+1
    return ans

def check(arr,n,mid,k):
    s=0
    c=1
    for i in range(n):
        if(s+arr[i]<=mid):
            s+=arr[i]
        else:
            s=arr[i]
            c+=1
    return c<=k

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    print(solve(arr,n,k))

    