parser grammar monkeyParser;

options {
    tokenVocab = monkeyLexer;
}

program
    : statement*                                                            #programAST
    ;

statement
    : LET letStatement                                                      #letStatementAST
    | RETURN returnStatement                                                #returnStatementAST
    | expressionStatement                                                   #expressionStatemenAST
    ;

letStatement
    : IDENT ASSIGN expression ( PCOMA | )                                   #letIdentStatementAST
    ;

returnStatement
    : expression ( PCOMA | )                                                #returnExpressionStatementAST
    ;

expressionStatement
    : expression ( PCOMA | )                                                #expressionStatementAST
    ;

expression
    : additionExpression comparison                                         #expressionAST
    ;

comparison
    : ((MENOR|MAYOR|MENOREQUAL|MAYOREQUAL|EQUAL) additionExpression)*       #comparisonAST
    ;

additionExpression
    : multiplicationExpression additionFactor                               #additionExpressionAST
    ;

additionFactor
    : ((SUMA|RESTA) multiplicationExpression)*                              #additionFactorAST
    ;

multiplicationExpression
    : elementExpression multiplicationFactor                                #multiplicationExpressionAST
    ;

multiplicationFactor
    : ((MULT|DIV) elementExpression)*                                       #multiplicationFactorAST
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
    :FN PIZQ functionParameters PDER blockStatement                         #functionLiteralAST
    ;

functionParameters
    : IDENT moreIdentifiers                                                 #functionParametersAST
    ;

moreIdentifiers
    : (COMA IDENT)*                                                         #moreIdentifiersAST
    ;

hashLiteral
    : LIZQ hashContent moreHashContent LDER                                 #hashLiteralAST
    ;

hashContent
    : expression DOSPUNTOS expression                                       #hashContentAST
    ;

moreHashContent
    : (COMA hashContent)*                                                   #moreHashContentAST
    ;

expressionList
    : expression (moreExpressions | )                                       #expressionListAST
    ;

moreExpressions
    : (COMA expression)*                                                    #moreExpressionsAST
    ;

printExpression
    : PUTS PIZQ expression PDER                                             #printExpressionAST
    ;

ifExpression
    : IF expression blockStatement (ELSE blockStatement | )                 #ifExpressionAST
    ;

blockStatement
    : LIZQ statement* LDER                                                  #blockStatementAST
    ;