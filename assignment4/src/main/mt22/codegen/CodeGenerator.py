# Student ID: 2113481

from Emitter import Emitter
from functools import reduce
from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self, name, mtype, value=None, value_init=None, inherit=None, out=None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.value_init = value_init
        self.inherit = inherit
        self.out = out

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) +"," + str(self.value) +"," + str(self.value_init) + "," + str(self.inherit) + ")"

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
                Symbol("readInteger", MType(list(), IntegerType()), CName(self.libName)),
                Symbol("readFloat", MType(list(), FloatType()), CName(self.libName)),
                Symbol("readBoolean", MType(list(), BooleanType()), CName(self.libName)),
                Symbol("readString", MType(list(), StringType()), CName(self.libName)),
                Symbol("printInteger", MType([IntegerType()],VoidType()), CName(self.libName)),
                Symbol("writeFloat", MType([FloatType()],VoidType()), CName(self.libName)),
                Symbol("printBoolean", MType([BooleanType()],VoidType()), CName(self.libName)),
                Symbol("printString", MType([StringType()],VoidType()), CName(self.libName)),
            ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]
        
        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int
        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String
        self.value = value
        
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None

class FirstVisit(Visitor):
    def __init__(self, astTree, env):
        self.astTree = astTree
        self.env = env
        self.className = "MT22Class"

    def visitProgram(self, astTree, o):
        env = SubBody(None, self.env)
        for onedecl in astTree.decls:
            if type(onedecl) is FuncDecl:
                env = self.visit(onedecl, env)
        self.env = env
        return o

    def visitFuncDecl(self, astTree, o):
        o.sym = [Symbol(astTree.name, MType([(x.typ,x.name,x.inherit,x.out) for x in astTree.params], astTree.return_type), CName(self.className), None, astTree.inherit)] + o.sym
        return SubBody(None, o.sym)
    
