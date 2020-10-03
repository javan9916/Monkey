# Generated from C:/Users/Javier/PycharmProjects/Monkey\monkeyParser.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\3\7\3\32\n\3\f")
        buf.write("\3\16\3\35\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4&\n\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4=\n\4\3\5\3\5\3\5\7\5")
        buf.write("B\n\5\f\5\16\5E\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6O\n\6\3\7\3\7\3\b\3\b\3\b\3\b\7\bW\n\b\f\b\16\bZ\13")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\5\tb\n\t\3\n\3\n\3\n\2\2\13")
        buf.write("\2\4\6\b\n\f\16\20\22\2\3\3\2\t\f\2g\2\24\3\2\2\2\4\26")
        buf.write("\3\2\2\2\6<\3\2\2\2\b>\3\2\2\2\nN\3\2\2\2\fP\3\2\2\2\16")
        buf.write("R\3\2\2\2\20a\3\2\2\2\22c\3\2\2\2\24\25\5\6\4\2\25\3\3")
        buf.write("\2\2\2\26\33\5\6\4\2\27\30\7\3\2\2\30\32\5\6\4\2\31\27")
        buf.write("\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34")
        buf.write("\5\3\2\2\2\35\33\3\2\2\2\36%\7\30\2\2\37 \7\5\2\2 &\5")
        buf.write("\16\b\2!\"\7\6\2\2\"#\5\16\b\2#$\7\7\2\2$&\3\2\2\2%\37")
        buf.write("\3\2\2\2%!\3\2\2\2&=\3\2\2\2\'(\7\r\2\2()\5\16\b\2)*\7")
        buf.write("\16\2\2*+\5\6\4\2+,\7\17\2\2,-\5\6\4\2-=\3\2\2\2./\7\20")
        buf.write("\2\2/\60\5\16\b\2\60\61\7\21\2\2\61\62\5\6\4\2\62=\3\2")
        buf.write("\2\2\63\64\7\22\2\2\64\65\5\b\5\2\65\66\7\23\2\2\66\67")
        buf.write("\5\6\4\2\67=\3\2\2\289\7\24\2\29:\5\4\3\2:;\7\25\2\2;")
        buf.write("=\3\2\2\2<\36\3\2\2\2<\'\3\2\2\2<.\3\2\2\2<\63\3\2\2\2")
        buf.write("<8\3\2\2\2=\7\3\2\2\2>C\5\n\6\2?@\7\3\2\2@B\5\n\6\2A?")
        buf.write("\3\2\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\t\3\2\2\2EC\3")
        buf.write("\2\2\2FG\7\26\2\2GH\7\30\2\2HI\7\b\2\2IO\5\16\b\2JK\7")
        buf.write("\27\2\2KL\7\30\2\2LM\7\4\2\2MO\5\f\7\2NF\3\2\2\2NJ\3\2")
        buf.write("\2\2O\13\3\2\2\2PQ\7\30\2\2Q\r\3\2\2\2RX\5\20\t\2ST\5")
        buf.write("\22\n\2TU\5\20\t\2UW\3\2\2\2VS\3\2\2\2WZ\3\2\2\2XV\3\2")
        buf.write("\2\2XY\3\2\2\2Y\17\3\2\2\2ZX\3\2\2\2[b\7\31\2\2\\b\7\30")
        buf.write("\2\2]^\7\6\2\2^_\5\16\b\2_`\7\7\2\2`b\3\2\2\2a[\3\2\2")
        buf.write("\2a\\\3\2\2\2a]\3\2\2\2b\21\3\2\2\2cd\t\2\2\2d\23\3\2")
        buf.write("\2\2\t\33%<CNXa")
        return buf.getvalue()


