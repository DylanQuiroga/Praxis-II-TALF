// Generated from c://Users//Usuario//Desktop//Praxis-II-TALF//APP3//Graph.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link GraphParser}.
 */
public interface GraphListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link GraphParser#graph}.
	 * @param ctx the parse tree
	 */
	void enterGraph(GraphParser.GraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphParser#graph}.
	 * @param ctx the parse tree
	 */
	void exitGraph(GraphParser.GraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphParser#edge}.
	 * @param ctx the parse tree
	 */
	void enterEdge(GraphParser.EdgeContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphParser#edge}.
	 * @param ctx the parse tree
	 */
	void exitEdge(GraphParser.EdgeContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphParser#node}.
	 * @param ctx the parse tree
	 */
	void enterNode(GraphParser.NodeContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphParser#node}.
	 * @param ctx the parse tree
	 */
	void exitNode(GraphParser.NodeContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphParser#weight}.
	 * @param ctx the parse tree
	 */
	void enterWeight(GraphParser.WeightContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphParser#weight}.
	 * @param ctx the parse tree
	 */
	void exitWeight(GraphParser.WeightContext ctx);
}