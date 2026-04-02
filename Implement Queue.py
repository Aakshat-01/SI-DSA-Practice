# Implement Queue
# Implement the Queue data structure and perform Enqueue / Dequeue operations.

# Note: 
#  Do not use any inbuilt functions / libraries for the Queue.


t=int(input())
queue=[]
for _ in range(t):
    s=input()
    if "Enqueue" in s:
        queue.append(int(s[7:]))
    else:
        if queue:
            print(queue.pop(0))
        else:
            print("Empty")