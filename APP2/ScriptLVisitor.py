# Generated from ScriptL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ScriptLParser import ScriptLParser
else:
    from ScriptLParser import ScriptLParser

# This class defines a complete generic visitor for a parse tree produced by ScriptLParser.

class ScriptLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ScriptLParser#program.
    def visitProgram(self, ctx:ScriptLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptLParser#statement.
    def visitStatement(self, ctx:ScriptLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptLParser#getStmt.
    def visitGetStmt(self, ctx:ScriptLParser.GetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptLParser#assignStmt.
    def visitAssignStmt(self, ctx:ScriptLParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptLParser#putStmt.
    def visitPutStmt(self, ctx:ScriptLParser.PutStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptLParser#whileStmt.
    def visitWhileStmt(self, ctx:ScriptLParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptLParser#ifStmt.
    def visitIfStmt(self, ctx:ScriptLParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptLParser#ifBlock.
    def visitIfBlock(self, ctx:ScriptLParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptLParser#elseBlock.
    def visitElseBlock(self, ctx:ScriptLParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptLParser#expr.
    def visitExpr(self, ctx:ScriptLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptLParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:ScriptLParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)



del ScriptLParser