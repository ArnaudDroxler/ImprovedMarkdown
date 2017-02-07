import AST
from AST import addToClass
from functools import reduce

@addToClass(AST.DocumentNode)
def execute(self,html):
    for c in self.children:
        c.execute(html)

@addToClass(AST.WordNode)
def execute(self,html):
    html.write(self.text)

@addToClass(AST.TagNode)
def execute(self,html):
    if self.type == "ITALIC":
        html.write("<i>" + self.text + "</i>")
    if self.type == "BOLD":
        html.write("<b>" + self.text + "</b>")
    if self.type == "SEPARATION_LINE":
        html.write("<hr>")
    if self.type == "FLUO":
        html.write("<em>" + self.text + "</em>")
    if self.type == "PARAGRAPHE":
        html.write("</p><p>")

@addToClass(AST.ImageNode)
def execute(self,html):
    html.write("<img src=" + self.link + " alt=" + self.text + ">")

@addToClass(AST.LinkNode)
def execute(self,html):
    html.write("<a href="+self.link+">"+ self.text +"</a>")

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
