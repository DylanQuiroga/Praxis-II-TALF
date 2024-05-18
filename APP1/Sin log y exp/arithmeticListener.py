# Generated from arithmetic.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .arithmeticParser import arithmeticParser
else:
    from arithmeticParser import arithmeticParser

# This class defines a complete listener for a parse tree produced by arithmeticParser.
class arithmeticListener(ParseTreeListener):

    # Enter a parse tree produced by arithmeticParser#file_.
    def enterFile_(self, ctx:arithmeticParser.File_Context):
        pass

    # Exit a parse tree produced by arithmeticParser#file_.
    def exitFile_(self, ctx:arithmeticParser.File_Context):
        pass


    # Enter a parse tree produced by arithmeticParser#equation.
    def enterEquation(self, ctx:arithmeticParser.EquationContext):
        pass

    # Exit a parse tree produced by arithmeticParser#equation.
    def exitEquation(self, ctx:arithmeticParser.EquationContext):
        pass


    # Enter a parse tree produced by arithmeticParser#expression.
    def enterExpression(self, ctx:arithmeticParser.ExpressionContext):
        pass

    # Exit a parse tree produced by arithmeticParser#expression.
    def exitExpression(self, ctx:arithmeticParser.ExpressionContext):
        pass


    # Enter a parse tree produced by arithmeticParser#atom.
    def enterAtom(self, ctx:arithmeticParser.AtomContext):
        pass

    # Exit a parse tree produced by arithmeticParser#atom.
    def exitAtom(self, ctx:arithmeticParser.AtomContext):
        pass


    # Enter a parse tree produced by arithmeticParser#scientific.
    def enterScientific(self, ctx:arithmeticParser.ScientificContext):
        pass

    # Exit a parse tree produced by arithmeticParser#scientific.
    def exitScientific(self, ctx:arithmeticParser.ScientificContext):
        pass


    # Enter a parse tree produced by arithmeticParser#variable.
    def enterVariable(self, ctx:arithmeticParser.VariableContext):
        pass

    # Exit a parse tree produced by arithmeticParser#variable.
    def exitVariable(self, ctx:arithmeticParser.VariableContext):
        pass


    # Enter a parse tree produced by arithmeticParser#relop.
    def enterRelop(self, ctx:arithmeticParser.RelopContext):
        pass

    # Exit a parse tree produced by arithmeticParser#relop.
    def exitRelop(self, ctx:arithmeticParser.RelopContext):
        pass



del arithmeticParser