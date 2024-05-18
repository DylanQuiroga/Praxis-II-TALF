grammar Graph;

graph: 'Graph {' edge* '}';
edge: node '->' node '(' weight ')' ;
node: LETTER ;
weight: NUMBER ;
LETTER: [A-Z] ;
NUMBER: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
