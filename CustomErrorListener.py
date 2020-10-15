from antlr4.error.ErrorListener import ErrorListener
from generated.monkeyParser import monkeyParser
from generated.monkeyLexer import monkeyLexer


class CustomErrorListener(ErrorListener):
    errorMsgs = []

    def __init__(self):
        self.errorMsgs = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if isinstance(recognizer, monkeyParser):
            self.errorMsgs.append("PARSER ERROR - line " + str(line) + ":" + str(column) + " " + msg)
        elif isinstance(recognizer, monkeyLexer):
            self.errorMsgs.append("LEXER ERROR - line " + str(line) + ":" + str(column) + " " + msg)
        else:
            self.errorMsgs.append("Other Error - line " + str(line) + ":" + str(column) + " " + msg)

    def HasErrors(self):
        return len(self.errorMsgs) > 0

    def toString(self):
        errors = ""
        if not (self.HasErrors()):
            return "0 Errors"
        for e in self.errorMsgs:
            errors += str(e)

        return errors
