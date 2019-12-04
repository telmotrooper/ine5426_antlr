# Generated from CC20192.g4 by ANTLR 4.7.2
from src.invertNumOrder import invertNumOrder
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CC20192Parser import CC20192Parser
else:
    from CC20192Parser import CC20192Parser

# This class defines a complete listener for a parse tree produced by CC20192Parser.
class CC20192Listener(ParseTreeListener):
    scope = 0

    def newScope(self):
        self.scope += 1
        return self.scope

    # Enter a parse tree produced by CC20192Parser#program.
    def enterProgram(self, ctx:CC20192Parser.ProgramContext):
        pass

    # Exit a parse tree produced by CC20192Parser#program.
    def exitProgram(self, ctx:CC20192Parser.ProgramContext):
        pass


    # Enter a parse tree produced by CC20192Parser#statement1.
    def enterStatement1(self, ctx:CC20192Parser.Statement1Context):
        pass

    # Exit a parse tree produced by CC20192Parser#statement1.
    def exitStatement1(self, ctx:CC20192Parser.Statement1Context):
        pass


    # Enter a parse tree produced by CC20192Parser#funclist.
    def enterFunclist(self, ctx:CC20192Parser.FunclistContext):
        pass

    # Exit a parse tree produced by CC20192Parser#funclist.
    def exitFunclist(self, ctx:CC20192Parser.FunclistContext):
        pass


    # Enter a parse tree produced by CC20192Parser#funclist1.
    def enterFunclist1(self, ctx:CC20192Parser.Funclist1Context):
        pass

    # Exit a parse tree produced by CC20192Parser#funclist1.
    def exitFunclist1(self, ctx:CC20192Parser.Funclist1Context):
        pass


    # Enter a parse tree produced by CC20192Parser#funcdef.
    def enterFuncdef(self, ctx:CC20192Parser.FuncdefContext):
        pass

    # Exit a parse tree produced by CC20192Parser#funcdef.
    def exitFuncdef(self, ctx:CC20192Parser.FuncdefContext):
        pass


    # Enter a parse tree produced by CC20192Parser#paramlist.
    def enterParamlist(self, ctx:CC20192Parser.ParamlistContext):
        pass

    # Exit a parse tree produced by CC20192Parser#paramlist.
    def exitParamlist(self, ctx:CC20192Parser.ParamlistContext):
        pass


    # Enter a parse tree produced by CC20192Parser#statement.
    def enterStatement(self, ctx:CC20192Parser.StatementContext):
        pass

    # Exit a parse tree produced by CC20192Parser#statement.
    def exitStatement(self, ctx:CC20192Parser.StatementContext):
        pass


    # Enter a parse tree produced by CC20192Parser#blockstatement.
    def enterBlockstatement(self, ctx:CC20192Parser.BlockstatementContext):
        pass

    # Exit a parse tree produced by CC20192Parser#blockstatement.
    def exitBlockstatement(self, ctx:CC20192Parser.BlockstatementContext):
        pass


    # Enter a parse tree produced by CC20192Parser#vardecl.
    def enterVardecl(self, ctx:CC20192Parser.VardeclContext):
        vardecl = ctx
        ident, brackets = ctx.children[1], ctx.children[2]

        vardecl.name = ident.getText()

    # Exit a parse tree produced by CC20192Parser#vardecl.
    def exitVardecl(self, ctx:CC20192Parser.VardeclContext):
        vardecl, vartype = ctx, ctx.children[0]
        ident, brackets = ctx.children[1], ctx.children[2]

        if hasattr(brackets, 'type'):
            vardecl.type = invertNumOrder(brackets.type)
        
        # Print them for testing
        # if hasattr(vardecl, 'type'):
        #     print("vardecl.name = " + vardecl.name)
        #     print("vardecl.type = " + vardecl.type)


    # Enter a parse tree produced by CC20192Parser#vartype.
    def enterVartype(self, ctx:CC20192Parser.VartypeContext):
        if type(ctx.parentCtx) == CC20192Parser.VardeclContext:
            brackets = ctx.parentCtx.children[2]
            # brackets.baseType = int | float | string
            brackets.baseType = ctx.children[0].getText()


    # Exit a parse tree produced by CC20192Parser#vartype.
    def exitVartype(self, ctx:CC20192Parser.VartypeContext):
        pass


    # Enter a parse tree produced by CC20192Parser#brackets.
    def enterBrackets(self, ctx:CC20192Parser.BracketsContext):
        if not ctx.children:
            # brackets.type = brackets.baseType
            if hasattr(ctx, 'baseType'):
                ctx.type = ctx.baseType
        else:
            brackets = ctx
            openBracket, intConst = ctx.children[0], ctx.children[1]
            closeBracket, bracketChild = ctx.children[2], ctx.children[3]

            if hasattr(brackets, 'baseType'):
                bracketChild.baseType = "array(" + brackets.baseType + ", " + intConst.getText() + ")"


    # Exit a parse tree produced by CC20192Parser#brackets.
    def exitBrackets(self, ctx:CC20192Parser.BracketsContext):
        if ctx.children:
            brackets, bracketChild = ctx, ctx.children[3]

            if hasattr(bracketChild, 'type'):
                brackets.type = bracketChild.type


    # Enter a parse tree produced by CC20192Parser#atribstat.
    def enterAtribstat(self, ctx:CC20192Parser.AtribstatContext):
        pass

    # Exit a parse tree produced by CC20192Parser#atribstat.
    def exitAtribstat(self, ctx:CC20192Parser.AtribstatContext):
        pass


    # Enter a parse tree produced by CC20192Parser#atribexpress.
    def enterAtribexpress(self, ctx:CC20192Parser.AtribexpressContext):
        pass

    # Exit a parse tree produced by CC20192Parser#atribexpress.
    def exitAtribexpress(self, ctx:CC20192Parser.AtribexpressContext):
        pass


    # Enter a parse tree produced by CC20192Parser#funccal.
    def enterFunccal(self, ctx:CC20192Parser.FunccalContext):
        pass

    # Exit a parse tree produced by CC20192Parser#funccal.
    def exitFunccal(self, ctx:CC20192Parser.FunccalContext):
        pass


    # Enter a parse tree produced by CC20192Parser#paramlistcall.
    def enterParamlistcall(self, ctx:CC20192Parser.ParamlistcallContext):
        pass

    # Exit a parse tree produced by CC20192Parser#paramlistcall.
    def exitParamlistcall(self, ctx:CC20192Parser.ParamlistcallContext):
        pass


    # Enter a parse tree produced by CC20192Parser#printstat.
    def enterPrintstat(self, ctx:CC20192Parser.PrintstatContext):
        pass

    # Exit a parse tree produced by CC20192Parser#printstat.
    def exitPrintstat(self, ctx:CC20192Parser.PrintstatContext):
        pass


    # Enter a parse tree produced by CC20192Parser#readstat.
    def enterReadstat(self, ctx:CC20192Parser.ReadstatContext):
        pass

    # Exit a parse tree produced by CC20192Parser#readstat.
    def exitReadstat(self, ctx:CC20192Parser.ReadstatContext):
        pass


    # Enter a parse tree produced by CC20192Parser#returnstat.
    def enterReturnstat(self, ctx:CC20192Parser.ReturnstatContext):
        pass

    # Exit a parse tree produced by CC20192Parser#returnstat.
    def exitReturnstat(self, ctx:CC20192Parser.ReturnstatContext):
        pass


    # Enter a parse tree produced by CC20192Parser#ifstat.
    def enterIfstat(self, ctx:CC20192Parser.IfstatContext):
        pass

    # Exit a parse tree produced by CC20192Parser#ifstat.
    def exitIfstat(self, ctx:CC20192Parser.IfstatContext):
        pass


    # Enter a parse tree produced by CC20192Parser#elsestat.
    def enterElsestat(self, ctx:CC20192Parser.ElsestatContext):
        pass

    # Exit a parse tree produced by CC20192Parser#elsestat.
    def exitElsestat(self, ctx:CC20192Parser.ElsestatContext):
        pass


    # Enter a parse tree produced by CC20192Parser#forstat.
    def enterForstat(self, ctx:CC20192Parser.ForstatContext):
        pass

    # Exit a parse tree produced by CC20192Parser#forstat.
    def exitForstat(self, ctx:CC20192Parser.ForstatContext):
        pass


    # Enter a parse tree produced by CC20192Parser#statelist.
    def enterStatelist(self, ctx:CC20192Parser.StatelistContext):
        pass

    # Exit a parse tree produced by CC20192Parser#statelist.
    def exitStatelist(self, ctx:CC20192Parser.StatelistContext):
        pass


    # Enter a parse tree produced by CC20192Parser#statelist1.
    def enterStatelist1(self, ctx:CC20192Parser.Statelist1Context):
        pass

    # Exit a parse tree produced by CC20192Parser#statelist1.
    def exitStatelist1(self, ctx:CC20192Parser.Statelist1Context):
        pass


    # Enter a parse tree produced by CC20192Parser#allocexpression.
    def enterAllocexpression(self, ctx:CC20192Parser.AllocexpressionContext):
        pass

    # Exit a parse tree produced by CC20192Parser#allocexpression.
    def exitAllocexpression(self, ctx:CC20192Parser.AllocexpressionContext):
        pass


    # Enter a parse tree produced by CC20192Parser#bracketexpress.
    def enterBracketexpress(self, ctx:CC20192Parser.BracketexpressContext):
        pass

    # Exit a parse tree produced by CC20192Parser#bracketexpress.
    def exitBracketexpress(self, ctx:CC20192Parser.BracketexpressContext):
        pass


    # Enter a parse tree produced by CC20192Parser#bracketexpress1.
    def enterBracketexpress1(self, ctx:CC20192Parser.Bracketexpress1Context):
        pass

    # Exit a parse tree produced by CC20192Parser#bracketexpress1.
    def exitBracketexpress1(self, ctx:CC20192Parser.Bracketexpress1Context):
        pass


    # Enter a parse tree produced by CC20192Parser#expression.
    def enterExpression(self, ctx:CC20192Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by CC20192Parser#expression.
    def exitExpression(self, ctx:CC20192Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by CC20192Parser#expression1.
    def enterExpression1(self, ctx:CC20192Parser.Expression1Context):
        pass

    # Exit a parse tree produced by CC20192Parser#expression1.
    def exitExpression1(self, ctx:CC20192Parser.Expression1Context):
        pass


    # Enter a parse tree produced by CC20192Parser#signal.
    def enterSignal(self, ctx:CC20192Parser.SignalContext):
        pass

    # Exit a parse tree produced by CC20192Parser#signal.
    def exitSignal(self, ctx:CC20192Parser.SignalContext):
        pass


    # Enter a parse tree produced by CC20192Parser#numexpression.
    def enterNumexpression(self, ctx:CC20192Parser.NumexpressionContext):
        pass

    # Exit a parse tree produced by CC20192Parser#numexpression.
    def exitNumexpression(self, ctx:CC20192Parser.NumexpressionContext):
        pass


    # Enter a parse tree produced by CC20192Parser#arithmetic1.
    def enterArithmetic1(self, ctx:CC20192Parser.Arithmetic1Context):
        pass

    # Exit a parse tree produced by CC20192Parser#arithmetic1.
    def exitArithmetic1(self, ctx:CC20192Parser.Arithmetic1Context):
        pass


    # Enter a parse tree produced by CC20192Parser#arithsignal1.
    def enterArithsignal1(self, ctx:CC20192Parser.Arithsignal1Context):
        pass

    # Exit a parse tree produced by CC20192Parser#arithsignal1.
    def exitArithsignal1(self, ctx:CC20192Parser.Arithsignal1Context):
        pass


    # Enter a parse tree produced by CC20192Parser#term.
    def enterTerm(self, ctx:CC20192Parser.TermContext):
        pass

    # Exit a parse tree produced by CC20192Parser#term.
    def exitTerm(self, ctx:CC20192Parser.TermContext):
        pass


    # Enter a parse tree produced by CC20192Parser#arithmetic2.
    def enterArithmetic2(self, ctx:CC20192Parser.Arithmetic2Context):
        pass

    # Exit a parse tree produced by CC20192Parser#arithmetic2.
    def exitArithmetic2(self, ctx:CC20192Parser.Arithmetic2Context):
        pass


    # Enter a parse tree produced by CC20192Parser#arithsignal2.
    def enterArithsignal2(self, ctx:CC20192Parser.Arithsignal2Context):
        pass

    # Exit a parse tree produced by CC20192Parser#arithsignal2.
    def exitArithsignal2(self, ctx:CC20192Parser.Arithsignal2Context):
        pass


    # Enter a parse tree produced by CC20192Parser#unaryexpr.
    def enterUnaryexpr(self, ctx:CC20192Parser.UnaryexprContext):
        pass

    # Exit a parse tree produced by CC20192Parser#unaryexpr.
    def exitUnaryexpr(self, ctx:CC20192Parser.UnaryexprContext):
        pass


    # Enter a parse tree produced by CC20192Parser#arithsignal3.
    def enterArithsignal3(self, ctx:CC20192Parser.Arithsignal3Context):
        pass

    # Exit a parse tree produced by CC20192Parser#arithsignal3.
    def exitArithsignal3(self, ctx:CC20192Parser.Arithsignal3Context):
        pass


    # Enter a parse tree produced by CC20192Parser#factor.
    def enterFactor(self, ctx:CC20192Parser.FactorContext):
        pass

    # Exit a parse tree produced by CC20192Parser#factor.
    def exitFactor(self, ctx:CC20192Parser.FactorContext):
        pass


    # Enter a parse tree produced by CC20192Parser#lvalue.
    def enterLvalue(self, ctx:CC20192Parser.LvalueContext):
        pass

    # Exit a parse tree produced by CC20192Parser#lvalue.
    def exitLvalue(self, ctx:CC20192Parser.LvalueContext):
        pass


