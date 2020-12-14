lexer grammar monkeyLexer;

// Simbolos
PCOMA       : ';';
DOSPUNTOS   : ':';
ASSIGN      : '=';
EQUAL       : '==';
LIZQ        : '{';
LDER        : '}';
PIZQ        : '(';
PDER        : ')';
PCIZQ       : '[';
PCDER       : ']';
VIR         : '~';
DCOMILLAS   : '"';
COMA        : ',';
MENOR       : '<';
MAYOR       : '>';
MENOREQUAL  : '<=';
MAYOREQUAL  : '>=';

// Operadores
SUMA    : '+';
RESTA   : '-';
MULT    : '*';
DIV     : '/';
FN      : 'fn';

// Palabras reservadas
IF      : 'if';
THEN    : 'then';
ELSE    : 'else';
WHILE   : 'while';
DO      : 'do';
LET     : 'let';
IN      : 'in';
BEGIN   : 'begin';
END     : 'end';
CONST   : 'const';
VAR     : 'var';
RETURN  : 'return';
TRUE    : 'true';
FALSE   : 'false';
PUTS    : 'puts';
LEN     : 'len';
FIRST   : 'first';
LAST    : 'last';
REST    : 'rest';
PUSH    : 'push';

// Otros tokens
IDENT   : LETRA (LETRA|DIGITO)*;
INTEGER : DIGITO DIGITO*;
STRING  : '"'LETRA(LETRA|DIGITO|' ')*'"';

fragment LETRA  : 'a'..'z' | 'A'..'Z' | '_';
fragment DIGITO : '0'..'9';

WS  : [ \t\n\r]+ -> skip;

COMMENT
: '/*' .*? '*/' -> skip
;
COMMENTANI
: '/*' .*? '/*' .*? '*/' .*?  '*/' -> skip
;
LINE_COMMENT
: '// =>' ~[\r\n]* -> skip
;