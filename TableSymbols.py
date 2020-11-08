from antlr4 import *


class TablaSimbolos:
    nivelActual = 0
    tabla = []

    #def __init__(self):
    #    self.nivelActual = 0
     #   self.tabla = []

    def getNiveActual(self):
        return self.nivelActual

    def setNiveActual(self, nA):
        self.nivelActual =nA

    def setTabla(self, nA):
        self.tabla =nA

    class Ident:

        def __init__(self):
            self.tok = None
            self.type = 0
            self.nivel = 0
            self.valor = 0
            self.declCtx = None

        def Ident(self, t, tp, decl):
            self.tok = t;
            self.type = tp;
            self.nivel = TablaSimbolos.getNiveActual();
            self.valor = 0;
            self.declCtx = decl;

        def setValue(self, v):
            self.valor = v
        def getNivel(self):
            return self.nivel

    def TablaSimbolos(self):

        TablaSimbolos.setTabla([])
        TablaSimbolos.setNiveActual(-1)


    def insertar(self, id, tipo, decl):
        #no se puede insertar un elemento repetido en el mismo nivel
        i = TablaSimbolos.Ident(id,tipo,decl);
        self.tabla.add(i);

    def buscar(self, nombre):
        #debe buscarse en otro orden... de atrás para adelante
        temp=None;
        for id in self.tabla:
            if (id.tok.getText() == nombre):
                temp = id;
        return temp;


    def openScope(self):
        self.nivelActual+=1;


    def closeScope(self):
        self.tabla = [i for i in self.tabla if self.Ident.getNivel() == self.nivelActual]
        self.nivelActual-=1;


    def imprimir(self):
        print("----- INICIO TABLA ------")
        for x in range(0, len(self.tabla)):
            s = self.tabla[x].tok
            print("Nombre: " + s.getText() + " - " + self.tabla[x].nivel + " - " + self.tabla[x].type)
        print("----- FIN TABLA ------")