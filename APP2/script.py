import sys
from antlr4 import *
from ScriptLLexer import ScriptLLexer
from ScriptLParser import ScriptLParser
from ScriptLVisitor import ScriptLVisitor

class VariableUsageVisitor(ScriptLVisitor):
    def __init__(self):
        self.declared_vars = set()
        self.used_vars = set()
        self.assignments = {}

    def visitAssignStmt(self, ctx:ScriptLParser.AssignStmtContext):
        var_name = ctx.ID().getText()
        self.declared_vars.add(var_name)
        self.assignments[var_name] = ctx.getText()
        if ctx.expr():
            self.visit(ctx.expr())
        return None

    def visitGetStmt(self, ctx:ScriptLParser.GetStmtContext):
        var_name = ctx.ID().getText()
        self.declared_vars.add(var_name)
        return None

    def visitPutStmt(self, ctx: ScriptLParser.PutStmtContext):
        if ctx.ID() is not None:
            var_name = ctx.ID().getText()
            self.used_vars.add(var_name)
        elif ctx.NUMBER() is not None:
            number_value = ctx.NUMBER().getText()
        return None

    def visitExpr(self, ctx:ScriptLParser.ExprContext):
        if ctx.ID():
            self.used_vars.add(ctx.ID().getText())
        for child in ctx.children:
            self.visit(child)
        return None

    def visitWhileStmt(self, ctx:ScriptLParser.WhileStmtContext):
        self.visit(ctx.expr())
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitIfStmt(self, ctx: ScriptLParser.IfStmtContext):
        self.visit(ctx.expr())  

      
        self.visit(ctx.ifBlock())

        
        if ctx.elseBlock() is not None:
            self.visit(ctx.elseBlock())
        return None


def main(argv):
    input_file = FileStream(argv[1])
    lexer = ScriptLLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = ScriptLParser(stream)
    tree = parser.program()

    visitor = VariableUsageVisitor()
    visitor.visit(tree)

    unused_vars = visitor.declared_vars - visitor.used_vars

    with open(argv[1], 'r') as file:
        input_code = file.read()

    output_code = ""
    lines = input_code.splitlines()
    for var in unused_vars:
        for i, line in enumerate(lines):
            if var in line:
                lines[i] = f"// -- var {var} no es usada -- " + line
                break

    output_code = "\n".join(lines)
    print(output_code)


if __name__ == '__main__':
    main(sys.argv)
