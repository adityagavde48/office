class Node:
    def __init__(self,data):
      self.data=data
      self.next=None
class Linkedlist:
    def __init__(self):
      self.head=None
      self.size=0
    def __len__(self):
      return len(self.size)
    def add(self,item):
      newNode=Node(item)
      newNode.next=self.head
      self.head=newNode
      self.size+=1
    def contains(self,target):
      curNode=self.head
      while curNode is not None and curNode.data !=target:
       curNode=curNode.next
      return curNode is not None
    def traversal(self):
      curNode=self.head
      while curNode is not None:
       if(curNode.next !=None):
          print(curNode.data,end="->")
       else:
          print(curNode.data,end=".\n")
       curNode=curNode.next

    def removeNode(self,target):
      predNode=None
      curNode=self.head
      while curNode is not None and curNode.data !=target:
       predNode=curNode
       curNode=curNode.next
      if curNode is not None:
         if curNode is self.head:
            self.head=curNode.next
         else:
            predNode.next=curNode.next

Llist=Linkedlist()

Llist.add(10)
Llist.add(20)
Llist.add(30)
Llist.add(40)
Llist.add(50)
Llist.add(60)
print("Linkled list data:")
Llist.traversal()
print(Llist.contains(55))
Llist.removeNode(10)
Llist.removeNode(60)
Llist.removeNode(30)
print("after removal")
print("Linkled list data:")
Llist.traversal()
