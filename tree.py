class Tree():
    def __init__(self,nodes):
        self.nodes = nodes 
        self.leftnode = None 
        self.rightnode = None 

def preorder(root):
    print (root.nodes)
    if root.leftnode != None: 
        preorder(root.leftnode)
    if root.rightnode != None: 
        preorder(root.rightnode)

def postorder(root):
    if root.leftnode != None:
        postorder(root.leftnode)
    if root.rightnode != None:
        postorder(root.rightnode)
    print(root.nodes)

def inorder(root):
    if root.leftnode != None:
        inorder(root.leftnode)
    print(root.nodes)
    if root.rightnode != None:
        inorder (root.rightnode)



def countnodes(root):
    if root == None:
        return 0 
    else:
       return 1 + countnodes(root.leftnode) + countnodes (root.rightnode)


A = Tree("A")
A.leftnode = Tree("B")
A.rightnode = Tree ("C")
A.leftnode.leftnode = Tree("D")
A.leftnode.rightnode = Tree ("E")

print ("Preorder")

preorder(A)

print("Postorder")
postorder(A)

print("Inorder")
inorder(A)


print("Total number of nodes:")
totalnodes = countnodes(A)
print(totalnodes)



        

