class Tree():
    def __init__(self,value):
        self.data=value
        self.children=[]

    def addChild(self,obj):
        self.children.append(obj)

class Node():
    def __init__(self,value):
        self.name=value
        self.children=[]

mynode= Node('child')

mytree=Tree('parent')
mytree.addChild(Node('child'))

print(mytree.children)