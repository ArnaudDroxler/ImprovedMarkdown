# Avec les parentheses

import ply.lex as lex

tokens = (
	'BOLD',
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
    'ITALIC',
    'OL1',
    'OL2',
    'TITLE1',
    'TITLE2',
    'TITLE3',
    'VARIABLE',
    'ASSIGNATION',
)

def t_BOLD(t):
    r'\*{2}.+\*{2}'
    return t

def t_ITALIC(t):
	r'\*{1}[^\*\n]+\*{1}'
	return t

def t_UL1(t):
    r'\*{1}\s{1}[^\r\n\*]*'
    return t

def t_UL2(t):
    r'\*{2}\s{1}[^\r\n\*]*'
    return t

def t_UL3(t):
    r'\*{3}\s{1}[^\r\n\*]*'
    return t

def t_OL1(t):
    r'[0-9]+\.{1}\s{1}.+'
    return t

def t_OL2(t):
    r'[0-9]+\.{1}[0-9]+\s{1}.+'
    return t

def t_OL3(t):
    r'[0-9]+\.{1}[0-9]+\.{1}[0-9]+\s{1}.+'
    return t

def t_TITLE1(t):
    # La regex prend toute la ligne, ce qui signifie qu'il n'y aura pas de mise
    # en forme autre que le titre
	r'\#{1}\s{1}.+'
	return t

def t_TITLE2(t):
	r'\#{2}\s{1}.+'
	return t

def t_TITLE3(t):
	r'\#{3}\s{1}.+'
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

# Avec le point, on prend tous le texte depuis la dernière balise comme texte de la référence
def t_REFERENCE(t):
    r'.[^\s]*\{{1}.*\}{1}'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_SEPARATION_LINE(t):
    r'__{2,}\h{0,}'
    return t

def t_WORD(t):
    r'[\wéàèê]+'
    return t

def t_VARIABLE(t):
    r'\${1}[\w_]+'
    return t

def t_ASSIGNATION(t):
    r'={1}'
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
