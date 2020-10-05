# Generated from E:/Almacenamiento/Tec/Semestre-II-2020/Compi/Proyecto Python/Monkey\monkeyParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .monkeyParser import monkeyParser
else:
    from monkeyParser import monkeyParser

# This class defines a complete listener for a parse tree produced by monkeyParser.
class monkeyParserListener(ParseTreeListener):

    # Enter a parse tree produced by monkeyParser#program.
    def enterProgram(self, ctx:monkeyParser.ProgramContext):
        pass

    # Exit a parse tree produced by monkeyParser#program.
    def exitProgram(self, ctx:monkeyParser.ProgramContext):
        pass


    # Enter a parse tree produced by monkeyParser#command.
    def enterCommand(self, ctx:monkeyParser.CommandContext):
        pass

    # Exit a parse tree produced by monkeyParser#command.
    def exitCommand(self, ctx:monkeyParser.CommandContext):
        pass


    # Enter a parse tree produced by monkeyParser#singleCommand.
    def enterSingleCommand(self, ctx:monkeyParser.SingleCommandContext):
        pass

    # Exit a parse tree produced by monkeyParser#singleCommand.
    def exitSingleCommand(self, ctx:monkeyParser.SingleCommandContext):
        pass


    # Enter a parse tree produced by monkeyParser#declaration.
    def enterDeclaration(self, ctx:monkeyParser.DeclarationContext):
        pass

    # Exit a parse tree produced by monkeyParser#declaration.
    def exitDeclaration(self, ctx:monkeyParser.DeclarationContext):
        pass


    # Enter a parse tree produced by monkeyParser#singleDeclaration.
    def enterSingleDeclaration(self, ctx:monkeyParser.SingleDeclarationContext):
        pass

    # Exit a parse tree produced by monkeyParser#singleDeclaration.
    def exitSingleDeclaration(self, ctx:monkeyParser.SingleDeclarationContext):
        pass


    # Enter a parse tree produced by monkeyParser#typeDenoter.
    def enterTypeDenoter(self, ctx:monkeyParser.TypeDenoterContext):
        pass

    # Exit a parse tree produced by monkeyParser#typeDenoter.
    def exitTypeDenoter(self, ctx:monkeyParser.TypeDenoterContext):
        pass


    # Enter a parse tree produced by monkeyParser#expression.
    def enterExpression(self, ctx:monkeyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by monkeyParser#expression.
    def exitExpression(self, ctx:monkeyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by monkeyParser#expressionList.
    def enterExpressionList(self, ctx:monkeyParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by monkeyParser#expressionList.
    def exitExpressionList(self, ctx:monkeyParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by monkeyParser#expressionDict.
    def enterExpressionDict(self, ctx:monkeyParser.ExpressionDictContext):
        pass

    # Exit a parse tree produced by monkeyParser#expressionDict.
    def exitExpressionDict(self, ctx:monkeyParser.ExpressionDictContext):
        pass


    # Enter a parse tree produced by monkeyParser#secondExpression.
    def enterSecondExpression(self, ctx:monkeyParser.SecondExpressionContext):
        pass

    # Exit a parse tree produced by monkeyParser#secondExpression.
    def exitSecondExpression(self, ctx:monkeyParser.SecondExpressionContext):
        pass


    # Enter a parse tree produced by monkeyParser#dictionaryExpression.
    def enterDictionaryExpression(self, ctx:monkeyParser.DictionaryExpressionContext):
        pass

    # Exit a parse tree produced by monkeyParser#dictionaryExpression.
    def exitDictionaryExpression(self, ctx:monkeyParser.DictionaryExpressionContext):
        pass


    # Enter a parse tree produced by monkeyParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:monkeyParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by monkeyParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:monkeyParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by monkeyParser#primaryExpressionI.
    def enterPrimaryExpressionI(self, ctx:monkeyParser.PrimaryExpressionIContext):
        pass

    # Exit a parse tree produced by monkeyParser#primaryExpressionI.
    def exitPrimaryExpressionI(self, ctx:monkeyParser.PrimaryExpressionIContext):
        pass


    # Enter a parse tree produced by monkeyParser#operator.
    def enterOperator(self, ctx:monkeyParser.OperatorContext):
        pass

    # Exit a parse tree produced by monkeyParser#operator.
    def exitOperator(self, ctx:monkeyParser.OperatorContext):
        pass


    # Enter a parse tree produced by monkeyParser#statement.
    def enterStatement(self, ctx:monkeyParser.StatementContext):
        pass

    # Exit a parse tree produced by monkeyParser#statement.
    def exitStatement(self, ctx:monkeyParser.StatementContext):
        pass



del monkeyParser