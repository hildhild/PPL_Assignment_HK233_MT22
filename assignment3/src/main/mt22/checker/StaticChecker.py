#Student ID: 2113481

from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *

''' 
    o = [Scope(0),Scope(1),...,GlobalScope]
    Scope(i) = {
        name1: Symbol1,
        name2: Symbol2,
        ...
        nameN: SymbolN
        }
    Symbol is VarSymbol, ParamSymbol or FuncSymbol
'''

class Symbol:
    pass

class VarSymbol(Symbol):
    def __init__(self, name = "", typ = None):
        self.name = name
        self.typ = typ

class ParamSymbol(Symbol):
    def __init__(self, name = "", typ = None, out = False, inherit = False, funcName = ""):
        self.name = name
        self.typ = typ
        self.out = out
        self.inherit = inherit
        self.funcName = funcName
        
class FuncSymbol(Symbol):
    def __init__(self, name = "", typ = None, param = [], parentFunc = None):
        self.name = name
        self.typ = typ
        self.param = param #list cac ParamSymBol
        self.parentFunc = parentFunc

class ArraySymbol(Type):
    # elementList: List[Type] Type là ParamSymbol, FuncSymbol (có typ = auto) hoặc là ArraySymbol
    def __init__(self, elementList):
        self.elementList = elementList
        
class FirstVisit(Visitor):
    # First Visit: Only get function decls - Do not throw any exceptions
    def __init__(self, ast):
        self.ast = ast
        
    def visitProgram(self, ast, o): 
        allFunc = {
            "readInteger" : FuncSymbol("readInteger", IntegerType(), []),
            "readFloat" : FuncSymbol("readFloat", FloatType(), []),
            "readBoolean" : FuncSymbol("readBoolean", BooleanType(), []),
            "readString" : FuncSymbol("readString", StringType(), []),
            "printInteger" : FuncSymbol("printInteger", VoidType(), [ParamSymbol(typ=IntegerType(), funcName="printInteger")]),
            "printString" : FuncSymbol("printString", VoidType(), [ParamSymbol(typ=StringType(), funcName="printString")]),
            "writeFloat" : FuncSymbol("writeFloat", VoidType(), [ParamSymbol(typ=FloatType(), funcName="writeFloat")]),
            "printBoolean" : FuncSymbol("printBoolean", VoidType(), [ParamSymbol(typ=BooleanType(), funcName="printBoolean")]),
            "preventDefault" : FuncSymbol("preventDefault", VoidType(), []), 
            "super" : FuncSymbol("super", VoidType(), []) 
        }
        
        for onedecl in ast.decls:
            self.visit(onedecl, allFunc)
            
        return allFunc #Chi tra ve cac funcDecl chua cac param của no

    def visitVarDecl(self, ast, o):
        pass

    def visitParamDecl(self, ast, o):
        pass
    
    def visitFuncDecl(self, ast, o):
        paramList = []
        for oneparam in ast.params:
            paramList += [ParamSymbol(oneparam.name, oneparam.typ, oneparam.out, oneparam.inherit, ast.name)]
        o[ast.name] = FuncSymbol(ast.name, ast.return_type, paramList, ast.inherit)
    
