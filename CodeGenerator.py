from generated.monkeyParser import monkeyParser
from generated.monkeyParserVisitor import monkeyParserVisitor
from Symbols import Symbols
import types


class CodeGenerator(monkeyParserVisitor):
    letMain = None
    indice = None
    codigo = None
    fromFunc = False
    isOperator = None
    var =None;
    isHas = False
    paramsFun = False
    isFuctionArray = False
    isAcces = False

    insideMain = False
    isMain = None
    table = None
    output = ""
    currentIdent = None
    hasReturn = False
    fromIf = False
    fromAccess = False
    fromCall = False
    fromElement = False
    fromList = False
    fromListName = ""
    fromListparams = -1
    bandOpe = None

    def __init__(self):
        self.letMain = -1
        self.isMain = False
        self.indice = 0
        self.codigo = []
        self.table = Symbols()
        self.bandOpe = False
        self.isOperator = False

    def blankTable(self):
        self.table.table.clear()

    def getOutput(self):
        return self.output

    def getSymbolTable(self):
        return self.table

    def generar(self, indice, instr, param):
        if param is not None:
            self.codigo.append(indice + " " + instr + " " + param)

        else:
            self.codigo.append(indice + " " + instr)
        self.indice += 1

    def visitProgramAST(self, ctx: monkeyParser.ProgramASTContext):
        i = 0
        while True:
            if i < len(ctx.statement()):
                self.visit(ctx.statement(i))
            else:
                break
            i += 1

        self.generar(str(self.indice), "END", None)
        if not self.isMain:
            print("WARNING: No se declaró el Main.")
        self.output = self.printEnd()
        return None

    def visitLetStatementAST(self, ctx: monkeyParser.LetStatementASTContext):
        identCtx = self.visit(ctx.ident())
        if not (identCtx.IDENT().__str__() == 'Main'):
            self.table.openScope()
        else:
            self.insideMain = True

        tagIndex = self.indice
        lvl = self.table.getCurrentLevel()
        if lvl <= 0 or self.insideMain:
            mode1 = 'GLOBAL'
            mode2 = 'GLOBAL'
        else:
            mode1 = 'LOCAL'
            mode2 = 'FAST'

        if identCtx.IDENT().__str__() == 'Main' and not self.isMain:
            self.isMain = True
            self.generar(str(self.indice), "DEF", "Main")
        elif identCtx.IDENT().__str__() == 'Main' and self.isMain:
            print("ERROR: Main ya ha sido declarado...")
            return None
        else:
            token = self.table.search(identCtx.IDENT().__str__())
            if token == None:
                self.generar(str(self.indice), "PUSH_" + mode1 + "_VAR", identCtx.IDENT().__str__())


        result = self.visit(ctx.expression())

        if not (identCtx.IDENT().__str__() == 'Main' or isinstance(result, list)):
            if self.var == '_D':
                mode2= mode2+'_DICT'
            elif self.var == '_L':
                mode2 = mode2+'_LIST'
            self.generar(str(self.indice), "STORE_" + mode2, identCtx.IDENT().__str__())

        if result is not None:
            if isinstance(result, int):
                instruction = self.codigo[tagIndex].split()
                isPush = instruction[1].split("_")
                var = None
                if isPush[0] == 'PUSH':
                    if self.var == '_L':
                        var = '_L'
                    else:
                        var = '_I'
                    self.codigo[tagIndex] = instruction[0] + " " + "PUSH_" + mode1 + var + " " + instruction[2]

                    if self.insideMain:
                        self.table.push(identCtx.IDENT().__str__(), 0, 1, ctx, False, 0, False)
                    else:
                        self.table.push(identCtx.IDENT().__str__(), lvl, 1, ctx, False, 0, False)
                    self.var = None
            elif isinstance(result, str):
                instruction = self.codigo[tagIndex].split()
                isPush = instruction[1].split("_")
                if isPush[0] == 'PUSH':
                    var = "_C"
                    if self.var == '_D':
                        var = '_D'
                    else:
                        var = '_C'
                    self.codigo[tagIndex] = instruction[0] + " " + "PUSH_" + mode1 + var+ " " + instruction[2]
                    if self.insideMain:
                        self.table.push(identCtx.IDENT().__str__(), 0, 2, ctx, False, 0, False)
                    else:
                        self.table.push(identCtx.IDENT().__str__(), lvl, 2, ctx, False, 0, False)
                    self.var = None
            else:
                if isinstance(result, list):
                    instruction = self.codigo[tagIndex].split()
                    self.codigo[tagIndex] = instruction[0] + " DEF " + identCtx.IDENT().__str__()
                    if result[0].IDENT().__str__() != '<missing IDENT>':
                        self.table.push(identCtx.IDENT().__str__(), lvl, 3, ctx, True, len(result), False)
                    else:
                        self.table.push(identCtx.IDENT().__str__(), lvl, 3, ctx, True, 0, False)
                else:
                    token = self.table.search(result.IDENT().__str__())
                    if token is not None:
                        if token.getType() == 1:
                            instruction = self.codigo[tagIndex].split()
                            self.codigo[tagIndex] = instruction[0] + " " + "PUSH_" + mode1 + "_I" + " " + \
                                                    instruction[2]
                            if self.insideMain:
                                self.table.push(identCtx.IDENT().__str__(), 0, 1, ctx, False, 0, False)
                            else:
                                self.table.push(identCtx.IDENT().__str__(), lvl, 1, ctx, False, 0, False)
                        elif token.getType() == 2:
                            instruction = self.codigo[tagIndex].split()
                            self.codigo[tagIndex] = instruction[0] + " " + "PUSH_" + mode1 + "_C" + " " + \
                                                    instruction[2]
                            if self.insideMain:
                                self.table.push(identCtx.IDENT().__str__(), 0, 2, ctx, False, 0, False)
                            else:
                                self.table.push(identCtx.IDENT().__str__(), lvl, 2, ctx, False, 0, False)
        else:
            print("ERROR: Ha sucedido algo inesperado...")
        res = self.table.search(identCtx.IDENT().__str__())
        if res is None:
            self.table.push(identCtx.IDENT().__str__(), lvl, 0, 0, False,0, False)
        if not (identCtx.IDENT().__str__() == 'Main'):
            token = self.table.search(identCtx.IDENT().__str__())
            if token is not None:
                if token.getType() == 3:
                    self.generar(str(self.indice), "RETURN", None)
            self.table.closeScope()


        return None

    def visitReturnStatementAST(self, ctx: monkeyParser.ReturnStatementASTContext):

        result = self.visit(ctx.expression())
        self.generar(str(self.indice), "LOAD_FAST", result.IDENT().__str__())
        self.generar(str(self.indice), "RETURN_VALUE", None)
        return result

    def visitExpressionStatementAST(self, ctx: monkeyParser.ExpressionStatementASTContext):
        result = self.visit(ctx.expression())
        # self.generar(str(self.indice), "visitExpressionStatementAST", result)
        return result

    def visitExpressionAST(self, ctx: monkeyParser.ExpressionASTContext):
        result = self.visit(ctx.additionExpression(0))

        i = 1
        while True:
            if i < len(ctx.additionExpression()):
                if not (ctx.equalOperators()[i - 1] is None):
                    operator = self.visit(ctx.equalOperators()[i - 1])
                self.visit(ctx.additionExpression(i))
                value = None
                if isinstance(result,monkeyParser.IdentASTContext):
                    token = self.table.search(result.IDENT().__str__())
                    lvl = token.getLevel()
                    mode1 = None
                    if lvl <= 0:
                        mode1 = 'CONST'
                    else:
                        mode1 = 'FAST'
                    self.generar(str(self.indice), "LOAD_" + mode1, result.IDENT().__str__())

                self.generar(str(self.indice), "COMPARE_OP", operator)
            else:
                break
            i += 1

        return result

    def visitAdditionExpressionAST(self, ctx: monkeyParser.AdditionExpressionASTContext):
        lvl = self.table.getCurrentLevel()
        if lvl <= 0:
            mode1 = 'GLOBAL'
        else:
            mode1 = 'FAST'

        operator = ""
        tokenType = 0
        result = self.visit(ctx.multiplicationExpression(0))

        if isinstance(result,int):
            tokenType =1
        elif isinstance(result,str):
            tokenType=2
        result2 = result
        if isinstance(result, monkeyParser.IdentASTContext) and not self.isHas and not self.paramsFun:
            token = self.table.search(result.IDENT().__str__())
            if token is not None:
                result2 = result.IDENT().__str__()
                tokenType = token.getType()
            else:
                print("ERROR: El identificador \"" + result.IDENT().__str__() + "\" no existe")
                return None

        i = 1
        while True:
            if i < len(ctx.multiplicationExpression()):
                if not (ctx.addOperators()[i - 1] is None):
                    operator = self.visit(ctx.addOperators()[i - 1])
                result = self.visit(ctx.multiplicationExpression(i))

                if isinstance(result, monkeyParser.IdentASTContext):
                    token = self.table.search(result.IDENT().__str__())
                    if token is not None:
                        if token.getType() != tokenType:
                            print("ERROR: Los tipos de dato no coinciden")
                            break
                    else:
                        print("ERROR: El identificador \"" + result.IDENT().__str__() + "\" no existe")
                        break
            else:
                break
            i += 1

            if operator == "+":
                operator = 'BINARY_ADD'
            elif operator == '-':
                operator = 'BINARY_SUBSTRACT'


            instruction = self.codigo[self.indice - 1].split()

            if not (instruction[1] == "BINARY_ADD" or instruction == "BINARY_SUBSTRACT"):
                if not isinstance(result2,int):
                    self.generar(str(self.indice), "LOAD_" + mode1, result2)
            if not isinstance(result,int):
                self.generar(str(self.indice), "LOAD_" + mode1, result.IDENT().__str__())
            self.generar(str(self.indice), operator, None)

        return result

    def visitMultiplicationExpressionAST(self, ctx: monkeyParser.MultiplicationExpressionASTContext):
        lvl = self.table.getCurrentLevel()
        if lvl <= 0:
            mode1 = 'GLOBAL'
        else:
            mode1 = 'FAST'

        operator = ""
        tokenType = 0
        result = self.visit(ctx.elementExpression(0))

        if isinstance(result, int):
            tokenType = 1
        elif isinstance(result, str):
            tokenType = 2
        result2 = result
        if isinstance(result, monkeyParser.IdentASTContext) and not self.isHas and not self.paramsFun:
            token = self.table.search(result.IDENT().__str__())
            if token is not None:
                result2 = result.IDENT().__str__()
                tokenType = token.getType()
            else:
                print("ERROR: El identificador \"" + result.IDENT().__str__() + "\" no existe")
                return None
        i = 1
        while True:

            if i < len(ctx.elementExpression()):
                if not (ctx.multOperators()[i - 1] is None):
                    operator = self.visit(ctx.multOperators()[i - 1])

                result = self.visit(ctx.elementExpression(i))
                if isinstance(result, monkeyParser.IdentASTContext):
                    token = self.table.search(result.IDENT().__str__())
                    if token is not None:
                        if token.getType() != tokenType:
                            print("ERROR: Los tipos de dato no coinciden")
                            break
                    else:
                        print("ERROR: El identificador \"" + result.IDENT().__str__() + "\" no existe")
                        break
            else:
                break
            i += 1

            if operator == '*':
                operator = 'BINARY_MULTIPLY'
            elif operator == '/':
                operator = 'BINARY_DIVIDE'

            instruction = self.codigo[self.indice - 1].split()
            if not (instruction[1] == "BINARY_MULTIPLY" or instruction == "BINARY_DIVIDE"):
                if not isinstance(result2,int):
                    self.generar(str(self.indice), "LOAD_" + mode1, result2)
            if not isinstance(result,int):
                self.generar(str(self.indice), "LOAD_" + mode1, result.IDENT().__str__())
            self.generar(str(self.indice), operator, None)

        return result

    def visitElementExpressionAST(self, ctx: monkeyParser.ElementExpressionASTContext):
        resultCtx = self.visit(ctx.primitiveExpression())
        if not self.fromFunc:
            if isinstance(resultCtx, monkeyParser.PrimitiveExpressionIdentASTContext):
                ident = self.table.search(resultCtx.IDENT().__str__())
                if ident is None:
                    self.output += "ERROR: El identificador \"" + resultCtx.IDENT().__str__() + "\" no ha sido " \
                                                                                                "declarado\n "

        if not (ctx.elementAccess() is None):
            self.currentIdent = resultCtx
            self.isAcces = True
            lvl = self.table.getCurrentLevel()
            mode1 = ""
            if lvl <= 0:
                mode1 = 'GLOBAL'
            else:
                mode1 = 'FAST'
            self.generar(str(self.indice), "LOAD_"+mode1, resultCtx.IDENT().__str__())
            resultCtx = self.visit(ctx.elementAccess())
            if isinstance(resultCtx, monkeyParser.IdentASTContext):
                self.generar(str(self.indice), "LOAD_INDEX", resultCtx.IDENT().__str__())
            elif isinstance(resultCtx,int):
                self.generar(str(self.indice), "LOAD_INDEX", str(resultCtx))
            else:
                self.generar(str(self.indice), "LOAD_INDEX", resultCtx)

            self.isAcces = False
            self.currentIdent = None
        elif not (ctx.callExpression() is None):
            self.fromCall = True
            self.currentIdent = resultCtx
            token = self.table.search(resultCtx.IDENT().__str__())
            resultCtx = self.visit(ctx.callExpression())
            self.generar(str(self.indice), "LOAD_GLOBAL", self.currentIdent.IDENT().__str__())
            if token is not None:
                if token.getType() == 3:
                    self.generar(str(self.indice), "CALL_FUNCTION", str(token.getLength()))
            self.currentIdent = None
            self.fromCall = False

        if isinstance(resultCtx, monkeyParser.IdentASTContext):
            token = self.table.search(resultCtx.IDENT().__str__())
            if token is not None:
                if token.getType() == 3:
                    self.generar(str(self.indice), "LOAD_GLOBAL", resultCtx.IDENT().__str__())
                    self.generar(str(self.indice), "CALL_FUNCTION", str(token.getLength()))

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
        if not self.isAcces:
            self.generar(str(self.indice), "LOAD_CONST", ctx.INTEGER().__str__())

        return int(ctx.INTEGER().__str__())

    def visitPrimitiveExpressionStringAST(self, ctx: monkeyParser.PrimitiveExpressionStringASTContext):
        if not self.isAcces:
            self.generar(str(self.indice), "LOAD_CONST", ctx.STRING().__str__())
            self.var = '_S'
        return ctx.STRING().__str__()

    def visitPrimitiveExpressionIdentAST(self, ctx: monkeyParser.PrimitiveExpressionIdentASTContext):
        identCtx = self.visit(ctx.ident())
        token = self.table.search(identCtx.IDENT().__str__())
        if token is not None:
            if token.getType() <= 0 or self.insideMain:
                mode = 'GLOBAL'
            else:
                mode = 'FAST'

            if self.fromCall:
                self.generar(str(self.indice), "LOAD_"+mode, identCtx.IDENT().__str__())

        return identCtx

    def visitPrimitiveExpressionTrueAST(self, ctx: monkeyParser.PrimitiveExpressionTrueASTContext):
        self.generar(str(self.indice), "LOAD_CONST", ctx.TRUE().__str__())
        return "true"

    def visitPrimitiveExpressionFalseAST(self, ctx: monkeyParser.PrimitiveExpressionFalseASTContext):
        self.generar(str(self.indice), "LOAD_CONST", ctx.FALSE().__str__())
        return "false"

    def visitPrimitiveExpressionExpressionAST(self, ctx: monkeyParser.PrimitiveExpressionExpressionASTContext):
        self.visit(ctx.expression())
        self.table.closeScope()
        return ctx

    def visitPrimitiveExpressionarrayLiteralast(self, ctx: monkeyParser.PrimitiveExpressionarrayLiteralastContext):
        self.isInt = False
        length = self.visit(ctx.arrayLiteral())
        self.fromList = True
        self.var = "_L"
        return length

    def visitPrimitiveExpressionarrayFunctionsAST(self, ctx: monkeyParser.PrimitiveExpressionarrayFunctionsASTContext):
        result = self.visit(ctx.arrayFunctions())
        self.isFuctionArray = True
        var = self.visit(ctx.expressionList())

        if result == 'push':
            if var > 3:
                print("Error el número de parametros aceptado es de 1 y vienen " + str(var)+" en la función de "+result)
            self.generar(str(self.indice), "LOAD_GLOBAL", result)
            self.generar(str(self.indice), "CALL_FUNCTION", str(1))
        else:
            if not var == 1:
                print("Error el número de parametros aceptado es de 1 y vienen " + str(var)+" en la función de "+result)
            self.generar(str(self.indice), "LOAD_GLOBAL", result)
            self.generar(str(self.indice), "CALL_FUNCTION", str(1))

        self.isFuctionArray = False
        return "arrayFunction"

    def visitPrimitiveExpressionfunctionLiteralAST(self,
                                                   ctx: monkeyParser.PrimitiveExpressionfunctionLiteralASTContext):
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
        index = self.visit(ctx.ifExpression())
        self.codigo[index]=str(index)+" JUMP_ABSOLUTE "+str(self.indice)
        return ctx

    def visitArrayFunctionsLenAST(self, ctx: monkeyParser.ArrayFunctionsLenASTContext):
        #self.generar(str(self.indice), "LEN", ctx.FALSE().__str__())
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
        self.paramsFun = True
        if not self.isMain:
            result = self.visit(ctx.ident()[0])
            if result.IDENT().__str__() != '<missing IDENT>':
                self.generar(str(self.indice), "PUSH_LOCAL_VAR", result.IDENT().__str__())
                self.table.push(result.IDENT().__str__(), self.table.getCurrentLevel(), 0, ctx, False, 0, False)
                i = 1
                while True:
                    if i < len(ctx.ident()):
                        result = self.visit(ctx.ident()[i])
                        self.generar(str(self.indice), "PUSH_LOCAL_VAR", result.IDENT().__str__())
                        self.table.push(result.IDENT().__str__(), self.table.getCurrentLevel(), 0, ctx, False, 0, False)
                    else:
                        break
                    i += 1
        self.paramsFun = False
        return ctx.ident()

    def visitHashLiteralAST(self, ctx: monkeyParser.HashLiteralASTContext):
        self.isHas = True
        self.visit(ctx.hashContent()[0])
        i = 1
        while True:
            if i < len(ctx.hashContent()):
                self.visit(ctx.hashContent()[i])
            else:
                break
            i += 1
        self.isHas=False
        return None

    def visitHashContentAST(self, ctx: monkeyParser.HashContentASTContext):
        ctxResult = self.visit(ctx.expression(0))
        if ctxResult == "true" or ctxResult == "false" or self.var == '_L' or isinstance(ctxResult,monkeyParser.IdentASTContext):
            if self.var == '_L':
                ctxResult = "Lista"
            if isinstance(ctxResult,monkeyParser.IdentASTContext):
                ctxResult = "Ident"
            print("ERROR: El has no puede llevar el valor de : "+ctxResult+" como llave.")
        if not type(ctxResult) is int and not type(ctxResult) is str:
            self.output += "ERROR: Dato no aceptado en hashContent\n"
        self.visit(ctx.expression(1))
        self.var = '_D'
        return None

    def visitExpressionListAST(self, ctx: monkeyParser.ExpressionListASTContext):
        length = 0
        if not (self.currentIdent is None):
            ident = self.table.search(self.currentIdent.IDENT().__str__())
            if not (ident is None):
                if not ident.fromList:
                    if ident.getLength() == len(ctx.expression()):
                        result = self.visit(ctx.expression()[0])
                        i = 1
                        while True:
                            if i < len(ctx.expression()):
                                result = self.visit(ctx.expression()[i])
                            else:
                                break
                            i += 1

                        ident = self.table.search(self.currentIdent.IDENT().__str__())
                    else:
                        print("ERROR: La función \"" + self.currentIdent.IDENT().__str__() + "\" tiene " + \
                                       str(ident.getLength()) + " parámetros en vez de " + str(len(ctx.expression())) + "\n")
                        return
                else:
                    print("ERROR: El identificador \"" + self.currentIdent.IDENT().__str__() + "\" no ha " \
                                                                                                        "sido declarado \n ")
                    return
            else:
                print("ERROR: El identificador \"" + self.currentIdent.IDENT().__str__() + "\" no ha " \
                                                                                                    "sido declarado \n ")
                return

        else:
            length = len(ctx.expression())
            result = self.visit(ctx.expression()[0])
            if self.isFuctionArray:
                self.generar(str(self.indice), "LOAD_FAST", result.IDENT().__str__())
            i = 1
            while True:
                if i < len(ctx.expression()):
                    self.visit(ctx.expression()[i])
                else:
                    break

                if not self.fromListparams == -1:
                    self.fromListName = "function_" + self.fromListName + str(i)
                    # self.table.push(self.fromListName, 7, 0, ctx, True, True, self.fromListparams, -1, True)
                i += 1

        return length

    def visitPrintExpressionAST(self, ctx: monkeyParser.PrintExpressionASTContext):
        result = self.visit(ctx.expression())
        token = self.table.search(result.IDENT().__str__())
        lvl = token.getLevel()
        if lvl <= 0:
            mode1 = 'GLOBAL'
        else:
            mode1 = 'FAST'

        self.generar(str(self.indice), "LOAD_" + mode1, result.IDENT().__str__())
        methodName = "write"
        self.generar(str(self.indice), "LOAD_GLOBAL", methodName)
        self.generar(str(self.indice), "CALL_FUNCTION", str(1))
        return None

    def visitIfExpressionAST(self, ctx: monkeyParser.IfExpressionASTContext):
        self.fromIf = True
        self.visit(ctx.expression())
        tagIndex = self.indice
        self.generar(str(self.indice), "JUMP_IF_FALSE", str(8))

        self.fromIf = False
        self.visit(ctx.statement()[0])
        tagIndex2 = self.indice
        self.generar(str(self.indice), "JUMP_ABSOLUTE", str(self.indice))
        jump = self.codigo[tagIndex].split()
        self.codigo[tagIndex] = jump[0]+" "+jump[1]+" "+str(self.indice)
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
        return tagIndex2

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

    def printEnd(self):
        result = ""
        for s in self.codigo:
            result += s + '\n'
        return result
