class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None

    def prepend(self,val):
        newnode=node(val)
        newnode.next=self.head
        self.head=newnode
