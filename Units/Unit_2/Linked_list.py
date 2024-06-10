
#Python Linked List Defintion guide



#creating a ListNode class
class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    #Method to Prepend a node at beginning of a Linked List
    def insertAtBegin(self,data): # how to prepend a new_node on to a list
        #create New Node
        new_Node=ListNode(data)
        if self.head is None:
            new_Node.next=self.head
            self.head=new_Node
        else:
            self.head=new_Node
            self.tail=new_Node


    def insertAtEnd(self,data):
        new_Node=ListNode(data)
        if self.head:
            self.tail.next =new_Node
            self.tail=new_Node
        else:
            self.head=new_Node
            self.tail=new_Node


    def search(self,data):
        current_node=self.head
        while(current_node is not None):
            if current_node.val == data:
                return True
            else:
                current_node = current_node.next
            return False

    def __str__(self):
        traverse_list=self.head
        LinkedList_values=[]
        while traverse_list:
            LinkedList_values.append(traverse_list.data)
            traverse_list=traverse_list.next
        return f"The Linked List values is {LinkedList_values}"

    def get_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            print(f"current value of slow {slow.data}")
            print(f"current value of fast {fast.data}")
            fast = fast.next.next
            if fast:
                print(f"current value of fast {fast.data}")

        return slow


#Slow and fast pointer technique (for linked lists Variation of Two pointers)
#is in Linear time O(N)

#Idea 2 pointers Fast Pointer Slow pointer

#on each iteration of the loop we shift the fast pointer by 2 spaces/node
#and we shift the slow pointer by 1 space/node
#keep traversering/iteration until the fast pointer reaches the end of the linked list

#Fast Pointer
#fast=fast.next.next

# Slow pointer
#slow=slow.next



if __name__ == '__main__':
    ll_cool_j=LinkedList()
    ll_cool_j.insertAtEnd(1)
    ll_cool_j.insertAtEnd(2)
    ll_cool_j.insertAtEnd(3)
    ll_cool_j.insertAtEnd(4)
    print(ll_cool_j)
    ll_cool_j.get_middle()


