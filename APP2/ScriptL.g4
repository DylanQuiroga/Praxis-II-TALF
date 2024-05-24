grammar ScriptL;

program: statement+ ;

statement
    : getStmt
    | assignStmt
    | putStmt
    | whileStmt
    | ifStmt
    ;

getStmt: 'get' ID ';' ;
assignStmt: ID '=' expr ';' ;
putStmt: 'put' (ID | NUMBER) ';' ; 
whileStmt: 'while' '(' expr ')' '{' statement* '}' ;
ifStmt
    : 'if' '(' expr ')' ifBlock (elseBlock)?
    ;

ifBlock: '{' statement* '}' ;
elseBlock: 'else' '{' statement* '}' ;

expr
    : expr ('*'|'/') expr
    | expr ('+'|'-') expr
    | expr comparisonOperator expr
    | '(' expr ')'
    | ID
    | NUMBER
    ;

comparisonOperator
    : '<='
    | '>='
    | '<'
    | '>'
    | '=='
    | '!='
    ;

ID: [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
