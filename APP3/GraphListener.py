# Generated from Graph.g4 by ANTLR 4.13.1
from antlr4 import *
from graphviz import Digraph

if "." in __name__:
    from .GraphParser import GraphParser
else:
    from GraphParser import GraphParser

# This class defines a complete listener for a parse tree produced by GraphParser.
class GraphListener(ParseTreeListener):
    def __init__(self):
        self.dot = Digraph()
        self.nodes = set()
        self.edges = []

    # Enter a parse tree produced by GraphParser#graph.
    def enterGraph(self, ctx:GraphParser.GraphContext):
        print("Vertices...")

    # Exit a parse tree produced by GraphParser#graph.
    def exitGraph(self, ctx:GraphParser.GraphContext):
        for node in sorted(list(self.nodes)):
            #print(node)
            self.nodes.add(node)
        nodes_str = ', '.join(sorted(list(self.nodes)))
        print(nodes_str)
        print("\nEdges...")
        for edge in self.edges:
            print(f"{edge[0]} to {edge[1]} with weight {edge[2]}")

    # Enter a parse tree produced by GraphParser#edge.
    def enterEdge(self, ctx:GraphParser.EdgeContext):
        node1 = ctx.node(0).getText()
        node2 = ctx.node(1).getText()
        weight = ctx.weight().getText()
    
        self.nodes.add(node1)
        self.nodes.add(node2)
        self.edges.append((node1, node2, weight))
    
        self.dot.edge(node1, node2, label=weight)

    # Exit a parse tree produced by GraphParser#edge.
    def exitEdge(self, ctx:GraphParser.EdgeContext):
        pass


    # Enter a parse tree produced by GraphParser#node.
    def enterNode(self, ctx:GraphParser.NodeContext):
        pass

    # Exit a parse tree produced by GraphParser#node.
    def exitNode(self, ctx:GraphParser.NodeContext):
        pass


    # Enter a parse tree produced by GraphParser#weight.
    def enterWeight(self, ctx:GraphParser.WeightContext):
        pass

    # Exit a parse tree produced by GraphParser#weight.
    def exitWeight(self, ctx:GraphParser.WeightContext):
        pass


del GraphParser