from generated.monkeyParserVisitor import monkeyParserVisitor
from generated.monkeyParser import monkeyParser


class CustomVisitor(monkeyParserVisitor):
    cantTabs = 0
    output = ""

    def getOutput(self):
        return self.output

    def addTabs(self, cantTabs):
        res = ""
        for i in range(cantTabs):
            res += "|\t"
        return res

    def visitProgramAST(self, ctx: monkeyParser.ProgramASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Program\n"
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
        self.output += (self.addTabs(self.cantTabs) + "- Let Statement: \"" +
                        ctx.LET().__str__() + "\"\n")
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.cantTabs -= 1
        return None

    def visitReturnStatementAST(self, ctx: monkeyParser.ReturnStatementASTContext):
        self.output += (self.addTabs(self.cantTabs) + "- Return Statement\"" +
                        ctx.RETURN().__str__() + "\"\n")
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.cantTabs -= 1

        return None

    def visitExpressionStatementAST(self, ctx: monkeyParser.ExpressionStatementASTContext):
        self.output += (self.addTabs(self.cantTabs) + "- Expression Statement\n")
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.cantTabs -= 1
        return None

    def visitExpressionAST(self, ctx: monkeyParser.ExpressionASTContext):
        if self.getExpression(ctx) == "[]":
            self.output += (self.addTabs(self.cantTabs) + "- Expression: \"" +
                            self.getExpression(ctx) + "\"\n")
        self.cantTabs += 1
        self.visit(ctx.additionExpression(0))
        i = 0
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
        self.output += self.addTabs(self.cantTabs) + "- Addition Expression\n"
        self.cantTabs += 1
        self.visit(ctx.multiplicationExpression(0))
        i = 0
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
        self.output += self.addTabs(self.cantTabs) + "- Multiplication Expression\n"
        self.cantTabs += 1
        self.visit(ctx.elementExpression(0))
        i = 0
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
        self.output += self.addTabs(self.cantTabs) + "- Element Expression\n"
        self.cantTabs += 1
        self.visit(ctx.primitiveExpression())
        if not (ctx.elementAccess() is None):
            self.visit(ctx.elementAccess())
        elif not (ctx.callExpression() is None):
            self.visit(ctx.callExpression())
        self.cantTabs -= 1
        return None

    def visitElementAccessAST(self, ctx: monkeyParser.ElementAccessASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Element Access\n"
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.cantTabs -= 1
        return None

    def visitCallExpressionAST(self, ctx: monkeyParser.CallExpressionASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Call Expression\n"
        self.cantTabs += 1
        self.visit(ctx.expressionList())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionIntegerAST(self, ctx: monkeyParser.PrimitiveExpressionIntegerASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Integer\n"
        return None

    def visitPrimitiveExpressionStringAST(self, ctx: monkeyParser.PrimitiveExpressionStringASTContext):
        self.output += self.addTabs(self.cantTabs) + "- String\n"
        return None

    def visitPrimitiveExpressionIdentAST(self, ctx: monkeyParser.PrimitiveExpressionIdentASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Identifier\n"
        return None

    def visitPrimitiveExpressionTrueAST(self, ctx: monkeyParser.PrimitiveExpressionTrueASTContext):
        self.output += self.addTabs(self.cantTabs) + "- True\n"
        return None

    def visitPrimitiveExpressionFalseAST(self, ctx: monkeyParser.PrimitiveExpressionFalseASTContext):
        self.output += self.addTabs(self.cantTabs) + "- False\n"
        return None

    def visitPrimitiveExpressionExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionExpressionASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression Expression\n"
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionarrayLiteralast(self, ctx: monkeyParser.PrimitiveExpressionarrayLiteralastContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression Array Literal\n"
        self.cantTabs += 1
        self.visit(ctx.arrayLiteral())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionarrayFunctionsAST(self, ctx: monkeyParser.PrimitiveExpressionarrayFunctionsASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression Array Function\n"
        self.cantTabs += 1
        self.visit(ctx.arrayFunctions())
        self.visit(ctx.expressionList())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionfunctionLiteralAST(self,
                                                   ctx: monkeyParser.PrimitiveExpressionfunctionLiteralASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression Function Literal\n"
        self.cantTabs += 1
        self.visit(ctx.functionLiteral())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionhashLiteralAST(self, ctx: monkeyParser.PrimitiveExpressionhashLiteralASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression Hash Literal\n"
        self.cantTabs += 1
        self.visit(ctx.hashLiteral())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionprintExpressionAST(self,
                                                   ctx: monkeyParser.PrimitiveExpressionprintExpressionASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression Print Expression\n"
        self.cantTabs += 1
        self.visit(ctx.printExpression())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionifExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionifExpressionASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression If Expression\n"
        self.cantTabs += 1
        self.visit(ctx.ifExpression())
        self.cantTabs -= 1
        return None

    def visitArrayFunctionsLenAST(self, ctx: monkeyParser.ArrayFunctionsLenASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Len\n"
        return None

    def visitArrayFunctionsFirstAST(self, ctx: monkeyParser.ArrayFunctionsFirstASTContext):
        self.output += self.addTabs(self.cantTabs) + "- First\n"
        return None

    def visitArrayFunctionsLastAST(self, ctx: monkeyParser.ArrayFunctionsLastASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Last\n"
        return None

    def visitArrayFunctionsRestAST(self, ctx: monkeyParser.ArrayFunctionsRestASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Rest\n"
        return None

    def visitArrayFunctionsPushAST(self, ctx: monkeyParser.ArrayFunctionsPushASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Push\n"
        return None

    def visitArrayLiteralAST(self, ctx: monkeyParser.ArrayLiteralASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Array Literal\n"
        self.cantTabs += 1
        self.visit(ctx.expressionList())
        self.cantTabs -= 1
        return None

    def visitFunctionLiteralAST(self, ctx: monkeyParser.FunctionLiteralASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Function Literal\n"
        self.cantTabs += 1
        self.visit(ctx.functionParameters())
        self.visit(ctx.blockStatement())
        self.cantTabs -= 1
        return None

    def visitFunctionParametersAST(self, ctx: monkeyParser.FunctionParametersASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Function Parameters\n"
        return None

    def visitHashLiteralAST(self, ctx: monkeyParser.HashLiteralASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Hash Literal\n"
        self.cantTabs += 1
        self.visit(ctx.hashContent(0))
        i = 0
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

    def visitHashContentAST(self, ctx: monkeyParser.HashContentASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Hash Content\n"
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

    def visitExpressionListAST(self, ctx: monkeyParser.ExpressionListASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Expression List\n"
        self.cantTabs += 1
        self.visit(ctx.expression(0))
        i = 0
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
        self.output += self.addTabs(self.cantTabs) + "- Print Expression\n"
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.cantTabs -= 1
        return None

    def visitIfExpressionAST(self, ctx: monkeyParser.IfExpressionASTContext):
        self.output += self.addTabs(self.cantTabs) + "- If Expression\n"
        self.cantTabs += 1
        self.visit(ctx.expression())

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

        if not (ctx.statement() is None):
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

    def getExpression(self, ctx: monkeyParser.ExpressionASTContext):
        if not (ctx.MENOR() is None):
            expr = ctx.MENOR().__str__()
        elif not (ctx.MAYOR() is None):
            expr = ctx.MAYOR().__str__()
        elif not (ctx.MENOREQUAL() is None):
            expr = ctx.MENOREQUAL().__str__()
        elif not (ctx.MAYOREQUAL() is None):
            expr = ctx.MAYOREQUAL().__str__()
        else:
            expr = ctx.EQUAL().__str__()

        return expr
