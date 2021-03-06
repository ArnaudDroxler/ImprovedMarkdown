import AST
from AST import addToClass
from functools import reduce
import re

import sys
import os

from parser1 import parse

vars ={}

@addToClass(AST.DocumentNode)
def execute(self,html):
    for c in self.children:
        c.execute(html)

@addToClass(AST.WordNode)
def execute(self,html):
    text = self.text
    text = re.sub('é', '&eacute;', text)
    html.write(text + " ")

@addToClass(AST.OlNode)
def execute(self,html):
    html.write("<li>" + self.text + "</li> ")

@addToClass(AST.OlListNode)
def execute(self,html):
    html.write("<ol>")
    self.parent.execute(html)
    for c in self.children:
        c.execute(html)
    html.write("</ol>")

@addToClass(AST.UlNode)
def execute(self,html):
    html.write("<li>" + self.text + "</li> ")

@addToClass(AST.UlListNode)
def execute(self,html):
    html.write("<ul>")
    self.parent.execute(html)
    for c in self.children:
        c.execute(html)
    html.write("</ul>")

@addToClass(AST.TagNode)
def execute(self,html):
    if self.type == "ITALIC":
        html.write("<i>" + self.text + "</i> ")
    if self.type == "BOLD":
        html.write("<b>" + self.text + "</b> ")
    if self.type == "SEPARATION_LINE":
        html.write("<hr>")
    if self.type == "FLUO":
        html.write("<mark>" + self.text + "</mark> ")
    if self.type == "PARAGRAPHE":
            html.write("</br>")
    if self.type == "TITLE1":
            html.write("<h1>" +self.text+"</h1> ")
    if self.type == "TITLE2":
            html.write("<h2>"+self.text+ "</h2>  ")
    if self.type == "TITLE3":
            html.write("<h3>"+self.text+ "</h3>")


@addToClass(AST.ImageNode)
def execute(self,html):
    html.write("<img src=" + self.link + " alt=" + self.text + ">")

@addToClass(AST.LinkNode)
def execute(self,html):
    html.write("<a href="+self.link+">"+ self.text +"</a> ")

@addToClass(AST.AssignNode)
def execute(self,html):
    vars[self.children[0].tok] = self.children[1].execute(html)

@addToClass(AST.TokenNode)
def execute(self,html):
    if isinstance(self.tok, str):
        try:
            return vars[self.tok]
        except KeyError:
            pass
    return self.tok


@addToClass(AST.PrintNode)
def execute(self,html):
    html.write(str(self.children[0].execute(html)))

if __name__ == "__main__":
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    name = os.path.splitext(sys.argv[1])[0]+'.html'

    html = open(name,'w')
    html.write("<!DOCTYPE html><html><head><meta charset=\"utf-8\"><title>" "</title></head><body><p>")
    ast.execute(html)
    html.write("</p></body></html>")
    html.close()
