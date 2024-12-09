class TreeNode:
    def __inti__(self,data):
        self.children = []
        self.parent = None


    def add_child(self,child):
        child.parent = self
        self.children.append(child)

def built_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode('laptop')
    root.add_child(laptop)
    return root


if __name__ == '__main__' :
    root = built_product_tree()
    print(root)
    pass

