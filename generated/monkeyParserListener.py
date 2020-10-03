# Generated from C:/Users/Javier/PycharmProjects/Monkey\monkeyParser.g4 by ANTLR 4.8
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


    # Enter a parse tree produced by monkeyParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:monkeyParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by monkeyParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:monkeyParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by monkeyParser#operator.
    def enterOperator(self, ctx:monkeyParser.OperatorContext):
        pass

    # Exit a parse tree produced by monkeyParser#operator.
    def exitOperator(self, ctx:monkeyParser.OperatorContext):
        pass



del monkeyParser