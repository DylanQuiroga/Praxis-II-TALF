grammar arithmetic;

file_
    : (expression | equation)* EOF
    ;

equation
    : expression relop expression
    ;

expression
    : expression POW expression
    | expression (TIMES | DIV) expression
    | expression (PLUS | MINUS) expression
    | LPAREN expression RPAREN
    | (PLUS | MINUS)* atom
    | EXP LPAREN expression RPAREN
    | LOG LPAREN expression RPAREN
    ;

atom
    : scientific
    | variable
    ;

scientific
    : SCIENTIFIC_NUMBER
    ;

variable
    : VARIABLE
    ;

relop
    : EQ
    | GT
    | LT
    ;

VARIABLE
    : VALID_ID_START VALID_ID_CHAR*
    ;

fragment VALID_ID_START
    : 'a' .. 'z'
    | 'A' .. 'Z'
    | '_'
    ;

fragment VALID_ID_CHAR
    : VALID_ID_START
    | '0' .. '9'
    ;

SCIENTIFIC_NUMBER
    : NUMBER (E SIGN? UNSIGNED_INTEGER)?
    ;

fragment NUMBER
    : ('0' .. '9')+ ('.' ('0' .. '9')+)?
    ;

fragment UNSIGNED_INTEGER
    : ('0' .. '9')+
    ;

fragment E
    : 'E'
    | 'e'
    ;

fragment SIGN
    : '+'
    | '-'
    ;

LPAREN
    : '('
    ;

RPAREN
    : ')'
    ;

PLUS
    : '+'
    ;

MINUS
    : '-'
    ;

TIMES
    : '*'
    ;

DIV
    : '/'
    ;

GT
    : '>'
    ;

LT
    : '<'
    ;

EQ
    : '='
    ;

POINT
    : '.'
    ;

POW
    : '^'
    ;

EXP
    : 'exp'
    ;

LOG
    : 'log'
    ;

WS
    : [ \r\n\t]+ -> skip
    ;