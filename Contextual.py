from generated.monkeyParserVisitor import monkeyParserVisitor
from generated.monkeyParser import monkeyParser
from SymbolTable import SymbolTable


class Contextual(monkeyParserVisitor):
    table = None
    output = ""
    fromFunc = False
    fromIf = False

    def __init__(self):
        self.table = SymbolTable()

    def getOutput(self):
        return self.output

    def visitProgramAST(self, ctx: monkeyParser.ProgramASTContext):
        i = 0
        while True:
            if i < len(ctx.statement()):
                self.visit(ctx.statement(i))
            else:
                break
            i += 1

        return None

    def visitLetStatementAST(self, ctx: monkeyParser.LetStatementASTContext):
        exprType = self.visit(ctx.expression())
        hasReturn, isFunction = False, False
        type = -1

        if exprType == "int":
            type = 1
        elif exprType == "string":
            type = 2
        elif exprType == "true" or exprType == "false":
            type = 3
        elif exprType == "array":
            type = 4
        elif exprType == "hash":
            type = 5
        elif exprType == "function" or exprType == "funcLiteral":
            type = 6
            isFunction = True
            hasReturn = True

        identCtx = self.visit(ctx.ident())
        lvl = self.table.getCurrentLevel()
        self.table.push(identCtx.IDENT(), type, lvl, ctx, isFunction, hasReturn)
        self.table.print()
        return None

    def visitReturnStatementAST(self, ctx: monkeyParser.ReturnStatementASTContext):
        result = self.visit(ctx.expression())

        return result

    def visitExpressionStatementAST(self, ctx: monkeyParser.ExpressionStatementASTContext):
        result = self.visit(ctx.expression())

        return result

    def visitExpressionAST(self, ctx: monkeyParser.ExpressionASTContext):
        result = self.visit(ctx.additionExpression(0))
        i = 1
        while True:
            if i < len(ctx.additionExpression()):
                if not (ctx.equalOperators()[i - 1] is None):
                    self.visit(ctx.equalOperators()[i - 1])
                self.visit(ctx.additionExpression(i))
            else:
                break
            i += 1

        return result

    def visitAdditionExpressionAST(self, ctx: monkeyParser.AdditionExpressionASTContext):
        result = self.visit(ctx.multiplicationExpression(0))
        i = 1
        while True:
            if i < len(ctx.multiplicationExpression()):
                if not (ctx.addOperators()[i - 1] is None):
                    self.visit(ctx.addOperators()[i - 1])
                self.visit(ctx.multiplicationExpression(i))
            else:
                break
            i += 1

        return result

    def visitMultiplicationExpressionAST(self, ctx: monkeyParser.MultiplicationExpressionASTContext):
        result = self.visit(ctx.elementExpression(0))
        i = 1
        while True:
            if i < len(ctx.elementExpression()):
                if not (ctx.multOperators()[i - 1] is None):
                    self.visit(ctx.multOperators()[i - 1])
                self.visit(ctx.elementExpression(i))
            else:
                break
            i += 1
        return result

    def visitElementExpressionAST(self, ctx: monkeyParser.ElementExpressionASTContext):
        result = self.visit(ctx.primitiveExpression())
        if not (ctx.elementAccess() is None):
            result = self.visit(ctx.elementAccess())
        elif not (ctx.callExpression() is None):
            result = self.visit(ctx.callExpression())

        return result

    def visitElementAccessAST(self, ctx: monkeyParser.ElementAccessASTContext):
        self.output += "- Element Access: \n"
        self.output += ("- PCIZQ: \"" + ctx.PCIZQ().__str__() + "\"\n")
        self.visit(ctx.expression())
        self.output += ("- PCDER: \"" + ctx.PCDER().__str__() + "\"\n")
        return "access"

    def visitCallExpressionAST(self, ctx: monkeyParser.CallExpressionASTContext):
        self.output += "- Call Expression: \n"
        self.output += ("- PIZQ: \"" + ctx.PIZQ().__str__() + "\"\n")
        self.visit(ctx.expressionList())
        self.output += ("- PDER: \"" + ctx.PDER().__str__() + "\"\n")
        return "call"

    def visitPrimitiveExpressionIntegerAST(self, ctx: monkeyParser.PrimitiveExpressionIntegerASTContext):
        return "int"

    def visitPrimitiveExpressionStringAST(self, ctx: monkeyParser.PrimitiveExpressionStringASTContext):
        return "string"

    def visitPrimitiveExpressionIdentAST(self, ctx: monkeyParser.PrimitiveExpressionIdentASTContext):
        identCtx = self.visit(ctx.ident())
        self.output += "- Identifier: \"" + identCtx.IDENT().__str__() + "\"\n"
        return "ident"

    def visitPrimitiveExpressionTrueAST(self, ctx: monkeyParser.PrimitiveExpressionTrueASTContext):
        return "true"

    def visitPrimitiveExpressionFalseAST(self, ctx: monkeyParser.PrimitiveExpressionFalseASTContext):
        return "false"

    def visitPrimitiveExpressionExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionExpressionASTContext):
        self.table.openScope()
        self.visit(ctx.expression())
        self.table.closeScope()
        if self.fromIf:
            self.output += ("- PDER: \"" + ctx.PDER().__str__() + "\"\n")
        else:
            self.output += ("- PDER: \"" + ctx.PDER().__str__() + "\"\n")
        return "expression"

    def visitPrimitiveExpressionarrayLiteralast(self, ctx: monkeyParser.PrimitiveExpressionarrayLiteralastContext):
        return "array"

    def visitPrimitiveExpressionarrayFunctionsAST(self, ctx: monkeyParser.PrimitiveExpressionarrayFunctionsASTContext):
        self.visit(ctx.arrayFunctions())
        self.visit(ctx.expressionList())

        return "function"

    def visitPrimitiveExpressionfunctionLiteralAST(self, ctx: monkeyParser.PrimitiveExpressionfunctionLiteralASTContext):
        self.output += "- Primitive Expression Function Literal:\n"
        self.table.openScope()
        print("func lit" + str(self.table.getCurrentLevel()))
        self.visit(ctx.functionLiteral())
        self.table.closeScope()
        return "funcLiteral"

    def visitPrimitiveExpressionhashLiteralAST(self, ctx: monkeyParser.PrimitiveExpressionhashLiteralASTContext):
        self.output += "- Primitive Expression Hash Literal:\n"
        self.visit(ctx.hashLiteral())
        return "hash"

    def visitPrimitiveExpressionprintExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionprintExpressionASTContext):
        self.output += "- Primitive Expression Print Expression:\n"
        self.visit(ctx.printExpression())
        return "print"

    def visitPrimitiveExpressionifExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionifExpressionASTContext):
        self.output += "- Primitive Expression If Expression:\n"
        self.visit(ctx.ifExpression())
        return "if"

    def visitArrayFunctionsLenAST(self, ctx: monkeyParser.ArrayFunctionsLenASTContext):
        return "len"

    def visitArrayFunctionsFirstAST(self, ctx: monkeyParser.ArrayFunctionsFirstASTContext):
        return "first"

    def visitArrayFunctionsLastAST(self, ctx: monkeyParser.ArrayFunctionsLastASTContext):
        return "last"

    def visitArrayFunctionsRestAST(self, ctx: monkeyParser.ArrayFunctionsRestASTContext):
        return "rest"

    def visitArrayFunctionsPushAST(self, ctx: monkeyParser.ArrayFunctionsPushASTContext):
        return "push"

    def visitArrayLiteralAST(self, ctx: monkeyParser.ArrayLiteralASTContext):
        self.output += "- Array Literal\n"
        self.output += "- PCIZQ: \"" + ctx.PCIZQ().__str__() + "\"\n"
        self.visit(ctx.expressionList())
        self.output += "- PCDER: \"" + ctx.PCDER().__str__() + "\"\n"
        return None

    def visitFunctionLiteralAST(self, ctx: monkeyParser.FunctionLiteralASTContext):
        self.output += "- Function Literal: \n"
        self.output += "- FN: \"" + ctx.FN().__str__() + "\"\n"
        self.output += "- PIZQ: \"" + ctx.PIZQ().__str__() + "\"\n"
        self.visit(ctx.functionParameters())
        self.output += "- PDER: \"" + ctx.PDER().__str__() + "\"\n"
        self.output += "- LIZQ: \"" + ctx.LIZQ().__str__() + "\"\n"
        i = 0
        while True:
            if i < len(ctx.statement()):
                self.fromFunc = True
                self.visit(ctx.statement()[i])
                self.fromFunc = False
            else:
                break
            i += 1

        self.output += "- LDER: \"" + ctx.LDER().__str__() + "\"\n"
        return None

    def visitFunctionParametersAST(self, ctx: monkeyParser.FunctionParametersASTContext):
        self.output += "- Function Parameters: \n"
        self.output += "- IDENT: \"" + ctx.IDENT()[0].__str__() + "\"\n"
        i = 1
        while True:
            if i < len(ctx.IDENT()):
                self.output += "- COMA: \"" + ctx.COMA()[i-1].__str__() + "\"\n"
                self.output += "- IDENT: \"" + ctx.IDENT()[i].__str__() + "\"\n"
            else:
                break
            i += 1

        return None

    def visitHashLiteralAST(self, ctx: monkeyParser.HashLiteralASTContext):
        self.output += "- Hash Literal: \n"
        self.output += "- LIZQ: \"" + ctx.LIZQ().__str__() + "\"\n"
        self.visit(ctx.hashContent()[0])
        i = 1
        while True:
            if i < len(ctx.hashContent()):
                self.output += "- COMA: \"" + ctx.COMA()[i-1].__str__() + "\"\n"
                self.visit(ctx.hashContent()[i])
            else:
                break
            i += 1

        self.output += "- LDER: \"" + ctx.LDER().__str__() + "\"\n"
        return None

    def visitHashContentAST(self, ctx: monkeyParser.HashContentASTContext):
        self.output += "- Hash Content: \n"
        self.visit(ctx.expression(0))
        self.output += "- DOSPUNTOS: \"" + ctx.DOSPUNTOS().__str__() + "\"\n"
        self.visit(ctx.expression(1))
        return None

    def visitExpressionListAST(self, ctx: monkeyParser.ExpressionListASTContext):
        self.output += "- Expression List: \n"
        self.visit(ctx.expression()[0])
        i = 1
        while True:
            if i < len(ctx.expression()):
                self.output += "- COMA: \"" + ctx.COMA()[i-1].__str__() + "\"\n"
                self.visit(ctx.expression()[i])
            else:
                break
            i += 1

        return None

    def visitPrintExpressionAST(self, ctx: monkeyParser.PrintExpressionASTContext):
        self.output += "- Print Expression: \n"
        self.output += "- PUTS: \"" + ctx.PUTS().__str__() + "\"\n"
        self.output += "- PIZQ: \"" + ctx.PIZQ().__str__() + "\"\n"
        self.visit(ctx.expression())
        self.output += "- PDER: \"" + ctx.PDER().__str__() + "\"\n"
        return None

    def visitIfExpressionAST(self, ctx: monkeyParser.IfExpressionASTContext):
        self.output += "- If Expression: \n"
        self.output += "- IF: \"" + ctx.IF().__str__() + "\"\n"
        self.fromIf = True
        self.table.openScope()
        print("Curr Lvl: "+str(self.table.getCurrentLevel()))
        self.visit(ctx.expression())
        self.table.closeScope()
        self.fromIf = False
        self.output += "- LIZQ: \"" + ctx.LIZQ().__str__() + "\"\n"
        self.visit(ctx.statement()[0])
        i = 1
        while True:
            if i < len(ctx.statement()):
                self.visit(ctx.statement()[i])
            else:
                break
            i += 1

        self.output += "- LDER: \"" + ctx.LDER().__str__() + "\"\n"

        if not (ctx.elseExpression() is None):
            self.visit(ctx.elseExpression())

        return None

    def visitElseExpressionAST(self, ctx: monkeyParser.ElseExpressionASTContext):
        self.output += "- ELSE: \"" + ctx.ELSE().__str__() + "\"\n"
        self.output += "- LIZQ: \"" + ctx.LIZQ().__str__() + "\"\n"

        i = 0
        while True:
            if i < len(ctx.statement()):
                self.visit(ctx.statement()[i])
            else:
                break
            i += 1

        self.output += "- LDER: \"" + ctx.LDER().__str__() + "\"\n"
        return None

    def visitMultOperators(self, ctx: monkeyParser.MultOperatorsContext):
        if not (ctx.MULT() is None):
            operator = ctx.MULT().__str__()
        elif not (ctx.DIV() is None):
            operator = ctx.DIV().__str__()
        else:
            operator = None

        return operator

    def visitAddOperators(self, ctx: monkeyParser.AddOperatorsContext):
        if not (ctx.SUMA() is None):
            operator = ctx.SUMA().__str__()
        elif not (ctx.RESTA() is None):
            operator = ctx.RESTA().__str__()
        else:
            operator = None
        return operator

    def visitEqualOperators(self, ctx: monkeyParser.EqualOperatorsContext):
        if not (ctx.EQUAL() is None):
            operator = ctx.EQUAL().__str__()
        elif not (ctx.MENOR() is None):
            operator = ctx.MENOR().__str__()
        elif not (ctx.MAYOR() is None):
            operator = ctx.MAYOR().__str__()
        elif not (ctx.MENOREQUAL() is None):
            operator = ctx.MENOREQUAL().__str__()
        elif not (ctx.MAYOREQUAL() is None):
            operator = ctx.MAYOREQUAL().__str__()
        else:
            operator = None
        return operator

    def visitIdentAST(self, ctx: monkeyParser.IdentASTContext):
        return ctx


