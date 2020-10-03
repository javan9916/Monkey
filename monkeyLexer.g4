lexer grammar monkeyLexer;

// Simbolos
PCOMA       : ';';
DOSPUNTOS   : ':';
ASSIGN      : ':=';
PIZQ        : '(';
PDER        : ')';
VIR         : '~';

// Operadores
SUMA    : '+';
RESTA   : '-';
MULT    : '*';
DIV     : '/';

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

// Otros tokens
IDENT   : LETRA (LETRA|DIGITO)*;
LITERAL : DIGITO DIGITO*;

fragment LETRA  : 'a'..'z' | 'A'..'Z';
fragment DIGITO : '0'..'9';

WS : [ \t\n\r]+ -> skip;