class StaticChecker(Visitor):
    def __init__(self,ast):
        self.ast = ast
        self.numLoopIn = 0 #so vong for dang vao
        self.function = None #ham hien tai
        self.parentFunction = None #ham cha cua ham hien tai (Neu co)
        self.inheritParam = {} #dict cac param ke thua tu cha
        self.funcList = {} #dict tat ca cac ham
        self.checkFirstStmt = False #check invalid first statement
        self.inferForCurFunc = False #co suy dien kieu cho self.function khong - dung khi suy dien kieu cua return
        self.checkReturnType = False #co check kieu cua return type khong (chi check tat ca trong stmt con ben ngoai check lan dau)
        self.returnInsideStmt = False 
        self.checkParamInherit = False
    
    def check(self):
        self.visit(self.ast, None)
        return None
    
    def arrayTypeCmp(self, ltyp, rtyp):
        if not self.typeCmp(ltyp.typ, rtyp.typ):
            return False
        elif type(ltyp.typ) is ArrayType:
            return self.arrayTypeCmp(ltyp.typ, rtyp.typ) and ltyp.dimensions == rtyp.dimensions
        return ltyp.dimensions == rtyp.dimensions
    
    def typeCmp(self, ltyp, rtyp):
        if type(ltyp) is ArrayType and type(rtyp) is ArrayType:
            return self.arrayTypeCmp(ltyp, rtyp)
        elif type(ltyp) == type(rtyp) or (type(ltyp) is FloatType and type(rtyp) is IntegerType):
            return True
        return False   
    
    def listTypeCmp(self, listtyp1, listtyp2):
        if len(listtyp1) != len(listtyp2):
            return False   
        for typ1, typ2 in zip(listtyp1, listtyp2):
            if not self.typeCmp(typ1, typ2):
                return False
        return True

    def inferVar(self, scope_list, idname, typ, raiseAst = None): #dung cho var auto - suy kieu typ cho idname
        for oneScope in scope_list:
            if oneScope.get(idname):
                if type(oneScope[idname].typ) is AutoType or self.typeCmp(oneScope[idname].typ, typ):
                    oneScope[idname].typ = typ
                    return typ
                else:
                    raise TypeMismatchInExpression(raiseAst)
     
    def inferParam(self, scope_list, idname, typ, funcName, raiseAst = None): #dung cho param - suy kieu typ cho idname
        if self.funcList.get(funcName):
            for oneparam in self.funcList[funcName].param:
                if oneparam.name == idname:
                    if type(oneparam.typ) is AutoType or self.typeCmp(oneparam.typ, typ):
                        oneparam.typ = typ
                        break
        if self.inheritParam.get(idname) and self.function.name == funcName:
            if type(self.inheritParam[idname].typ) is AutoType or self.typeCmp(self.inheritParam[idname].typ, typ):
                self.inheritParam[idname].typ = typ
        for oneScope in scope_list:
            if oneScope.get(idname):
                if type(oneScope[idname]) is ParamSymbol:
                    if type(oneScope[idname].typ) is AutoType or self.typeCmp(oneScope[idname].typ, typ):
                        oneScope[idname].typ = typ
                        return typ
                    else:
                        raise TypeMismatchInExpression(raiseAst)
                
    def inferFunc(self, scope_list, idname, typ, raiseAst = None): #dung cho func - suy kieu typ cho idname
        if self.inferForCurFunc and (type(self.function.typ) is AutoType or self.typeCmp(self.function.typ, typ)):
            self.function.typ = typ
        if self.funcList.get(idname):
            if type(self.funcList[idname].typ) is AutoType or self.typeCmp(self.funcList[idname].typ, typ):
                self.funcList[idname].typ = typ
        for oneScope in scope_list:
            if oneScope.get(idname):
                if type(oneScope[idname].typ) is AutoType or self.typeCmp(oneScope[idname].typ, typ):
                    oneScope[idname].typ = typ
                    return typ
                else:
                    raise TypeMismatchInExpression(raiseAst)
    
    def inferArray(self, typeArray, typeArraySymbol, typeArraySymbolAst, o, forSubExpr): #dung cho arr lit
        if typeArray.dimensions[0] != len(typeArraySymbol.elementList):
            if forSubExpr:
                raise TypeMismatchInExpression(typeArraySymbolAst)
            else:
                return False
        if len(typeArray.dimensions) == 1:
            for element in typeArraySymbol.elementList:
                if type(element.typ) is AutoType:
                    if type(element) is FuncSymbol:
                        self.inferFunc(o, element.name, typeArray.typ, typeArraySymbolAst)
                    elif type(element) is ParamSymbol:
                        self.inferParam(o, element.name, typeArray.typ, element.funcName, typeArraySymbolAst)
                    elif type(element) is VarSymbol:
                        self.inferVar(o, element.name, typeArray.typ, typeArraySymbolAst)
                elif type(element) is ArraySymbol:
                    return False
            return True
        else:
            for element in typeArraySymbol.elementList:
                if type(element.typ) is AutoType:
                    if type(element) is FuncSymbol:
                        element.typ = self.inferFunc(o, element.name, ArrayType(typeArray.dimensions[1:], typeArray.typ), typeArraySymbolAst)
                    elif type(element) is ParamSymbol:
                        element.typ = self.inferParam(o, element.name, ArrayType(typeArray.dimensions[1:], typeArray.typ), element.funcName, typeArraySymbolAst)
                    elif type(element) is VarSymbol:
                        element.typ = self.inferVar(o, element.name, ArrayType(typeArray.dimensions[1:], typeArray.typ), typeArraySymbolAst)
                elif type(element) is ArraySymbol:
                    if not self.inferArray(ArrayType(typeArray.dimensions[1:], typeArray.typ), element, typeArraySymbolAst, o, True):
                        return False
            return True
    
    def inferTypeForExpr(self, ast, ltyp, last, rtyp, rast, o):
        if type(ltyp) is ArrayType and type(rtyp) is ArraySymbol:
            if self.inferArray(ltyp, rtyp, rast, o, True):
                return ltyp
            else:
                raise TypeMismatchInExpression(ast)
        elif type(ltyp) in [ParamSymbol, FuncSymbol, VarSymbol] and not (type(rtyp) in [AutoType, FuncSymbol, ParamSymbol, VarSymbol]):
            if type(ltyp) is FuncSymbol:
                self.inferFunc(o, ltyp.name, rtyp, rast)
            elif type(ltyp) is VarSymbol:
                self.inferVar(o, ltyp.name, rtyp, rast)
            else:
                self.inferParam(o, ltyp.name, rtyp, ltyp.funcName, rast)
        elif type(rtyp) in [ParamSymbol, FuncSymbol, VarSymbol] and not (type(ltyp) in [AutoType, FuncSymbol, ParamSymbol, VarSymbol]):
            if type(rtyp) is FuncSymbol:
                self.inferFunc(o, rtyp.name, ltyp, last)
            elif type(rtyp) is VarSymbol:
                self.inferVar(o, rtyp.name, ltyp, last)
            else:
                self.inferParam(o, rtyp.name, ltyp, rtyp.funcName, last)
                
        elif not (type(ltyp) in [AutoType, FuncSymbol, ParamSymbol, VarSymbol]) and not (type(rtyp) in [AutoType, FuncSymbol, ParamSymbol, VarSymbol]):
            if self.typeCmp(ltyp, rtyp):
                return ltyp
            else:
                raise TypeMismatchInExpression(ast)

    def inferTypeForStmtOrVardecl(self, ast, ltyp, last, rtyp, rast, o):
        if type(ltyp) is ArrayType and type(rtyp) is ArraySymbol:
            if self.inferArray(ltyp, rtyp, rast, o, False):
                return ltyp
            elif type(ast) is VarDecl:
                raise TypeMismatchInVarDecl(ast)
            else:   
                raise TypeMismatchInStatement(ast)
        elif type(ltyp) in [ParamSymbol, FuncSymbol, VarSymbol] and not (type(rtyp) in [AutoType, FuncSymbol, ParamSymbol, VarSymbol]):
            if type(ltyp) is FuncSymbol:
                self.inferFunc(o, ltyp.name, rtyp, rast)
            elif type(ltyp) is ParamSymbol:
                self.inferParam(o, ltyp.name, rtyp, ltyp.funcName, rast)
            else:
                self.inferVar(o, ltyp.name, rtyp, rast)
                
        elif type(rtyp) in [ParamSymbol, FuncSymbol, VarSymbol] and not (type(ltyp) in [AutoType, FuncSymbol, ParamSymbol, VarSymbol]):
            if type(rtyp) is FuncSymbol:
                self.inferFunc(o, rtyp.name, ltyp, last)
            elif type(rtyp) is VarSymbol:
                self.inferVar(o, rtyp.name, ltyp, last)
            else:
                self.inferParam(o, rtyp.name, ltyp, rtyp.funcName, last)
        elif not (type(ltyp) in [AutoType, FuncSymbol, ParamSymbol, VarSymbol]) and not (type(rtyp) in [AutoType, FuncSymbol, ParamSymbol, VarSymbol]):
            if self.typeCmp(ltyp, rtyp):
                return ltyp
            elif type(ast) is VarDecl:
                raise TypeMismatchInVarDecl(ast)
            else:   
                raise TypeMismatchInStatement(ast)
                
    def visitProgram(self, ast, o):
        # Preliminary, no need to check for errors
        self.funcList = FirstVisit(ast).visit(ast, o)
        
        # Round 2 - Detailed Visit
        oNew = [{}]
        for onedecl in ast.decls:
            self.visit(onedecl, oNew)
            
        # Finally, check for Entry Point
        if not self.funcList.get("main"):
            raise NoEntryPoint()
        if type(self.funcList["main"]) is not FuncSymbol:
            raise NoEntryPoint()
        if len(self.funcList["main"].param) != 0:
            raise NoEntryPoint()
        if type(self.funcList["main"].typ) is not VoidType:
            raise NoEntryPoint()
        
    def visitVarDecl(self, ast, o):
        # Check if existed - at the same scope
        if o[0].get(ast.name) or self.inheritParam.get(ast.name):
            raise Redeclared(Variable(), ast.name)
        
        # Auto Type and Without Init
        if type(ast.typ) is AutoType and not ast.init:
            raise Invalid(Variable(), ast.name) 

        o[0][ast.name] = VarSymbol(ast.name, ast.typ) 
        
        # With Init - Inference
        if ast.init: 
            rtype = self.visit(ast.init, o)
            ltype = ast.typ
            if type(ltype) is not AutoType:
                self.inferTypeForStmtOrVardecl(ast, ltype, ast, rtype, ast.init, o)
            else:
                o[0][ast.name].typ = rtype
    
    def visitParamDecl(self, ast, o):
        if self.checkParamInherit:
            if self.inheritParam.get(ast.name):
                raise Invalid(Parameter(), ast.name)
        else:    
            # Check if existed - at the same scope
            if o[0].get(ast.name):
                raise Redeclared(Parameter(), ast.name)
            #Check if invalid:
            # if self.inheritParam.get(ast.name):
            #     raise Invalid(Parameter(), ast.name)
            # o[0][ast.name] = ParamSymbol(ast.name, ast.typ, ast.out, ast.inherit, self.function.name) 
            for oneparam in self.funcList[self.function.name].param:
                if oneparam.name == ast.name:
                    o[0][ast.name] = oneparam
    
    def visitFuncDecl(self, ast, o):
        self.inheritParam = {}
        oNew = [{}] + o
        if o[0].get(ast.name):
            raise Redeclared(Function(), ast.name)
        else:
            if ast.inherit:
                if not self.funcList.get(ast.inherit):
                    raise Undeclared(Function(),ast.inherit)
                else:
                    self.parentFunction = self.funcList[ast.inherit]
                    for oneparam in self.funcList[ast.inherit].param:
                        if oneparam.inherit:
                            if self.inheritParam.get(oneparam.name):
                                raise Redeclared(Parameter(), oneparam.name)
                            self.inheritParam[oneparam.name] = oneparam
            else: 
                self.inheritParam = {}
                self.parentFunction = None
            if self.funcList.get(ast.name):
                paramList = self.funcList[ast.name].param
            o[0][ast.name] = FuncSymbol(ast.name, ast.return_type, paramList, ast.inherit)
        
        self.function = o[0][ast.name]
        
        for item in ast.params:
            self.visit(item, oNew)
        
        self.checkParamInherit = True
        for item in ast.params:
            self.visit(item, oNew)
        self.checkParamInherit = False
        
        
        if ast.inherit is not None:
            self.checkFirstStmt = True
        self.checkReturnType = True
        self.visit(ast.body, oNew)
        return
          
    def visitId(self, ast, o):
        for oneScope in o:
            if oneScope.get(ast.name):
                if type(oneScope[ast.name].typ) is AutoType:
                    return oneScope[ast.name]
                else:
                    if type(oneScope[ast.name]) is FuncSymbol:
                        raise Undeclared(Identifier(), ast.name) 
                    return oneScope[ast.name].typ
        if self.inheritParam.get(ast.name):
            if type(self.inheritParam[ast.name].typ) is AutoType:
                return self.inheritParam[ast.name]
            else:
                return self.inheritParam[ast.name].typ
        raise Undeclared(Identifier(), ast.name) 
    
    def visitBinExpr(self, ast, o):
        ltype = self.visit(ast.left, o)
        rtype = self.visit(ast.right, o)
        if (type(ltype) in [ParamSymbol, FuncSymbol, VarSymbol] and not type(rtype) in [AutoType, FuncSymbol, ParamSymbol, VarSymbol]) or (type(rtype) in [ParamSymbol, FuncSymbol, VarSymbol] and not type(ltype) in [AutoType, FuncSymbol, ParamSymbol, VarSymbol]):
            self.inferTypeForExpr(ast, ltype, ast.left, rtype, ast.right, o)
            if type(ltype) in [ParamSymbol, FuncSymbol, VarSymbol] and not type(rtype) in [AutoType, FuncSymbol, ParamSymbol, VarSymbol]:
                ltype = rtype
            else:
                rtype = ltype
            
        if ast.op in ['+','-','*','/']:
            if type(ltype) in [ParamSymbol, FuncSymbol, VarSymbol] and type(rtype) in [ParamSymbol, FuncSymbol, VarSymbol]:
                return IntegerType()
            if not (type(ltype) is IntegerType or type(ltype) is FloatType) or not (type(rtype) is IntegerType or type(rtype) is FloatType):
                raise TypeMismatchInExpression(ast)
            if type(ltype) is IntegerType and type(rtype) is IntegerType:
                return IntegerType() # if op != '/' else FloatType()
            if type(ltype) is FloatType or type(rtype) is FloatType:
                return FloatType()
            
        if ast.op in ['%']:
            if type(ltype) in [ParamSymbol, FuncSymbol, VarSymbol] and type(rtype) in [ParamSymbol, FuncSymbol, VarSymbol]:
                return IntegerType()
            if type(ltype) is IntegerType and type(rtype) is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ['&&','||']:
            if type(ltype) in [ParamSymbol, FuncSymbol, VarSymbol] and type(rtype) in [ParamSymbol, FuncSymbol, VarSymbol]:
                return BooleanType()
            if type(ltype) is BooleanType and type(rtype) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['::']:
            if type(ltype) in [ParamSymbol, FuncSymbol, VarSymbol] and type(rtype) in [ParamSymbol, FuncSymbol, VarSymbol]:
                return StringType()
            if type(ltype) is StringType and type(rtype) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ['<', '>', '<=', '>=']:
            if type(ltype) in [ParamSymbol, FuncSymbol, VarSymbol] and type(rtype) in [ParamSymbol, FuncSymbol, VarSymbol]:
                return BooleanType()
            if not (type(ltype) is IntegerType or type(ltype) is FloatType) or not (type(rtype) is IntegerType or type(rtype) is FloatType):
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        
        if ast.op in ['!=','==']:
            if type(ltype) in [ParamSymbol, FuncSymbol, VarSymbol] and type(rtype) in [ParamSymbol, FuncSymbol, VarSymbol]:
                return BooleanType()
            if not (type(ltype) is IntegerType or type(ltype) is BooleanType) or not (type(rtype) is IntegerType or type(rtype) is BooleanType):
                raise TypeMismatchInExpression(ast)
            return BooleanType()    
        
    def visitUnExpr(self, ast, o):
        vtype = self.visit(ast.val, o)
        
        if ast.op in ['-']:
            if type(vtype) is IntegerType:
                return IntegerType()
            if type(vtype) is FloatType:
                return FloatType()
            if not type(vtype) in [AutoType, FuncSymbol, ParamSymbol, VarSymbol]:
                raise TypeMismatchInExpression(ast)
            return vtype
        
        if ast.op in ['!']:
            if type(vtype) is BooleanType:
                return BooleanType()
            if not type(vtype) in [AutoType, FuncSymbol, ParamSymbol, VarSymbol]:
                raise TypeMismatchInExpression(ast)
            return vtype  
        
    def visitArrayCell(self, ast, o):
        for onescope in o:
            if onescope.get(ast.name):
                arr = onescope[ast.name].typ
                if type(arr) is not ArrayType:
                    raise TypeMismatchInExpression(ast)
                for ele in ast.cell:
                    eleType = self.visit(ele, o)
                    self.inferTypeForExpr(ast, IntegerType(), "", eleType, ele, o)
                if len(arr.dimensions) < len(ast.cell):
                    raise TypeMismatchInExpression(ast)
                elif len(arr.dimensions) == len(ast.cell):
                    return arr.typ
                else:
                    sub = len(arr.dimensions) - len(ast.cell)
                    newSize = arr.dimensions[len(arr.dimensions) - sub:]
                    return ArrayType(newSize, arr.typ)
        raise Undeclared(Identifier(),ast.name)   
        
    def visitFuncCall(self, ast, o):
        argList = [self.visit(onearg, o) for onearg in ast.args] #list cac typ
        if self.funcList.get(ast.name):
            paramList =  [oneparam if (type(oneparam.typ) is AutoType) else oneparam.typ for oneparam in self.funcList[ast.name].param] #list cac typ
            if len(argList) != len(paramList):
                raise TypeMismatchInExpression(ast)
            i = 0
            for onearg, oneparam in zip(argList, paramList):
                self.inferTypeForExpr(ast, oneparam, self.funcList[ast.name].param[i], onearg, ast.args[i], o)
                i+=1
            if self.typeCmp(self.funcList[ast.name].typ, VoidType()):
                raise TypeMismatchInExpression(ast)
            else:
                if type(self.funcList[ast.name].typ) is AutoType:
                    return self.funcList[ast.name]
                else:
                    return self.funcList[ast.name].typ
        else:
            raise Undeclared(Function(), ast.name)
        
    def visitAssignStmt(self, ast, o): #xet phai truoc
        rtype = self.visit(ast.rhs, o)
        ltype = self.visit(ast.lhs, o)
        # if lhs is VoidType/ArrayType
        if type(ltype) is VoidType or type(ltype) is ArrayType:
            raise TypeMismatchInStatement(ast)
        return self.inferTypeForStmtOrVardecl(ast, ltype, ast.lhs, rtype, ast.rhs, o)  

    def visitIfStmt(self, ast, o):
        condTyp = self.visit(ast.cond, o)
        self.inferTypeForStmtOrVardecl(ast, BooleanType(), "", condTyp, ast.cond, o)
        self.checkReturnType = True
        self.returnInsideStmt = True
        self.inheritParam = {}
        self.visit(ast.tstmt, [{}] + o) 
        self.returnInsideStmt = False 
          
        if ast.fstmt is not None:
            self.checkReturnType = True
            self.returnInsideStmt = True
            self.inheritParam = {}
            self.visit(ast.fstmt, [{}] + o) 
            self.returnInsideStmt = False
            
    def visitForStmt(self, ast, o):
        initTyp = self.visit(ast.init, o)
        self.inferTypeForStmtOrVardecl(ast, IntegerType(), "", initTyp, ast.init, o)
        condTyp = self.visit(ast.cond, o)
        self.inferTypeForStmtOrVardecl(ast, BooleanType(), "", condTyp, ast.cond, o)
        updTyp = self.visit(ast.upd, o)
        self.inferTypeForStmtOrVardecl(ast, IntegerType(), "", updTyp, ast.upd, o)
        
        self.checkReturnType = True
        self.returnInsideStmt = True
        self.numLoopIn += 1 
        self.inheritParam = {}
        self.visit(ast.stmt, [{}] + o)
        self.numLoopIn -= 1 
        self.returnInsideStmt = False
        
    def visitWhileStmt(self, ast, o):
        condTyp = self.visit(ast.cond, o)
        self.inferTypeForStmtOrVardecl(ast, BooleanType(), "", condTyp, ast.cond, o)
        
        self.checkReturnType = True
        self.returnInsideStmt = True
        self.numLoopIn += 1 
        self.inheritParam = {}
        self.visit(ast.stmt, [{}] + o)
        self.numLoopIn -= 1 
        self.returnInsideStmt = False
        
    def visitDoWhileStmt(self, ast, o):
        condTyp = self.visit(ast.cond, o)
        self.inferTypeForStmtOrVardecl(ast, BooleanType(), "", condTyp, ast.cond, o)
        
        self.checkReturnType = True
        self.returnInsideStmt = True
        self.numLoopIn += 1 
        self.visit(ast.stmt, o + [{}])
        self.numLoopIn -= 1 
        self.returnInsideStmt = False
        
    def visitBreakStmt(self, ast, o):
        if self.numLoopIn == 0: 
            raise MustInLoop(ast)
        return None
        
    def visitContinueStmt(self, ast, o):
        if self.numLoopIn == 0: 
            raise MustInLoop(ast)
        return None
        
    def visitReturnStmt(self, ast, o):
        if self.checkReturnType:
            self.inferForCurFunc = True
            funcName = self.function.name
            lhs =  self.funcList[funcName] if (type(self.funcList[funcName].typ) is AutoType) else self.funcList[funcName].typ
            rhs = self.visit(ast.expr, o) if ast.expr else VoidType()
            self.inferTypeForStmtOrVardecl(ast, lhs, None, rhs, ast.expr, o)
            self.inferForCurFunc = False
            self.checkReturnType = False
        
    def visitCallStmt(self, ast, o):
        argList = [self.visit(onearg, o) for onearg in ast.args]
        if self.funcList.get(ast.name):
            if ast.name != "super":
                if ast.name == "preventDefault" and not self.parentFunction:
                    raise InvalidStatementInFunction(self.function.name)
                paramList =  [oneparam.typ if type(oneparam.typ) is not AutoType else oneparam for oneparam in self.funcList[ast.name].param]
                if len(argList) != len(paramList):
                    raise TypeMismatchInStatement(ast)
                i = 0
                for onearg, oneparam in zip(argList, paramList):
                    self.inferTypeForStmtOrVardecl(ast, oneparam, self.funcList[ast.name].param[i], onearg, ast.args[i], o)
                    i+=1
                if type(self.funcList[ast.name].typ) is AutoType:
                    self.funcList[ast.name].typ = VoidType()
                    for oneScope in o:
                        if oneScope.get(ast.name):
                            oneScope[ast.name].typ =  VoidType()
                    return self.funcList[ast.name].typ
                # elif not self.typeCmp(self.funcList[ast.name].typ, VoidType()):
                #     raise TypeMismatchInStatement(ast)
                else:
                    if type(self.funcList[ast.name].typ) is AutoType:
                        return self.funcList[ast.name]
                    else:
                        return self.funcList[ast.name].typ
            else:
                if self.parentFunction:
                    paramList =  [oneparam.typ if type(oneparam.typ) is not AutoType else oneparam for oneparam in self.parentFunction.param] 
                    if len(argList) > len(paramList):
                        raise TypeMismatchInExpression(argList[len(paramList)])
                    elif len(argList) < len(paramList):
                        raise TypeMismatchInExpression(None)
                    i = 0
                    for onearg, oneparam in zip(argList, paramList):
                        self.inferTypeForExpr(ast, oneparam, self.parentFunction.param[i], onearg, ast.args[i], o)
                        i+=1
                else:
                    raise InvalidStatementInFunction(self.function.name)
        else:
            raise Undeclared(Function(), ast.name)
            
    def visitBlockStmt(self, ast, o):
        #check first stmt
        if self.checkFirstStmt:
            if len(self.parentFunction.param) != 0:
                if len(ast.body) != 0:
                    if not (hasattr(ast.body[0], 'name')):
                        raise InvalidStatementInFunction(self.function.name)
                    elif not (ast.body[0].name in ['super', 'preventDefault']):
                        raise InvalidStatementInFunction(self.function.name)
                else:
                    raise InvalidStatementInFunction(self.function.name)
                
            self.checkFirstStmt = False
        for onestmt in ast.body: 
            if type(onestmt) is BlockStmt:
                self.inheritParam = {}
                self.visit(onestmt, [{}] + o)   
            else:    
                self.visit(onestmt, o)   
        
    def visitIntegerType(self, ast, o):
        return ast
    
    def visitFloatType(self, ast, o):
        return ast
    
    def visitBooleanType(self, ast, o):
        return ast
    
    def visitStringType(self, ast, o):
        return ast
    
    def visitArrayType(self, ast, o):
        return ast
    
    def visitAutoType(self, ast, o):
        return ast
    
    def visitVoidType(self, ast, o):
        return ast
        
    def visitIntegerLit(self, ast, o):
        return IntegerType()
    
    def visitFloatLit(self, ast, o):
        return FloatType()
    
    def visitStringLit(self, ast, o):
        return StringType()
    
    def visitBooleanLit(self, ast, o):
        return BooleanType()
    
    def visitArrayLit(self, ast, o):
        typ = None
        for item in ast.explist:
            checkTyp = self.visit(item, o)
            if type(checkTyp) in [BooleanType, StringType, IntegerType, FloatType, ArrayType]:
                typ = checkTyp
                break
            
        if typ is None:
            return ArraySymbol([self.visit(item, o) for item in ast.explist])
        elif type(typ) in [BooleanType, StringType, IntegerType, FloatType]:
            for item in ast.explist:
                checkTyp = self.visit(item, o)
                if self.typeCmp(typ, checkTyp):  
                    continue
                elif type(checkTyp) is FuncSymbol:
                    self.inferFunc(o, item.name, typ, item)
                elif type(checkTyp) is ParamSymbol:
                    self.inferParam(o, item.name, typ, self.function.name, item)
                elif type(checkTyp) is VarSymbol:
                    self.inferVar(o, item.name, typ, item)
                else:
                    raise IllegalArrayLiteral(ast)
            return ArrayType([len(ast.explist)], typ)
        else: #ArrayType
            for item in ast.explist:
                checkTyp = self.visit(item, o)
                if self.typeCmp(typ, checkTyp):  
                    continue
                elif type(checkTyp) is FuncSymbol:
                    self.inferFunc(o, item.name, typ, item)
                elif type(checkTyp) is ParamSymbol:
                    self.inferParam(o, item.name, typ, self.function.name, item)
                elif type(checkTyp) is VarSymbol:
                    self.inferVar(o, item.name, typ, item)
                elif type(checkTyp) is ArraySymbol:
                    if self.inferArray(typ, checkTyp, item, o, False):
                        continue
                    else:
                        raise IllegalArrayLiteral(ast) 
                else:
                    raise IllegalArrayLiteral(ast)
            return ArrayType([len(ast.explist)] + typ.dimensions, typ.typ)