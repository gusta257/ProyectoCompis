// Generated from c:\Users\Gustavo\Desktop\Compis\ProyectoCompis\Decaf.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DecafParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		ID=39, NUM=40, CHAR=41, WHITESPACE=42;
	public static final int
		RULE_program = 0, RULE_declaration = 1, RULE_varDeclaration = 2, RULE_structDeclaration = 3, 
		RULE_varType = 4, RULE_methodDeclaration = 5, RULE_methodType = 6, RULE_parameter = 7, 
		RULE_parameterType = 8, RULE_block = 9, RULE_statement = 10, RULE_location = 11, 
		RULE_expression = 12, RULE_methodCall = 13, RULE_rel_op = 14, RULE_eq_op = 15, 
		RULE_arith_op_fifth = 16, RULE_arith_op_fourth = 17, RULE_arith_op_third = 18, 
		RULE_arith_op_second = 19, RULE_arith_op_first = 20, RULE_literal = 21, 
		RULE_int_literal = 22, RULE_char_literal = 23, RULE_bool_literal = 24;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "declaration", "varDeclaration", "structDeclaration", "varType", 
			"methodDeclaration", "methodType", "parameter", "parameterType", "block", 
			"statement", "location", "expression", "methodCall", "rel_op", "eq_op", 
			"arith_op_fifth", "arith_op_fourth", "arith_op_third", "arith_op_second", 
			"arith_op_first", "literal", "int_literal", "char_literal", "bool_literal"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'Program'", "'{'", "'}'", "';'", "'['", "']'", "'struct'", 
			"'int'", "'char'", "'boolean'", "'void'", "'('", "','", "')'", "'if'", 
			"'else'", "'while'", "'return'", "'='", "'.'", "'-'", "'!'", "'<'", "'>'", 
			"'<='", "'>='", "'=='", "'!='", "'*'", "'/'", "'%'", "'+'", "'&&'", "'||'", 
			"'''", "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "ID", "NUM", "CHAR", "WHITESPACE"
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

	@Override
	public String getGrammarFileName() { return "Decaf.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DecafParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			match(T__0);
			setState(51);
			match(T__1);
			setState(52);
			match(T__2);
			setState(56);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11))) != 0)) {
				{
				{
				setState(53);
				declaration();
				}
				}
				setState(58);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(59);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public StructDeclarationContext structDeclaration() {
			return getRuleContext(StructDeclarationContext.class,0);
		}
		public VarDeclarationContext varDeclaration() {
			return getRuleContext(VarDeclarationContext.class,0);
		}
		public MethodDeclarationContext methodDeclaration() {
			return getRuleContext(MethodDeclarationContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaration);
		try {
			setState(64);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(61);
				structDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(62);
				varDeclaration();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(63);
				methodDeclaration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarDeclarationContext extends ParserRuleContext {
		public VarTypeContext varType() {
			return getRuleContext(VarTypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(DecafParser.ID, 0); }
		public TerminalNode NUM() { return getToken(DecafParser.NUM, 0); }
		public VarDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDeclaration; }
	}

	public final VarDeclarationContext varDeclaration() throws RecognitionException {
		VarDeclarationContext _localctx = new VarDeclarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_varDeclaration);
		try {
			setState(77);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(66);
				varType();
				setState(67);
				match(ID);
				setState(68);
				match(T__4);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(70);
				varType();
				setState(71);
				match(ID);
				setState(72);
				match(T__5);
				setState(73);
				match(NUM);
				setState(74);
				match(T__6);
				setState(75);
				match(T__4);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StructDeclarationContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DecafParser.ID, 0); }
		public List<VarDeclarationContext> varDeclaration() {
			return getRuleContexts(VarDeclarationContext.class);
		}
		public VarDeclarationContext varDeclaration(int i) {
			return getRuleContext(VarDeclarationContext.class,i);
		}
		public StructDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structDeclaration; }
	}

	public final StructDeclarationContext structDeclaration() throws RecognitionException {
		StructDeclarationContext _localctx = new StructDeclarationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_structDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(T__7);
			setState(80);
			match(ID);
			setState(81);
			match(T__2);
			setState(85);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11))) != 0)) {
				{
				{
				setState(82);
				varDeclaration();
				}
				}
				setState(87);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(88);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarTypeContext extends ParserRuleContext {
		public VarTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varType; }
	 
		public VarTypeContext() { }
		public void copyFrom(VarTypeContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class STRUCT_VARTYPEContext extends VarTypeContext {
		public TerminalNode ID() { return getToken(DecafParser.ID, 0); }
		public STRUCT_VARTYPEContext(VarTypeContext ctx) { copyFrom(ctx); }
	}
	public static class STRUCTDECLARATION_VARTYPEContext extends VarTypeContext {
		public StructDeclarationContext structDeclaration() {
			return getRuleContext(StructDeclarationContext.class,0);
		}
		public STRUCTDECLARATION_VARTYPEContext(VarTypeContext ctx) { copyFrom(ctx); }
	}
	public static class BOOL_VARTYPEContext extends VarTypeContext {
		public BOOL_VARTYPEContext(VarTypeContext ctx) { copyFrom(ctx); }
	}
	public static class CHAR_VARTYPEContext extends VarTypeContext {
		public CHAR_VARTYPEContext(VarTypeContext ctx) { copyFrom(ctx); }
	}
	public static class INT_VARTYPEContext extends VarTypeContext {
		public INT_VARTYPEContext(VarTypeContext ctx) { copyFrom(ctx); }
	}
	public static class VOID_VARTYPEContext extends VarTypeContext {
		public VOID_VARTYPEContext(VarTypeContext ctx) { copyFrom(ctx); }
	}

	public final VarTypeContext varType() throws RecognitionException {
		VarTypeContext _localctx = new VarTypeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_varType);
		try {
			setState(97);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				_localctx = new INT_VARTYPEContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(90);
				match(T__8);
				}
				break;
			case 2:
				_localctx = new CHAR_VARTYPEContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(91);
				match(T__9);
				}
				break;
			case 3:
				_localctx = new BOOL_VARTYPEContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(92);
				match(T__10);
				}
				break;
			case 4:
				_localctx = new STRUCT_VARTYPEContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(93);
				match(T__7);
				setState(94);
				match(ID);
				}
				break;
			case 5:
				_localctx = new STRUCTDECLARATION_VARTYPEContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(95);
				structDeclaration();
				}
				break;
			case 6:
				_localctx = new VOID_VARTYPEContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(96);
				match(T__11);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MethodDeclarationContext extends ParserRuleContext {
		public MethodTypeContext methodType() {
			return getRuleContext(MethodTypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(DecafParser.ID, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<ParameterContext> parameter() {
			return getRuleContexts(ParameterContext.class);
		}
		public ParameterContext parameter(int i) {
			return getRuleContext(ParameterContext.class,i);
		}
		public MethodDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodDeclaration; }
	}

	public final MethodDeclarationContext methodDeclaration() throws RecognitionException {
		MethodDeclarationContext _localctx = new MethodDeclarationContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_methodDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			methodType();
			setState(100);
			match(ID);
			setState(101);
			match(T__12);
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10))) != 0)) {
				{
				{
				setState(102);
				parameter();
				setState(107);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__13) {
					{
					{
					setState(103);
					match(T__13);
					setState(104);
					parameter();
					}
					}
					setState(109);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				setState(114);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(115);
			match(T__14);
			setState(116);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MethodTypeContext extends ParserRuleContext {
		public MethodTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodType; }
	 
		public MethodTypeContext() { }
		public void copyFrom(MethodTypeContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class VOID_METHODTYPEContext extends MethodTypeContext {
		public VOID_METHODTYPEContext(MethodTypeContext ctx) { copyFrom(ctx); }
	}
	public static class CHAR_METHODTYPEContext extends MethodTypeContext {
		public CHAR_METHODTYPEContext(MethodTypeContext ctx) { copyFrom(ctx); }
	}
	public static class BOOL_METHODTYPEContext extends MethodTypeContext {
		public BOOL_METHODTYPEContext(MethodTypeContext ctx) { copyFrom(ctx); }
	}
	public static class INT_METHODTYPEContext extends MethodTypeContext {
		public INT_METHODTYPEContext(MethodTypeContext ctx) { copyFrom(ctx); }
	}

	public final MethodTypeContext methodType() throws RecognitionException {
		MethodTypeContext _localctx = new MethodTypeContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_methodType);
		try {
			setState(122);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
				_localctx = new INT_METHODTYPEContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(118);
				match(T__8);
				}
				break;
			case T__9:
				_localctx = new CHAR_METHODTYPEContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(119);
				match(T__9);
				}
				break;
			case T__10:
				_localctx = new BOOL_METHODTYPEContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(120);
				match(T__10);
				}
				break;
			case T__11:
				_localctx = new VOID_METHODTYPEContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(121);
				match(T__11);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParameterContext extends ParserRuleContext {
		public ParameterTypeContext parameterType() {
			return getRuleContext(ParameterTypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(DecafParser.ID, 0); }
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_parameter);
		try {
			setState(132);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(124);
				parameterType();
				setState(125);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(127);
				parameterType();
				setState(128);
				match(ID);
				setState(129);
				match(T__5);
				setState(130);
				match(T__6);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParameterTypeContext extends ParserRuleContext {
		public ParameterTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameterType; }
	}

	public final ParameterTypeContext parameterType() throws RecognitionException {
		ParameterTypeContext _localctx = new ParameterTypeContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_parameterType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public List<VarDeclarationContext> varDeclaration() {
			return getRuleContexts(VarDeclarationContext.class);
		}
		public VarDeclarationContext varDeclaration(int i) {
			return getRuleContext(VarDeclarationContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			match(T__2);
			setState(140);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11))) != 0)) {
				{
				{
				setState(137);
				varDeclaration();
				}
				}
				setState(142);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(146);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << T__15) | (1L << T__17) | (1L << T__18) | (1L << ID))) != 0)) {
				{
				{
				setState(143);
				statement();
				}
				}
				setState(148);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(149);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class StatementIFContext extends StatementContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public StatementIFContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class StatementMETHODCALLContext extends StatementContext {
		public MethodCallContext methodCall() {
			return getRuleContext(MethodCallContext.class,0);
		}
		public StatementMETHODCALLContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class StatementLOCATIONContext extends StatementContext {
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementLOCATIONContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class StatementRETURNContext extends StatementContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementRETURNContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class StatementWHILEContext extends StatementContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public StatementWHILEContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class StatementBLOCKContext extends StatementContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public StatementBLOCKContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_statement);
		int _la;
		try {
			setState(179);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				_localctx = new StatementIFContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(151);
				match(T__15);
				setState(152);
				match(T__12);
				setState(153);
				expression(0);
				setState(154);
				match(T__14);
				setState(155);
				block();
				setState(158);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__16) {
					{
					setState(156);
					match(T__16);
					setState(157);
					block();
					}
				}

				}
				break;
			case 2:
				_localctx = new StatementWHILEContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(160);
				match(T__17);
				setState(161);
				match(T__12);
				setState(162);
				expression(0);
				setState(163);
				match(T__14);
				setState(164);
				block();
				}
				break;
			case 3:
				_localctx = new StatementRETURNContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(166);
				match(T__18);
				setState(167);
				expression(0);
				setState(168);
				match(T__4);
				}
				break;
			case 4:
				_localctx = new StatementMETHODCALLContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(170);
				methodCall();
				setState(171);
				match(T__4);
				}
				break;
			case 5:
				_localctx = new StatementBLOCKContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(173);
				block();
				}
				break;
			case 6:
				_localctx = new StatementLOCATIONContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(174);
				location();
				setState(175);
				match(T__19);
				setState(176);
				expression(0);
				setState(177);
				match(T__4);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LocationContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DecafParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public LocationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_location; }
	}

	public final LocationContext location() throws RecognitionException {
		LocationContext _localctx = new LocationContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_location);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(181);
				match(ID);
				}
				break;
			case 2:
				{
				setState(182);
				match(ID);
				setState(183);
				match(T__5);
				setState(184);
				expression(0);
				setState(185);
				match(T__6);
				}
				break;
			}
			setState(191);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(189);
				match(T__20);
				setState(190);
				location();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class Expr_literalContext extends ExpressionContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public Expr_literalContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_locContext extends ExpressionContext {
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public Expr_locContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_parenthesisContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Expr_parenthesisContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_mcallContext extends ExpressionContext {
		public MethodCallContext methodCall() {
			return getRuleContext(MethodCallContext.class,0);
		}
		public Expr_mcallContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_minusContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Expr_minusContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_arith1Context extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Arith_op_firstContext arith_op_first() {
			return getRuleContext(Arith_op_firstContext.class,0);
		}
		public Expr_arith1Context(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_arith2Context extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Arith_op_secondContext arith_op_second() {
			return getRuleContext(Arith_op_secondContext.class,0);
		}
		public Expr_arith2Context(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_notContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Expr_notContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_arith3Context extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Arith_op_thirdContext arith_op_third() {
			return getRuleContext(Arith_op_thirdContext.class,0);
		}
		public Expr_arith3Context(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_arith4Context extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Arith_op_fourthContext arith_op_fourth() {
			return getRuleContext(Arith_op_fourthContext.class,0);
		}
		public Expr_arith4Context(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_arith5Context extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Arith_op_fifthContext arith_op_fifth() {
			return getRuleContext(Arith_op_fifthContext.class,0);
		}
		public Expr_arith5Context(ExpressionContext ctx) { copyFrom(ctx); }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 24;
		enterRecursionRule(_localctx, 24, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				_localctx = new Expr_mcallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(194);
				methodCall();
				}
				break;
			case 2:
				{
				_localctx = new Expr_locContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(195);
				location();
				}
				break;
			case 3:
				{
				_localctx = new Expr_literalContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(196);
				literal();
				}
				break;
			case 4:
				{
				_localctx = new Expr_minusContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(197);
				match(T__21);
				setState(198);
				expression(8);
				}
				break;
			case 5:
				{
				_localctx = new Expr_notContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(199);
				match(T__22);
				setState(200);
				expression(7);
				}
				break;
			case 6:
				{
				_localctx = new Expr_parenthesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(201);
				match(T__12);
				setState(202);
				expression(0);
				setState(203);
				match(T__14);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(229);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(227);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
					case 1:
						{
						_localctx = new Expr_arith5Context(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(207);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(208);
						arith_op_fifth();
						setState(209);
						expression(6);
						}
						break;
					case 2:
						{
						_localctx = new Expr_arith4Context(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(211);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(212);
						arith_op_fourth();
						setState(213);
						expression(5);
						}
						break;
					case 3:
						{
						_localctx = new Expr_arith3Context(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(215);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(216);
						arith_op_third();
						setState(217);
						expression(4);
						}
						break;
					case 4:
						{
						_localctx = new Expr_arith2Context(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(219);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(220);
						arith_op_second();
						setState(221);
						expression(3);
						}
						break;
					case 5:
						{
						_localctx = new Expr_arith1Context(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(223);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(224);
						arith_op_first();
						setState(225);
						expression(2);
						}
						break;
					}
					} 
				}
				setState(231);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class MethodCallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DecafParser.ID, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public MethodCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodCall; }
	}

	public final MethodCallContext methodCall() throws RecognitionException {
		MethodCallContext _localctx = new MethodCallContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_methodCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(ID);
			setState(233);
			match(T__12);
			setState(242);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__12) | (1L << T__21) | (1L << T__22) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << ID) | (1L << NUM))) != 0)) {
				{
				setState(234);
				expression(0);
				setState(239);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__13) {
					{
					{
					setState(235);
					match(T__13);
					setState(236);
					expression(0);
					}
					}
					setState(241);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(244);
			match(T__14);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Rel_opContext extends ParserRuleContext {
		public Rel_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rel_op; }
	}

	public final Rel_opContext rel_op() throws RecognitionException {
		Rel_opContext _localctx = new Rel_opContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_rel_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(246);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Eq_opContext extends ParserRuleContext {
		public Eq_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_eq_op; }
	}

	public final Eq_opContext eq_op() throws RecognitionException {
		Eq_opContext _localctx = new Eq_opContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_eq_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			_la = _input.LA(1);
			if ( !(_la==T__27 || _la==T__28) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Arith_op_fifthContext extends ParserRuleContext {
		public Arith_op_fifthContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_op_fifth; }
	}

	public final Arith_op_fifthContext arith_op_fifth() throws RecognitionException {
		Arith_op_fifthContext _localctx = new Arith_op_fifthContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_arith_op_fifth);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(250);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__29) | (1L << T__30) | (1L << T__31))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Arith_op_fourthContext extends ParserRuleContext {
		public Arith_op_fourthContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_op_fourth; }
	}

	public final Arith_op_fourthContext arith_op_fourth() throws RecognitionException {
		Arith_op_fourthContext _localctx = new Arith_op_fourthContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_arith_op_fourth);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252);
			_la = _input.LA(1);
			if ( !(_la==T__21 || _la==T__32) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Arith_op_thirdContext extends ParserRuleContext {
		public Rel_opContext rel_op() {
			return getRuleContext(Rel_opContext.class,0);
		}
		public Eq_opContext eq_op() {
			return getRuleContext(Eq_opContext.class,0);
		}
		public Arith_op_thirdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_op_third; }
	}

	public final Arith_op_thirdContext arith_op_third() throws RecognitionException {
		Arith_op_thirdContext _localctx = new Arith_op_thirdContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_arith_op_third);
		try {
			setState(256);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__23:
			case T__24:
			case T__25:
			case T__26:
				enterOuterAlt(_localctx, 1);
				{
				setState(254);
				rel_op();
				}
				break;
			case T__27:
			case T__28:
				enterOuterAlt(_localctx, 2);
				{
				setState(255);
				eq_op();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Arith_op_secondContext extends ParserRuleContext {
		public Arith_op_secondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_op_second; }
	}

	public final Arith_op_secondContext arith_op_second() throws RecognitionException {
		Arith_op_secondContext _localctx = new Arith_op_secondContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_arith_op_second);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			match(T__33);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Arith_op_firstContext extends ParserRuleContext {
		public Arith_op_firstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_op_first; }
	}

	public final Arith_op_firstContext arith_op_first() throws RecognitionException {
		Arith_op_firstContext _localctx = new Arith_op_firstContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_arith_op_first);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			match(T__34);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public Int_literalContext int_literal() {
			return getRuleContext(Int_literalContext.class,0);
		}
		public Char_literalContext char_literal() {
			return getRuleContext(Char_literalContext.class,0);
		}
		public Bool_literalContext bool_literal() {
			return getRuleContext(Bool_literalContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_literal);
		try {
			setState(265);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM:
				enterOuterAlt(_localctx, 1);
				{
				setState(262);
				int_literal();
				}
				break;
			case T__35:
				enterOuterAlt(_localctx, 2);
				{
				setState(263);
				char_literal();
				}
				break;
			case T__36:
			case T__37:
				enterOuterAlt(_localctx, 3);
				{
				setState(264);
				bool_literal();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Int_literalContext extends ParserRuleContext {
		public TerminalNode NUM() { return getToken(DecafParser.NUM, 0); }
		public Int_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_literal; }
	}

	public final Int_literalContext int_literal() throws RecognitionException {
		Int_literalContext _localctx = new Int_literalContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_int_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(NUM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Char_literalContext extends ParserRuleContext {
		public TerminalNode CHAR() { return getToken(DecafParser.CHAR, 0); }
		public Char_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_char_literal; }
	}

	public final Char_literalContext char_literal() throws RecognitionException {
		Char_literalContext _localctx = new Char_literalContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_char_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(269);
			match(T__35);
			setState(270);
			match(CHAR);
			setState(271);
			match(T__35);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Bool_literalContext extends ParserRuleContext {
		public Bool_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bool_literal; }
	}

	public final Bool_literalContext bool_literal() throws RecognitionException {
		Bool_literalContext _localctx = new Bool_literalContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_bool_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(273);
			_la = _input.LA(1);
			if ( !(_la==T__36 || _la==T__37) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 12:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		case 2:
			return precpred(_ctx, 3);
		case 3:
			return precpred(_ctx, 2);
		case 4:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,\u0116\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\3\2\3\2\3\2\3\2\7\29\n\2\f\2\16\2<\13\2\3\2\3\2\3\3\3\3\3\3"+
		"\5\3C\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4P\n\4\3\5\3\5"+
		"\3\5\3\5\7\5V\n\5\f\5\16\5Y\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5"+
		"\6d\n\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7l\n\7\f\7\16\7o\13\7\7\7q\n\7\f\7\16"+
		"\7t\13\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b}\n\b\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\5\t\u0087\n\t\3\n\3\n\3\13\3\13\7\13\u008d\n\13\f\13\16\13\u0090"+
		"\13\13\3\13\7\13\u0093\n\13\f\13\16\13\u0096\13\13\3\13\3\13\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\5\f\u00a1\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00b6\n\f\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\5\r\u00be\n\r\3\r\3\r\5\r\u00c2\n\r\3\16\3\16\3\16\3\16\3\16\3"+
		"\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00d0\n\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\7\16\u00e6\n\16\f\16\16\16\u00e9\13\16\3\17\3\17\3\17\3\17"+
		"\3\17\7\17\u00f0\n\17\f\17\16\17\u00f3\13\17\5\17\u00f5\n\17\3\17\3\17"+
		"\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\5\24\u0103\n\24\3\25"+
		"\3\25\3\26\3\26\3\27\3\27\3\27\5\27\u010c\n\27\3\30\3\30\3\31\3\31\3\31"+
		"\3\31\3\32\3\32\3\32\2\3\32\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36"+
		" \"$&(*,.\60\62\2\b\3\2\13\r\3\2\32\35\3\2\36\37\3\2 \"\4\2\30\30##\3"+
		"\2\'(\2\u0125\2\64\3\2\2\2\4B\3\2\2\2\6O\3\2\2\2\bQ\3\2\2\2\nc\3\2\2\2"+
		"\fe\3\2\2\2\16|\3\2\2\2\20\u0086\3\2\2\2\22\u0088\3\2\2\2\24\u008a\3\2"+
		"\2\2\26\u00b5\3\2\2\2\30\u00bd\3\2\2\2\32\u00cf\3\2\2\2\34\u00ea\3\2\2"+
		"\2\36\u00f8\3\2\2\2 \u00fa\3\2\2\2\"\u00fc\3\2\2\2$\u00fe\3\2\2\2&\u0102"+
		"\3\2\2\2(\u0104\3\2\2\2*\u0106\3\2\2\2,\u010b\3\2\2\2.\u010d\3\2\2\2\60"+
		"\u010f\3\2\2\2\62\u0113\3\2\2\2\64\65\7\3\2\2\65\66\7\4\2\2\66:\7\5\2"+
		"\2\679\5\4\3\28\67\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;=\3\2\2\2<:\3"+
		"\2\2\2=>\7\6\2\2>\3\3\2\2\2?C\5\b\5\2@C\5\6\4\2AC\5\f\7\2B?\3\2\2\2B@"+
		"\3\2\2\2BA\3\2\2\2C\5\3\2\2\2DE\5\n\6\2EF\7)\2\2FG\7\7\2\2GP\3\2\2\2H"+
		"I\5\n\6\2IJ\7)\2\2JK\7\b\2\2KL\7*\2\2LM\7\t\2\2MN\7\7\2\2NP\3\2\2\2OD"+
		"\3\2\2\2OH\3\2\2\2P\7\3\2\2\2QR\7\n\2\2RS\7)\2\2SW\7\5\2\2TV\5\6\4\2U"+
		"T\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2YW\3\2\2\2Z[\7\6\2\2"+
		"[\t\3\2\2\2\\d\7\13\2\2]d\7\f\2\2^d\7\r\2\2_`\7\n\2\2`d\7)\2\2ad\5\b\5"+
		"\2bd\7\16\2\2c\\\3\2\2\2c]\3\2\2\2c^\3\2\2\2c_\3\2\2\2ca\3\2\2\2cb\3\2"+
		"\2\2d\13\3\2\2\2ef\5\16\b\2fg\7)\2\2gr\7\17\2\2hm\5\20\t\2ij\7\20\2\2"+
		"jl\5\20\t\2ki\3\2\2\2lo\3\2\2\2mk\3\2\2\2mn\3\2\2\2nq\3\2\2\2om\3\2\2"+
		"\2ph\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2su\3\2\2\2tr\3\2\2\2uv\7\21"+
		"\2\2vw\5\24\13\2w\r\3\2\2\2x}\7\13\2\2y}\7\f\2\2z}\7\r\2\2{}\7\16\2\2"+
		"|x\3\2\2\2|y\3\2\2\2|z\3\2\2\2|{\3\2\2\2}\17\3\2\2\2~\177\5\22\n\2\177"+
		"\u0080\7)\2\2\u0080\u0087\3\2\2\2\u0081\u0082\5\22\n\2\u0082\u0083\7)"+
		"\2\2\u0083\u0084\7\b\2\2\u0084\u0085\7\t\2\2\u0085\u0087\3\2\2\2\u0086"+
		"~\3\2\2\2\u0086\u0081\3\2\2\2\u0087\21\3\2\2\2\u0088\u0089\t\2\2\2\u0089"+
		"\23\3\2\2\2\u008a\u008e\7\5\2\2\u008b\u008d\5\6\4\2\u008c\u008b\3\2\2"+
		"\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0094"+
		"\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0093\5\26\f\2\u0092\u0091\3\2\2\2"+
		"\u0093\u0096\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097"+
		"\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0098\7\6\2\2\u0098\25\3\2\2\2\u0099"+
		"\u009a\7\22\2\2\u009a\u009b\7\17\2\2\u009b\u009c\5\32\16\2\u009c\u009d"+
		"\7\21\2\2\u009d\u00a0\5\24\13\2\u009e\u009f\7\23\2\2\u009f\u00a1\5\24"+
		"\13\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00b6\3\2\2\2\u00a2"+
		"\u00a3\7\24\2\2\u00a3\u00a4\7\17\2\2\u00a4\u00a5\5\32\16\2\u00a5\u00a6"+
		"\7\21\2\2\u00a6\u00a7\5\24\13\2\u00a7\u00b6\3\2\2\2\u00a8\u00a9\7\25\2"+
		"\2\u00a9\u00aa\5\32\16\2\u00aa\u00ab\7\7\2\2\u00ab\u00b6\3\2\2\2\u00ac"+
		"\u00ad\5\34\17\2\u00ad\u00ae\7\7\2\2\u00ae\u00b6\3\2\2\2\u00af\u00b6\5"+
		"\24\13\2\u00b0\u00b1\5\30\r\2\u00b1\u00b2\7\26\2\2\u00b2\u00b3\5\32\16"+
		"\2\u00b3\u00b4\7\7\2\2\u00b4\u00b6\3\2\2\2\u00b5\u0099\3\2\2\2\u00b5\u00a2"+
		"\3\2\2\2\u00b5\u00a8\3\2\2\2\u00b5\u00ac\3\2\2\2\u00b5\u00af\3\2\2\2\u00b5"+
		"\u00b0\3\2\2\2\u00b6\27\3\2\2\2\u00b7\u00be\7)\2\2\u00b8\u00b9\7)\2\2"+
		"\u00b9\u00ba\7\b\2\2\u00ba\u00bb\5\32\16\2\u00bb\u00bc\7\t\2\2\u00bc\u00be"+
		"\3\2\2\2\u00bd\u00b7\3\2\2\2\u00bd\u00b8\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf"+
		"\u00c0\7\27\2\2\u00c0\u00c2\5\30\r\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3"+
		"\2\2\2\u00c2\31\3\2\2\2\u00c3\u00c4\b\16\1\2\u00c4\u00d0\5\34\17\2\u00c5"+
		"\u00d0\5\30\r\2\u00c6\u00d0\5,\27\2\u00c7\u00c8\7\30\2\2\u00c8\u00d0\5"+
		"\32\16\n\u00c9\u00ca\7\31\2\2\u00ca\u00d0\5\32\16\t\u00cb\u00cc\7\17\2"+
		"\2\u00cc\u00cd\5\32\16\2\u00cd\u00ce\7\21\2\2\u00ce\u00d0\3\2\2\2\u00cf"+
		"\u00c3\3\2\2\2\u00cf\u00c5\3\2\2\2\u00cf\u00c6\3\2\2\2\u00cf\u00c7\3\2"+
		"\2\2\u00cf\u00c9\3\2\2\2\u00cf\u00cb\3\2\2\2\u00d0\u00e7\3\2\2\2\u00d1"+
		"\u00d2\f\7\2\2\u00d2\u00d3\5\"\22\2\u00d3\u00d4\5\32\16\b\u00d4\u00e6"+
		"\3\2\2\2\u00d5\u00d6\f\6\2\2\u00d6\u00d7\5$\23\2\u00d7\u00d8\5\32\16\7"+
		"\u00d8\u00e6\3\2\2\2\u00d9\u00da\f\5\2\2\u00da\u00db\5&\24\2\u00db\u00dc"+
		"\5\32\16\6\u00dc\u00e6\3\2\2\2\u00dd\u00de\f\4\2\2\u00de\u00df\5(\25\2"+
		"\u00df\u00e0\5\32\16\5\u00e0\u00e6\3\2\2\2\u00e1\u00e2\f\3\2\2\u00e2\u00e3"+
		"\5*\26\2\u00e3\u00e4\5\32\16\4\u00e4\u00e6\3\2\2\2\u00e5\u00d1\3\2\2\2"+
		"\u00e5\u00d5\3\2\2\2\u00e5\u00d9\3\2\2\2\u00e5\u00dd\3\2\2\2\u00e5\u00e1"+
		"\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8"+
		"\33\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb\7)\2\2\u00eb\u00f4\7\17\2"+
		"\2\u00ec\u00f1\5\32\16\2\u00ed\u00ee\7\20\2\2\u00ee\u00f0\5\32\16\2\u00ef"+
		"\u00ed\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2"+
		"\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00ec\3\2\2\2\u00f4"+
		"\u00f5\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\7\21\2\2\u00f7\35\3\2\2"+
		"\2\u00f8\u00f9\t\3\2\2\u00f9\37\3\2\2\2\u00fa\u00fb\t\4\2\2\u00fb!\3\2"+
		"\2\2\u00fc\u00fd\t\5\2\2\u00fd#\3\2\2\2\u00fe\u00ff\t\6\2\2\u00ff%\3\2"+
		"\2\2\u0100\u0103\5\36\20\2\u0101\u0103\5 \21\2\u0102\u0100\3\2\2\2\u0102"+
		"\u0101\3\2\2\2\u0103\'\3\2\2\2\u0104\u0105\7$\2\2\u0105)\3\2\2\2\u0106"+
		"\u0107\7%\2\2\u0107+\3\2\2\2\u0108\u010c\5.\30\2\u0109\u010c\5\60\31\2"+
		"\u010a\u010c\5\62\32\2\u010b\u0108\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010a"+
		"\3\2\2\2\u010c-\3\2\2\2\u010d\u010e\7*\2\2\u010e/\3\2\2\2\u010f\u0110"+
		"\7&\2\2\u0110\u0111\7+\2\2\u0111\u0112\7&\2\2\u0112\61\3\2\2\2\u0113\u0114"+
		"\t\7\2\2\u0114\63\3\2\2\2\30:BOWcmr|\u0086\u008e\u0094\u00a0\u00b5\u00bd"+
		"\u00c1\u00cf\u00e5\u00e7\u00f1\u00f4\u0102\u010b";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}