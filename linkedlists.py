class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None
    def remove(self,data,previousNode):
        if self.data==data:
            previousNode.nextNode=self.nextNode
            del self.data
            del self.nextNode
        else:
            if self.nextNode is not None:
                self.nextNode.remove(self,data)
class LinkedList(object):
    def __init__(self):
        self.head=None
        self.counter=0
    def insertstart(self,data):
        self.counter+=1
        newNode=Node(data)
        if not self.head:
            self.head=newNode
        else:
            newNode=self.head
            self.head=newNode
    def size(self):
            return self.counter
    def insertend(self,data):
            newNode=Node(data)
            actualNode=self.head
            print("mohit")
            while (actualNode.nextNode is not None):
                actualNode=actualNode.nextNode
            actualNode.nextNode=newNode
    def remove(self,data):
            if self.head:
                if data==self.head.data:
                    self.head=self.head.nextNode
                else:
                    self.head.remove(data,self.head)
lk = LinkedList()
print("mogit")
lk.insertend(10)