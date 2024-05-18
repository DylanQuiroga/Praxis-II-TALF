# Generated from Graph.g4 by ANTLR 4.13.1
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
        4,1,8,29,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,5,0,11,8,0,10,0,
        12,0,14,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,
        1,3,0,0,4,0,2,4,6,0,0,25,0,8,1,0,0,0,2,17,1,0,0,0,4,24,1,0,0,0,6,
        26,1,0,0,0,8,12,5,1,0,0,9,11,3,2,1,0,10,9,1,0,0,0,11,14,1,0,0,0,
        12,10,1,0,0,0,12,13,1,0,0,0,13,15,1,0,0,0,14,12,1,0,0,0,15,16,5,
        2,0,0,16,1,1,0,0,0,17,18,3,4,2,0,18,19,5,3,0,0,19,20,3,4,2,0,20,
        21,5,4,0,0,21,22,3,6,3,0,22,23,5,5,0,0,23,3,1,0,0,0,24,25,5,6,0,
        0,25,5,1,0,0,0,26,27,5,7,0,0,27,7,1,0,0,0,1,12
    ]

class GraphParser ( Parser ):

    grammarFileName = "Graph.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Graph {'", "'}'", "'->'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "LETTER", "NUMBER", "WS" ]

    RULE_graph = 0
    RULE_edge = 1
    RULE_node = 2
    RULE_weight = 3

    ruleNames =  [ "graph", "edge", "node", "weight" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    LETTER=6
    NUMBER=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class GraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edge(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.EdgeContext)
            else:
                return self.getTypedRuleContext(GraphParser.EdgeContext,i)


        def getRuleIndex(self):
            return GraphParser.RULE_graph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraph" ):
                listener.enterGraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraph" ):
                listener.exitGraph(self)




    def graph(self):

        localctx = GraphParser.GraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_graph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(GraphParser.T__0)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 9
                self.edge()
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
            self.match(GraphParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphParser.NodeContext)
            else:
                return self.getTypedRuleContext(GraphParser.NodeContext,i)


        def weight(self):
            return self.getTypedRuleContext(GraphParser.WeightContext,0)


        def getRuleIndex(self):
            return GraphParser.RULE_edge

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdge" ):
                listener.enterEdge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdge" ):
                listener.exitEdge(self)




    def edge(self):

        localctx = GraphParser.EdgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_edge)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.node()
            self.state = 18
            self.match(GraphParser.T__2)
            self.state = 19
            self.node()
            self.state = 20
            self.match(GraphParser.T__3)
            self.state = 21
            self.weight()
            self.state = 22
            self.match(GraphParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self):
            return self.getToken(GraphParser.LETTER, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode" ):
                listener.enterNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode" ):
                listener.exitNode(self)




    def node(self):

        localctx = GraphParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(GraphParser.LETTER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WeightContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(GraphParser.NUMBER, 0)

        def getRuleIndex(self):
            return GraphParser.RULE_weight

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWeight" ):
                listener.enterWeight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWeight" ):
                listener.exitWeight(self)




    def weight(self):

        localctx = GraphParser.WeightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_weight)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(GraphParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





