// Generated from c://Users//Usuario//Desktop//Praxis-II-TALF//APP1//Sin log y exp//arithmetic.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class arithmeticLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		VARIABLE=1, SCIENTIFIC_NUMBER=2, LPAREN=3, RPAREN=4, PLUS=5, MINUS=6, 
		TIMES=7, DIV=8, GT=9, LT=10, EQ=11, POINT=12, POW=13, WS=14;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"VARIABLE", "VALID_ID_START", "VALID_ID_CHAR", "SCIENTIFIC_NUMBER", "NUMBER", 
			"UNSIGNED_INTEGER", "E", "SIGN", "LPAREN", "RPAREN", "PLUS", "MINUS", 
			"TIMES", "DIV", "GT", "LT", "EQ", "POINT", "POW", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", 
			"'='", "'.'", "'^'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VARIABLE", "SCIENTIFIC_NUMBER", "LPAREN", "RPAREN", "PLUS", "MINUS", 
			"TIMES", "DIV", "GT", "LT", "EQ", "POINT", "POW", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public arithmeticLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "arithmetic.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u000er\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0001\u0000\u0001\u0000\u0005"+
		"\u0000,\b\u0000\n\u0000\f\u0000/\t\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0003\u00025\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0003\u0003:\b\u0003\u0001\u0003\u0001\u0003\u0003\u0003>\b\u0003"+
		"\u0001\u0004\u0004\u0004A\b\u0004\u000b\u0004\f\u0004B\u0001\u0004\u0001"+
		"\u0004\u0004\u0004G\b\u0004\u000b\u0004\f\u0004H\u0003\u0004K\b\u0004"+
		"\u0001\u0005\u0004\u0005N\b\u0005\u000b\u0005\f\u0005O\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n"+
		"\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0004\u0013m\b"+
		"\u0013\u000b\u0013\f\u0013n\u0001\u0013\u0001\u0013\u0000\u0000\u0014"+
		"\u0001\u0001\u0003\u0000\u0005\u0000\u0007\u0002\t\u0000\u000b\u0000\r"+
		"\u0000\u000f\u0000\u0011\u0003\u0013\u0004\u0015\u0005\u0017\u0006\u0019"+
		"\u0007\u001b\b\u001d\t\u001f\n!\u000b#\f%\r\'\u000e\u0001\u0000\u0004"+
		"\u0003\u0000AZ__az\u0002\u0000EEee\u0002\u0000++--\u0003\u0000\t\n\r\r"+
		"  t\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000"+
		"\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000"+
		"\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000"+
		"\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000"+
		"\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000"+
		"%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0001)\u0001"+
		"\u0000\u0000\u0000\u00030\u0001\u0000\u0000\u0000\u00054\u0001\u0000\u0000"+
		"\u0000\u00076\u0001\u0000\u0000\u0000\t@\u0001\u0000\u0000\u0000\u000b"+
		"M\u0001\u0000\u0000\u0000\rQ\u0001\u0000\u0000\u0000\u000fS\u0001\u0000"+
		"\u0000\u0000\u0011U\u0001\u0000\u0000\u0000\u0013W\u0001\u0000\u0000\u0000"+
		"\u0015Y\u0001\u0000\u0000\u0000\u0017[\u0001\u0000\u0000\u0000\u0019]"+
		"\u0001\u0000\u0000\u0000\u001b_\u0001\u0000\u0000\u0000\u001da\u0001\u0000"+
		"\u0000\u0000\u001fc\u0001\u0000\u0000\u0000!e\u0001\u0000\u0000\u0000"+
		"#g\u0001\u0000\u0000\u0000%i\u0001\u0000\u0000\u0000\'l\u0001\u0000\u0000"+
		"\u0000)-\u0003\u0003\u0001\u0000*,\u0003\u0005\u0002\u0000+*\u0001\u0000"+
		"\u0000\u0000,/\u0001\u0000\u0000\u0000-+\u0001\u0000\u0000\u0000-.\u0001"+
		"\u0000\u0000\u0000.\u0002\u0001\u0000\u0000\u0000/-\u0001\u0000\u0000"+
		"\u000001\u0007\u0000\u0000\u00001\u0004\u0001\u0000\u0000\u000025\u0003"+
		"\u0003\u0001\u000035\u000209\u000042\u0001\u0000\u0000\u000043\u0001\u0000"+
		"\u0000\u00005\u0006\u0001\u0000\u0000\u00006=\u0003\t\u0004\u000079\u0003"+
		"\r\u0006\u00008:\u0003\u000f\u0007\u000098\u0001\u0000\u0000\u00009:\u0001"+
		"\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000;<\u0003\u000b\u0005\u0000"+
		"<>\u0001\u0000\u0000\u0000=7\u0001\u0000\u0000\u0000=>\u0001\u0000\u0000"+
		"\u0000>\b\u0001\u0000\u0000\u0000?A\u000209\u0000@?\u0001\u0000\u0000"+
		"\u0000AB\u0001\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000BC\u0001\u0000"+
		"\u0000\u0000CJ\u0001\u0000\u0000\u0000DF\u0005.\u0000\u0000EG\u000209"+
		"\u0000FE\u0001\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000HF\u0001\u0000"+
		"\u0000\u0000HI\u0001\u0000\u0000\u0000IK\u0001\u0000\u0000\u0000JD\u0001"+
		"\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000K\n\u0001\u0000\u0000\u0000"+
		"LN\u000209\u0000ML\u0001\u0000\u0000\u0000NO\u0001\u0000\u0000\u0000O"+
		"M\u0001\u0000\u0000\u0000OP\u0001\u0000\u0000\u0000P\f\u0001\u0000\u0000"+
		"\u0000QR\u0007\u0001\u0000\u0000R\u000e\u0001\u0000\u0000\u0000ST\u0007"+
		"\u0002\u0000\u0000T\u0010\u0001\u0000\u0000\u0000UV\u0005(\u0000\u0000"+
		"V\u0012\u0001\u0000\u0000\u0000WX\u0005)\u0000\u0000X\u0014\u0001\u0000"+
		"\u0000\u0000YZ\u0005+\u0000\u0000Z\u0016\u0001\u0000\u0000\u0000[\\\u0005"+
		"-\u0000\u0000\\\u0018\u0001\u0000\u0000\u0000]^\u0005*\u0000\u0000^\u001a"+
		"\u0001\u0000\u0000\u0000_`\u0005/\u0000\u0000`\u001c\u0001\u0000\u0000"+
		"\u0000ab\u0005>\u0000\u0000b\u001e\u0001\u0000\u0000\u0000cd\u0005<\u0000"+
		"\u0000d \u0001\u0000\u0000\u0000ef\u0005=\u0000\u0000f\"\u0001\u0000\u0000"+
		"\u0000gh\u0005.\u0000\u0000h$\u0001\u0000\u0000\u0000ij\u0005^\u0000\u0000"+
		"j&\u0001\u0000\u0000\u0000km\u0007\u0003\u0000\u0000lk\u0001\u0000\u0000"+
		"\u0000mn\u0001\u0000\u0000\u0000nl\u0001\u0000\u0000\u0000no\u0001\u0000"+
		"\u0000\u0000op\u0001\u0000\u0000\u0000pq\u0006\u0013\u0000\u0000q(\u0001"+
		"\u0000\u0000\u0000\n\u0000-49=BHJOn\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}