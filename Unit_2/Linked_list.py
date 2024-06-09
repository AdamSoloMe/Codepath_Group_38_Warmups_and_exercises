
#Python Linked List Defintion guide



#creating a ListNode class
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None


class LinkedList:
    def __init__(self,val):
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
        if self.head is None:
            self.tail.next= new_Node
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






