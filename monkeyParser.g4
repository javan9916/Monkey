parser grammar monkeyParser;

options {
    tokenVocab = monkeyLexer;
}

program
    : statement*;

statement
    : LET letStatement
    | RETURN returnStatement
    | expressionStatement;

letStatement
    : IDENT ASSIGN expression ( PCOMA | ε) ;

returnStatement
    : expression ( PCOMA | ε) ;

expressionStatement
    : expression ( PCOMA | ε);

expression
    : additionExpression comparison;

comparison
    : ((MENOR|MAYOR|MENOREQUAL|MAYOREQUAL|EQUAL) additionExpression)*;

additionExpression
    : multiplicationExpression additionFactor;

additionFactor
    : ((SUMA|RESTA) multiplicationExpression)*;

multiplicationExpression
    : elementExpression multiplicationFactor ;

multiplicationFactor
    : ((MULT|DIV) elementExpression)* ;

elementExpression
    : primitiveExpression (elementAccess | callExpression | ε) ;

elementAccess
    : PCIZQ expression PCDER;

callExpression
    : PIZQ expressionList PDER;

primitiveExpression
    : Integer
    | STRING
    | IDENT
    | TRUE
    | FALSE
    | PIZQ expression PDER
    | arrayLiteral
    | arrayFunctions PIZQ expressionList PDER
    | functionLiteral
    | hashLiteral
    | printExpression
    | ifExpression;

arrayFunctions
    : LEN
    | FIRST
    | LAST
    | REST
    | PUSH;

arrayLiteral
    : PCIZQ expressionList PCDER;

functionLiteral
    :FN PIZQ functionParameters PDER blockStatement;

functionParameters
    : IDENT moreIdentifiers;

moreIdentifiers
    : (COMA IDENT)*;

hashLiteral
    : LIZQ hashContent moreHashContent LDER ;

hashContent
    : expression DOSPUNTOS expression;

moreHashContent
    : (COMA hashContent)*;

expressionList
    : expression moreExpressions | ε;

moreExpressions
    : (COMA expression)*;

printExpression
    : PUTS PIZQ expression PDER;

ifExpression
    : IF expression blockStatement (ELSE blockStatement | ε);

blockStatement
    : LIZQ statement* LDER;