# Generated from .\Decaf.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafParser import DecafParser
else:
    from DecafParser import DecafParser

# This class defines a complete listener for a parse tree produced by DecafParser.
class DecafListener(ParseTreeListener):

    # Enter a parse tree produced by DecafParser#program.
    def enterProgram(self, ctx:DecafParser.ProgramContext):
        pass # print("pase por enterProgram",ctx)

    # Exit a parse tree produced by DecafParser#program.
    def exitProgram(self, ctx:DecafParser.ProgramContext):
        pass # print("pase por exitProgram",ctx)


    # Enter a parse tree produced by DecafParser#declaration.
    def enterDeclaration(self, ctx:DecafParser.DeclarationContext):
        pass # print("pase por enterDeclaration",ctx)

    # Exit a parse tree produced by DecafParser#declaration.
    def exitDeclaration(self, ctx:DecafParser.DeclarationContext):
        pass # print("pase por exitDeclaration",ctx)


    # Enter a parse tree produced by DecafParser#varDeclaration.
    def enterVarDeclaration(self, ctx:DecafParser.VarDeclarationContext):
        pass # print("pase por enterVarDeclaration",ctx)

    # Exit a parse tree produced by DecafParser#varDeclaration.
    def exitVarDeclaration(self, ctx:DecafParser.VarDeclarationContext):
        pass # print("pase por exitVarDeclaration",ctx)


    # Enter a parse tree produced by DecafParser#structDeclaration.
    def enterStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
        pass # print("pase por enterStructDeclaration",ctx)

    # Exit a parse tree produced by DecafParser#structDeclaration.
    def exitStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
        pass # print("pase por exitStructDeclaration",ctx)


    # Enter a parse tree produced by DecafParser#INT_VARTYPE.
    def enterINT_VARTYPE(self, ctx:DecafParser.INT_VARTYPEContext):
        pass # print("pase por enterINT_VARTYPE",ctx)

    # Exit a parse tree produced by DecafParser#INT_VARTYPE.
    def exitINT_VARTYPE(self, ctx:DecafParser.INT_VARTYPEContext):
        pass # print("pase por exitINT_VARTYPE",ctx)


    # Enter a parse tree produced by DecafParser#CHAR_VARTYPE.
    def enterCHAR_VARTYPE(self, ctx:DecafParser.CHAR_VARTYPEContext):
        pass # print("pase por",ctx)

    # Exit a parse tree produced by DecafParser#CHAR_VARTYPE.
    def exitCHAR_VARTYPE(self, ctx:DecafParser.CHAR_VARTYPEContext):
        pass # print("pase por",ctx)


    # Enter a parse tree produced by DecafParser#BOOL_VARTYPE.
    def enterBOOL_VARTYPE(self, ctx:DecafParser.BOOL_VARTYPEContext):
        pass # print("pase por",ctx)

    # Exit a parse tree produced by DecafParser#BOOL_VARTYPE.
    def exitBOOL_VARTYPE(self, ctx:DecafParser.BOOL_VARTYPEContext):
        pass # print("pase por",ctx)


    # Enter a parse tree produced by DecafParser#STRUCT_VARTYPE.
    def enterSTRUCT_VARTYPE(self, ctx:DecafParser.STRUCT_VARTYPEContext):
        pass # print("pase por enterSTRUCT_VARTYPE",ctx)

    # Exit a parse tree produced by DecafParser#STRUCT_VARTYPE.
    def exitSTRUCT_VARTYPE(self, ctx:DecafParser.STRUCT_VARTYPEContext):
        pass # print("pase por exitSTRUCT_VARTYPE",ctx)


    # Enter a parse tree produced by DecafParser#STRUCTDECLARATION_VARTYPE.
    def enterSTRUCTDECLARATION_VARTYPE(self, ctx:DecafParser.STRUCTDECLARATION_VARTYPEContext):
        pass # print("pase por enterSTRUCTDECLARATION_VARTYPE",ctx)

    # Exit a parse tree produced by DecafParser#STRUCTDECLARATION_VARTYPE.
    def exitSTRUCTDECLARATION_VARTYPE(self, ctx:DecafParser.STRUCTDECLARATION_VARTYPEContext):
        pass # print("pase por exitSTRUCTDECLARATION_VARTYPE",ctx)


    # Enter a parse tree produced by DecafParser#VOID_VARTYPE.
    def enterVOID_VARTYPE(self, ctx:DecafParser.VOID_VARTYPEContext):
        pass # print("pase por enterVOID_VARTYPE",ctx)

    # Exit a parse tree produced by DecafParser#VOID_VARTYPE.
    def exitVOID_VARTYPE(self, ctx:DecafParser.VOID_VARTYPEContext):
        pass # print("pase por exitVOID_VARTYPE",ctx)


    # Enter a parse tree produced by DecafParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        pass # print("pase por enterMethodDeclaration",ctx)

    # Exit a parse tree produced by DecafParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        pass # print("pase por exitMethodDeclaration",ctx)


    # Enter a parse tree produced by DecafParser#INT_METHODTYPE.
    def enterINT_METHODTYPE(self, ctx:DecafParser.INT_METHODTYPEContext):
        pass # print("pase por enterINT_METHODTYPE",ctx)

    # Exit a parse tree produced by DecafParser#INT_METHODTYPE.
    def exitINT_METHODTYPE(self, ctx:DecafParser.INT_METHODTYPEContext):
        pass # print("pase por exitINT_METHODTYPE",ctx)


    # Enter a parse tree produced by DecafParser#CHAR_METHODTYPE.
    def enterCHAR_METHODTYPE(self, ctx:DecafParser.CHAR_METHODTYPEContext):
        pass # print("pase por enterCHAR_METHODTYPE",ctx)

    # Exit a parse tree produced by DecafParser#CHAR_METHODTYPE.
    def exitCHAR_METHODTYPE(self, ctx:DecafParser.CHAR_METHODTYPEContext):
        pass # print("pase por exitCHAR_METHODTYPE",ctx)


    # Enter a parse tree produced by DecafParser#BOOL_METHODTYPE.
    def enterBOOL_METHODTYPE(self, ctx:DecafParser.BOOL_METHODTYPEContext):
        pass # print("pase por enterBOOL_METHODTYPE",ctx)

    # Exit a parse tree produced by DecafParser#BOOL_METHODTYPE.
    def exitBOOL_METHODTYPE(self, ctx:DecafParser.BOOL_METHODTYPEContext):
        pass # print("pase por",ctx)


    # Enter a parse tree produced by DecafParser#VOID_METHODTYPE.
    def enterVOID_METHODTYPE(self, ctx:DecafParser.VOID_METHODTYPEContext):
        pass # print("pase por enterVOID_METHODTYPE",ctx)

    # Exit a parse tree produced by DecafParser#VOID_METHODTYPE.
    def exitVOID_METHODTYPE(self, ctx:DecafParser.VOID_METHODTYPEContext):
        pass # print("pase por exitVOID_METHODTYPE",ctx)


    # Enter a parse tree produced by DecafParser#parameter.
    def enterParameter(self, ctx:DecafParser.ParameterContext):
        pass # print("pase por enterParameter",ctx)

    # Exit a parse tree produced by DecafParser#parameter.
    def exitParameter(self, ctx:DecafParser.ParameterContext):
        pass # print("pase por exitParameter",ctx)


    # Enter a parse tree produced by DecafParser#parameterType.
    def enterParameterType(self, ctx:DecafParser.ParameterTypeContext):
        pass # print("pase por enterParameterType",ctx)

    # Exit a parse tree produced by DecafParser#parameterType.
    def exitParameterType(self, ctx:DecafParser.ParameterTypeContext):
        pass # print("pase por exitParameterType",ctx)


    # Enter a parse tree produced by DecafParser#block.
    def enterBlock(self, ctx:DecafParser.BlockContext):
        pass # print("pase por enterBlock",ctx)

    # Exit a parse tree produced by DecafParser#block.
    def exitBlock(self, ctx:DecafParser.BlockContext):
        pass # print("pase por exitBlock",ctx)


    # Enter a parse tree produced by DecafParser#StatementIF.
    def enterStatementIF(self, ctx:DecafParser.StatementIFContext):
        pass # print("pase por enterStatementIF",ctx)

    # Exit a parse tree produced by DecafParser#StatementIF.
    def exitStatementIF(self, ctx:DecafParser.StatementIFContext):
        pass # print("pase por exitStatementIF",ctx)


    # Enter a parse tree produced by DecafParser#StatementWHILE.
    def enterStatementWHILE(self, ctx:DecafParser.StatementWHILEContext):
        pass # print("pase por enterStatementWHILE",ctx)

    # Exit a parse tree produced by DecafParser#StatementWHILE.
    def exitStatementWHILE(self, ctx:DecafParser.StatementWHILEContext):
        pass # print("pase por enterStatementWHILE",ctx)


    # Enter a parse tree produced by DecafParser#StatementRETURN.
    def enterStatementRETURN(self, ctx:DecafParser.StatementRETURNContext):
        pass # print("pase por enterStatementRETURN",ctx)

    # Exit a parse tree produced by DecafParser#StatementRETURN.
    def exitStatementRETURN(self, ctx:DecafParser.StatementRETURNContext):
        pass # print("pase por exitStatementRETURN",ctx)


    # Enter a parse tree produced by DecafParser#StatementMETHODCALL.
    def enterStatementMETHODCALL(self, ctx:DecafParser.StatementMETHODCALLContext):
        pass # print("pase por enterStatementMETHODCALL",ctx)

    # Exit a parse tree produced by DecafParser#StatementMETHODCALL.
    def exitStatementMETHODCALL(self, ctx:DecafParser.StatementMETHODCALLContext):
        pass # print("pase por exitStatementMETHODCALL",ctx)


    # Enter a parse tree produced by DecafParser#StatementBLOCK.
    def enterStatementBLOCK(self, ctx:DecafParser.StatementBLOCKContext):
        pass # print("pase por enterStatementBLOCK",ctx)

    # Exit a parse tree produced by DecafParser#StatementBLOCK.
    def exitStatementBLOCK(self, ctx:DecafParser.StatementBLOCKContext):
        pass # print("pase por exitStatementBLOCK ",ctx)


    # Enter a parse tree produced by DecafParser#StatementLOCATION.
    def enterStatementLOCATION(self, ctx:DecafParser.StatementLOCATIONContext):
        pass # print("pase por enterStatementLOCATION",ctx)

    # Exit a parse tree produced by DecafParser#StatementLOCATION.
    def exitStatementLOCATION(self, ctx:DecafParser.StatementLOCATIONContext):
        pass # print("pase por exitStatementLOCATION",ctx)


    # Enter a parse tree produced by DecafParser#StatementEXPRESSION.
    def enterStatementEXPRESSION(self, ctx:DecafParser.StatementEXPRESSIONContext):
        pass # print("pase por enterStatementEXPRESSION",ctx)

    # Exit a parse tree produced by DecafParser#StatementEXPRESSION.
    def exitStatementEXPRESSION(self, ctx:DecafParser.StatementEXPRESSIONContext):
        pass # print("pase por exitStatementEXPRESSION",ctx)


    # Enter a parse tree produced by DecafParser#location.
    def enterLocation(self, ctx:DecafParser.LocationContext):
        pass # print("pase por enterLocation",ctx)

    # Exit a parse tree produced by DecafParser#location.
    def exitLocation(self, ctx:DecafParser.LocationContext):
        pass # print("pase por exitLocation",ctx)


    # Enter a parse tree produced by DecafParser#expr_literal.
    def enterExpr_literal(self, ctx:DecafParser.Expr_literalContext):
        pass # print("pase por enterExpr_literal",ctx)

    # Exit a parse tree produced by DecafParser#expr_literal.
    def exitExpr_literal(self, ctx:DecafParser.Expr_literalContext):
        pass # print("pase por exitExpr_literal",ctx)


    # Enter a parse tree produced by DecafParser#expr_loc.
    def enterExpr_loc(self, ctx:DecafParser.Expr_locContext):
        pass # print("pase por enterExpr_loc",ctx)

    # Exit a parse tree produced by DecafParser#expr_loc.
    def exitExpr_loc(self, ctx:DecafParser.Expr_locContext):
        pass # print("pase por exitExpr_loc",ctx)


    # Enter a parse tree produced by DecafParser#expr_parenthesis.
    def enterExpr_parenthesis(self, ctx:DecafParser.Expr_parenthesisContext):
        pass # print("pase por enterExpr_parenthesis",ctx)

    # Exit a parse tree produced by DecafParser#expr_parenthesis.
    def exitExpr_parenthesis(self, ctx:DecafParser.Expr_parenthesisContext):
        pass # print("pase por exitExpr_parenthesis",ctx)


    # Enter a parse tree produced by DecafParser#expr_mcall.
    def enterExpr_mcall(self, ctx:DecafParser.Expr_mcallContext):
        pass # print("pase por enterExpr_mcall",ctx)

    # Exit a parse tree produced by DecafParser#expr_mcall.
    def exitExpr_mcall(self, ctx:DecafParser.Expr_mcallContext):
        pass # print("pase por exitExpr_mcall",ctx)


    # Enter a parse tree produced by DecafParser#expr_minus.
    def enterExpr_minus(self, ctx:DecafParser.Expr_minusContext):
        pass # print("pase por enterExpr_minus",ctx)

    # Exit a parse tree produced by DecafParser#expr_minus.
    def exitExpr_minus(self, ctx:DecafParser.Expr_minusContext):
        pass # print("pase por exitExpr_minus",ctx)


    # Enter a parse tree produced by DecafParser#expr_arith1.
    def enterExpr_arith1(self, ctx:DecafParser.Expr_arith1Context):
        pass # print("pase por enterExpr_arith1",ctx)

    # Exit a parse tree produced by DecafParser#expr_arith1.
    def exitExpr_arith1(self, ctx:DecafParser.Expr_arith1Context):
        pass # print("pase por exitExpr_arith1",ctx)


    # Enter a parse tree produced by DecafParser#expr_arith2.
    def enterExpr_arith2(self, ctx:DecafParser.Expr_arith2Context):
        pass # print("pase por enterExpr_arith2",ctx)

    # Exit a parse tree produced by DecafParser#expr_arith2.
    def exitExpr_arith2(self, ctx:DecafParser.Expr_arith2Context):
        pass # print("pase por exitExpr_arith2",ctx)


    # Enter a parse tree produced by DecafParser#expr_not.
    def enterExpr_not(self, ctx:DecafParser.Expr_notContext):
        pass # print("pase por enterExpr_not",ctx)

    # Exit a parse tree produced by DecafParser#expr_not.
    def exitExpr_not(self, ctx:DecafParser.Expr_notContext):
        pass # print("pase por exitExpr_not",ctx)


    # Enter a parse tree produced by DecafParser#expr_arith3.
    def enterExpr_arith3(self, ctx:DecafParser.Expr_arith3Context):
        pass # print("pase por enterExpr_arith3",ctx)

    # Exit a parse tree produced by DecafParser#expr_arith3.
    def exitExpr_arith3(self, ctx:DecafParser.Expr_arith3Context):
        pass # print("pase por exitExpr_arith3",ctx)


    # Enter a parse tree produced by DecafParser#expr_arith4.
    def enterExpr_arith4(self, ctx:DecafParser.Expr_arith4Context):
        pass # print("pase por enterExpr_arith4",ctx)

    # Exit a parse tree produced by DecafParser#expr_arith4.
    def exitExpr_arith4(self, ctx:DecafParser.Expr_arith4Context):
        pass # print("pase por exitExpr_arith4",ctx)


    # Enter a parse tree produced by DecafParser#expr_arith5.
    def enterExpr_arith5(self, ctx:DecafParser.Expr_arith5Context):
        pass # print("pase por enterExpr_arith5",ctx)

    # Exit a parse tree produced by DecafParser#expr_arith5.
    def exitExpr_arith5(self, ctx:DecafParser.Expr_arith5Context):
        pass # print("pase por enterExpr_arith5",ctx)


    # Enter a parse tree produced by DecafParser#methodCall.
    def enterMethodCall(self, ctx:DecafParser.MethodCallContext):
        pass # print("pase por enterMethodCall",ctx)

    # Exit a parse tree produced by DecafParser#methodCall.
    def exitMethodCall(self, ctx:DecafParser.MethodCallContext):
        pass # print("pase por exitMethodCall",ctx)


    # Enter a parse tree produced by DecafParser#rel_op.
    def enterRel_op(self, ctx:DecafParser.Rel_opContext):
        pass # print("pase por enterRel_op",ctx)

    # Exit a parse tree produced by DecafParser#rel_op.
    def exitRel_op(self, ctx:DecafParser.Rel_opContext):
        pass # print("pase por enterRel_op",ctx)


    # Enter a parse tree produced by DecafParser#eq_op.
    def enterEq_op(self, ctx:DecafParser.Eq_opContext):
        pass # print("pase por enterEq_op",ctx)

    # Exit a parse tree produced by DecafParser#eq_op.
    def exitEq_op(self, ctx:DecafParser.Eq_opContext):
        pass # print("pase por exitEq_op",ctx)


    # Enter a parse tree produced by DecafParser#arith_op_fifth.
    def enterArith_op_fifth(self, ctx:DecafParser.Arith_op_fifthContext):
        pass # print("pase por enterArith_op_fifth",ctx)

    # Exit a parse tree produced by DecafParser#arith_op_fifth.
    def exitArith_op_fifth(self, ctx:DecafParser.Arith_op_fifthContext):
        pass # print("pase por exitArith_op_fifth",ctx)


    # Enter a parse tree produced by DecafParser#arith_op_fourth.
    def enterArith_op_fourth(self, ctx:DecafParser.Arith_op_fourthContext):
        pass # print("pase por enterArith_op_fourth",ctx)

    # Exit a parse tree produced by DecafParser#arith_op_fourth.
    def exitArith_op_fourth(self, ctx:DecafParser.Arith_op_fourthContext):
        pass # print("pase por exitArith_op_fourth",ctx)


    # Enter a parse tree produced by DecafParser#arith_op_third.
    def enterArith_op_third(self, ctx:DecafParser.Arith_op_thirdContext):
        pass # print("pase por enterArith_op_third",ctx)

    # Exit a parse tree produced by DecafParser#arith_op_third.
    def exitArith_op_third(self, ctx:DecafParser.Arith_op_thirdContext):
        pass # print("pase por exitArith_op_third",ctx)


    # Enter a parse tree produced by DecafParser#arith_op_second.
    def enterArith_op_second(self, ctx:DecafParser.Arith_op_secondContext):
        pass # print("pase por enterArith_op_second",ctx)

    # Exit a parse tree produced by DecafParser#arith_op_second.
    def exitArith_op_second(self, ctx:DecafParser.Arith_op_secondContext):
        pass # print("pase por exitArith_op_second",ctx)


    # Enter a parse tree produced by DecafParser#arith_op_first.
    def enterArith_op_first(self, ctx:DecafParser.Arith_op_firstContext):
        pass # print("pase por enterArith_op_first",ctx)

    # Exit a parse tree produced by DecafParser#arith_op_first.
    def exitArith_op_first(self, ctx:DecafParser.Arith_op_firstContext):
        pass # print("pase por exitArith_op_first",ctx)


    # Enter a parse tree produced by DecafParser#literal.
    def enterLiteral(self, ctx:DecafParser.LiteralContext):
        pass # print("pase por enterLiteral",ctx)

    # Exit a parse tree produced by DecafParser#literal.
    def exitLiteral(self, ctx:DecafParser.LiteralContext):
        pass # print("pase por exitLiteral",ctx)


    # Enter a parse tree produced by DecafParser#int_literal.
    def enterInt_literal(self, ctx:DecafParser.Int_literalContext):
        pass # print("pase por enterInt_literal",ctx)

    # Exit a parse tree produced by DecafParser#int_literal.
    def exitInt_literal(self, ctx:DecafParser.Int_literalContext):
        pass # print("pase por exitInt_literal",ctx)


    # Enter a parse tree produced by DecafParser#char_literal.
    def enterChar_literal(self, ctx:DecafParser.Char_literalContext):
        pass # print("pase por",ctx)

    # Exit a parse tree produced by DecafParser#char_literal.
    def exitChar_literal(self, ctx:DecafParser.Char_literalContext):
        pass # print("pase por",ctx)


    # Enter a parse tree produced by DecafParser#bool_literal.
    def enterBool_literal(self, ctx:DecafParser.Bool_literalContext):
        pass # print("pase por",ctx)

    # Exit a parse tree produced by DecafParser#bool_literal.
    def exitBool_literal(self, ctx:DecafParser.Bool_literalContext):
        pass # print("pase por",ctx)



del DecafParser