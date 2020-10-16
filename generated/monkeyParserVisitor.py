# Generated from E:/Almacenamiento/Tec/Semestre-II-2020/Compi/Proyecto Python/Monkey\monkeyParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .monkeyParser import monkeyParser
else:
    from monkeyParser import monkeyParser

# This class defines a complete generic visitor for a parse tree produced by monkeyParser.

class monkeyParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by monkeyParser#programAST.
    def visitProgramAST(self, ctx:monkeyParser.ProgramASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#letStatementAST.
    def visitLetStatementAST(self, ctx:monkeyParser.LetStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#returnStatementAST.
    def visitReturnStatementAST(self, ctx:monkeyParser.ReturnStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#expressionStatementAST.
    def visitExpressionStatementAST(self, ctx:monkeyParser.ExpressionStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#expressionAST.
    def visitExpressionAST(self, ctx:monkeyParser.ExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#additionExpressionAST.
    def visitAdditionExpressionAST(self, ctx:monkeyParser.AdditionExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#multiplicationExpressionAST.
    def visitMultiplicationExpressionAST(self, ctx:monkeyParser.MultiplicationExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#elementExpressionAST.
    def visitElementExpressionAST(self, ctx:monkeyParser.ElementExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#elementAccessAST.
    def visitElementAccessAST(self, ctx:monkeyParser.ElementAccessASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#callExpressionAST.
    def visitCallExpressionAST(self, ctx:monkeyParser.CallExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#primitiveExpressionIntegerAST.
    def visitPrimitiveExpressionIntegerAST(self, ctx:monkeyParser.PrimitiveExpressionIntegerASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#primitiveExpressionStringAST.
    def visitPrimitiveExpressionStringAST(self, ctx:monkeyParser.PrimitiveExpressionStringASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#primitiveExpressionIdentAST.
    def visitPrimitiveExpressionIdentAST(self, ctx:monkeyParser.PrimitiveExpressionIdentASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#primitiveExpressionTrueAST.
    def visitPrimitiveExpressionTrueAST(self, ctx:monkeyParser.PrimitiveExpressionTrueASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#primitiveExpressionFalseAST.
    def visitPrimitiveExpressionFalseAST(self, ctx:monkeyParser.PrimitiveExpressionFalseASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#primitiveExpressionExpressionAST.
    def visitPrimitiveExpressionExpressionAST(self, ctx:monkeyParser.PrimitiveExpressionExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#primitiveExpressionarrayLiteralast.
    def visitPrimitiveExpressionarrayLiteralast(self, ctx:monkeyParser.PrimitiveExpressionarrayLiteralastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#primitiveExpressionarrayFunctionsAST.
    def visitPrimitiveExpressionarrayFunctionsAST(self, ctx:monkeyParser.PrimitiveExpressionarrayFunctionsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#primitiveExpressionfunctionLiteralAST.
    def visitPrimitiveExpressionfunctionLiteralAST(self, ctx:monkeyParser.PrimitiveExpressionfunctionLiteralASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#primitiveExpressionhashLiteralAST.
    def visitPrimitiveExpressionhashLiteralAST(self, ctx:monkeyParser.PrimitiveExpressionhashLiteralASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#primitiveExpressionprintExpressionAST.
    def visitPrimitiveExpressionprintExpressionAST(self, ctx:monkeyParser.PrimitiveExpressionprintExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#primitiveExpressionifExpressionAST.
    def visitPrimitiveExpressionifExpressionAST(self, ctx:monkeyParser.PrimitiveExpressionifExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#arrayFunctionsLenAST.
    def visitArrayFunctionsLenAST(self, ctx:monkeyParser.ArrayFunctionsLenASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#arrayFunctionsFirstAST.
    def visitArrayFunctionsFirstAST(self, ctx:monkeyParser.ArrayFunctionsFirstASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#arrayFunctionsLastAST.
    def visitArrayFunctionsLastAST(self, ctx:monkeyParser.ArrayFunctionsLastASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#arrayFunctionsRestAST.
    def visitArrayFunctionsRestAST(self, ctx:monkeyParser.ArrayFunctionsRestASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#arrayFunctionsPushAST.
    def visitArrayFunctionsPushAST(self, ctx:monkeyParser.ArrayFunctionsPushASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#arrayLiteralAST.
    def visitArrayLiteralAST(self, ctx:monkeyParser.ArrayLiteralASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#functionLiteralAST.
    def visitFunctionLiteralAST(self, ctx:monkeyParser.FunctionLiteralASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#functionParametersAST.
    def visitFunctionParametersAST(self, ctx:monkeyParser.FunctionParametersASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#hashLiteralAST.
    def visitHashLiteralAST(self, ctx:monkeyParser.HashLiteralASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#hashContentAST.
    def visitHashContentAST(self, ctx:monkeyParser.HashContentASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#expressionListAST.
    def visitExpressionListAST(self, ctx:monkeyParser.ExpressionListASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#printExpressionAST.
    def visitPrintExpressionAST(self, ctx:monkeyParser.PrintExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#ifExpressionAST.
    def visitIfExpressionAST(self, ctx:monkeyParser.IfExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#elseExpressionAST.
    def visitElseExpressionAST(self, ctx:monkeyParser.ElseExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#multOperators.
    def visitMultOperators(self, ctx:monkeyParser.MultOperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#addOperators.
    def visitAddOperators(self, ctx:monkeyParser.AddOperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by monkeyParser#equalOperators.
    def visitEqualOperators(self, ctx:monkeyParser.EqualOperatorsContext):
        return self.visitChildren(ctx)



del monkeyParser