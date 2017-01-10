# Avec les parentheses

import ply.lex as lex

tokens = (
	'BOLD',
	'ITALIC',
	'FLUO',
      'LINK',
      'REFERENCE',
      'IMAGE',
      'WORD',
      'NUMBER',
      'SEPARATION_LINE',
      'PARAGRAPHE',
      'UL1',
      'UL2',
      'UL3',
)

def t_BOLD(t):
	r'\*{2}\w+\*{2}'
	return t

def t_ITALIC(t):
	r'\*{1}\w+\*{1}'
	return t
 
def t_FLUO(t):
	r'!.*!'
	return t

def t_LINK(t):
    r'\[.*\]\({1}.*\){1}'
    return t
    
def t_IMAGE(t):
    r'!{1}\[{1}.*\]{1}\({1}.*\){1}'
    return t

def t_REFERENCE(t):
    r'\w*\{{1}.*\}{1}'
    return t
    
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_SEPARATION_LINE(t):
    r'__{2,}\s{0,}'
    return t
    
def t_WORD(t):
    r'\w+[\s,.?:;&\-!?]?'
    return t
    
    
def t_UL1(t):
    r'\*{1}\s{1}.*'
    return t

def t_UL2(t):
    r'\*{2}\s{1}.*'
    return t

def t_UL3(t):
    r'\*{3}\s{1}.*'
    return t

def t_PARAGRAPHE(t):
    r'(\n){2}'
    return t
 
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_error(t):
	print ("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

t_ignore  = ' \t'

lex.lex()

if __name__ == "__main__":
	import sys
	prog = open(sys.argv[1]).read()

	lex.input(prog)

	while 1:
		tok = lex.token()
		if not tok: break
		print ("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))
