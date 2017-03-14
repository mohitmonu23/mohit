# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:57:33 2017

@author: MOHIT
"""

class Node(object):
    def __init__(self,data=None,next_node=None):
      self.data=data
      self.next_node=next_node
    def set_next(self,new_node):
        self.next_node=new_node
    def remove(self,data,previousNode):
        if self.data==data:
            previousNode.next_node=self.next_node
            del self.data
            del self.next_node
        else:
            if(self.next_node is not None):
                 self.next_node.remove(data,self)
class LinkedLink(object):
    def __init__(self,head=None):
        self.head=head
    def insert(self,data):
        newNode=Node(data)
        newNode.set_next(self.head)
        self.head=newNode
    def travel(self):
        actualNode=self.head
        while actualNode is not None:
            print(actualNode.data)
            actualNode=actualNode.next_node
    def search(self,data):
        flag=0
        actualNode=self.head
        if self.head is not None:
            if self.head.data == data:
                print(self.head)
            else:
                while(actualNode is not None):
                    if(actualNode.data==data):
                        print(actualNode)
                        break;
                    else:
                        actualNode=actualNode.next_node
        if(flag==0):
            print("no element")
    def delete(self,data):
        if self.head:
            if data == self.head.data:
                self.head=self.head.next_node
            else:
                self.head.remove(data,self.head)
lk=LinkedLink()
lk.insert(10)
lk.insert(50)
lk.insert(20)
lk.insert(30)
lk.insert(5)
lk.search(5)
lk.travel()
lk.delete(20)
lk.travel()