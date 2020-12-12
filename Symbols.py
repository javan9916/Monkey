class Symbols:
    table = []
    currentLevel = 0

    def __init__(self):
        self.table = []
        self.currentLevel = -1

    class Ident:
        def __init__(self, token, level, type, decl, isFunc, length, fromList):
            self.token = token
            self.type = type
            self.level = level
            self.declCtx = decl
            self.isFunc = isFunc
            self.length = length
            self.fromList = fromList

        def getLevel(self):
            return self.level

        def getType(self):
            return self.type

        def getLength(self):
            return self.length

        def getFromList(self):
            return self.fromList


    def getCurrentLevel(self):
        return self.currentLevel

    def push(self, id, level, type, decl, isFunc, length, fromList):
        ident = Symbols.Ident(id, level, type, decl, isFunc, length, fromList)
        self.table.append(ident)

    def search(self, name):
        for item in self.table:
            if item.token.__str__() == name:
                return item
        return None

    def openScope(self):
        self.currentLevel += 1

    def closeScope(self):
        self.currentLevel -= 1

    def printTable(self):
        print("----- INICIO TABLA ------")
        for item in self.table:
            if item.getType() == 3:
                print("Nombre: " + item.token + " - Level: " + str(item.level) + " - params: " + str(item.length))
            else:
                print("Nombre: " + item.token + " - Level: " + str(item.level) + " - Type: " + str(item.type))

        print("----- FIN TABLA ------")
