class BST:
    def __init__(self,key):
        self.key = key
        self.l_child = None
        self.r_child = None
        
    def insert_node(self,data):
        if self.key is None:
            print("empty")
            return
        if self.key == data:
            print("data element is already present")
            return
        if self.key > data:
            if self.l_child:
                self.l_child.insert_node(data)
                
            else:
                self.l_child = BST(data)
        else:
            if self.r_child:
                self.r_child.insert_node(data)
            
            else:
                self.r_child = BST(data)
                
                
                
root = BST(45)
root.insert_node(30)
root.insert_node(50)

print(root)