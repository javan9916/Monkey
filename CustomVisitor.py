from generated.monkeyParserVisitor import monkeyParserVisitor
from generated.monkeyParser import monkeyParser


class CustomVisitor(monkeyParserVisitor):
    cantTabs = 0
    output = ""
    fromIf = False
    fromFunc = False

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
            if i < len(ctx.statement()):
                self.cantTabs += 1
                self.visit(ctx.statement(i))
                self.cantTabs -= 1
            else:
                break
            i += 1

        return None

    def visitLetStatementAST(self, ctx: monkeyParser.LetStatementASTContext):
        self.output += (self.addTabs(self.cantTabs) + "- Let Statement: \n")
        self.cantTabs += 1
        self.output += (self.addTabs(self.cantTabs) + "- LET: \"" + ctx.LET().__str__() + "\"\n")
        self.output += (self.addTabs(self.cantTabs) + "- IDENT: \"" + ctx.IDENT().__str__() + "\"\n")
        self.output += (self.addTabs(self.cantTabs) + "- ASSIGN: \"" + ctx.ASSIGN().__str__() + "\"\n")
        self.cantTabs += 1
        self.visit(ctx.expression())
        if not (ctx.PCOMA().__str__() == "None"):
            if not self.fromFunc:
                self.output += (self.addTabs(self.cantTabs - 1) + "- PCOMA: \"" + ctx.PCOMA().__str__() + "\"\n")
            else:
                self.output += (self.addTabs(self.cantTabs + 1) + "- PCOMA: \"" + ctx.PCOMA().__str__() + "\"\n")

        self.cantTabs -= 1
        return None

    def visitReturnStatementAST(self, ctx: monkeyParser.ReturnStatementASTContext):
        self.output += (self.addTabs(self.cantTabs) + "- Return Statement: \n")
        self.cantTabs += 1
        self.output += (self.addTabs(self.cantTabs) + "- RETURN: \"" + ctx.RETURN().__str__() + "\"\n")
        self.cantTabs += 1
        self.visit(ctx.expression())
        if not (ctx.PCOMA().__str__() == "None"):
            if not self.fromFunc:
                self.output += (self.addTabs(self.cantTabs - 1) + "- PCOMA: \"" + ctx.PCOMA().__str__() + "\"\n")
            else:
                self.output += (self.addTabs(self.cantTabs + 1) + "- PCOMA: \"" + ctx.PCOMA().__str__() + "\"\n")

        self.cantTabs -= 1
        return None

    def visitExpressionStatementAST(self, ctx: monkeyParser.ExpressionStatementASTContext):
        self.output += (self.addTabs(self.cantTabs) + "- Expression Statement\n")
        self.cantTabs += 1
        self.visit(ctx.expression())
        if not (ctx.PCOMA().__str__() == "None"):
            if not self.fromFunc:
                self.output += (self.addTabs(self.cantTabs - 1) + "- PCOMA: \"" + ctx.PCOMA().__str__() + "\"\n")
            else:
                self.output += (self.addTabs(self.cantTabs + 1) + "- PCOMA: \"" + ctx.PCOMA().__str__() + "\"\n")
        self.cantTabs -= 1

        return None

    def visitExpressionAST(self, ctx: monkeyParser.ExpressionASTContext):
        self.output += (self.addTabs(self.cantTabs) + "- Expression: \n")
        self.cantTabs += 1
        self.visit(ctx.additionExpression(0))
        i = 1
        while True:
            if i < len(ctx.additionExpression()):
                if not (ctx.equalOperators()[i - 1] is None):
                    self.visit(ctx.equalOperators()[i - 1])
                self.visit(ctx.additionExpression(i))
                self.cantTabs -= 1
            else:
                break
            i += 1

        self.cantTabs -= 1
        return None

    def visitAdditionExpressionAST(self, ctx: monkeyParser.AdditionExpressionASTContext):
        self.output += (self.addTabs(self.cantTabs) + "- Addition Expression: \n")
        self.cantTabs += 1
        self.visit(ctx.multiplicationExpression(0))
        i = 1
        while True:
            if i < len(ctx.multiplicationExpression()):
                if not (ctx.addOperators()[i - 1] is None):
                    self.visit(ctx.addOperators()[i - 1])
                self.visit(ctx.multiplicationExpression(i))
                self.cantTabs -= 1
            else:
                break
            i += 1

        self.cantTabs -= 1
        return None

    def visitMultiplicationExpressionAST(self, ctx: monkeyParser.MultiplicationExpressionASTContext):
        self.output += (self.addTabs(self.cantTabs) + "- Multiplication Expression: \n")
        self.cantTabs += 1
        self.visit(ctx.elementExpression(0))
        i = 1
        while True:
            if i < len(ctx.elementExpression()):
                self.cantTabs += 1
                if not (ctx.multOperators()[i - 1] is None):
                    self.visit(ctx.multOperators()[i - 1])
                self.visit(ctx.elementExpression(i))
                self.cantTabs -= 1
            else:
                break
            i += 1

        self.cantTabs -= 1
        return None

    def visitElementExpressionAST(self, ctx: monkeyParser.ElementExpressionASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Element Expression: \n"
        self.cantTabs += 1
        self.visit(ctx.primitiveExpression())
        self.cantTabs -= 1
        if not (ctx.elementAccess() is None):
            self.cantTabs += 1
            self.visit(ctx.elementAccess())
            self.cantTabs -= 1
        elif not (ctx.callExpression() is None):
            self.cantTabs += 1
            self.visit(ctx.callExpression())
            self.cantTabs -= 1
        return None

    def visitElementAccessAST(self, ctx: monkeyParser.ElementAccessASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Element Access: \n"
        self.cantTabs += 1
        self.output += (self.addTabs(self.cantTabs) + "- PCIZQ: \"" + ctx.PCIZQ().__str__() + "\"\n")
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.output += (self.addTabs(self.cantTabs) + "- PCDER: \"" + ctx.PCDER().__str__() + "\"\n")
        return None

    def visitCallExpressionAST(self, ctx: monkeyParser.CallExpressionASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Call Expression: \n"
        self.cantTabs += 1
        self.output += (self.addTabs(self.cantTabs) + "- PIZQ: \"" + ctx.PIZQ().__str__() + "\"\n")
        self.cantTabs += 1
        self.visit(ctx.expressionList())
        self.cantTabs += 2
        self.output += (self.addTabs(self.cantTabs) + "- PDER: \"" + ctx.PDER().__str__() + "\"\n")
        return None

    def visitPrimitiveExpressionIntegerAST(self, ctx: monkeyParser.PrimitiveExpressionIntegerASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression: \n"
        self.cantTabs += 1
        self.output += self.addTabs(self.cantTabs) + "- Integer: \"" + ctx.INTEGER().__str__() + "\"\n"
        self.cantTabs -= 2
        return None

    def visitPrimitiveExpressionStringAST(self, ctx: monkeyParser.PrimitiveExpressionStringASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression: \n"
        self.cantTabs += 1
        self.output += self.addTabs(self.cantTabs) + "- String: \"" + ctx.STRING().__str__() + "\"\n"
        self.cantTabs -= 2
        return None

    def visitPrimitiveExpressionIdentAST(self, ctx: monkeyParser.PrimitiveExpressionIdentASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression: \n"
        self.cantTabs += 1
        self.output += self.addTabs(self.cantTabs) + "- Identifier: \"" + ctx.IDENT().__str__() + "\"\n"
        self.cantTabs -= 2
        return None

    def visitPrimitiveExpressionTrueAST(self, ctx: monkeyParser.PrimitiveExpressionTrueASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression: \n"
        self.cantTabs += 1
        self.output += self.addTabs(self.cantTabs) + "- True: \"" + ctx.TRUE().__str__() + "\"\n"
        self.cantTabs -= 2
        return None

    def visitPrimitiveExpressionFalseAST(self, ctx: monkeyParser.PrimitiveExpressionFalseASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression: \n"
        self.cantTabs += 1
        self.output += self.addTabs(self.cantTabs) + "- False: \"" + ctx.FALSE().__str__() + "\"\n"
        self.cantTabs -= 2
        return None

    def visitPrimitiveExpressionExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionExpressionASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression Expression: \n"
        self.cantTabs += 1
        self.output += (self.addTabs(self.cantTabs) + "- PIZQ: \"" + ctx.PIZQ().__str__() + "\"\n")
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.cantTabs += 1
        if self.fromIf:
            self.output += (self.addTabs(self.cantTabs + 1) + "- PDER: \"" + ctx.PDER().__str__() + "\"\n")
        else:
            self.output += (self.addTabs(self.cantTabs) + "- PDER: \"" + ctx.PDER().__str__() + "\"\n")
        self.cantTabs -= 1

        return None

    def visitPrimitiveExpressionarrayLiteralast(self, ctx: monkeyParser.PrimitiveExpressionarrayLiteralastContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression Array Literal:\n"
        self.cantTabs += 1
        self.visit(ctx.arrayLiteral())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionarrayFunctionsAST(self, ctx: monkeyParser.PrimitiveExpressionarrayFunctionsASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression Array Function:\n"
        self.cantTabs += 1
        self.visit(ctx.arrayFunctions())
        self.output += (self.addTabs(self.cantTabs) + "- PIZQ: \"" + ctx.PIZQ().__str__() + "\"\n")
        self.cantTabs += 1
        self.visit(ctx.expressionList())
        self.output += (self.addTabs(self.cantTabs) + "- PDER: \"" + ctx.PDER().__str__() + "\"\n")
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionfunctionLiteralAST(self, ctx: monkeyParser.PrimitiveExpressionfunctionLiteralASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression Function Literal:\n"
        self.cantTabs += 1
        self.visit(ctx.functionLiteral())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionhashLiteralAST(self, ctx: monkeyParser.PrimitiveExpressionhashLiteralASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression Hash Literal:\n"
        self.cantTabs += 1
        self.visit(ctx.hashLiteral())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionprintExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionprintExpressionASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression Print Expression:\n"
        self.cantTabs += 1
        self.visit(ctx.printExpression())
        self.cantTabs -= 1
        return None

    def visitPrimitiveExpressionifExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionifExpressionASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Primitive Expression If Expression:\n"
        self.cantTabs += 1
        self.visit(ctx.ifExpression())
        self.cantTabs -= 1
        return None

    def visitArrayFunctionsLenAST(self, ctx: monkeyParser.ArrayFunctionsLenASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Array Function: \n"
        self.cantTabs += 1
        self.output += self.addTabs(self.cantTabs) + "- LEN: \"" + ctx.LEN().__str__() + "\"\n"
        self.cantTabs -= 1
        return None

    def visitArrayFunctionsFirstAST(self, ctx: monkeyParser.ArrayFunctionsFirstASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Array Function: \n"
        self.cantTabs += 1
        self.output += self.addTabs(self.cantTabs) + "- FIRST: \"" + ctx.FIRST().__str__() + "\"\n"
        self.cantTabs -= 1
        return None

    def visitArrayFunctionsLastAST(self, ctx: monkeyParser.ArrayFunctionsLastASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Array Function: \n"
        self.cantTabs += 1
        self.output += self.addTabs(self.cantTabs) + "- LAST: \"" + ctx.LAST().__str__() + "\"\n"
        self.cantTabs -= 1
        return None

    def visitArrayFunctionsRestAST(self, ctx: monkeyParser.ArrayFunctionsRestASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Array Function: \n"
        self.cantTabs += 1
        self.output += self.addTabs(self.cantTabs) + "- REST: \"" + ctx.REST().__str__() + "\"\n"
        self.cantTabs -= 1
        return None

    def visitArrayFunctionsPushAST(self, ctx: monkeyParser.ArrayFunctionsPushASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Array Function: \n"
        self.cantTabs += 1
        self.output += self.addTabs(self.cantTabs) + "- PUSH: \"" + ctx.PUSH().__str__() + "\"\n"
        self.cantTabs -= 1
        return None

    def visitArrayLiteralAST(self, ctx: monkeyParser.ArrayLiteralASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Array Literal\n"
        self.cantTabs += 1
        self.output += (self.addTabs(self.cantTabs) + "- PCIZQ: \"" + ctx.PCIZQ().__str__() + "\"\n")
        self.cantTabs += 1
        self.visit(ctx.expressionList())
        self.output += (self.addTabs(self.cantTabs) + "- PCDER: \"" + ctx.PCDER().__str__() + "\"\n")
        self.cantTabs -= 2
        return None

    def visitFunctionLiteralAST(self, ctx: monkeyParser.FunctionLiteralASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Function Literal: \n"
        self.cantTabs += 1
        self.output += (self.addTabs(self.cantTabs) + "- FN: \"" + ctx.FN().__str__() + "\"\n")
        self.output += (self.addTabs(self.cantTabs) + "- PIZQ: \"" + ctx.PIZQ().__str__() + "\"\n")
        self.cantTabs += 1
        self.visit(ctx.functionParameters())
        self.cantTabs -= 1
        self.output += (self.addTabs(self.cantTabs) + "- PDER: \"" + ctx.PDER().__str__() + "\"\n")
        self.output += (self.addTabs(self.cantTabs) + "- LIZQ: \"" + ctx.LIZQ().__str__() + "\"\n")
        i = 0
        while True:
            if i < len(ctx.statement()):
                self.cantTabs += 1
                self.fromFunc = True
                self.visit(ctx.statement()[i])
                self.fromFunc = False
            else:
                break
            i += 1

        self.output += (self.addTabs(self.cantTabs) + "- LDER: \"" + ctx.LDER().__str__() + "\"\n")
        self.cantTabs -= 1
        return None

    def visitFunctionParametersAST(self, ctx: monkeyParser.FunctionParametersASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Function Parameters: \n"
        self.cantTabs += 1
        self.output += (self.addTabs(self.cantTabs) + "- IDENT: \"" + ctx.IDENT()[0].__str__() + "\"\n")
        i = 1
        while True:
            if i < len(ctx.IDENT()):
                self.output += (self.addTabs(self.cantTabs) + "- COMA: \"" + ctx.COMA()[i-1].__str__() + "\"\n")
                self.output += (self.addTabs(self.cantTabs) + "- IDENT: \"" + ctx.IDENT()[i].__str__() + "\"\n")
            else:
                break
            i += 1

        self.cantTabs -= 1
        return None

    def visitHashLiteralAST(self, ctx: monkeyParser.HashLiteralASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Hash Literal: \n"
        self.cantTabs += 1
        self.output += (self.addTabs(self.cantTabs) + "- LIZQ: \"" + ctx.LIZQ().__str__() + "\"\n")
        self.cantTabs += 1
        self.visit(ctx.hashContent()[0])
        i = 1
        while True:
            if i < len(ctx.hashContent()):
                self.output += (self.addTabs(self.cantTabs) + "- COMA: \"" + ctx.COMA()[i-1].__str__() + "\"\n")
                self.visit(ctx.hashContent()[i])
            else:
                break
            i += 1

        self.cantTabs -= 1
        self.output += (self.addTabs(self.cantTabs) + "- LDER: \"" + ctx.LDER().__str__() + "\"\n")
        self.cantTabs -= 2
        return None

    def visitHashContentAST(self, ctx: monkeyParser.HashContentASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Hash Content: \n"
        self.cantTabs += 1
        self.visit(ctx.expression(0))
        self.cantTabs += 1
        self.output += (self.addTabs(self.cantTabs) + "- DOSPUNTOS: \"" + ctx.DOSPUNTOS().__str__() + "\"\n")
        self.visit(ctx.expression(1))
        return None

    def visitExpressionListAST(self, ctx: monkeyParser.ExpressionListASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Expression List: \n"
        self.cantTabs += 1
        self.visit(ctx.expression()[0])
        i = 1
        while True:
            if i < len(ctx.expression()):
                self.output += (self.addTabs(self.cantTabs + 1) + "- COMA: \"" + ctx.COMA()[i-1].__str__() + "\"\n")
                self.cantTabs += 1
                self.visit(ctx.expression()[i])
            else:
                break
            i += 1

        self.cantTabs -= 1
        return None

    def visitPrintExpressionAST(self, ctx: monkeyParser.PrintExpressionASTContext):
        self.output += self.addTabs(self.cantTabs) + "- Print Expression: \n"
        self.cantTabs += 1
        self.output += (self.addTabs(self.cantTabs) + "- PUTS: \"" + ctx.PUTS().__str__() + "\"\n")
        self.output += (self.addTabs(self.cantTabs) + "- PIZQ: \"" + ctx.PIZQ().__str__() + "\"\n")
        self.cantTabs += 1
        self.visit(ctx.expression())
        self.cantTabs -= 1
        self.output += (self.addTabs(self.cantTabs) + "- PDER: \"" + ctx.PDER().__str__() + "\"\n")
        self.cantTabs -= 1
        return None

    def visitIfExpressionAST(self, ctx: monkeyParser.IfExpressionASTContext):
        self.output += self.addTabs(self.cantTabs) + "- If Expression: \n"
        self.cantTabs += 1
        self.output += (self.addTabs(self.cantTabs) + "- IF: \"" + ctx.IF().__str__() + "\"\n")
        self.fromIf = True
        self.visit(ctx.expression())
        self.fromIf = False
        self.cantTabs += 1
        self.output += (self.addTabs(self.cantTabs) + "- LIZQ: \"" + ctx.LIZQ().__str__() + "\"\n")
        self.visit(ctx.statement()[0])
        i = 1
        while True:
            if i < len(ctx.statement()):
                self.visit(ctx.statement()[i])
                self.cantTabs -= 1
            else:
                break
            i += 1

        self.cantTabs += 1
        self.output += (self.addTabs(self.cantTabs) + "- LDER: \"" + ctx.LDER().__str__() + "\"\n")

        if not (ctx.elseExpression() is None):
            self.visit(ctx.elseExpression())

        self.cantTabs -= 1
        return None

    def visitElseExpressionAST(self, ctx: monkeyParser.ElseExpressionASTContext):
        self.output += (self.addTabs(self.cantTabs) + "- ELSE: \"" + ctx.ELSE().__str__() + "\"\n")
        self.output += (self.addTabs(self.cantTabs) + "- LIZQ: \"" + ctx.LIZQ().__str__() + "\"\n")

        i = 0
        while True:
            if i < len(ctx.statement()):
                self.cantTabs += 1
                self.visit(ctx.statement()[i])
                self.cantTabs -= 1
            else:
                break
            i += 1

        self.output += (self.addTabs(self.cantTabs + 1) + "- LDER: \"" + ctx.LDER().__str__() + "\"\n")
        return None

    def visitMultOperators(self, ctx: monkeyParser.MultOperatorsContext):
        self.output += (self.addTabs(self.cantTabs) + "- MultOperators: \n")
        self.cantTabs += 1
        if not (ctx.MULT() is None):
            self.output += (self.addTabs(self.cantTabs) + "- MULT: \"" + ctx.MULT().__str__() + "\"\n")
            operator = ctx.MULT().__str__()
        elif not (ctx.DIV() is None):
            self.output += (self.addTabs(self.cantTabs) + "- DIV: \"" + ctx.DIV().__str__() + "\"\n")
            operator = ctx.DIV().__str__()
        else:
            operator = None

        self.cantTabs -= 1
        return operator

    def visitAddOperators(self, ctx: monkeyParser.AddOperatorsContext):
        self.output += (self.addTabs(self.cantTabs) + "- AddOperators: \n")
        self.cantTabs += 1
        if not (ctx.SUMA() is None):
            self.output += (self.addTabs(self.cantTabs) + "- SUMA: \"" + ctx.SUMA().__str__() + "\"\n")
            operator = ctx.SUMA().__str__()
        elif not (ctx.RESTA() is None):
            self.output += (self.addTabs(self.cantTabs) + "- RESTA: \"" + ctx.RESTA().__str__() + "\"\n")
            operator = ctx.RESTA().__str__()
        else:
            operator = None

        self.cantTabs -= 1
        return operator

    def visitEqualOperators(self, ctx: monkeyParser.EqualOperatorsContext):
        self.output += (self.addTabs(self.cantTabs) + "- EqualOperators: \n")
        self.cantTabs += 1
        if not (ctx.EQUAL() is None):
            self.output += (self.addTabs(self.cantTabs) + "- EQUAL: \"" + ctx.EQUAL().__str__() + "\"\n")
            operator = ctx.EQUAL().__str__()
        elif not (ctx.MENOR() is None):
            self.output += (self.addTabs(self.cantTabs) + "- MENOR: \"" + ctx.MENOR().__str__() + "\"\n")
            operator = ctx.MENOR().__str__()
        elif not (ctx.MAYOR() is None):
            self.output += (self.addTabs(self.cantTabs) + "- MAYOR: \"" + ctx.MAYOR().__str__() + "\"\n")
            operator = ctx.MAYOR().__str__()
        elif not (ctx.MENOREQUAL() is None):
            self.output += (self.addTabs(self.cantTabs) + "- MENOREQUAL: \"" + ctx.MENOREQUAL().__str__() + "\"\n")
            operator = ctx.MENOREQUAL().__str__()
        elif not (ctx.MAYOREQUAL() is None):
            self.output += (self.addTabs(self.cantTabs) + "- MAYOREQUAL: \"" + ctx.MAYOREQUAL().__str__() + "\"\n")
            operator = ctx.MAYOREQUAL().__str__()
        else:
            operator = None

        self.cantTabs -= 1
        return operator
