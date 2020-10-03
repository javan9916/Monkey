from antlr4 import *
from generated.monkeyLexer import monkeyLexer
from generated.monkeyParser import monkeyParser


def main():
    file_stream = FileStream('test.txt')
    lexer = monkeyLexer(file_stream)
    tokens = CommonTokenStream(lexer)
    parser = monkeyParser(tokens)

    parser.program()
    print("Compilación terminada")


if __name__ == "__main__":
    main()
