# avec parentheses et "moins unaire"

import ply.yacc as yacc

from lexemes import tokens

operations = {
	'+' : lambda x,y: x+y,
	'-' : lambda x,y: x-y,
	'*' : lambda x,y: x*y,
	'/' : lambda x,y: x/y,
}

def p_expression_op(p):
	"""expression : expression ADD_OP expression
			| expression MUL_OP expression"""
	p[0] = operations[p[2]](p[1],p[3])

def p_expression_num(p):
	"""expression : NUMBER"""
	p[0] = p[1]

def p_expression_paren(p):
	"""expression : '(' expression ')' """
	p[0] = p[2]

def p_minus(p):
	"""expression : ADD_OP expression %prec UMINUS"""
	p[0] = operations[p[1]](0,p[2])

def p_error(p):
    print ("Syntax error in line %d" % p.lineno)
    yacc.errok()

precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),
    ('right', 'UMINUS'),
)

yacc.yacc(outputdir='generated')

if __name__ == "__main__":
	import sys
	prog = open(sys.argv[1]).read()
	result = yacc.parse(prog, debug=1)
	print (result)
