# Generated from CC20192.g4 by ANTLR 4.7.2
import sys
from src.invertNumOrder import invertNumOrder
from database import setScope, checkForScopeError, getEntryWithError
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CC20192Parser import CC20192Parser
else:
    from CC20192Parser import CC20192Parser

# This class defines a complete listener for a parse tree produced by CC20192Parser.
class CC20192Listener(ParseTreeListener):
    # Counters
    scope = 0
    register = 0
    label = 0

    def newScope(self):
        self.scope += 1
        return self.scope
    
    def newRegister(self):
        self.register += 1
        return "t" + self.register

    def newLabel(self, name):
        self.label += 1
        return name + "_LABEL"+ self.label

    # Enter a parse tree produced by CC20192Parser#program.
    def enterProgram(self, ctx:CC20192Parser.ProgramContext):
        program, statement1 = ctx, ctx.children[0]
        statement1.scope = self.newScope()
        statement1.loopScope = False
        # GCI
        statement1.next = "STOP"

    # Exit a parse tree produced by CC20192Parser#program.
    def exitProgram(self, ctx:CC20192Parser.ProgramContext):
        program, statement1 = ctx, ctx.children[0]
        # GCI
        program.code = statement1.code + "\nSTOP"
        print("Código intermediário:\n" + program.code)


    # Enter a parse tree produced by CC20192Parser#statement1.
    def enterStatement1(self, ctx:CC20192Parser.Statement1Context):
        statement1 = ctx

        if not ctx.children: # statement1 → ε
            # GCI
            statement1.code = ""
        elif type(ctx.children[0]) == CC20192Parser.FunclistContext:  # statement1 → funclist
            funclist = ctx.children[0]
            funclist.scope = statement1.scope
        elif type(ctx.children[0]) == CC20192Parser.StatementContext: # statement1 → statement
            statement = ctx.children[0]
            statement.loopScope = statement1.loopScope
            statement.scope = statement1.scope
            # GCI
            statement.next = statement1.next

    # Exit a parse tree produced by CC20192Parser#statement1.
    def exitStatement1(self, ctx:CC20192Parser.Statement1Context):
        statement1 = ctx
        if not ctx.children: # statement1 → ε
            pass
        elif type(ctx.children[0]) == CC20192Parser.FunclistContext:  # statement1 → funclist
            funclist = ctx.children[0]
            # GCI
            statement1.code = funclist.code
            pass
        elif type(ctx.children[0]) == CC20192Parser.StatementContext: # statement1 → statement
            # GCI
            statement = ctx.children[0]
            statement1.code = statement.code


    # Enter a parse tree produced by CC20192Parser#funclist.
    def enterFunclist(self, ctx:CC20192Parser.FunclistContext):
        funclist, funcdef = ctx, ctx.children[0]
        funclist1 = ctx.children[1]

        funcdef.scope = self.newScope()
        funclist1.scope = funclist.scope


    # Exit a parse tree produced by CC20192Parser#funclist.
    def exitFunclist(self, ctx:CC20192Parser.FunclistContext):
        funclist, funcdef, funclist1 = ctx, ctx.children[0], ctx.children[1]
        funclist.loopScope = funclist1.loopScope
        # GCI
        funclist.code = funcdef.start + funcdef.code + funclist1.code


    # Enter a parse tree produced by CC20192Parser#funclist1.
    def enterFunclist1(self, ctx:CC20192Parser.Funclist1Context):
        pass

    # Exit a parse tree produced by CC20192Parser#funclist1.
    def exitFunclist1(self, ctx:CC20192Parser.Funclist1Context):
        funclist1 = ctx

        if not ctx.children:  # funclist1 → ε  
            funclist1.loopScope = False
            # GCI
            funclist1.code = ""
        if(ctx.children):     # funclist1 → funclist
            funclist = ctx.children[0]
            funclist1.loopScope = funclist.loopScope
            # GCI
            funclist1.code = funclist.code


    # Enter a parse tree produced by CC20192Parser#funcdef.
    def enterFuncdef(self, ctx:CC20192Parser.FuncdefContext):
        funcdef, Def, ident   = ctx, ctx.children[0], ctx.children[1]
        openpar, paramlist    = ctx.children[2], ctx.children[3]
        closepar, openbrace   = ctx.children[4], ctx.children[5]
        statelist, closebrace = ctx.children[6], ctx.children[7]

        statelist.scope = funcdef.scope
        statelist.loopScope = False
        paramlist.scope = funcdef.scope

        # GCI
        funcdef.start = self.newLabel('FUNCDEF')


    # Exit a parse tree produced by CC20192Parser#funcdef.
    def exitFuncdef(self, ctx:CC20192Parser.FuncdefContext):
        funcdef, Def, ident   = ctx, ctx.children[0], ctx.children[1]
        openpar, paramlist    = ctx.children[2], ctx.children[3]
        closepar, openbrace   = ctx.children[4], ctx.children[5]
        statelist, closebrace = ctx.children[6], ctx.children[7]
        
        # GCI
        funcdef.code = funcdef.start + statelist.code


    # Enter a parse tree produced by CC20192Parser#paramlist.
    def enterParamlist(self, ctx:CC20192Parser.ParamlistContext):
        paramlist = ctx

        if(not ctx.children):         # paramlist → ε
            pass
        elif len(ctx.children) == 4:  # paramlist → vartype IDENT COMMA paramlist
            vartype, ident = ctx.children[0], ctx.children[1]
            comma, paramlistChild = ctx.children[2], ctx.children[3]

            # IDENT.Scope = paramlist.Scope
            setScope(ident.getText(), paramlist.scope)

            paramlistChild.scope = paramlist.scope

        elif len(ctx.children) == 2:  # paramlist → vartype IDENT
            vartype, ident = ctx.children[0], ctx.children[1]
            setScope(ident.getText(), paramlist.scope)


    # Exit a parse tree produced by CC20192Parser#paramlist.
    def exitParamlist(self, ctx:CC20192Parser.ParamlistContext):
        pass


    # Enter a parse tree produced by CC20192Parser#statement.
    def enterStatement(self, ctx:CC20192Parser.StatementContext):
        statement = ctx

        if ctx.children[0].getText() == "break":
            setScope('break', statement.scope)
            Break = ctx.children[0]
            Break.valid = statement.loopScope
            if not Break.valid:
                entry = getEntryWithError('break', statement.scope)
                print(f"ERROR: Invalid break (line {entry[1]}, column {entry[2]})")
                sys.exit()

        elif type(ctx.children[0]) == CC20192Parser.VardeclContext:
            vardecl, semicolon = ctx.children[0], ctx.children[1]
            vardecl.scope = statement.scope
            # GCI
            statement.code = ""

        elif type(ctx.children[0] == CC20192Parser.IfstatContext):
            ifstat = ctx.children[0]
            ifstat.scope = self.newScope()
            ifstat.loopScope = statement.loopScope
            # GCI
            ifstat.next = statement.next

        elif type(ctx.children[0] == CC20192Parser.ForstatContext):
            forstat = ctx.children[0]
            forstat.scope = self.newScope()
            forstat.loopScope = True

        elif type(ctx.children[0] == CC20192Parser.BlockstatementContext):
            blockstatement = ctx.children[0]
            blockstatement.scope = self.newScope()
            blockstatement.loopScope = statement.loopScope

        elif type(ctx.children[0] == CC20192Parser.PrintstatContext):
            printstat = ctx.children[0]
            # GCI
            statement.code = ""

        elif type(ctx.children[0] == CC20192Parser.ReadstatContext):
            readstat = ctx.children[0]
            # GCI
            statement.code = ""
        elif ctx.children[0].getText() == ";":
            pass


    # Exit a parse tree produced by CC20192Parser#statement.
    def exitStatement(self, ctx:CC20192Parser.StatementContext):
        statement = ctx

        if ctx.children[0].getText() == "break":
            statement.code = "go to " + statement.next()
        elif type(ctx.children[0] == CC20192Parser.AtribstatContext):
            atribstat = ctx.children[0]
            # GCI
            statement.code = atribstat.code
        elif type(ctx.children[0] == CC20192Parser.ReturnstatContext):
            returnstat = ctx.children[0]
            # GCI
            statement.code = "go to " + statement.next
        elif type(ctx.children[0] == CC20192Parser.IfstatContext):
            ifstat = ctx.children[0]
            # GCI
            statement.code = ifstat.code
        elif type(ctx.children[0] == CC20192Parser.ForstatContext):
            forstat = ctx.children[0]
            # GCI
            statement.code = forstat.code
        elif type(ctx.children[0] == CC20192Parser.BlockstatementContext):
            blockstatement = ctx.children[0]
            # GCI
            statement.code = blockstatement.code


    # Enter a parse tree produced by CC20192Parser#blockstatement.
    def enterBlockstatement(self, ctx:CC20192Parser.BlockstatementContext):
        blockstatement = ctx
        if len(ctx.children) == 3:  # blockstatement → OPENBRACE statelist CLOSEBRACE
            openbrace, statelist = ctx.children[0], ctx.children[1]
            closebrace = ctx.children[2]

            statelist.scope = blockstatement.scope
            statelist.loopScope = blockstatement.loopScope

    # Exit a parse tree produced by CC20192Parser#blockstatement.
    def exitBlockstatement(self, ctx:CC20192Parser.BlockstatementContext):
        pass


    # Enter a parse tree produced by CC20192Parser#vardecl.
    def enterVardecl(self, ctx:CC20192Parser.VardeclContext):
        vardecl = ctx
        ident, brackets = ctx.children[1], ctx.children[2]

        vardecl.name = ident.getText()
        setScope(ident.getText(), vardecl.scope)

        if checkForScopeError(ident.getText(), vardecl.scope):
            entry = getEntryWithError(ident.getText(), vardecl.scope)
            print(f"ERROR: Name collision in scope (line {entry[1]}, column {entry[2]})")
            sys.exit()

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
        ifstat = ctx

        if len(ctx.children) == 6:
            If, openpar = ctx.children[0], ctx.children[1]
            expression, closepar = ctx.children[2], ctx.children[3]
            blockstatement, elsestat = ctx.children[4], ctx.children[5]

            blockstatement.scope = ifstat.scope
            blockstatement.loopScope = ifstat.loopScope
            elsestat.scope = ifstat.scope
            elsestat.loopScope = ifstat.loopScope


    # Exit a parse tree produced by CC20192Parser#ifstat.
    def exitIfstat(self, ctx:CC20192Parser.IfstatContext):
        pass


    # Enter a parse tree produced by CC20192Parser#elsestat.
    def enterElsestat(self, ctx:CC20192Parser.ElsestatContext):
        elsestat = ctx

        if not ctx.children:
            pass
        elif len(ctx.children) == 2:
            Else, blockstatement = ctx.children[0], ctx.children[1]
            
            blockstatement.scope = elsestat.scope
            blockstatement.loopScope = elsestat.loopScope


    # Exit a parse tree produced by CC20192Parser#elsestat.
    def exitElsestat(self, ctx:CC20192Parser.ElsestatContext):
        pass


    # Enter a parse tree produced by CC20192Parser#forstat.
    def enterForstat(self, ctx:CC20192Parser.ForstatContext):
        forstat = ctx

        if len(ctx.children) == 9:
            For, openpar = ctx.children[0], ctx.children[1]
            atribstat, semicolon = ctx.children[2], ctx.children[3]
            expression, semicolon2 = ctx.children[4], ctx.children[5]
            atribstat2, closepar = ctx.children[6], ctx.children[7]
            statement = ctx.children[8]

            statement.scope = forstat.scope
            statement.loopScope = True

    # Exit a parse tree produced by CC20192Parser#forstat.
    def exitForstat(self, ctx:CC20192Parser.ForstatContext):
        pass


    # Enter a parse tree produced by CC20192Parser#statelist.
    def enterStatelist(self, ctx:CC20192Parser.StatelistContext):
        statelist = ctx

        if len(ctx.children) == 2:
            statement, statelist1 = ctx.children[0], ctx.children[1]

            statement.scope = statelist.scope
            statelist1.scope = statelist.scope
            statement.loopScope = statelist.loopScope
            statelist1.loopScope = statelist.loopScope


    # Exit a parse tree produced by CC20192Parser#statelist.
    def exitStatelist(self, ctx:CC20192Parser.StatelistContext):
        pass


    # Enter a parse tree produced by CC20192Parser#statelist1.
    def enterStatelist1(self, ctx:CC20192Parser.Statelist1Context):
        statelist1 = ctx

        if not ctx.children:
            pass
        elif len(ctx.children) == 1:
            statelist = ctx.children[0]

            statelist.scope = statelist1.scope
            statelist.loopScope = statelist1.loopScope


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


