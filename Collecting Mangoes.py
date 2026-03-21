# Collecting Mangoes
# One day after the storm Mina went to pick up mangoes in the garden with a basket. She began to pick up mangoes
# from the garden. And if she wants, she can throw away the last picked-up mango from the basket. In this way, 
# Mina kept picking up mangoes. She brought you with her to keep track of the biggest size of mango in the basket 
# at that time. At any moment Mina can ask you about the biggest size of mango. Your job is to help Mina.
# Since you are a good programmer, you write a program by which you are easily able to answer the questions of Mina. 
# While picking up mangoes, Mina can have 3 types of questions/instructions for you.Type 1: Put an "x" size mango in 
# the basket, which is picked up from the garden.Type 2: Throw out the last picked-up mango.Type 3: Ask for the biggest 
# mango size in the basket at that moment.


t=int(input())
for tc in range(t):
    stack=[]
    m=[]
    q=int(input())
    print(f"Case {tc+1}:")
    for _ in range(q):
        s=input()
        if "A" in s:
            x=int(s.split()[1])
            stack.append(x)
            if not m:
                m.append(x)
            else:
                m.append(max(m[-1],x))
        elif "R" in s:
            if stack:
                stack.pop()
                m.pop()
        elif "Q" in s:
            if m:
                print(m[-1])
            else:
                print("Empty")
