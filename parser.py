# avec parentheses et "moins unaire"

import ply.yacc as yacc

import AST

from lexemes import tokens

def p_document(p):
    ''' document : sentence
                   | document sentence
    '''
    try:
        print("DOCUMENT PLUSIEURS LIGNES")
        print("P1 - ", p[1])
        print("P2 - ", p[2])
        p[0] = AST.DocumentNode([p[1]], p[2])
        print("========")
    except:
        print("DOCUMENT UNE SEULE LIGNE")
        print(p[1])
        p[0] = AST.DocumentNode([p[1]])
        print("erreur")
def p_sentence(p):
    ''' sentence : WORD
        | tag
        | WORD sentence
        | tag sentence'''
    try:
        sequence = p[2]
        print("LE P2==============================")
        print(p[2])
        p[0] = AST.SentenceNode(p[1], p[2])
        print("LE P2==============================")
    except:
        print("UN SEUL TERME")
        print(p[1])
        p[0] = AST.SentenceNode(p[1])
    try:
        print("SENTENCE")
        print(p[1])
        print(p[2])
        print("========")
    except:
        print("erreur")

def p_tag(p):
    ''' tag : BOLD
        | FLUO
        | LINK
        | REFERENCE
        | IMAGE
        | SEPARATION_LINE
        | UL1
        | UL2
        | UL3
        | ITALIC
        | OL1
        | OL2
        | OL3
        | TITLE1
        | TITLE2
        | TITLE3
        | PARAGRAPHE
    '''
    print("TAGNODE")
    p[0] = AST.TagNode(p[1])
    print(p[1])
    print("----------------------")


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
