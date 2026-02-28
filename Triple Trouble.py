#Triple Trouble 
#Given an array of size 3X+1, where every element occurs three times, except one element, which occurs only once.
#Find the element that occurs only once.


t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    d={}
    for i in l:
        d[i]=d.get(i,0)+1
    for k,v in d.items():
        if v==1:
            print(k)

