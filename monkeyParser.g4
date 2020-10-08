parser grammar monkeyParser;

options {
    tokenVocab = monkeyLexer;
}

program
    : singleCommand
    ;

command
    : singleCommand ( PCOMA singleCommand  )*
    ;


singleCommand
    : statement
    | posArray
    |elmentArray
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
    : primaryExpression ( operator primaryExpression)*
    | DCOMILLAS IDENT ( operator IDENT)*DCOMILLAS
    | PIZQ primaryExpression ( operator primaryExpression PDER)*
    | primaryExpression operator PIZQ primaryExpression ( operator primaryExpression PDER)*
    | PCIZQ expressionList
    | LIZQ expressionDict
    | expressionFn
    ;

expressionList
    : primaryExpression PCDER
    | primaryExpression COMA expressionList
    ;

expressionDict
    : dictionaryExpression DOSPUNTOS secondExpression LDER
    | dictionaryExpression DOSPUNTOS secondExpression COMA expressionDict
    ;

secondExpression
    : LITERAL | expression
    ;

dictionaryExpression
    : DCOMILLAS IDENT DCOMILLAS
    ;

primaryExpression
    : LITERAL
    ;

primaryExpressionI
    : IDENT
    ;

posArray
    :IDENT PCIZQ LITERAL PCDER;

elmentArray
    :IDENT PCIZQ DCOMILLAS IDENT ( operator IDENT)* DCOMILLAS PCDER;

expressionFn
    :FN PIZQ IDENT COMA IDENT PDER LIZQ RETURN IDENT SUMA IDENT LDER;

operator
    : SUMA | RESTA | MULT | DIV
    ;

statement
    :LET IDENT ( ASSIGN expression )
    ;