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
    | elmentArray
    | ifExpression
    | whileExpression
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
    | expressionFnAux
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

expressionFnAux
    :FN PIZQ IDENT PDER LIZQ command LDER ;

whileExpression
    : WHILE PIZQ IDENT EQUAL DCOMILLAS IDENT DCOMILLAS PDER LIZQ singleCommand LDER
    | WHILE PIZQ IDENT EQUAL (TRUE|FALSE) PDER LIZQ singleCommand LDER
    | WHILE PIZQ TRUE PDER LIZQ singleCommand LDER;

ifExpression
    : IF PIZQ IDENT EQUAL DCOMILLAS IDENT DCOMILLAS PDER LIZQ  singleCommand LDER ELSE LIZQ singleCommand LDER
    | IF PIZQ IDENT EQUAL (TRUE|FALSE) PDER LIZQ  singleCommand LDER ELSE LIZQ singleCommand LDER;

expressionAux
    :FN PIZQ IDENT PDER LIZQ command LDER ;

operator
    : SUMA | RESTA | MULT | DIV
    ;

statement
    :LET IDENT ( ASSIGN expression )
    ;