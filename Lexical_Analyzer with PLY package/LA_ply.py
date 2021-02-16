from ply.lex import lex

#----Tokens
tokens=(
# add constant's Types
'VAR','NUM','LIST_LABEL','NUM_LABEL',
# Reserved words
'VOID','FOR','IF','ELSE','IN',
'RETURN','WHILE','OR','AND','PRINT',
# Operators
'PLUS','TIMES','DIVIDE','MOD','MINUS',
# Delimeters
'LPAREN','RPAREN','LBRACE','RBRACE','LSQUAREBR','RSQUAREBR','COLON','COMMA','SEMI_COLON',
 # Logical Operators
'LESS_THAN','LESS_EQUAL','GREATER_THAN','GREATER_EQUAL','EQ','NOT_EQ','PARITY','NOT')



# Get Tokens
def t_NUM(t):
    r'[0-9]+'
    t.value=int(t.value)
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value=='void':
        t.type='VOID'
    elif t.value=='for':
        t.type='FOR'
    elif t.value=='if':
        t.type='IF'
    elif t.value=='else':
        t.type='ELSE'
    elif t.value=='return':
        t.type='RETURN'
    elif t.value=='while':
        t.type='WHILE'
    elif t.value=='print':
        t.type='PRINT' 
    elif t.value=='in':
        t.type='IN' 
    elif t.value=='num':
        t.type='NUM_LABEL' 
    elif t.value=='list':
        t.type='LIST_LABEL' 
    return t

t_AND=r'\&\&'
t_OR=r'\|\|'
t_PLUS=r'\+'
t_MINUS=r'\-'
t_TIMES=r'\*'
t_DIVIDE=r'\/'
t_MOD=r'%'
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_LBRACE=r'\{'
t_RBRACE=r'\}'
t_COLON=r':'
t_COMMA=r','
t_SEMI_COLON=r';'
t_LESS_THAN=r'\<'
t_LESS_EQUAL=r'\<\='
t_GREATER_THAN=r'>'
t_GREATER_EQUAL=r'>='
t_NOT_EQ=r'\!\='
t_EQ=r'='
t_PARITY=r'\=\='
t_NOT=r'\!'
t_LSQUAREBR=r'\['
t_RSQUAREBR=r'\]'



# recognize illegal character
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

#ignore Tab and enter
t_ignore=' \t \n' 


#Create comment pattern with /* ... */
def t_comment(t):
    r"[ ]*\057 \052 ([^\052]|\052+[^\052\057])* \052 \057 "  # \052 is '/' and \057 is '*'
    pass

#Create comment pattern with # ... \n
def t_comment2(t):
    r"[ ]*\043[^\n]*"  # \043 is '#'
    pass

precedence = (
   ('nonassoc', 'LESS_THAN', 'GREATER_THAN'),  # Nonassociative operators
   ('nonassoc', 'LESS_EQUAL', 'GREATER_EQUAL'),  # Nonassociative operators
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
)

lexer=lex()

file = open("teslangText.txt")

line = file.read()
file.close()


if __name__ == "__main__":
#  '/* if(ar=10) */ if list in a[10] || = % && ,: num 3 * 4 + 5 != < <= == !;/* ar=10*10 */'
    lexer.input(line)

    for tok in lexer:
        print(tok)