class CodeGenVisitor(Visitor):
    def __init__(self, astTree, env, path):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File
        
        self.astTree = astTree
        self.env = env
        self.className = "MT22Class"
        self.path = path
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        
    def defaultValue(self, inType): #khởi tạo giá trị mặc định
        if type(inType) in [IntegerType]:
            return IntegerLit(0)
        elif type(inType) in [FloatType]: 
            return FloatLit(0.0)
        elif type(inType) in [BooleanType]: 
            return BooleanLit(False)
        elif type(inType) in [StringType]: 
            return StringLit("")
        elif type(inType) in [ArrayType]: 
            expr = []
            if len(inType.dimensions) == 1:
                for x in range(inType.dimensions[0]):
                    expr += [self.defaultValue(inType.typ)]
                return ArrayLit(expr)
            else:
                dimen = inType.dimensions
                for x in range(dimen[0]):
                    temp = self.defaultValue(ArrayType(dimen[1:], inType.typ))
                    expr += [temp]
                return ArrayLit(expr)
        
    def visitProgram(self, astTree, o):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        premenv = FirstVisit(self.astTree, self.env)
        premenv.visit(self.astTree, self.env)
        env = SubBody(None, premenv.env.sym)
        for onedecl in astTree.decls:
            env = self.visit(onedecl, env)
        # generate default constructor___
        self.genMETHOD(FuncDecl("<init>", None, list(), None, BlockStmt([])), o, Frame("<init>", VoidType))
        self.genMETHOD(FuncDecl("<clinit>", None, list(), None, BlockStmt([])), env, Frame("<clinit>", VoidType))
        self.emit.emitEPILOG()
        return o

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame
        isInit = consdecl.name == "<init>"
        isClinit = consdecl.name == "<clinit>"
        isMain = str(consdecl.name) == "main" and len(consdecl.params) == 0 and type(consdecl.return_type) in [VoidType]
        return_type = VoidType() if (isInit or isClinit) else consdecl.return_type
        methodName = "<init>" if isInit else consdecl.name
        intype = [ArrayType([0], StringType())] if isMain else list(map(lambda x: x.typ, consdecl.params))
        mtype = MType(intype, return_type)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))
        frame.enterScope(True)
        glovalEnv = o

        # Generate code for other-declarations
        if isInit == True:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isClinit == True:
            for globalVar in o.sym:
                if hasattr(globalVar.mtype, "rettype"): 
                    continue # skip
                init = globalVar.value_init if globalVar.value_init else self.defaultValue(globalVar.mtype)
                initCodeValue, initTypeValue = self.visit(init, Access(frame, o.sym, False, False)) 
                code = initCodeValue
                code += self.emit.emitI2F(o.frame) if (isinstance(globalVar.mtype, FloatType) and isinstance(initTypeValue, IntegerType)) else ""
                code += self.emit.emitPUTSTATIC(self.className + "." + globalVar.name, globalVar.mtype, frame)
                self.emit.printout(code)
        elif isMain == True:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([0], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            if consdecl.params:
                local = reduce(lambda env, ele: SubBody(frame, [self.visit(ele, env)] + env.sym), consdecl.params, SubBody(frame, []))
                glovalEnv = local.sym + glovalEnv

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statementss
        if isInit == True:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame) + self.emit.emitINVOKESPECIAL(frame))
            
        env = SubBody(frame, glovalEnv)
        retCheck = False
        for oneBodyEle in body.body:
            if type(oneBodyEle) in [VarDecl]:
                env = self.visit(oneBodyEle, env)
            elif type(oneBodyEle) in [ReturnStmt]:
                retCheck = True
                for oneparam in consdecl.params:
                    if oneparam.out:
                        self.visit(AssignStmt(ArrayCell(consdecl.name + "_" + oneparam.name, [IntegerLit(0)]), Id(oneparam.name)), env)
                self.visit(oneBodyEle, env)
            else:
                self.visit(oneBodyEle, env)
        if retCheck == False:
            for oneparam in consdecl.params:
                if oneparam.out:
                    self.visit(AssignStmt(ArrayCell(consdecl.name + "_" + oneparam.name, [IntegerLit(0)]), Id(oneparam.name)), env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(return_type) in [VoidType]:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, astTree, o):
        for oneparam in astTree.params:
            if oneparam.out:
                self.visit(VarDecl(astTree.name+"_"+oneparam.name, ArrayType([1],oneparam.typ), self.defaultValue(ArrayType([1],oneparam.typ))), o)
        o.sym = [Symbol(astTree.name, MType([(oneparam.typ, oneparam.name, oneparam.inherit, oneparam.out) for oneparam in astTree.params], astTree.return_type), CName(self.className), None, astTree.inherit)] + o.sym
        self.genMETHOD(astTree, o.sym, Frame(astTree.name, astTree.return_type))
        return SubBody(None, o.sym)
    
    def visitParamDecl(self, astTree, o):
        curFrame = o.frame
        code = None
        if curFrame:
            index = curFrame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(index, astTree.name.lower(), astTree.typ, curFrame.getStartLabel(), curFrame.getEndLabel(), curFrame))
            code = SubBody(curFrame, [Symbol(astTree.name.lower(), astTree.typ, Index(index), None, astTree.inherit)] + o.sym)
        return code

    def visitVarDecl(self, astTree, o):
        curFrame = o.frame
        code = None
        if curFrame: #local
            index = curFrame.getNewIndex()
            o.sym = [[Symbol(astTree.name, astTree.typ, Index(index))]] + o.sym
            self.emit.printout(self.emit.emitVAR(index, astTree.name, astTree.typ, curFrame.getStartLabel(), curFrame.getEndLabel(), curFrame))
            code = SubBody(curFrame, o.sym)
            if not astTree.init and type(astTree.typ) is ArrayType:
                # self-generate astTree.init from astTree.typ.dimensions
                def genInit(dimensions):
                    if len(dimensions) != 1:
                        return ArrayLit([genInit(dimensions[1:]) for _ in range(int(dimensions[0]))])
                    else:
                        return ArrayLit([self.defaultValue(astTree.typ.typ) for _ in range(int(dimensions[0]))])
                init = genInit(astTree.typ.dimensions)
                self.visit(AssignStmt(Id(astTree.name), init), o)
            if astTree.init:
                self.visit(AssignStmt(Id(astTree.name), astTree.init), o)
        else: #global
            o.sym = [Symbol(astTree.name, astTree.typ, CName(self.className), astTree.init if astTree.init else self.defaultValue(astTree.typ))] + o.sym
            self.emit.printout(self.emit.emitATTRIBUTE(astTree.name, astTree.typ, False, ""))
            code = SubBody(None, o.sym)
        return code
    
    def visitId(self,astTree,o):
        curFrame = o.frame
        sym = None
        for onesym in o.sym:
            if isinstance(onesym, list) == True: # local
                sym = list(filter(lambda x: x.name == astTree.name, onesym))
                if sym == []: 
                    sym = None
                else: 
                    sym = sym[0]
                    break
            elif isinstance(onesym, SubBody) == True: # func params
                sym = list(filter(lambda x: hasattr(x,"name") and x.name == astTree.name, onesym.sym))
                if sym == []: 
                    sym = None
                else: 
                    sym = sym[0]
                    break
            elif hasattr(onesym, "name") and onesym.name == astTree.name:
                sym = onesym
                break
        if sym:
            if not o.isLeft:
                if type(sym.value) in [Index]:
                    return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, curFrame), sym.mtype
                elif type(sym.value) in [CName]:
                    return self.emit.emitGETSTATIC(sym.value.value + "." + sym.name, sym.mtype, curFrame), sym.mtype
            else:
                if type(sym.value) in [Index]:
                    return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, curFrame), sym.mtype
                elif type(sym.value) in [CName]:
                    return self.emit.emitPUTSTATIC(sym.value.value + "." + sym.name, sym.mtype, curFrame), sym.mtype
    
    def visitFuncCall(self, astTree, o):
        newO = o
        curFrame = newO.frame
        nenv = newO.sym
        sym = None
        for onesym in o.sym:
            if isinstance(onesym, SubBody): 
                continue
            if isinstance(onesym, list): # local
                sym = list(filter(lambda x: x.name == astTree.name, onesym))
                if sym == []: 
                    sym = None
                else: 
                    sym = sym[0]
                    break
            elif onesym.name == astTree.name:
                sym = onesym
                break
        className = sym.value.value
        inType = None
        ctype = sym.mtype
        if type(ctype) in [MType]:
            inType = ctype.partype
        in__ = ("", list())
        for index, arg in enumerate(astTree.args):
            str1, typ1 = self.visit(arg, Access(curFrame, nenv, False, True))
            if inType:
                paramType = inType[index] if type(inType[index]) is not tuple else inType[index][0]
                if type(paramType) in [FloatType] and type(typ1) in [IntegerType]:
                    str1 += self.emit.emitI2F(curFrame)
            in__ = (in__[0] + str1, in__[1] + [typ1])
        ccode = in__[0] + self.emit.emitINVOKESTATIC(className + "/" + astTree.name, MType(ctype.partype[0], ctype.rettype) if type(ctype.partype) is tuple else ctype, curFrame)
        for index, parType in enumerate(sym.mtype.partype):
            if(type(parType) is tuple and parType[3]):
                curFrame = o.frame
                ccode += self.visit(ArrayCell(astTree.name + "_" + parType[1], [IntegerLit(0)]), Access(curFrame, o.sym, False))[0]
                ccode += self.visit(astTree.args[index], Access(curFrame, o.sym, True))[0]
        return ccode, ctype
        
    def visitBinExpr(self, astTree, o):
        curFrame = o.frame
        ret_typ, opCode = None, None
        lcode, ltype = self.visit(astTree.left, o)
        rcode, rtype = self.visit(astTree.right, o)
        if type(ltype) in [MType]: 
            ltype = ltype.rettype
        if type(rtype) in [MType]: 
            rtype = rtype.rettype
        if isinstance(ltype, FloatType) or isinstance(rtype, FloatType):
            if type(rtype) in [IntegerType]:
                rcode = rcode + self.emit.emitI2F(curFrame)
            elif type(ltype) in [IntegerType]:
                lcode = lcode + self.emit.emitI2F(curFrame)
            ret_typ = FloatType()
        else:
            ret_typ = ltype
        if astTree.op in ['+','-']:
            opCode = self.emit.emitADDOP(astTree.op, ret_typ, curFrame)
        elif astTree.op in ['*','/']:
            opCode = self.emit.emitMULOP(astTree.op, ret_typ, curFrame)
        elif astTree.op in ['%']:
            opCode = self.emit.emitMOD(curFrame)
        elif astTree.op in ['&&']:
            opCode = self.emit.emitANDOP(curFrame)
        elif astTree.op in ['||']:
            opCode = self.emit.emitOROP(curFrame)
        elif astTree.op in ['::']:
            opCode = self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), curFrame)
        else:
            opCode = self.emit.emitREOP(astTree.op, ret_typ, curFrame)
            ret_typ = BooleanType()
        return lcode + rcode + opCode, ret_typ
    
    def visitUnExpr(self, astTree, o):
        curFrame = o.frame
        oCode, oType = self.visit(astTree.val, o)
        if type(oType) in [MType]: 
            oType = oType.rettype
        if astTree.op in ["!"]:
            oCode += self.emit.emitNOT(oType, curFrame)
            return oCode, oType
        else: 
            oCode += self.emit.emitNEGOP(oType, curFrame)
            return oCode, oType
    
    def visitArrayLit(self, astTree, o):
        curFrame = o.frame
        code = ""
        ele_typ = None
        curFrame.push()
        for i in range(len(astTree.explist)):
            code += self.emit.emitDUP(curFrame)
            code += self.emit.emitPUSHICONST(i, curFrame)
            ele_code, ele_typ = self.visit(astTree.explist[i], o)
            code += ele_code
            code += self.emit.emitASTORE(ele_typ, curFrame)
        curFrame.pop()
        dimensions = [len(astTree.explist)]
        firstElement = astTree.explist[0]
        while(type(firstElement) in [ArrayType]):
            subExplist = firstElement.explist
            dimensions.append(len(subExplist))
            firstElement = subExplist[0]
        code = self.emit.emitARRAYLITERAL(ArrayType(dimensions, ele_typ), curFrame) + code
        return code, ArrayType(dimensions, ele_typ)
    
    def visitArrayCell(self, astTree, o):
        o, expr = (o[0], o[1]) if isinstance(o, tuple) else (o, None)
        curFrame = o.frame
        code, array_type = self.visit(Id(astTree.name), Access(curFrame, o.sym, False, True))
        for i in range(len(astTree.cell) - 1):
            idx_code, _ = self.visit(astTree.cell[i], Access(curFrame, o.sym, False, True))
            code += idx_code
            code += self.emit.emitALOAD(array_type, curFrame)
        # last ele
        idx_code, _ = self.visit(astTree.cell[-1], Access(curFrame, o.sym, False, True))
        if not o.isLeft:
            code += idx_code
            code += self.emit.emitALOAD(array_type.typ, curFrame) 
        else:
            code += idx_code
            code += self.visit(expr, Access(curFrame, o.sym, False, True))[0]
            code += self.emit.emitASTORE(array_type.typ, curFrame)
        return code, array_type.typ
    
    def visitReturnStmt(self, astTree, o):
        curFrame = o.frame
        if astTree.expr:
            expCode, expType = self.visit(astTree.expr, Access(curFrame, o.sym, False, True))
            if type(expType) in [IntegerType] and type(curFrame.returnType) in [FloatType]:
                expCode += self.emit.emitI2F(curFrame)
                expCode += self.emit.emitRETURN(FloatType(), curFrame)
            else:
                expCode += self.emit.emitRETURN(expType, curFrame)
            self.emit.printout(expCode)
            
    def visitAssignStmt(self, astTree, o):
        curFrame = o.frame
        arrCellCode, _ = (self.visit(astTree.lhs, (Access(curFrame, o.sym, True, True), astTree.rhs))) if isinstance(astTree.lhs, ArrayCell) else ("", VoidType())
        if arrCellCode != "":
            self.emit.printout(arrCellCode)
            return o
        rcode, rtype = self.visit(astTree.rhs, Access(curFrame, o.sym, False))
        lcode, ltype = self.visit(astTree.lhs, Access(curFrame, o.sym, True))
        self.emit.printout(rcode)
        if isinstance(rtype, IntegerType) and isinstance(ltype, FloatType):
            self.emit.printout(self.emit.emitI2F(curFrame))
        self.emit.printout(lcode)
        return o
     
    def visitCallStmt(self, astTree, o):
        oNew = o
        curFrame = oNew.frame
        nenv = oNew.sym
        sym = None
        isNotSuper = astTree.name != 'super'
        if astTree.name == "preventDefault": 
            return
        if not isNotSuper: 
            astTree.name = o.sym[1].inherit
        for onesym in o.sym:
            if isinstance(onesym, SubBody): 
                continue
            if isinstance(onesym, list): # local
                sym = list(filter(lambda x: x.name == astTree.name, onesym))
                if sym == []: 
                    sym = None
                else: 
                    sym = sym[0]
                    break
            elif onesym.name == astTree.name:
                sym = onesym
                break
        if not isNotSuper:
            for index, param in enumerate(sym.mtype.partype):
                if param[2]:
                    self.visit(VarDecl(param[1], param[0], astTree.args[index]), o)
        else:
            className = sym.value.value
            inputType = None
            ctype = sym.mtype
            if type(ctype) in [MType]:
                inputType = ctype.partype
            in__ = ("", list())
            for index, arg in enumerate(astTree.args):
                str1, typ1 = self.visit(arg, Access(curFrame, nenv, False, True))
                if inputType:
                    paramtyp = inputType[index] if type(inputType[index]) is not tuple else inputType[index][0]
                    if type(paramtyp) in [FloatType] and type(typ1) in [IntegerType]:
                        str1 = str1 + self.emit.emitI2F(curFrame)
                in__ = (in__[0] + str1, in__[1] + [typ1])
            self.emit.printout(in__[0])
            self.emit.printout(self.emit.emitINVOKESTATIC(className + "/" + astTree.name, ctype, curFrame))
            for index, parType in enumerate(sym.mtype.partype):
                if(type(parType) is tuple and parType[3]):
                    self.visit(AssignStmt(astTree.args[index], ArrayCell(astTree.name + "_" + parType[1], [IntegerLit(0)])), o)
    
    def visitIfStmt(self, astTree, o):
        curFrame =  o.frame
        self.emit.printout(self.visit(astTree.cond, Access(curFrame, o.sym, False, True))[0])
        ifLabel = curFrame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(ifLabel, curFrame))
        self.visit(astTree.tstmt, o)
        if astTree.fstmt is None:
            self.emit.printout(self.emit.emitLABEL(ifLabel, curFrame))
        else:
            elseLabel = curFrame.getNewLabel()
            self.emit.printout(self.emit.emitGOTO(elseLabel, curFrame))
            self.emit.printout(self.emit.emitLABEL(ifLabel, curFrame))
            self.visit(astTree.fstmt, o)
            self.emit.printout(self.emit.emitLABEL(elseLabel, curFrame))
            
    def visitForStmt(self, astTree, o):
        curFrame = o.frame
        self.visit(astTree.init, o)
        curFrame.enterLoop()
        continueLabel = curFrame.getContinueLabel()
        breakLabel = curFrame.getBreakLabel()
        conditionLabel = curFrame.getNewLabel()
        bodyLabel = curFrame.getNewLabel()
        updateLabel = curFrame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(conditionLabel, curFrame))
        self.emit.printout(self.visit(astTree.cond, Access(curFrame, o.sym, False, True))[0])
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, curFrame))
        self.emit.printout(self.emit.emitLABEL(bodyLabel, curFrame))
        self.visit(astTree.stmt, o)
        self.emit.printout(self.emit.emitLABEL(continueLabel, curFrame))
        self.emit.printout(self.emit.emitLABEL(updateLabel, curFrame))
        self.visit(AssignStmt(astTree.init.lhs, astTree.upd), o)
        self.emit.printout(self.emit.emitGOTO(conditionLabel, curFrame))
        self.emit.printout(self.emit.emitLABEL(breakLabel, curFrame))
        curFrame.exitLoop()
    
    def visitWhileStmt(self, astTree, o):
        curFrame = o.frame
        curFrame.enterLoop()
        continueLabel = curFrame.getContinueLabel()
        breakLabel = curFrame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(continueLabel, curFrame))
        self.emit.printout(self.visit(astTree.cond, Access(curFrame, o.sym, False))[0])
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, curFrame))
        self.visit(astTree.stmt, o)
        self.emit.printout(self.emit.emitGOTO(continueLabel, curFrame))
        self.emit.printout(self.emit.emitLABEL(breakLabel, curFrame))
        curFrame.exitLoop()
    
    def visitDoWhileStmt(self, astTree, o):
        curFrame = o.frame
        curFrame.enterLoop()
        continueLabel = curFrame.getContinueLabel()
        breakLabel = curFrame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(continueLabel, curFrame))
        self.visit(astTree.stmt, o)
        self.emit.printout(self.visit(astTree.cond, Access(curFrame, o.sym, False))[0])
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, curFrame))
        self.emit.printout(self.emit.emitGOTO(continueLabel, curFrame))
        self.emit.printout(self.emit.emitLABEL(breakLabel, curFrame))
        curFrame.exitLoop()
    
    def visitContinueStmt(self, astTree, o):
        curFrame = o.frame
        return self.emit.printout(self.emit.emitGOTO(curFrame.getContinueLabel(), curFrame))
    
    def visitBreakStmt(self, astTree, o):
        curFrame = o.frame
        return self.emit.printout(self.emit.emitGOTO(curFrame.getBreakLabel(), curFrame))
    
    def visitBlockStmt(self, astTree, o):
        for onestmt in astTree.body:
            self.visit(onestmt, o)

    def visitIntegerLit(self, astTree, o):
        curFrame = o.frame
        return self.emit.emitPUSHICONST(astTree.val, curFrame), IntegerType()

    def visitFloatLit(self, astTree, o):
        curFrame = o.frame
        return self.emit.emitPUSHFCONST(str(astTree.val), curFrame), FloatType()
    
    def visitBooleanLit(self, astTree, o):
        curFrame = o.frame
        return self.emit.emitPUSHCONST(str(astTree.val), BooleanType(), curFrame), BooleanType()
    
    def visitStringLit(self, astTree, o):
        curFrame = o.frame
        return self.emit.emitPUSHCONST('"' + str(astTree.val) + '"', StringType(), curFrame), StringType()
    