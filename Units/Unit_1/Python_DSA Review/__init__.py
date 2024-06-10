from collections import deque
if __name__ == '__main__':
    # #python stack
    # stack=[x for x in range(0,10)]
    #
    # while stack:
    #     print(stack.pop())
    #
    # #python Queue(Deque)
    # Queue=deque([x for x in range(10)])
    # while Queue:
    #     print(Queue.popleft())

    queue=deque()
    queue.append(0)
    queue.append(1)
    for i in range(4):
        a= queue.popleft()
        b= queue.popleft()
        queue.append(b)
        queue.append(a+b)
        print(a)


    stack=[x for x in range(10,0,-1)]
    while stack:
        print(stack.pop())

    char_map = {")": "(", "}": "{", "]": "["}
    for char in "()[]{}":
        if char in char_map.values():
            stack.append(char)

    print(stack)