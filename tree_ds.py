class Node:
    def __init__(self,data):
        self.data=data
        self.l_child=None
        self.r_child=None
        
class Tree:
    def __init__(self):
        self.root=None

cl=Tree()
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(10)
n6=Node(20)
n7=Node(30)

print(n1)

obj=Tree()
obj.root = n1
print(obj.root)



n1.r_child=n2
n1.l_child=n3
n2.r_child=n4
n2.l_child=n5
n3.r_child=n6
n3.l_child=n7

print(n1.r_child)
print(n1.l_child)
print(n2.r_child)
print(n2.l_child)
print(n3.r_child)
print(n3.l_child)

     
        
    