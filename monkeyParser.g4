parser grammar monkeyParser;

options {
    tokenVocab = monkeyLexer;
}

program
    : singleCommand
    ;

command
    : singleCommand ( PCOMA singleCommand )*
    ;

singleCommand
    : IDENT ( ASSIGN expression | PIZQ expression PDER )
    | IF expression THEN singleCommand ELSE singleCommand
    | WHILE expression DO singleCommand
    | LET declaration IN singleCommand
    | BEGIN command END
    ;

declaration
    : singleDeclaration ( PCOMA singleDeclaration )*
    ;

singleDeclaration
    : CONST IDENT VIR expression
    | VAR IDENT DOSPUNTOS typeDenoter
    ;

typeDenoter
    : IDENT
    ;

expression
    : primaryExpression ( operator primaryExpression )*
    ;

primaryExpression
    : LITERAL | IDENT | PIZQ expression PDER
    ;

operator
    : SUMA | RESTA | MULT | DIV
    ;