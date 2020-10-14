from antlr4 import *

from CustomErrorListener import CustomErrorListener
from CustomVisitor import CustomVisitor
from generated.monkeyLexer import monkeyLexer
from generated.monkeyParser import monkeyParser


def main():
    file_stream = FileStream('test.txt')
    lexer = monkeyLexer(file_stream)
    tokens = CommonTokenStream(lexer)
    parser = monkeyParser(tokens)

    errorListener = CustomErrorListener()

    lexer.removeErrorListeners()
    lexer.addErrorListener(errorListener)

    parser.removeErrorListeners()
    parser.addErrorListener(errorListener)

    tree = parser.program()

    if not(errorListener.HasErrors()):
        print("Compilación Exitosa!!\n")
        visitor = CustomVisitor()
        visitor.visit(tree)
    else:
        print("Compilación Fallida!!\n")
        print(errorListener.toString())

    print("Compilación terminada")


if __name__ == "__main__":
    main()
