# Generated from arithmetic.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        2,1,2,1,2,1,2,1,2,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,50,8,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,5,2,61,8,2,10,2,12,2,64,9,2,1,3,1,3,3,3,68,8,3,1,4,1,
        4,1,5,1,5,1,6,1,6,1,6,0,1,4,7,0,2,4,6,8,10,12,0,3,1,0,5,6,1,0,7,
        8,1,0,9,11,78,0,18,1,0,0,0,2,23,1,0,0,0,4,49,1,0,0,0,6,67,1,0,0,
        0,8,69,1,0,0,0,10,71,1,0,0,0,12,73,1,0,0,0,14,17,3,4,2,0,15,17,3,
        2,1,0,16,14,1,0,0,0,16,15,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,
        19,1,0,0,0,19,21,1,0,0,0,20,18,1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,
        0,23,24,3,4,2,0,24,25,3,12,6,0,25,26,3,4,2,0,26,3,1,0,0,0,27,28,
        6,2,-1,0,28,29,5,3,0,0,29,30,3,4,2,0,30,31,5,4,0,0,31,50,1,0,0,0,
        32,34,7,0,0,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,
        0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,50,3,6,3,0,39,40,5,14,0,0,40,
        41,5,3,0,0,41,42,3,4,2,0,42,43,5,4,0,0,43,50,1,0,0,0,44,45,5,15,
        0,0,45,46,5,3,0,0,46,47,3,4,2,0,47,48,5,4,0,0,48,50,1,0,0,0,49,27,
        1,0,0,0,49,35,1,0,0,0,49,39,1,0,0,0,49,44,1,0,0,0,50,62,1,0,0,0,
        51,52,10,7,0,0,52,53,5,13,0,0,53,61,3,4,2,8,54,55,10,6,0,0,55,56,
        7,1,0,0,56,61,3,4,2,7,57,58,10,5,0,0,58,59,7,0,0,0,59,61,3,4,2,6,
        60,51,1,0,0,0,60,54,1,0,0,0,60,57,1,0,0,0,61,64,1,0,0,0,62,60,1,
        0,0,0,62,63,1,0,0,0,63,5,1,0,0,0,64,62,1,0,0,0,65,68,3,8,4,0,66,
        68,3,10,5,0,67,65,1,0,0,0,67,66,1,0,0,0,68,7,1,0,0,0,69,70,5,2,0,
        0,70,9,1,0,0,0,71,72,5,1,0,0,72,11,1,0,0,0,73,74,7,2,0,0,74,13,1,
        0,0,0,7,16,18,35,49,60,62,67
    ]

