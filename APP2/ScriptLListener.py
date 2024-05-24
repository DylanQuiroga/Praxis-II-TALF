# Generated from ScriptL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ScriptLParser import ScriptLParser
else:
    from ScriptLParser import ScriptLParser

# This class defines a complete listener for a parse tree produced by ScriptLParser.
class ScriptLListener(ParseTreeListener):

    # Enter a parse tree produced by ScriptLParser#program.
    def enterProgram(self, ctx:ScriptLParser.ProgramContext):
        pass

    # Exit a parse tree produced by ScriptLParser#program.
    def exitProgram(self, ctx:ScriptLParser.ProgramContext):
        pass


    # Enter a parse tree produced by ScriptLParser#statement.
    def enterStatement(self, ctx:ScriptLParser.StatementContext):
        pass

    # Exit a parse tree produced by ScriptLParser#statement.
    def exitStatement(self, ctx:ScriptLParser.StatementContext):
        pass


    # Enter a parse tree produced by ScriptLParser#getStmt.
    def enterGetStmt(self, ctx:ScriptLParser.GetStmtContext):
        pass

    # Exit a parse tree produced by ScriptLParser#getStmt.
    def exitGetStmt(self, ctx:ScriptLParser.GetStmtContext):
        pass


    # Enter a parse tree produced by ScriptLParser#assignStmt.
    def enterAssignStmt(self, ctx:ScriptLParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by ScriptLParser#assignStmt.
    def exitAssignStmt(self, ctx:ScriptLParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by ScriptLParser#putStmt.
    def enterPutStmt(self, ctx:ScriptLParser.PutStmtContext):
        pass

    # Exit a parse tree produced by ScriptLParser#putStmt.
    def exitPutStmt(self, ctx:ScriptLParser.PutStmtContext):
        pass


    # Enter a parse tree produced by ScriptLParser#whileStmt.
    def enterWhileStmt(self, ctx:ScriptLParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by ScriptLParser#whileStmt.
    def exitWhileStmt(self, ctx:ScriptLParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by ScriptLParser#ifStmt.
    def enterIfStmt(self, ctx:ScriptLParser.IfStmtContext):
        pass

    # Exit a parse tree produced by ScriptLParser#ifStmt.
    def exitIfStmt(self, ctx:ScriptLParser.IfStmtContext):
        pass


    # Enter a parse tree produced by ScriptLParser#ifBlock.
    def enterIfBlock(self, ctx:ScriptLParser.IfBlockContext):
        pass

    # Exit a parse tree produced by ScriptLParser#ifBlock.
    def exitIfBlock(self, ctx:ScriptLParser.IfBlockContext):
        pass


    # Enter a parse tree produced by ScriptLParser#elseBlock.
    def enterElseBlock(self, ctx:ScriptLParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by ScriptLParser#elseBlock.
    def exitElseBlock(self, ctx:ScriptLParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by ScriptLParser#expr.
    def enterExpr(self, ctx:ScriptLParser.ExprContext):
        pass

    # Exit a parse tree produced by ScriptLParser#expr.
    def exitExpr(self, ctx:ScriptLParser.ExprContext):
        pass


    # Enter a parse tree produced by ScriptLParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:ScriptLParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by ScriptLParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:ScriptLParser.ComparisonOperatorContext):
        pass



del ScriptLParser