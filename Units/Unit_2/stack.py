import queue
from collections import deque


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Stack:
    def __init__(self):
        self.top= None
        self.size=0

    def push(self,data):
        new_Node=Node(data)
        if self.top is not None:
            new_Node.next=self.top
        self.top=new_Node
        self.size+=1

    def pop(self):
        if self.top is None:
            return
        else:
            popped_node=self.top
            self.size -= 1
            self.top=self.top.next
            popped_node.next=None
            return popped_node.data

    def peek(self):
        if self.top is not None:
            return self.top.data
        else:
            return None

    def __repr__(self):
        traverse_stack=self.top
        stack_values=[]
        while traverse_stack:
            stack_values.append(traverse_stack.data)
            traverse_stack=traverse_stack.next
        return f" the stack values are {stack_values} and current size of the stack is {self.size}"



from queue import LifoQueue
if __name__ == '__main__':

    stack=deque()
    for i in range(21):
        stack.append(i)

    while stack: # while the stack is not empty
        print(f"the value of the stack are {stack.pop()}")

    ll_stack=Stack()
    ll_stack.push(1)
    ll_stack.push(2)
    ll_stack.push(3)
    print(ll_stack)
    ll_stack.pop()
    print(ll_stack)










