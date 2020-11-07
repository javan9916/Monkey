parser grammar monkeyParser;

options {
    tokenVocab = monkeyLexer;
}

program
    : statement*                                                    #programAST
    ;

statement
    : LET ident ASSIGN expression ( PCOMA | )                       #letStatementAST
    | RETURN expression ( PCOMA | )                                 #returnStatementAST
    | expression ( PCOMA | )                                        #expressionStatementAST
    ;

expression
    : additionExpression
    (equalOperators additionExpression)*                            #expressionAST
    ;

additionExpression
    : multiplicationExpression
    (addOperators multiplicationExpression)*                        #additionExpressionAST
    ;

multiplicationExpression
    : elementExpression (multOperators elementExpression)*          #multiplicationExpressionAST
    ;

elementExpression
    : primitiveExpression ( elementAccess | callExpression | )      #elementExpressionAST
    ;

elementAccess
    : PCIZQ expression PCDER                                        #elementAccessAST
    ;

callExpression
    : PIZQ expressionList PDER                                      #callExpressionAST
    ;

primitiveExpression
    : INTEGER                                                       #primitiveExpressionIntegerAST
    | STRING                                                        #primitiveExpressionStringAST
    | ident                                                         #primitiveExpressionIdentAST
    | TRUE                                                          #primitiveExpressionTrueAST
    | FALSE                                                         #primitiveExpressionFalseAST
    | PIZQ expression PDER                                          #primitiveExpressionExpressionAST
    | arrayLiteral                                                  #primitiveExpressionarrayLiteralast
    | arrayFunctions PIZQ expressionList PDER                       #primitiveExpressionarrayFunctionsAST
    | functionLiteral                                               #primitiveExpressionfunctionLiteralAST
    | hashLiteral                                                   #primitiveExpressionhashLiteralAST
    | printExpression                                               #primitiveExpressionprintExpressionAST
    | ifExpression                                                  #primitiveExpressionifExpressionAST
    ;

arrayFunctions
    : LEN                                                           #arrayFunctionsLenAST
    | FIRST                                                         #arrayFunctionsFirstAST
    | LAST                                                          #arrayFunctionsLastAST
    | REST                                                          #arrayFunctionsRestAST
    | PUSH                                                          #arrayFunctionsPushAST
    ;

arrayLiteral
    : PCIZQ expressionList PCDER                                    #arrayLiteralAST
    ;

functionLiteral
    : FN PIZQ functionParameters PDER LIZQ statement* LDER          #functionLiteralAST
    ;

functionParameters
    : IDENT (COMA IDENT)*                                           #functionParametersAST
    ;

hashLiteral
    : LIZQ hashContent (COMA hashContent)* LDER                     #hashLiteralAST
    ;

hashContent
    : expression DOSPUNTOS expression                               #hashContentAST
    ;

expressionList
    : expression ((COMA expression)* | )                            #expressionListAST
    ;

printExpression
    : PUTS PIZQ expression PDER                                     #printExpressionAST
    ;

ifExpression
    : IF expression LIZQ statement* LDER ( elseExpression | )       #ifExpressionAST
    ;

elseExpression
    : ELSE LIZQ statement* LDER                                     #elseExpressionAST
    ;

multOperators
    : MULT | DIV                                                    #multOperatorsAST
    ;

addOperators
    : SUMA | RESTA                                                  #addOperatorsAST
    ;

equalOperators
    : MENOR | MAYOR | MENOREQUAL | MAYOREQUAL | EQUAL               #equalOperatorsAST
    ;

ident
locals[ decl=None]: IDENT                          #identAST;