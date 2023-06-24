class Node:
 
   def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_end(self,newVal):
        newNode=Node(newVal)
        if self.head==None:
            self.head=newNode
            return
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=newNode


    def Print_the_LL(self):
        temp = self.head
        if(temp != None):
          print("\nThe linked list elements are:", end=" ")
          while (temp != None):
            print(temp.val, end=" ")
            temp = temp.next
        else:
          print("The list is empty.")
    def detect_loop(self):
        slow=self.head
        fast=self.head
        while(fast):
            if slow==fast:
                print("\nA loop has been detected in the linked list ")
                return
            slow=slow.next
            fast=fast.next


newList = LinkedList()
newList.insert_at_the_end(1)
newList.insert_at_the_end(2)
newList.insert_at_the_end(3)
newList.insert_at_the_end(4)
newList.Print_the_LL()
print("\n")
newList.head.next.next.next.next=newList.head.next
newList.detect_loop()