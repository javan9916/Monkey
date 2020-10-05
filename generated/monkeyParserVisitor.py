# Generated from E:/Almacenamiento/Tec/Semestre-II-2020/Compi/Proyecto Python/Monkey\monkeyParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .monkeyParser import monkeyParser
else:
    from monkeyParser import monkeyParser

# This class defines a complete generic visitor for a parse tree produced by monkeyParser.

class monkeyParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by monkeyParser#program.
    def visitProgram(self, ctx:monkeyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#command.
    def visitCommand(self, ctx:monkeyParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#singleCommand.
    def visitSingleCommand(self, ctx:monkeyParser.SingleCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#declaration.
    def visitDeclaration(self, ctx:monkeyParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#singleDeclaration.
    def visitSingleDeclaration(self, ctx:monkeyParser.SingleDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#typeDenoter.
    def visitTypeDenoter(self, ctx:monkeyParser.TypeDenoterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#expression.
    def visitExpression(self, ctx:monkeyParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#expressionList.
    def visitExpressionList(self, ctx:monkeyParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#expressionDict.
    def visitExpressionDict(self, ctx:monkeyParser.ExpressionDictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#secondExpression.
    def visitSecondExpression(self, ctx:monkeyParser.SecondExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#dictionaryExpression.
    def visitDictionaryExpression(self, ctx:monkeyParser.DictionaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:monkeyParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#primaryExpressionI.
    def visitPrimaryExpressionI(self, ctx:monkeyParser.PrimaryExpressionIContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#operator.
    def visitOperator(self, ctx:monkeyParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#statement.
    def visitStatement(self, ctx:monkeyParser.StatementContext):
        return self.visitChildren(ctx)



del monkeyParser