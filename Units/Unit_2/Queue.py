class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class My_Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def enqueue(self,data):
        new_Node=Node(data)
        if self.head ==None:
            self.head=new_Node
            self.tail=new_Node
            self.size=1
        else:
            self.tail.next=new_Node
            self.tail=new_Node
            self.size+=1


    def dequeue(self):
        if self.head:
            removed_node=self.head
            self.size -= 1
            self.head=self.head.next
            print(f"the node value dequeued is {removed_node.data}")
            return removed_node

    def __repr__(self):
        traverse_list=self.head
        queue_values=[]
        while traverse_list != None:
            print(traverse_list.data)
            queue_values.append(traverse_list.data)
            traverse_list=traverse_list.next
        return f" the values of the queue is {queue_values} and the size of the queue is {self.size} "


if __name__ == '__main__':
    ll_q= My_Queue()
    ll_q.enqueue(1)
    ll_q.enqueue(2)
    ll_q.enqueue(4)
    ll_q.enqueue(3)
    print(ll_q)

