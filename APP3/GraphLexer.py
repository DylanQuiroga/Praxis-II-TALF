# Generated from Graph.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,48,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,
        2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,4,6,38,8,6,11,6,12,6,39,1,7,4,7,43,
        8,7,11,7,12,7,44,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,
        8,1,0,3,1,0,65,90,1,0,48,57,3,0,9,10,13,13,32,32,49,0,1,1,0,0,0,
        0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,25,1,0,0,0,5,27,1,0,0,0,7,30,
        1,0,0,0,9,32,1,0,0,0,11,34,1,0,0,0,13,37,1,0,0,0,15,42,1,0,0,0,17,
        18,5,71,0,0,18,19,5,114,0,0,19,20,5,97,0,0,20,21,5,112,0,0,21,22,
        5,104,0,0,22,23,5,32,0,0,23,24,5,123,0,0,24,2,1,0,0,0,25,26,5,125,
        0,0,26,4,1,0,0,0,27,28,5,45,0,0,28,29,5,62,0,0,29,6,1,0,0,0,30,31,
        5,40,0,0,31,8,1,0,0,0,32,33,5,41,0,0,33,10,1,0,0,0,34,35,7,0,0,0,
        35,12,1,0,0,0,36,38,7,1,0,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,
        0,0,0,39,40,1,0,0,0,40,14,1,0,0,0,41,43,7,2,0,0,42,41,1,0,0,0,43,
        44,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,47,6,7,0,
        0,47,16,1,0,0,0,3,0,39,44,1,6,0,0
    ]

class GraphLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    LETTER = 6
    NUMBER = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Graph {'", "'}'", "'->'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "LETTER", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "LETTER", "NUMBER", 
                  "WS" ]

    grammarFileName = "Graph.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


