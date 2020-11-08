class SymbolTable:
    currentLevel = 0
    table = []

    def __init__(self):
        self.push("len", 0, 0, 0, True, True)
        self.push("first", 0, 0, 0, True, True)
        self.push("last", 0, 0, 0, True, True)
        self.push("rest", 0, 0, 0, True, True)
        self.push("push", 0, 0, 0, False, False)
        self.push("puts", 0, 0, 0, False, False)
        self.currentLevel = 0

    class Ident:
        def __init__(self, token, type, lvl, decl, isFunc, hasReturn):
            if isFunc:
                self.token = token
                self.type = type
                self.level = lvl
                self.value = 0
                self.declCtx = decl
                self.isFunc = isFunc
                self.hasReturn = hasReturn
            else:
                self.token = token
                self.type = type
                self.level = lvl
                self.value = 0
                self.declCtx = decl
                self.isFunc = isFunc

        def setValue(self, value):
            self.value = value

        def getLevel(self):
            return self.level

    def getCurrentLevel(self):
        return self.currentLevel

    def setCurrentLevel(self, cl):
        self.currentLevel = cl

    def setTable(self, table):
        self.table = table

    def ST(self):
        SymbolTable.setTable([])
        SymbolTable.setCurrentLevel(-1)

    def push(self, id, type, lvl, decl, isFunc, hasReturn):
        #no se puede insertar un elemento repetido en el mismo nivel
        item = SymbolTable.Ident(id, type, lvl, decl, isFunc, hasReturn)
        self.table.append(item)

    def search(self, name):
        #debe buscarse en otro orden... de atrás para adelante
        temp = None
        for id in self.table:
            if (id.token.__str__()== name):
                return id
        return temp

    def openScope(self):
        self.currentLevel += 1

    def closeScope(self):
        self.table = [i for i in self.table if not(i.getLevel() == self.getCurrentLevel())]
        self.currentLevel -= 1

    def print(self):
        print("----- INICIO TABLA ------")
        print("Variables: ")
        for x in range(0, len(self.table)):
            if not self.table[x].isFunc:
                s = self.table[x].token
                print("Nombre: " + s.__str__() + " - " + str(self.table[x].level) + " - " + str(self.table[x].type))

        print("Funciones: ")
        for x in range(0, len(self.table)):
            if self.table[x].isFunc:
                s = self.table[x].token
                print("Nombre: " + s.__str__() + " - " + str(self.table[x].level) + " - " + str(self.table[x].type))

        print("------ FIN TABLA -------")