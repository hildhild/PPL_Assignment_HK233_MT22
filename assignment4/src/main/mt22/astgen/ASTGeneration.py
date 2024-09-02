# Student ID: 2113481

from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program: list_declared EOF;
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return Program(self.visit(ctx.list_declared()))


    # list_declared:  declared list_declared |  declared;
    def visitList_declared(self, ctx:MT22Parser.List_declaredContext):
        if ctx.list_declared():
            return self.visit(ctx.declared()) + self.visit(ctx.list_declared())
        return self.visit(ctx.declared())


    # declared: function | variable;
    def visitDeclared(self, ctx:MT22Parser.DeclaredContext):
        if ctx.function():
            return [self.visit(ctx.function())]
        return self.visit(ctx.variable())


    # atomic_type: BOOLEAN | INTEGER | FLOAT | STRING;
    def visitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        else:
            return StringType()


    # array_type: ARRAY LSB dimensions RSB OF atomic_type;
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return ArrayType(self.visit(ctx.dimensions()), self.visit(ctx.atomic_type()))


    # dimensions: INT_LIT | INT_LIT COMMA dimensions;
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        if ctx.dimensions():
            return [int(ctx.INT_LIT().getText())] + self.visit(ctx.dimensions())
        return [int(ctx.INT_LIT().getText())]


    # void_type: VOID;
    def visitVoid_type(self, ctx:MT22Parser.Void_typeContext):
        return VoidType()


    # auto_type: AUTO;
    def visitAuto_type(self, ctx:MT22Parser.Auto_typeContext):
        return AutoType()


    # var_type: atomic_type | array_type | auto_type;
    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        if ctx.atomic_type():
            return self.visit(ctx.atomic_type())
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        else:
            return self.visit(ctx.auto_type())


    # func_type: var_type | void_type;
    def visitFunc_type(self, ctx:MT22Parser.Func_typeContext):
        if ctx.var_type():
            return self.visit(ctx.var_type())
        else:
            return self.visit(ctx.void_type())
        

    # variable returns[n] @init {$n = 0}: list_id COLON var_type (ASSIGN (exp ({ $list_id.text.count(',') > $n }? COMMA exp {$n += 1})*) { $list_id.text.count(',') == $n }?)? SEMI;
    def visitVariable(self, ctx:MT22Parser.VariableContext):
        list_id = self.visit(ctx.list_id())
        result = []
        for i in range(0, len(list_id)):
            if ctx.ASSIGN():
                result += [VarDecl(list_id[i], self.visit(ctx.var_type()), self.visit(ctx.exp()[i]))]
            else:
                result += [VarDecl(list_id[i], self.visit(ctx.var_type()), None)]
        return result    


    # list_id: ID | ID COMMA list_id;
    def visitList_id(self, ctx:MT22Parser.List_idContext):
        if ctx.list_id():
            return [ctx.ID().getText()] + self.visit(ctx.list_id())
        else:
            return [ctx.ID().getText()]


    # parameter: INHERIT? OUT? ID COLON var_type;
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return ParamDecl(ctx.ID().getText(), self.visit(ctx.var_type()), True if ctx.OUT() else False, True if ctx.INHERIT() else False)


    # function: ID COLON FUNCTION func_type LP list_param? RP (INHERIT ID)? block_stmt;
    def visitFunction(self, ctx:MT22Parser.FunctionContext):
        return FuncDecl(ctx.ID()[0].getText(), self.visit(ctx.func_type()), self.visit(ctx.list_param()) if ctx.list_param() else [], ctx.ID()[1].getText() if ctx.INHERIT() else None, self.visit(ctx.block_stmt())) 


    # list_param: parameter COMMA list_param | parameter;
    def visitList_param(self, ctx:MT22Parser.List_paramContext):
        if ctx.list_param():
            return [self.visit(ctx.parameter())] + self.visit(ctx.list_param())
        return [self.visit(ctx.parameter())] 


    # exp: exp0 (CONCAT) exp0 | exp0;
    def visitExp(self, ctx:MT22Parser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp0()[0])
        op = ctx.CONCAT().getText()
        left = self.visit(ctx.exp0()[0])
        right = self.visit(ctx.exp0()[1])
        return BinExpr(op, left, right)

    # exp0: exp1 (EQUAL | DIFF | LT | GT | LTE | GTE) exp1 | exp1;
    def visitExp0(self, ctx:MT22Parser.Exp0Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1()[0])
        op = ''
        if ctx.EQUAL():
            op = ctx.EQUAL().getText()
        elif ctx.DIFF():
            op = ctx.DIFF().getText()
        elif ctx.LT():
            op = ctx.LT().getText()
        elif ctx.GT():
            op = ctx.GT().getText()
        elif ctx.LTE():
            op = ctx.LTE().getText()
        elif ctx.GTE():
            op = ctx.GTE().getText()
        left = self.visit(ctx.exp1()[0])
        right = self.visit(ctx.exp1()[1])
        return BinExpr(op, left, right)


    # exp1: exp1 (AND | OR) exp2 | exp2;
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2())
        op = ''
        if ctx.AND():
            op = ctx.AND().getText()
        elif ctx.OR():
            op = ctx.OR().getText()
        left = self.visit(ctx.exp1())
        right = self.visit(ctx.exp2())
        return BinExpr(op, left, right)


    # exp2: exp2 (ADD | SUB) exp3 | exp3;
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        op = ''
        if ctx.ADD():
            op = ctx.ADD().getText()
        elif ctx.SUB():
            op = ctx.SUB().getText()
        left = self.visit(ctx.exp2())
        right = self.visit(ctx.exp3())
        return BinExpr(op, left, right)


    # exp3: exp3 (MUL | DIV | MOD) exp4 | exp4;
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        op = ''
        if ctx.MUL():
            op = ctx.MUL().getText()
        elif ctx.DIV():
            op = ctx.DIV().getText()
        elif ctx.MOD():
            op = ctx.MOD().getText()
        left = self.visit(ctx.exp3())
        right = self.visit(ctx.exp4())
        return BinExpr(op, left, right)

    # exp4: NOT exp4 | exp5;
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        op = ctx.NOT().getText()
        operand = self.visit(ctx.exp4())
        return UnExpr(op, operand)


    # exp5: SUB exp5 | exp6; 
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        op = ctx.SUB().getText()
        operand = self.visit(ctx.exp5())
        return UnExpr(op, operand)


    # exp6: ID LSB list_exp RSB | operand; 
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operand())
        elif ctx.ID():
            return ArrayCell(ctx.ID().getText(),self.visit(ctx.list_exp()))


    # list_exp: exp COMMA list_exp | exp;
    def visitList_exp(self, ctx:MT22Parser.List_expContext):
        if ctx.list_exp():
            return [self.visit(ctx.exp())] + self.visit(ctx.list_exp())
        return [self.visit(ctx.exp())]


    # operand: ID | literal | LP exp RP | func_call; 
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        elif ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.ID():
            return Id(ctx.ID().getText())


    # literal: INT_LIT | FLOAT_LIT | STR_LIT | TRUE | FALSE | arr_lit;
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        if ctx.INT_LIT():
            return IntegerLit(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            float_lit = ctx.FLOAT_LIT().getText()
            if len(float_lit) >= 3:
                if float_lit[0] == '.':
                    float_lit = '0' + float_lit
                    return FloatLit(float(float_lit))
            return FloatLit(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STR_LIT():
            return StringLit(ctx.STR_LIT().getText())
        elif ctx.TRUE():
            return BooleanLit(True)
        elif ctx.FALSE():
            return BooleanLit(False)
        return ArrayLit(self.visit(ctx.arr_lit()))


    # arr_lit: LCB list_exp? RCB; 
    def visitArr_lit(self, ctx:MT22Parser.Arr_litContext):
        if ctx.list_exp():
            return self.visit(ctx.list_exp())
        else:
            return []


    # func_call: ID LP list_exp? RP;
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        if ctx.list_exp():
            return FuncCall(ctx.ID().getText(), self.visit(ctx.list_exp()))
        return FuncCall(ctx.ID().getText(), [])


    # stmt: 
	# assign_stmt
	# | if_stmt
	# | for_stmt 
	# | while_stmt
	# | do_while_stmt
	# | break_stmt
	# | continue_stmt
	# | return_stmt
	# | call_stmt 
	# | block_stmt;
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        if ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        elif ctx.do_while_stmt():
            return self.visit(ctx.do_while_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.call_stmt():
            return self.visit(ctx.call_stmt())
        return self.visit(ctx.block_stmt())


    # assign_stmt: lhs ASSIGN exp SEMI;
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.exp()))


    # lhs: ID | index_exp;
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if ctx.index_exp():
            return self.visit(ctx.index_exp())
        return Id(ctx.ID().getText())


    # index_exp: ID LSB list_exp RSB;
    def visitIndex_exp(self, ctx:MT22Parser.Index_expContext):
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.list_exp()))


    # if_stmt: IF LP exp RP stmt (ELSE stmt)?;
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return IfStmt(self.visit(ctx.exp()), self.visit(ctx.stmt()[0]), self.visit(ctx.stmt()[1]) if ctx.ELSE() else None)


    # for_stmt: FOR LP lhs ASSIGN exp COMMA exp COMMA exp RP stmt;
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return ForStmt(AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.exp()[0])), self.visit(ctx.exp()[1]), self.visit(ctx.exp()[2]), self.visit(ctx.stmt()))


    # while_stmt: WHILE LP exp RP stmt;
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return WhileStmt(self.visit(ctx.exp()), self.visit(ctx.stmt()))


    # do_while_stmt: DO block_stmt WHILE LP exp RP SEMI;
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return DoWhileStmt(self.visit(ctx.exp()), self.visit(ctx.block_stmt()))


    # break_stmt: BREAK SEMI;
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return BreakStmt()


    # continue_stmt: CONTINUE SEMI;
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return ContinueStmt()


    # return_stmt: RETURN exp? SEMI;
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        if ctx.exp():
            return ReturnStmt(self.visit(ctx.exp()))
        return ReturnStmt(None)


    # call_stmt: ID LP list_exp? RP SEMI;
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        if ctx.list_exp():
            return CallStmt(ctx.ID().getText(), self.visit(ctx.list_exp()))
        return CallStmt(ctx.ID().getText(), [])


    # block_stmt: LCB list_block_component RCB;
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return BlockStmt(self.visit(ctx.list_block_component()))


    # block_component: stmt | variable;
    def visitBlock_component(self, ctx:MT22Parser.Block_componentContext):
        if ctx.stmt():
            return [self.visit(ctx.stmt())]
        else:
            return self.visit(ctx.variable())


    # list_block_component: block_component list_block_component | ;
    def visitList_block_component(self, ctx:MT22Parser.List_block_componentContext):
        if ctx.list_block_component():
            return self.visit(ctx.block_component()) + self.visit(ctx.list_block_component())
        return []