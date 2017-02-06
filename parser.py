# avec parentheses et "moins unaire"

import ply.yacc as yacc
import re

import AST

from lexemes import tokens

def p_document(p):
    ''' document : sentence
    '''
    p[0] = AST.DocumentNode("DOCUMENT",p[1])

def p_sentence(p):
    ''' sentence : WORD
        | tag
        | WORD sentence
        | tag sentence'''
    try:
        p[0] = AST.SentenceNode(p[1], p[2])
    except:
        print("UN SEUL TERME")
        print(p[1])
        p[0] = AST.SentenceNode(p[1])

def p_italic(p):
    ''' tag : ITALIC '''
    text = p[1]
    text = re.sub('[\*]', '', text)
    p[0] = AST.TagNode("ITALIC",text)

def p_ol1(p):
    ''' tag : OL1
    '''
    text = p[1]
    text = re.sub('[[0-9]+\.{1}\s{1}.]', '', text)
    p[0] = AST.TagNode("OL1",text)

def p_ol2(p):
    ''' tag : OL2
    '''
    text = p[1]
    text = re.sub('[[0-9]+\.{1}[0-9]+\s{1}.]', '', text)
    p[0] = AST.TagNode("OL2",text)

def p_ol3(p):
    ''' tag : OL3
    '''
    text = p[1]
    text = re.sub('[[0-9]+\.{1}[0-9]+\.{1}[0-9]+\s{1}.]', '', text)
    p[0] = AST.TagNode("OL3",text)

def p_title3(p):
    ''' tag : TITLE3
    '''
    text = p[1]
    text = re.sub('[\#{3}\s{1}.]', '', text)
    p[0] = AST.TagNode("TITLE3",text)

def p_title2(p):
    ''' tag : TITLE2
    '''
    text = p[1]
    text = re.sub('[\#{2}\s{1}.]', '', text)
    p[0] = AST.TagNode("TITLE2",text)

def p_title1(p):
    ''' tag : TITLE1
    '''
    text = p[1]
    text = re.sub('[\#{1}\s{1}.]', '', text)
    p[0] = AST.TagNode("TITLE1",text)


def p_paragraph(p):
    ''' tag : PARAGRAPHE
    '''
    p[0] = AST.TagNode("PARAGRAPHE", "")

def p_separation_line(p):
    ''' tag : SEPARATION_LINE
    '''
    p[0] = AST.TagNode("SEPARATION_LINE", "")

def p_ul1(p):
    ''' tag : UL1
    '''
    text = p[1]
    text = re.sub('[\*]', '', text)
    p[0] = AST.TagNode("UL1",text)

def p_ul2(p):
    ''' tag : UL2
    '''
    text = p[1]
    text = re.sub('[\*]', '', text)
    p[0] = AST.TagNode("UL2",text)

def p_ul3(p):
    ''' tag : UL3
    '''
    text = p[1]
    text = re.sub('[\*]', '', text)
    p[0] = AST.TagNode("UL3",text)

def p_bold(p):
    ''' tag : BOLD
    '''
    text = p[1]
    text = re.sub('[\*\*]', '', text)
    p[0] = AST.TagNode("BOLD",text)

def p_fluo(p):
    ''' tag : FLUO
    '''
    text = p[1]
    text = re.sub('[!]', '', text)
    p[0] = AST.TagNode("FLUO",text)

def p_link(p):
    ''' tag : LINK
    '''
    text = p[1]
    tab = text.split("(")
    print(tab)
    text = re.sub('[\[\]]', '', tab[0])
    link = re.sub('[\(\)]', '', tab[1])
    p[0] = AST.LinkNode(text, link)


def p_image(p):
    ''' tag : IMAGE
    '''
    text = p[1]
    tab = text.split("(")
    text = re.sub('[!\[\]]', '', tab[0])
    link = re.sub('[\(\)]', '', tab[1])
    p[0] = AST.ImageNode(text, link)


# TODO: Faire un nouveau noeud
def p_reference(p):
    ''' tag : REFERENCE
    '''
    text = p[1]
    tab = text.split("{")
    text = tab[0]
    link = re.sub('[{}]', '', tab[1])
    p[0] = AST.ReferenceNode(text, link)

def p_error(p):
    if p:
        print ("Syntax error in line %d" % p.lineno)
        parser.errok()
    else:
        print ("Sytax error: unexpected end of file!")

def parse(program):
    return yacc.parse(program)

parser = yacc.yacc(outputdir='generated')

if __name__ == "__main__":
	# import sys
	# prog = open(sys.argv[1]).read()
	# result = yacc.parse(prog, debug=0)
	# print (result)

    import sys
    prog = open(sys.argv[1]).read()
    ast = yacc.parse(prog, debug=0)
    print (ast)

    import os
    graph = ast.makegraphicaltree()
    name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
    graph.write_pdf(name)
    print ("wrote ast to", name)
