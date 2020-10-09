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
FALSE   :'false';

// Otros tokens
IDENT   : LETRA (LETRA|DIGITO)*;
LITERAL : DIGITO DIGITO*;

fragment LETRA  : 'a'..'z' | 'A'..'Z';
fragment DIGITO : '0'..'9';

WS : [ \t\n\r]+ -> skip;