class arithmeticParser ( Parser ):

    grammarFileName = "arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'='", "'.'", 
                     "'^'", "'exp'", "'log'" ]

    symbolicNames = [ "<INVALID>", "VARIABLE", "SCIENTIFIC_NUMBER", "LPAREN", 
                      "RPAREN", "PLUS", "MINUS", "TIMES", "DIV", "GT", "LT", 
                      "EQ", "POINT", "POW", "EXP", "LOG", "WS" ]

    RULE_file_ = 0
    RULE_equation = 1
    RULE_expression = 2
    RULE_atom = 3
    RULE_scientific = 4
    RULE_variable = 5
    RULE_relop = 6

    ruleNames =  [ "file_", "equation", "expression", "atom", "scientific", 
                   "variable", "relop" ]

    EOF = Token.EOF
    VARIABLE=1
    SCIENTIFIC_NUMBER=2
    LPAREN=3
    RPAREN=4
    PLUS=5
    MINUS=6
    TIMES=7
    DIV=8
    GT=9
    LT=10
    EQ=11
    POINT=12
    POW=13
    EXP=14
    LOG=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class File_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(arithmeticParser.EOF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(arithmeticParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(arithmeticParser.ExpressionContext,i)


        def equation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(arithmeticParser.EquationContext)
            else:
                return self.getTypedRuleContext(arithmeticParser.EquationContext,i)


        def getRuleIndex(self):
            return arithmeticParser.RULE_file_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_" ):
                listener.enterFile_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_" ):
                listener.exitFile_(self)




    def file_(self):

        localctx = arithmeticParser.File_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 49262) != 0):
                self.state = 16
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 14
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 15
                    self.equation()
                    pass


                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
            self.match(arithmeticParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EquationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(arithmeticParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(arithmeticParser.ExpressionContext,i)


        def relop(self):
            return self.getTypedRuleContext(arithmeticParser.RelopContext,0)


        def getRuleIndex(self):
            return arithmeticParser.RULE_equation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquation" ):
                listener.enterEquation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquation" ):
                listener.exitEquation(self)




    def equation(self):

        localctx = arithmeticParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_equation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.expression(0)
            self.state = 24
            self.relop()
            self.state = 25
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(arithmeticParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(arithmeticParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(arithmeticParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(arithmeticParser.RPAREN, 0)

        def atom(self):
            return self.getTypedRuleContext(arithmeticParser.AtomContext,0)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(arithmeticParser.PLUS)
            else:
                return self.getToken(arithmeticParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(arithmeticParser.MINUS)
            else:
                return self.getToken(arithmeticParser.MINUS, i)

        def EXP(self):
            return self.getToken(arithmeticParser.EXP, 0)

        def LOG(self):
            return self.getToken(arithmeticParser.LOG, 0)

        def POW(self):
            return self.getToken(arithmeticParser.POW, 0)

        def TIMES(self):
            return self.getToken(arithmeticParser.TIMES, 0)

        def DIV(self):
            return self.getToken(arithmeticParser.DIV, 0)

        def getRuleIndex(self):
            return arithmeticParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = arithmeticParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 28
                self.match(arithmeticParser.LPAREN)
                self.state = 29
                self.expression(0)
                self.state = 30
                self.match(arithmeticParser.RPAREN)
                pass
            elif token in [1, 2, 5, 6]:
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5 or _la==6:
                    self.state = 32
                    _la = self._input.LA(1)
                    if not(_la==5 or _la==6):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 38
                self.atom()
                pass
            elif token in [14]:
                self.state = 39
                self.match(arithmeticParser.EXP)
                self.state = 40
                self.match(arithmeticParser.LPAREN)
                self.state = 41
                self.expression(0)
                self.state = 42
                self.match(arithmeticParser.RPAREN)
                pass
            elif token in [15]:
                self.state = 44
                self.match(arithmeticParser.LOG)
                self.state = 45
                self.match(arithmeticParser.LPAREN)
                self.state = 46
                self.expression(0)
                self.state = 47
                self.match(arithmeticParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 60
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = arithmeticParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 51
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 52
                        self.match(arithmeticParser.POW)
                        self.state = 53
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = arithmeticParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 54
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 55
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = arithmeticParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 57
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 58
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        self.expression(6)
                        pass

             
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scientific(self):
            return self.getTypedRuleContext(arithmeticParser.ScientificContext,0)


        def variable(self):
            return self.getTypedRuleContext(arithmeticParser.VariableContext,0)


        def getRuleIndex(self):
            return arithmeticParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = arithmeticParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.scientific()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.variable()
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


    class ScientificContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCIENTIFIC_NUMBER(self):
            return self.getToken(arithmeticParser.SCIENTIFIC_NUMBER, 0)

        def getRuleIndex(self):
            return arithmeticParser.RULE_scientific

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScientific" ):
                listener.enterScientific(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScientific" ):
                listener.exitScientific(self)




    def scientific(self):

        localctx = arithmeticParser.ScientificContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_scientific)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(arithmeticParser.SCIENTIFIC_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(arithmeticParser.VARIABLE, 0)

        def getRuleIndex(self):
            return arithmeticParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = arithmeticParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(arithmeticParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(arithmeticParser.EQ, 0)

        def GT(self):
            return self.getToken(arithmeticParser.GT, 0)

        def LT(self):
            return self.getToken(arithmeticParser.LT, 0)

        def getRuleIndex(self):
            return arithmeticParser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)




    def relop(self):

        localctx = arithmeticParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




