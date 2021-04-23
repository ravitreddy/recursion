class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        self.root=self.insert1(self.root,data)

    def insert1(self,node,data):
        temp=Node(data)
        if not node:
            return temp
        if data<node.data:
            node.left=self.insert1(node.left,data)
        else:
            node.right=self.insert1(node.right,data)
        return node

    def inOrder(self):
        self.inOrder1(self.root)
        print()
    def inOrder1(self,node):
        if not node:
            return
        self.inOrder1(node.left)
        print(node.data, end=" ")
        self.inOrder1(node.right)

def main():
    ar=[int(i) for i in input().split()]
    bst=BST()
    for k in ar:
        bst.insert(k)
    bst.inOrder()
main()
