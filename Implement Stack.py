# Implement Stack
# Implement the Stack data structure and perform push / pop operations.

# Note: 
#  Do not use any inbuilt functions / libraries for the Stack.


t=int(input())
stack=[]
for _ in range(t):
    s=input()
    if "push" in s:
        stack.append(int(s[5:]))
    elif "pop" in s:
        if stack:
            a=stack.pop()
            print(a)
        else:
            print("Empty")