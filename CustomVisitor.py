from generated.monkeyParserVisitor import monkeyParserVisitor
from generated.monkeyParser import monkeyParser

class CustomVisitor(monkeyParserVisitor):
    cantTabs = 0

    def printTabs(self, cantTabs):
        res = ""
        for i in range(cantTabs):
            res += "|\t"
        return res

    def visitProgramAST(self, ctx: monkeyParser.ProgramASTContext):
        print(self.printTabs(self.cantTabs) + "- Program")
        self.cantTabs += 1
        i = 0
        while True:
            if i < len(ctx.statement()) - 1:
                self.cantTabs += 1
                self.visit(ctx.statement(i))
                self.cantTabs -= 1
            else:
                break
            i += 1

        self.cantTabs -= 1
        return None

    def visitLetStatementAST(self, ctx: monkeyParser.LetStatementASTContext):
        print(self.printTabs(self.cantTabs) + "- Let Statement")
        self.cantTabs += 1
        self.visit(ctx.letStatement())
        self.cantTabs -= 1
        return None

    def visitReturnStatementAST(self, ctx: monkeyParser.ReturnStatementASTContext):
        print(self.printTabs(self.cantTabs) + "- Return Statement")
        self.cantTabs += 1
        self.visit(ctx.returnStatement())
        self.cantTabs -= 1
        return None

    def visitExpressionStatemenAST(self, ctx: monkeyParser.ExpressionStatemenASTContext):
        print(self.printTabs(self.cantTabs) + "- Expression Statement")
        self.cantTabs += 1
        self.visit(ctx.expressionStatement())
        self.cantTabs -= 1
        return None

    def visitLetIdentStatementAST(self, ctx: monkeyParser.LetIdentStatementASTContext):
        print(self.printTabs(self.cantTabs) + "- Let Identification Statement")
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.cantTabs -= 1
        return None

    def visitReturnExpressionStatementAST(self, ctx: monkeyParser.ReturnExpressionStatementASTContext):
        print(self.printTabs(self.cantTabs) + "- Return Expression Statement")
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.cantTabs -= 1
        return None

    def visitExpressionStatementAST(self, ctx: monkeyParser.ExpressionStatementASTContext):
        print(self.printTabs(self.cantTabs) + "- Expression Statement")
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.cantTabs -= 1
        return None

    def visitExpressionAST(self, ctx: monkeyParser.ExpressionASTContext):
        print(self.printTabs(self.cantTabs) + "- Expression")
        self.cantTabs += 1
        self.visit(ctx.additionExpression())
        self.visit(ctx.comparison())
        self.cantTabs -= 1
        return None

    def visitComparisonAST(self, ctx: monkeyParser.ComparisonASTContext):
        print(self.printTabs(self.cantTabs) + "- Comparison")
        self.cantTabs += 1
        i = 1
        while True:
            if i < len(ctx.additionExpression()) - 1:
                self.cantTabs += 1
                self.visit(ctx.additionExpression(i))
                self.cantTabs -= 1
            else:
                break
            i += 1

        self.cantTabs -= 1
        return None

    def visitAdditionExpressionAST(self, ctx: monkeyParser.AdditionExpressionASTContext):
        print(self.printTabs(self.cantTabs) + "- Addition Expression")
        self.cantTabs += 1
        self.visit(ctx.multiplicationExpression())
        self.visit(ctx.additionFactor())
        self.cantTabs -= 1
        return None

    def visitAdditionFactorAST(self, ctx: monkeyParser.AdditionFactorASTContext):
        print(self.printTabs(self.cantTabs) + "- Addition Factor")
        self.cantTabs += 1
        i = 1
        while True:
            if i < len(ctx.multiplicationExpression()) - 1:
                self.cantTabs += 1
                self.visit(ctx.multiplicationExpression(i))
                self.cantTabs -= 1
            else:
                break
            i += 1

        self.cantTabs -= 1
        return None

    def visitMultiplicationExpressionAST(self, ctx: monkeyParser.MultiplicationExpressionASTContext):
        print(self.printTabs(self.cantTabs) + "- Multiplication Expression")
        self.cantTabs += 1
        self.visit(ctx.elementExpression())
        self.visit(ctx.multiplicationFactor())
        self.cantTabs -= 1
        return None

    def visitMultiplicationFactorAST(self, ctx: monkeyParser.MultiplicationFactorASTContext):
        print(self.printTabs(self.cantTabs) + "- Multiplication Factor")
        self.cantTabs += 1
        i = 1
        while True:
            if i < len(ctx.elementExpression()) - 1:
                self.cantTabs += 1
                self.visit(ctx.elementExpression(i))
                self.cantTabs -= 1
            else:
                break
            i += 1

        self.cantTabs -= 1
        return None

    def visitElementExpressionAST(self, ctx: monkeyParser.ElementExpressionASTContext):
        print(self.printTabs(self.cantTabs) + "- Element Expression")
        self.cantTabs += 1
        self.visit(ctx.primitiveExpression())
        if not(ctx.elementAccess() is None):
            self.visit(ctx.elementAccess())
        elif not(ctx.callExpression() is None):
            self.visit(ctx.callExpression())
        self.cantTabs -= 1
        return None

    def visitElementAccessAST(self, ctx: monkeyParser.ElementAccessASTContext):
        print(self.printTabs(self.cantTabs) + "- Element Access")
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.cantTabs -= 1
        return None

    def visitCallExpressionAST(self, ctx: monkeyParser.CallExpressionASTContext):
        print(self.printTabs(self.cantTabs) + "- Call Expression")
        self.cantTabs += 1
        self.visit(ctx.expressionList())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionIntegerAST(self, ctx: monkeyParser.PrimitiveExpressionIntegerASTContext):
        print(self.printTabs(self.cantTabs) + "- Integer")
        return None

    def visitPrimitiveExpressionStringAST(self, ctx: monkeyParser.PrimitiveExpressionStringASTContext):
        print(self.printTabs(self.cantTabs) + "- String")
        return None

    def visitPrimitiveExpressionIdentAST(self, ctx: monkeyParser.PrimitiveExpressionIdentASTContext):
        print(self.printTabs(self.cantTabs) + "- Identifier")
        return None

    def visitPrimitiveExpressionTrueAST(self, ctx: monkeyParser.PrimitiveExpressionTrueASTContext):
        print(self.printTabs(self.cantTabs) + "- True")
        return None

    def visitPrimitiveExpressionFalseAST(self, ctx: monkeyParser.PrimitiveExpressionFalseASTContext):
        print(self.printTabs(self.cantTabs) + "- False")
        return None

    def visitPrimitiveExpressionExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionExpressionASTContext):
        print(self.printTabs(self.cantTabs) + "- Primitive Expression Expression")
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionarrayLiteralast(self, ctx: monkeyParser.PrimitiveExpressionarrayLiteralastContext):
        print(self.printTabs(self.cantTabs) + "- Primitive Expression Array Literal")
        self.cantTabs += 1
        self.visit(ctx.arrayLiteral())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionarrayFunctionsAST(self, ctx: monkeyParser.PrimitiveExpressionarrayFunctionsASTContext):
        print(self.printTabs(self.cantTabs) + "- Primitive Expression Array Function")
        self.cantTabs += 1
        self.visit(ctx.arrayFunctions())
        self.visit(ctx.expressionList())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionfunctionLiteralAST(self, ctx: monkeyParser.PrimitiveExpressionfunctionLiteralASTContext):
        print(self.printTabs(self.cantTabs) + "- Primitive Expression Function Literal")
        self.cantTabs += 1
        self.visit(ctx.functionLiteral())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionhashLiteralAST(self, ctx: monkeyParser.PrimitiveExpressionhashLiteralASTContext):
        print(self.printTabs(self.cantTabs) + "- Primitive Expression Hash Literal")
        self.cantTabs += 1
        self.visit(ctx.hashLiteral())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionprintExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionprintExpressionASTContext):
        print(self.printTabs(self.cantTabs) + "- Primitive Expression Print Expression")
        self.cantTabs += 1
        self.visit(ctx.printExpression())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionifExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionifExpressionASTContext):
        print(self.printTabs(self.cantTabs) + "- Primitive Expression If Expression")
        self.cantTabs += 1
        self.visit(ctx.ifExpression())
        self.cantTabs -= 1
        return None

    def visitArrayFunctionsLenAST(self, ctx: monkeyParser.ArrayFunctionsLenASTContext):
        print(self.printTabs(self.cantTabs) + "- Len")
        return None

    def visitArrayFunctionsFirstAST(self, ctx: monkeyParser.ArrayFunctionsFirstASTContext):
        print(self.printTabs(self.cantTabs) + "- First")
        return None

    def visitArrayFunctionsLastAST(self, ctx: monkeyParser.ArrayFunctionsLastASTContext):
        print(self.printTabs(self.cantTabs) + "- Last")
        return None

    def visitArrayFunctionsRestAST(self, ctx: monkeyParser.ArrayFunctionsRestASTContext):
        print(self.printTabs(self.cantTabs) + "- Rest")
        return None

    def visitArrayFunctionsPushAST(self, ctx: monkeyParser.ArrayFunctionsPushASTContext):
        print(self.printTabs(self.cantTabs) + "- Push")
        return None

    def visitArrayLiteralAST(self, ctx: monkeyParser.ArrayLiteralASTContext):
        print(self.printTabs(self.cantTabs) + "- Array Literal")
        self.cantTabs += 1
        self.visit(ctx.expressionList())
        self.cantTabs -= 1
        return None

    def visitFunctionLiteralAST(self, ctx: monkeyParser.FunctionLiteralASTContext):
        print(self.printTabs(self.cantTabs) + "- Function Literal")
        self.cantTabs += 1
        self.visit(ctx.functionParameters())
        self.visit(ctx.blockStatement())
        self.cantTabs -= 1
        return None

    def visitFunctionParametersAST(self, ctx: monkeyParser.FunctionParametersASTContext):
        print(self.printTabs(self.cantTabs) + "- Function Parameters")
        self.cantTabs += 1
        self.visit(ctx.moreIdentifiers())
        self.cantTabs -= 1
        return None

    def visitMoreIdentifiersAST(self, ctx: monkeyParser.MoreIdentifiersASTContext):
        print(self.printTabs(self.cantTabs) + "- More Identifiers")
        return None

    def visitHashLiteralAST(self, ctx: monkeyParser.HashLiteralASTContext):
        print(self.printTabs(self.cantTabs) + "- Hash Literal")
        self.cantTabs += 1
        self.visit(ctx.hashContent())
        self.visit(ctx.moreHashContent())
        self.cantTabs -= 1
        return None

    def visitHashContentAST(self, ctx: monkeyParser.HashContentASTContext):
        print(self.printTabs(self.cantTabs) + "- Hash Content")
        self.cantTabs += 1
        self.visit(ctx.expression(0))
        i = 1
        while True:
            if i < len(ctx.expression()) - 1:
                self.cantTabs += 1
                self.visit(ctx.expression(i))
                self.cantTabs -= 1
            else:
                break
            i += 1

        self.visit(ctx.expression(0))
        i = 1
        while True:
            if i < len(ctx.expression()) - 1:
                self.cantTabs += 1
                self.visit(ctx.expression(i))
                self.cantTabs -= 1
            else:
                break
            i += 1

        self.cantTabs -= 1
        return None

    def visitMoreHashContentAST(self, ctx: monkeyParser.MoreHashContentASTContext):
        print(self.printTabs(self.cantTabs) + "- More Hash Content")
        self.cantTabs += 1
        i = 1
        while True:
            if i < len(ctx.hashContent()) - 1:
                self.cantTabs += 1
                self.visit(ctx.hashContent(i))
                self.cantTabs -= 1
            else:
                break
            i += 1

        self.cantTabs -= 1
        return None

    def visitExpressionListAST(self, ctx: monkeyParser.ExpressionListASTContext):
        print(self.printTabs(self.cantTabs) + "- Expression List")
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.visit(ctx.moreExpressions())
        self.cantTabs -= 1
        return None

    def visitMoreExpressionsAST(self, ctx: monkeyParser.MoreExpressionsASTContext):
        print(self.printTabs(self.cantTabs) + "- More Expression Content")
        self.cantTabs += 1
        i = 1
        while True:
            if i < len(ctx.expression()) - 1:
                self.cantTabs += 1
                self.visit(ctx.expression(i))
                self.cantTabs -= 1
            else:
                break
            i += 1

        self.cantTabs -= 1
        return None

    def visitPrintExpressionAST(self, ctx: monkeyParser.PrintExpressionASTContext):
        print(self.printTabs(self.cantTabs) + "- Print Expression")
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.cantTabs -= 1
        return None

    def visitIfExpressionAST(self, ctx: monkeyParser.IfExpressionASTContext):
        print(self.printTabs(self.cantTabs) + "- If Expression")
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.visit(ctx.blockStatement())
        if not(ctx.blockStatement() is None):
            self.visit(ctx.blockStatement())
        self.cantTabs -= 1
        return None

    def visitBlockStatementAST(self, ctx: monkeyParser.BlockStatementASTContext):
        print(self.printTabs(self.cantTabs) + "- Block Statement")
        self.cantTabs += 1
        self.visit(ctx.statement(0))
        i = 1
        while True:
            if i < len(ctx.statement()) - 1:
                self.cantTabs += 1
                self.visit(ctx.statement(i))
                self.cantTabs -= 1
            else:
                break
            i += 1

        self.cantTabs -= 1
        return None
