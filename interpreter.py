import AST
from AST import addToClass
from functools import reduce

def execute(node,html):
    while node:
        if node.__class__ == AST.DocumentNode:
            print("Document")
        elif node.__class__ == AST.WordNode:
            print("Word")
            html.write(node.text)
        elif node.__class__ == AST.TagNode:
            print("Tag")
            #html.write(node.text)
        if node.children:
            print("Next")
            node = node.children[0]
        else:
            print("None")
            node = None


@addToClass(AST.DocumentNode)
def execute(self,html):
    print("DocumentNode")
    for c in self.children:
        c.execute(html)

@addToClass(AST.WordNode)
def execute(self,html):
    print("WordNode")
    html.write(self.text)

@addToClass(AST.TagNode)
def execute(self,html):
    print("TagNode")

@addToClass(AST.ImageNode)
def execute(self,html):
    print("ImageNode")

@addToClass(AST.LinkNode)
def execute(self,html):
    print("LinkNode")

@addToClass(AST.ReferenceNode)
def execute(self,html):
    print("ReferenceNode")


if __name__ == "__main__":

    import sys
    import os

    from parser1 import parse

    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    name = os.path.splitext(sys.argv[1])[0]+'.html'

    html = open(name,'w')
    html.write("<!DOCTYPE html><html><head><meta charset=\"utf-8\"><title></title></head><body>")
    ast.execute(html)
    html.write("</body></html>")
    html.close()