class monkeyParser ( Parser ):

    grammarFileName = "monkeyParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "':'", "':='", "'('", "')'", "'~'", 
                     "'+'", "'-'", "'*'", "'/'", "'if'", "'then'", "'else'", 
                     "'while'", "'do'", "'let'", "'in'", "'begin'", "'end'", 
                     "'const'", "'var'" ]

    symbolicNames = [ "<INVALID>", "PCOMA", "DOSPUNTOS", "ASSIGN", "PIZQ", 
                      "PDER", "VIR", "SUMA", "RESTA", "MULT", "DIV", "IF", 
                      "THEN", "ELSE", "WHILE", "DO", "LET", "IN", "BEGIN", 
                      "END", "CONST", "VAR", "IDENT", "LITERAL", "WS" ]

    RULE_program = 0
    RULE_command = 1
    RULE_singleCommand = 2
    RULE_declaration = 3
    RULE_singleDeclaration = 4
    RULE_typeDenoter = 5
    RULE_expression = 6
    RULE_primaryExpression = 7
    RULE_operator = 8

    ruleNames =  [ "program", "command", "singleCommand", "declaration", 
                   "singleDeclaration", "typeDenoter", "expression", "primaryExpression", 
                   "operator" ]

    EOF = Token.EOF
    PCOMA=1
    DOSPUNTOS=2
    ASSIGN=3
    PIZQ=4
    PDER=5
    VIR=6
    SUMA=7
    RESTA=8
    MULT=9
    DIV=10
    IF=11
    THEN=12
    ELSE=13
    WHILE=14
    DO=15
    LET=16
    IN=17
    BEGIN=18
    END=19
    CONST=20
    VAR=21
    IDENT=22
    LITERAL=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleCommand(self):
            return self.getTypedRuleContext(monkeyParser.SingleCommandContext,0)


        def getRuleIndex(self):
            return monkeyParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = monkeyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.singleCommand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(monkeyParser.SingleCommandContext)
            else:
                return self.getTypedRuleContext(monkeyParser.SingleCommandContext,i)


        def PCOMA(self, i:int=None):
            if i is None:
                return self.getTokens(monkeyParser.PCOMA)
            else:
                return self.getToken(monkeyParser.PCOMA, i)

        def getRuleIndex(self):
            return monkeyParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = monkeyParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.singleCommand()
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==monkeyParser.PCOMA:
                self.state = 21
                self.match(monkeyParser.PCOMA)
                self.state = 22
                self.singleCommand()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleCommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(monkeyParser.IDENT, 0)

        def ASSIGN(self):
            return self.getToken(monkeyParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(monkeyParser.ExpressionContext,0)


        def PIZQ(self):
            return self.getToken(monkeyParser.PIZQ, 0)

        def PDER(self):
            return self.getToken(monkeyParser.PDER, 0)

        def IF(self):
            return self.getToken(monkeyParser.IF, 0)

        def THEN(self):
            return self.getToken(monkeyParser.THEN, 0)

        def singleCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(monkeyParser.SingleCommandContext)
            else:
                return self.getTypedRuleContext(monkeyParser.SingleCommandContext,i)


        def ELSE(self):
            return self.getToken(monkeyParser.ELSE, 0)

        def WHILE(self):
            return self.getToken(monkeyParser.WHILE, 0)

        def DO(self):
            return self.getToken(monkeyParser.DO, 0)

        def LET(self):
            return self.getToken(monkeyParser.LET, 0)

        def declaration(self):
            return self.getTypedRuleContext(monkeyParser.DeclarationContext,0)


        def IN(self):
            return self.getToken(monkeyParser.IN, 0)

        def BEGIN(self):
            return self.getToken(monkeyParser.BEGIN, 0)

        def command(self):
            return self.getTypedRuleContext(monkeyParser.CommandContext,0)


        def END(self):
            return self.getToken(monkeyParser.END, 0)

        def getRuleIndex(self):
            return monkeyParser.RULE_singleCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleCommand" ):
                listener.enterSingleCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleCommand" ):
                listener.exitSingleCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleCommand" ):
                return visitor.visitSingleCommand(self)
            else:
                return visitor.visitChildren(self)




    def singleCommand(self):

        localctx = monkeyParser.SingleCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_singleCommand)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [monkeyParser.IDENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(monkeyParser.IDENT)
                self.state = 35
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [monkeyParser.ASSIGN]:
                    self.state = 29
                    self.match(monkeyParser.ASSIGN)
                    self.state = 30
                    self.expression()
                    pass
                elif token in [monkeyParser.PIZQ]:
                    self.state = 31
                    self.match(monkeyParser.PIZQ)
                    self.state = 32
                    self.expression()
                    self.state = 33
                    self.match(monkeyParser.PDER)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [monkeyParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(monkeyParser.IF)
                self.state = 38
                self.expression()
                self.state = 39
                self.match(monkeyParser.THEN)
                self.state = 40
                self.singleCommand()
                self.state = 41
                self.match(monkeyParser.ELSE)
                self.state = 42
                self.singleCommand()
                pass
            elif token in [monkeyParser.WHILE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.match(monkeyParser.WHILE)
                self.state = 45
                self.expression()
                self.state = 46
                self.match(monkeyParser.DO)
                self.state = 47
                self.singleCommand()
                pass
            elif token in [monkeyParser.LET]:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.match(monkeyParser.LET)
                self.state = 50
                self.declaration()
                self.state = 51
                self.match(monkeyParser.IN)
                self.state = 52
                self.singleCommand()
                pass
            elif token in [monkeyParser.BEGIN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.match(monkeyParser.BEGIN)
                self.state = 55
                self.command()
                self.state = 56
                self.match(monkeyParser.END)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(monkeyParser.SingleDeclarationContext)
            else:
                return self.getTypedRuleContext(monkeyParser.SingleDeclarationContext,i)


        def PCOMA(self, i:int=None):
            if i is None:
                return self.getTokens(monkeyParser.PCOMA)
            else:
                return self.getToken(monkeyParser.PCOMA, i)

        def getRuleIndex(self):
            return monkeyParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = monkeyParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.singleDeclaration()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==monkeyParser.PCOMA:
                self.state = 61
                self.match(monkeyParser.PCOMA)
                self.state = 62
                self.singleDeclaration()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(monkeyParser.CONST, 0)

        def IDENT(self):
            return self.getToken(monkeyParser.IDENT, 0)

        def VIR(self):
            return self.getToken(monkeyParser.VIR, 0)

        def expression(self):
            return self.getTypedRuleContext(monkeyParser.ExpressionContext,0)


        def VAR(self):
            return self.getToken(monkeyParser.VAR, 0)

        def DOSPUNTOS(self):
            return self.getToken(monkeyParser.DOSPUNTOS, 0)

        def typeDenoter(self):
            return self.getTypedRuleContext(monkeyParser.TypeDenoterContext,0)


        def getRuleIndex(self):
            return monkeyParser.RULE_singleDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleDeclaration" ):
                listener.enterSingleDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleDeclaration" ):
                listener.exitSingleDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleDeclaration" ):
                return visitor.visitSingleDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def singleDeclaration(self):

        localctx = monkeyParser.SingleDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_singleDeclaration)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [monkeyParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(monkeyParser.CONST)
                self.state = 69
                self.match(monkeyParser.IDENT)
                self.state = 70
                self.match(monkeyParser.VIR)
                self.state = 71
                self.expression()
                pass
            elif token in [monkeyParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(monkeyParser.VAR)
                self.state = 73
                self.match(monkeyParser.IDENT)
                self.state = 74
                self.match(monkeyParser.DOSPUNTOS)
                self.state = 75
                self.typeDenoter()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDenoterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(monkeyParser.IDENT, 0)

        def getRuleIndex(self):
            return monkeyParser.RULE_typeDenoter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDenoter" ):
                listener.enterTypeDenoter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDenoter" ):
                listener.exitTypeDenoter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDenoter" ):
                return visitor.visitTypeDenoter(self)
            else:
                return visitor.visitChildren(self)




    def typeDenoter(self):

        localctx = monkeyParser.TypeDenoterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typeDenoter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(monkeyParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(monkeyParser.PrimaryExpressionContext)
            else:
                return self.getTypedRuleContext(monkeyParser.PrimaryExpressionContext,i)


        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(monkeyParser.OperatorContext)
            else:
                return self.getTypedRuleContext(monkeyParser.OperatorContext,i)


        def getRuleIndex(self):
            return monkeyParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = monkeyParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.primaryExpression()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << monkeyParser.SUMA) | (1 << monkeyParser.RESTA) | (1 << monkeyParser.MULT) | (1 << monkeyParser.DIV))) != 0):
                self.state = 81
                self.operator()
                self.state = 82
                self.primaryExpression()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL(self):
            return self.getToken(monkeyParser.LITERAL, 0)

        def IDENT(self):
            return self.getToken(monkeyParser.IDENT, 0)

        def PIZQ(self):
            return self.getToken(monkeyParser.PIZQ, 0)

        def expression(self):
            return self.getTypedRuleContext(monkeyParser.ExpressionContext,0)


        def PDER(self):
            return self.getToken(monkeyParser.PDER, 0)

        def getRuleIndex(self):
            return monkeyParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = monkeyParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_primaryExpression)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [monkeyParser.LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(monkeyParser.LITERAL)
                pass
            elif token in [monkeyParser.IDENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(monkeyParser.IDENT)
                pass
            elif token in [monkeyParser.PIZQ]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.match(monkeyParser.PIZQ)
                self.state = 92
                self.expression()
                self.state = 93
                self.match(monkeyParser.PDER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(monkeyParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(monkeyParser.RESTA, 0)

        def MULT(self):
            return self.getToken(monkeyParser.MULT, 0)

        def DIV(self):
            return self.getToken(monkeyParser.DIV, 0)

        def getRuleIndex(self):
            return monkeyParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = monkeyParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << monkeyParser.SUMA) | (1 << monkeyParser.RESTA) | (1 << monkeyParser.MULT) | (1 << monkeyParser.DIV))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





