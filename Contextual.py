from generated.monkeyParserVisitor import monkeyParserVisitor
from generated.monkeyParser import monkeyParser
from SymbolTable import SymbolTable


class Contextual(monkeyParserVisitor):
    table = None
    output = ""
    currentIdent = None
    fromFunc = False
    hasReturn = False
    fromIf = False
    fromAccess = False
    fromCall = False
    fromElement = False
    fromList = False
    fromListName = ""
    fromListparams=-1

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
        self.table.print()
        return None

    def visitLetStatementAST(self, ctx: monkeyParser.LetStatementASTContext):
        result = self.visit(ctx.expression())
        hasReturn, isFunction = False, False
        tp = -1
        params = -1
        length = None
        if type(result) is str:
            if result == "int":
                tp = 1
            elif result == "string":
                tp = 2
            elif result == "true" or result == "false":
                tp = 3
            elif result == "hash":
                tp = 5
        elif type(result) is int:
            tp = 4
            length = result
            print("-------------- "+ str(length))
        else:
            tp = 6
            isFunction = True
            hasReturn = self.hasReturn
            params = len(result)
        if not self.hasReturn and isFunction:
            print("La función no tiene retorno, no se puede asignar a una variable")
            self.hasReturn = False

        identCtx = self.visit(ctx.ident())
        lvl = self.table.getCurrentLevel()
        if self.fromList:

            self.fromListName = "funtion"+identCtx.IDENT().__str__() + str(self.fromListName)
            self.table.push(self.fromListName, tp, lvl, ctx, True, hasReturn, self.fromListparams, length)
            self.fromList = False
            self.fromListName = ""
        else:
            self.table.push(identCtx.IDENT(), tp, lvl, ctx, isFunction, hasReturn, params, length)
        return None

    def visitReturnStatementAST(self, ctx: monkeyParser.ReturnStatementASTContext):
        result = self.visit(ctx.expression())
        if not self.fromFunc:
            print("No se puede retornar, es necesario una función.")
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
            if type(resultCtx) == 'generated.monkeyParser.monkeyParser.IdentASTContext':
                ident = self.table.search(resultCtx.IDENT().__str__())
                if ident is None:
                    print("El identificador \"" + resultCtx.IDENT().__str__() + "\" no ha sido declarado")
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
                if result >= ident.length:
                    print("El array \"" + self.currentIdent.IDENT().__str__() + "\" tiene " + str(ident.length) +
                          " elementos en vez de " + str(result))
        self.fromAccess = False

        return result

    def visitCallExpressionAST(self, ctx: monkeyParser.CallExpressionASTContext):
        self.fromCall = True
        result = self.visit(ctx.expressionList())
        self.fromCall = False
        return result

    def visitPrimitiveExpressionIntegerAST(self, ctx: monkeyParser.PrimitiveExpressionIntegerASTContext):
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
        if self.fromIf:
            self.output += ("- PDER: \"" + ctx.PDER().__str__() + "\"\n")
        else:
            self.output += ("- PDER: \"" + ctx.PDER().__str__() + "\"\n")
        return ctx

    def visitPrimitiveExpressionarrayLiteralast(self, ctx: monkeyParser.PrimitiveExpressionarrayLiteralastContext):
        length = self.visit(ctx.arrayLiteral())
        self.fromList = True
        return length

    def visitPrimitiveExpressionarrayFunctionsAST(self, ctx: monkeyParser.PrimitiveExpressionarrayFunctionsASTContext):
        self.visit(ctx.arrayFunctions())
        self.visit(ctx.expressionList())
        return "arrayFunction"

    def visitPrimitiveExpressionfunctionLiteralAST(self,
                                                   ctx: monkeyParser.PrimitiveExpressionfunctionLiteralASTContext):
        self.output += "- Primitive Expression Function Literal:\n"
        self.table.openScope()
        self.fromFunc = True
        fnCtx = self.visit(ctx.functionLiteral())
        self.fromFunc = False
        self.table.closeScope()
        return fnCtx

    def visitPrimitiveExpressionhashLiteralAST(self, ctx: monkeyParser.PrimitiveExpressionhashLiteralASTContext):
        self.output += "- Primitive Expression Hash Literal:\n"
        self.visit(ctx.hashLiteral())
        return "hash"

    def visitPrimitiveExpressionprintExpressionAST(self,
                                                   ctx: monkeyParser.PrimitiveExpressionprintExpressionASTContext):
        self.output += "- Primitive Expression Print Expression:\n"
        self.visit(ctx.printExpression())
        return ctx

    def visitPrimitiveExpressionifExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionifExpressionASTContext):
        self.output += "- Primitive Expression If Expression:\n"
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
        self.fromListName = self.fromListName+str(length)
        return length

    def visitFunctionLiteralAST(self, ctx: monkeyParser.FunctionLiteralASTContext):
        self.output += "- Function Literal: \n"
        self.output += "- FN: \"" + ctx.FN().__str__() + "\"\n"
        self.output += "- PIZQ: \"" + ctx.PIZQ().__str__() + "\"\n"
        parametersCtx = self.visit(ctx.functionParameters())
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

        self.fromListparams = len(parametersCtx)
        return parametersCtx

    def visitFunctionParametersAST(self, ctx: monkeyParser.FunctionParametersASTContext):
        i = 1
        while True:
            if i < len(ctx.ident()):
                self.output += "- COMA: \"" + ctx.COMA()[i - 1].__str__() + "\"\n"
                self.output += "- IDENT: \"" + ctx.ident(i).__str__() + "\"\n"
            else:
                break
            i += 1

        return ctx.ident()

    def visitHashLiteralAST(self, ctx: monkeyParser.HashLiteralASTContext):
        self.output += "- Hash Literal: \n"
        self.output += "- LIZQ: \"" + ctx.LIZQ().__str__() + "\"\n"
        self.visit(ctx.hashContent()[0])
        i = 1
        while True:
            if i < len(ctx.hashContent()):
                self.output += "- COMA: \"" + ctx.COMA()[i - 1].__str__() + "\"\n"
                self.visit(ctx.hashContent()[i])
            else:
                break
            i += 1

        self.output += "- LDER: \"" + ctx.LDER().__str__() + "\"\n"
        return None

    def visitHashContentAST(self, ctx: monkeyParser.HashContentASTContext):
        self.output += "- Hash Content: \n"

        ctxResult1 = self.visit(ctx.expression(0))
        if not type(ctxResult1) is int and not type(ctxResult1) is str:
            print("Error, dato no aceptado en hashContent")
        self.output += "- DOSPUNTOS: \"" + ctx.DOSPUNTOS().__str__() + "\"\n"
        self.visit(ctx.expression(1))
        return None

    def visitExpressionListAST(self, ctx: monkeyParser.ExpressionListASTContext):
        length = 0
        if not (self.currentIdent is None):
            ident = self.table.search(self.currentIdent.IDENT().__str__())
            if not (ident is None):
                if ident.params == len(ctx.expression()):
                    self.visit(ctx.expression()[0])
                    i = 1
                    while True:
                        if i < len(ctx.expression()):
                            self.output += "- COMA: \"" + ctx.COMA()[i - 1].__str__() + "\"\n"
                            self.visit(ctx.expression()[i])
                        else:
                            break
                        i += 1
                else:
                    print("La función \"" + self.currentIdent.IDENT().__str__() + "\" tiene " + str(ident.params) +
                          " parámetros en vez de " + str(len(ctx.expression())))
        else:
            length = len(ctx.expression())
            self.visit(ctx.expression()[0])
            i = 1
            while True:
                if i < len(ctx.expression()):
                    self.visit(ctx.expression()[i])
                else:
                    break
                i += 1

        return length

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
        self.visit(ctx.expression())
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
        self.table.closeScope()
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
