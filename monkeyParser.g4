parser grammar monkeyParser;

options {
    tokenVocab = monkeyLexer;
}

program
    : statement*                                                            #programAST
    ;

statement
    : LET IDENT ASSIGN expression ( PCOMA | )                               #letStatementAST
    | RETURN expression ( PCOMA | )                                         #returnStatementAST
    | expression ( PCOMA | )                                                #expressionStatementAST
    ;

expression
    : additionExpression (
    (MENOR|MAYOR|MENOREQUAL|MAYOREQUAL|EQUAL) additionExpression)*          #expressionAST
    ;

additionExpression
    : multiplicationExpression ((SUMA|RESTA) multiplicationExpression)*     #additionExpressionAST
    ;

multiplicationExpression
    : elementExpression ((MULT|DIV) elementExpression)*                     #multiplicationExpressionAST
    ;

elementExpression
    : primitiveExpression ( elementAccess | callExpression | )              #elementExpressionAST
    ;

elementAccess
    : PCIZQ expression PCDER                                                #elementAccessAST
    ;

callExpression
    : PIZQ expressionList PDER                                              #callExpressionAST
    ;

primitiveExpression
    : INTEGER                                                               #primitiveExpressionIntegerAST
    | STRING                                                                #primitiveExpressionStringAST
    | IDENT                                                                 #primitiveExpressionIdentAST
    | TRUE                                                                  #primitiveExpressionTrueAST
    | FALSE                                                                 #primitiveExpressionFalseAST
    | PIZQ expression PDER                                                  #primitiveExpressionExpressionAST
    | arrayLiteral                                                          #primitiveExpressionarrayLiteralast
    | arrayFunctions PIZQ expressionList PDER                               #primitiveExpressionarrayFunctionsAST
    | functionLiteral                                                       #primitiveExpressionfunctionLiteralAST
    | hashLiteral                                                           #primitiveExpressionhashLiteralAST
    | printExpression                                                       #primitiveExpressionprintExpressionAST
    | ifExpression                                                          #primitiveExpressionifExpressionAST
    ;

arrayFunctions
    : LEN                                                                   #arrayFunctionsLenAST
    | FIRST                                                                 #arrayFunctionsFirstAST
    | LAST                                                                  #arrayFunctionsLastAST
    | REST                                                                  #arrayFunctionsRestAST
    | PUSH                                                                  #arrayFunctionsPushAST
    ;

arrayLiteral
    : PCIZQ expressionList PCDER                                            #arrayLiteralAST
    ;

functionLiteral
    :FN PIZQ functionParameters PDER LIZQ statement* LDER                   #functionLiteralAST
    ;

functionParameters
    : IDENT (COMA IDENT)*                                                   #functionParametersAST
    ;

hashLiteral
    : LIZQ hashContent (COMA hashContent)* LDER                             #hashLiteralAST
    ;

hashContent
    : expression DOSPUNTOS expression                                       #hashContentAST
    ;

expressionList
    : expression ((COMA expression)* | )                                    #expressionListAST
    ;

printExpression
    : PUTS PIZQ expression PDER                                             #printExpressionAST
    ;

ifExpression
    : IF expression LIZQ statement* LDER
    (ELSE LIZQ statement* LDER | )                                          #ifExpressionAST
    ;