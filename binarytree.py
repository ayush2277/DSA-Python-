class BinarySearchNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def add_child(self,data):
        if data == self.data:
           return
        
        if data < self.data:
            # add element to left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchNode(data)


    def in_Order_traversal(self):
        
        elements = []
        if self.left:
            elements += self.left.in_Order_traversal()
      
        elements.append(self.data)
        #visit right node
        if self.right:
            elements += self.right.in_Order_traversal()

        return elements



    
    def search_element(self,val):
        if self.data == val:
             return True
        if val < self.data:
            if self.left:
               return self.left.search_element(val)
        if val > self.data:
            if self.right:
                return self.right.search_element(val)
            else:
                return False
    
    def max_number(self):
      if self.right == None:
        return self.data 
      return self.right.max_number()

    def min_number(self):
        if self.left == None:
            return self.data
        return self.left.min_number()

    def delete(self,val):
        if val < self.data:
            if self.left:
               self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            max = self.left.max_number()
            self.data = max
            self.left = self.left.delete(min)
        return self

            


        


            
            
def build_tree(elements):
    root = BinarySearchNode(elements[0])
    for i in range (1,len(elements)):
        root.add_child(elements[i])

    return root
    

if __name__ == '__main__':
    numbers = [13,2,10,6,7,89,23]
    numbers_tree = build_tree(numbers)
    # print(numbers_tree.max_number())
    # print(numbers_tree.min_number())
    print (numbers_tree.in_Order_traversal())
    numbers_tree.delete(23)
    print (numbers_tree.in_Order_traversal())

    

    
 
