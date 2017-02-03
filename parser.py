# avec parentheses et "moins unaire"

import ply.yacc as yacc

import AST

from lexemes import tokens

def p_document_paragraph(p):
    ''' document : paragraph '''
    p[0] = AST.DocumentNode(p[1])

def p_paragraph(p):
    ''' paragraph : PARAGRAPHE WORD PARAGRAPHE '''
    p[0] = AST.ParagraphNode(p[1])

def p_error(p):
    print ("Syntax error in line %d" % p.lineno)
    yacc.errok()


yacc.yacc(outputdir='generated')

if __name__ == "__main__":
	import sys
	prog = open(sys.argv[1]).read()
	result = yacc.parse(prog, debug=1)
	print (result)
