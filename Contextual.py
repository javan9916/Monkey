from generated.monkeyParserVisitor import monkeyParserVisitor
from generated.monkeyParser import monkeyParser
from SymbolTable import SymbolTable


class Contextual(monkeyParserVisitor):
    table = None
    output = ""
    currentIdent = None
    isInt = False
    fromFunc = False
    hasReturn = False
    fromIf = False
    fromAccess = False
    fromCall = False
    fromElement = False
    fromList = False
    fromListName = ""
    fromListparams = -1

    def __init__(self):
        self.table = SymbolTable()
        self.table.pushInternals()

    def blankTable(self):
        self.table.table.clear()

    def getOutput(self):
        return self.output

    def getSymbolTable(self):
        return self.table

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
        identCtx = self.visit(ctx.ident())
        self.fromListName = identCtx.IDENT().__str__()
        result = self.visit(ctx.expression())
        hasReturn, isFunction = False, False
        tp = -1
        params = -1
        length = None
        if type(result) is str:
            if result == "string":
                tp = 2
            elif result == "true" or result == "false":
                tp = 3
            elif result == "hash":
                tp = 5
        elif type(result) is int:
            if not self.fromList:
                tp = 1
            elif self.isInt:
                tp = 4
                length = result
        else:
            tp = 6
            isFunction = True
            hasReturn = self.hasReturn
            params = len(result)
        if not self.hasReturn and isFunction:
            self.output += "ERROR: La función no tiene retorno, no se puede asignar a una variable\n"
            self.hasReturn = False

        lvl = self.table.getCurrentLevel()

        self.table.push(identCtx.IDENT(), tp, lvl, ctx, isFunction, hasReturn, params, length, False)
        return None

    def visitReturnStatementAST(self, ctx: monkeyParser.ReturnStatementASTContext):
        result = self.visit(ctx.expression())
        if not self.fromFunc:
            self.output += "ERROR: No se puede retornar, es necesario una función\n"
        else:
            self.hasReturn = True
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
        resultCtx = self.visit(ctx.primitiveExpression())
        if not self.fromFunc:
            if type(resultCtx) == 'generated.monkeyParser.monkeyParser.PrimitiveExpressionIdentASTContext':
                ident = self.table.search(resultCtx.IDENT().__str__())
                if ident is None:
                    self.output += "ERROR: El identificador \"" + resultCtx.IDENT().__str__() + "\" no ha sido " \
                                                                                                "declarado\n "
        if not (ctx.elementAccess() is None):
            self.currentIdent = resultCtx
            resultCtx = self.visit(ctx.elementAccess())
            self.currentIdent = None
        elif not (ctx.callExpression() is None):
            self.currentIdent = resultCtx
            resultCtx = self.visit(ctx.callExpression())
            self.currentIdent = None
        return resultCtx

    def visitElementAccessAST(self, ctx: monkeyParser.ElementAccessASTContext):
        self.fromAccess = True
        result = self.visit(ctx.expression())
        if type(result) == int:
            ident = self.table.search(self.currentIdent.IDENT().__str__())
            if not ident is None:
                if not (ident.length is None):
                    if result >= ident.length:
                        self.output += "ERROR: El array \"" + self.currentIdent.IDENT().__str__() + "\" tiene " + \
                                       str(ident.length) + " elementos en vez de " + str(result) + "\n "
            else:
                self.output += "ERROR: El array \"" + self.currentIdent.IDENT().__str__() + "\" no está declarado \n"
        self.fromAccess = False
        return result

    def visitCallExpressionAST(self, ctx: monkeyParser.CallExpressionASTContext):
        self.fromCall = True
        result = self.visit(ctx.expressionList())
        self.fromCall = False
        return result

    def visitPrimitiveExpressionIntegerAST(self, ctx: monkeyParser.PrimitiveExpressionIntegerASTContext):
        self.fromList = False
        self.isInt = True
        return int(ctx.INTEGER().__str__())

    def visitPrimitiveExpressionStringAST(self, ctx: monkeyParser.PrimitiveExpressionStringASTContext):
        return "string"

    def visitPrimitiveExpressionIdentAST(self, ctx: monkeyParser.PrimitiveExpressionIdentASTContext):
        identCtx = self.visit(ctx.ident())
        return identCtx

    def visitPrimitiveExpressionTrueAST(self, ctx: monkeyParser.PrimitiveExpressionTrueASTContext):
        return "true"

    def visitPrimitiveExpressionFalseAST(self, ctx: monkeyParser.PrimitiveExpressionFalseASTContext):
        return "false"

    def visitPrimitiveExpressionExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionExpressionASTContext):
        self.table.openScope()
        self.visit(ctx.expression())
        self.table.closeScope()
        return ctx

    def visitPrimitiveExpressionarrayLiteralast(self, ctx: monkeyParser.PrimitiveExpressionarrayLiteralastContext):
        self.isInt = False
        length = self.visit(ctx.arrayLiteral())
        self.fromList = True
        return length

    def visitPrimitiveExpressionarrayFunctionsAST(self, ctx: monkeyParser.PrimitiveExpressionarrayFunctionsASTContext):
        self.visit(ctx.arrayFunctions())
        self.visit(ctx.expressionList())
        return "arrayFunction"

    def visitPrimitiveExpressionfunctionLiteralAST(self,
                                                   ctx: monkeyParser.PrimitiveExpressionfunctionLiteralASTContext):
        self.table.openScope()
        self.fromFunc = True
        fnCtx = self.visit(ctx.functionLiteral())
        self.fromFunc = False
        self.table.closeScope()
        return fnCtx

    def visitPrimitiveExpressionhashLiteralAST(self, ctx: monkeyParser.PrimitiveExpressionhashLiteralASTContext):
        self.visit(ctx.hashLiteral())
        return "hash"

    def visitPrimitiveExpressionprintExpressionAST(self,
                                                   ctx: monkeyParser.PrimitiveExpressionprintExpressionASTContext):
        self.visit(ctx.printExpression())
        return ctx

    def visitPrimitiveExpressionifExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionifExpressionASTContext):
        self.visit(ctx.ifExpression())
        return ctx

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
        length = self.visit(ctx.expressionList())
        return length

    def visitFunctionLiteralAST(self, ctx: monkeyParser.FunctionLiteralASTContext):
        parametersCtx = self.visit(ctx.functionParameters())
        i = 0
        while True:
            if i < len(ctx.statement()):
                self.fromFunc = True
                self.visit(ctx.statement()[i])
                self.fromFunc = False
            else:
                break
            i += 1

        self.fromListparams = len(parametersCtx)
        return parametersCtx

    def visitFunctionParametersAST(self, ctx: monkeyParser.FunctionParametersASTContext):
        return ctx.ident()

    def visitHashLiteralAST(self, ctx: monkeyParser.HashLiteralASTContext):
        self.visit(ctx.hashContent()[0])
        i = 1
        while True:
            if i < len(ctx.hashContent()):
                self.visit(ctx.hashContent()[i])
            else:
                break
            i += 1

        return None

    def visitHashContentAST(self, ctx: monkeyParser.HashContentASTContext):
        ctxResult = self.visit(ctx.expression(0))
        if not type(ctxResult) is int and not type(ctxResult) is str:
            self.output += "ERROR: Dato no aceptado en hashContent\n"
        self.visit(ctx.expression(1))
        return None

    def visitExpressionListAST(self, ctx: monkeyParser.ExpressionListASTContext):
        length = 0
        if not (self.currentIdent is None):
            ident = self.table.search(self.currentIdent.IDENT().__str__())
            if not (ident is None):
                if not ident.fromList:
                    if ident.params == len(ctx.expression()):
                        self.visit(ctx.expression()[0])
                        i = 1
                        while True:
                            if i < len(ctx.expression()):
                                self.visit(ctx.expression()[i])
                            else:
                                break
                            i += 1
                    else:
                        self.output += "ERROR: La función \"" + self.currentIdent.IDENT().__str__() + "\" tiene " + \
                                       str(ident.params) + " parámetros en vez de " + str(len(ctx.expression())) + "\n"
                else:
                    self.output += "ERROR: El identificador \"" + self.currentIdent.IDENT().__str__() + "\" no ha " \
                                                                                                        "sido declarado \n "
            else:
                self.output += "ERROR: El identificador \"" + self.currentIdent.IDENT().__str__() + "\" no ha " \
                                                                                                    "sido declarado \n "

        else:
            length = len(ctx.expression())
            self.visit(ctx.expression()[0])
            i = 1
            while True:
                if i < len(ctx.expression()):
                    self.visit(ctx.expression()[i])
                else:
                    break

                if not self.fromListparams == -1:
                    self.fromListName = "function_" + self.fromListName + str(i)
                    self.table.push(self.fromListName, 7, 0, ctx, True, True, self.fromListparams, -1, True)
                i += 1

        return length

    def visitPrintExpressionAST(self, ctx: monkeyParser.PrintExpressionASTContext):
        self.visit(ctx.expression())
        return None

    def visitIfExpressionAST(self, ctx: monkeyParser.IfExpressionASTContext):
        self.fromIf = True
        self.table.openScope()
        self.visit(ctx.expression())
        self.fromIf = False
        self.visit(ctx.statement()[0])
        i = 1
        while True:
            if i < len(ctx.statement()):
                self.visit(ctx.statement()[i])
            else:
                break
            i += 1

        if not (ctx.elseExpression() is None):
            self.visit(ctx.elseExpression())
        self.table.closeScope()
        return None

    def visitElseExpressionAST(self, ctx: monkeyParser.ElseExpressionASTContext):
        i = 0
        while True:
            if i < len(ctx.statement()):
                self.visit(ctx.statement()[i])
            else:
                break
            i += 1

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
