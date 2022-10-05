import lex as lex
import yacc as yacc

tokens = [
    'LPAREN',
    'RPAREN',
    'PREDICATE',
    'AND',
    'OR',
    'IMPLIES',
    'NEGATION',
    'DOUBLEIMPLIES'
]

t_PREDICATE = r'[p-z0-1]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_AND = r'\^'
t_OR = r'[o]'
t_IMPLIES = r'\=>'
t_NEGATION = r'\~'
t_DOUBLEIMPLIES = r'\<=>'

t_ignore = r' '

def t_error(t):
    print("Illegeal characters")
    t.lexer.skip(1)

lexer = lex.lex()


def p_expression_normal(p):
    '''
    expression : PREDICATE
    '''
    p[0] = (p[1])
    print(p[0])

def p_expression_negation(p):
    '''
    expression : LPAREN NEGATION PREDICATE RPAREN
               | LPAREN NEGATION expression RPAREN 
    '''
    p[0] = ('()', p[2], p[3])
    print(p[0])

def p_expression_negationpar(p):
    '''
    expression : NEGATION PREDICATE
               | NEGATION expression
    '''
    p[0] = (p[1], p[2])
    print(p[0])

def p_expression_operation(p):
    '''
    expression : LPAREN expression IMPLIES expression RPAREN 
               | LPAREN expression AND expression RPAREN 
               | LPAREN expression OR expression RPAREN 
               | LPAREN expression DOUBLEIMPLIES expression RPAREN 
               | LPAREN PREDICATE IMPLIES expression RPAREN 
               | LPAREN PREDICATE AND expression RPAREN 
               | LPAREN PREDICATE OR expression RPAREN 
               | LPAREN PREDICATE DOUBLEIMPLIES expression RPAREN 
               | LPAREN expression IMPLIES PREDICATE RPAREN 
               | LPAREN expression AND PREDICATE RPAREN 
               | LPAREN expression OR PREDICATE RPAREN
               | LPAREN expression DOUBLEIMPLIES PREDICATE RPAREN 

               | LPAREN PREDICATE IMPLIES PREDICATE RPAREN
               | LPAREN PREDICATE AND PREDICATE RPAREN
               | LPAREN PREDICATE OR PREDICATE RPAREN 
               | LPAREN PREDICATE DOUBLEIMPLIES PREDICATE RPAREN 

    '''
    p[0] = ('()', p[3], p[2], p[4])
    print(p[0])

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()


#while True:
#    try:
#        s = input('Enter the input: ')
#    except EOFError:
#        break
#    parser.parse(s, lexer=lexer)

test = [
    'p',
    '~~~q',
    '(p^q)',
    '(0=>(ros))',
    '~(p^q)',
    '(p<=>~p)',
    '((p=>q)^p)',
    '(~(p^(qor))os)'
]

for s in test:
    print(s)
    print()
    parser.parse(s, lexer=lexer)
    print('\n------\n')
