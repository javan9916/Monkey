class SymbolTable:
    currentLevel = 0
    table = []

    def __init__(self):
        self.table = []
        self.currentLevel = 0

    class Ident:
        def __init__(self, token, type, lvl, decl, isFunc, hasReturn, params, length, fromList):
            if isFunc:
                self.token = token
                self.type = type
                self.level = lvl
                self.value = 0
                self.declCtx = decl
                self.isFunc = isFunc
                self.hasReturn = hasReturn
                self.params = params
                self.fromList = fromList
            else:
                self.token = token
                self.type = type
                self.level = lvl
                self.value = 0
                self.declCtx = decl
                self.isFunc = isFunc
                self.length = length

        def setValue(self, value):
            self.value = value

        def getLevel(self):
            return self.level

    def pushInternals(self):
        self.push("len", 0, 0, 0, True, True, 1, None, False)
        self.push("first", 0, 0, 0, True, True, 1, None, False)
        self.push("last", 0, 0, 0, True, True, 1, None, False)
        self.push("rest", 0, 0, 0, True, True, 1, None, False)
        self.push("push", 0, 0, 0, True, False, 1, None, False)
        self.push("puts", 0, 0, 0, True, False, 1, None, False)

    def getCurrentLevel(self):
        return self.currentLevel

    def setCurrentLevel(self, cl):
        self.currentLevel = cl

    def setTable(self, table):
        self.table = table

    def ST(self):
        SymbolTable.setTable([])
        SymbolTable.setCurrentLevel(-1)

    def push(self, id, type, lvl, decl, isFunc, hasReturn, params, length, fromList):
        # no se puede insertar un elemento repetido en el mismo nivel
        item = SymbolTable.Ident(id, type, lvl, decl, isFunc, hasReturn, params, length, fromList)
        self.table.append(item)

    def search(self, name):
        # debe buscarse en otro orden... de atrás para adelante
        temp = None
        for id in self.table:
            if (id.token.__str__() == name):
                return id
        return temp

    def openScope(self):
        self.currentLevel += 1

    def closeScope(self):
        self.table = [i for i in self.table if not (i.getLevel() == self.getCurrentLevel())]
        self.currentLevel -= 1

    def typeToString(self, item):
        if item.type == 0:
            return "internal function"
        elif item.type == 1:
            return "int"
        elif item.type == 2:
            return "string"
        elif item.type == 3:
            return "boolean"
        elif item.type == 4:
            return "array"
        elif item.type == 5:
            return "hash"
        elif item.type == 6:
            return "function"
        elif item.type == 7:
            return "array function"
        else:
            return "NA"

    def getOutput(self):
        output = ""
        output += "-------- INICIO TABLA --------\n"
        output += "Variables: \n"
        for x in range(0, len(self.table)):
            item = self.table[x]
            if not item.isFunc:
                if item.length is None:
                    output += "Nombre: " + item.token.__str__() + " - Nivel: " + str(
                        item.level) + " - Tipo: " + self.typeToString(item) + "\n"
                else:
                    output += "Nombre: " + item.token.__str__() + " - Nivel: " + str(
                        item.level) + " - Tipo: " + self.typeToString(item) + " - " \
                              + "Tamaño: " + str(item.length) + "\n"

        output += "\nFunciones: \n"
        for x in range(0, len(self.table)):
            item = self.table[x]
            if item.isFunc:
                output += "Nombre: " + item.token.__str__() + " - Nivel: " + str(
                    item.level) + " - Tipo: " + self.typeToString(item) + \
                          " - Número parametros: " + str(item.params) + "\n"

        output += "-------- FIN TABLA --------"
        return output
