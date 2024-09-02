import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 400))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 401))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 402))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 403))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 404))
        
    def test_program(self):
        """More complex program"""
        input = """foo: function void (inherit a: integer, inherit out b: float) inherit bar {}"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 405))

    def test_program2(self):
        """More complex program"""
        input = """n: function void (){
            if (a > 1) if (b > 2) return 1; else return 2;
            }"""
        expect = """Program([
	FuncDecl(n, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(1)), IfStmt(BinExpr(>, Id(b), IntegerLit(2)), ReturnStmt(IntegerLit(1)), ReturnStmt(IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 406))
        
    def test_1(self):
        input = """a : array [1] of integer = {};"""
        expect = """Program([
	VarDecl(a, ArrayType([1], IntegerType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_2(self):
        input = """a : array [1] of string = {a[0], True, 1, 1., 2.e3};"""
        expect = """Program([
	VarDecl(a, ArrayType([1], StringType), ArrayLit([ArrayCell(a, [IntegerLit(0)]), Id(True), IntegerLit(1), FloatLit(1.0), FloatLit(2000.0)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_3(self):
        input = """a : string = {};"""
        expect = """Program([
	VarDecl(a, StringType, ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_4(self):
        input = """a : array [1] of boolean = {a[0], true, 1, 1., .e3};"""
        expect = """Program([
	VarDecl(a, ArrayType([1], BooleanType), ArrayLit([ArrayCell(a, [IntegerLit(0)]), BooleanLit(True), IntegerLit(1), FloatLit(1.0), FloatLit(0.0)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_5(self):
        input = """a : integer = {};"""
        expect = """Program([
	VarDecl(a, IntegerType, ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    # Xem lai
    def test_6(self):
        input = """a,b,c : integer = a, foo(), 15;"""
        expect = """Program([
	VarDecl(a, IntegerType, Id(a))
	VarDecl(b, IntegerType, FuncCall(foo, []))
	VarDecl(c, IntegerType, IntegerLit(15))
])""" 
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_7(self):
        input = """a : integer = {{1},foo({1})};"""
        expect = """Program([
	VarDecl(a, IntegerType, ArrayLit([ArrayLit([IntegerLit(1)]), FuncCall(foo, [ArrayLit([IntegerLit(1)])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_8(self):
        input = """a : function void (inherit a : boolean, out b : array [1] of integer) inherit c {return 1;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [InheritParam(a, BooleanType), OutParam(b, ArrayType([1], IntegerType))], c, BlockStmt([ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_9(self):
        input = """a : function void (inherit a : integer, inherit out b : array [1] of float) inherit c {return 1;}"""
        expect = """Program([
	FuncDecl(a, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, ArrayType([1], FloatType))], c, BlockStmt([ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_10(self):
        input = """a : function void (inherit a : integer, out b : array [1] of string) inherit c {}"""
        expect = """Program([
	FuncDecl(a, VoidType, [InheritParam(a, IntegerType), OutParam(b, ArrayType([1], StringType))], c, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_11(self):
        input = """a : function void (inherit a : integer, out b : array [1] of string) inherit c {
                    {
                    }
                    if (a > 2) return;
                }"""
        expect = """Program([
	FuncDecl(a, VoidType, [InheritParam(a, IntegerType), OutParam(b, ArrayType([1], StringType))], c, BlockStmt([BlockStmt([]), IfStmt(BinExpr(>, Id(a), IntegerLit(2)), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_12(self):
        input = """a : function void (inherit a : integer, out b : array [1] of string) inherit c {
                  i : integer = a[5];
                }"""
        expect = """Program([
	FuncDecl(a, VoidType, [InheritParam(a, IntegerType), OutParam(b, ArrayType([1], StringType))], c, BlockStmt([VarDecl(i, IntegerType, ArrayCell(a, [IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_13(self):
        input = """a : function void (inherit a : integer, out b : array [1] of string) inherit c {
                  i : integer = a == (b >= c);
                }"""
        expect = """Program([
	FuncDecl(a, VoidType, [InheritParam(a, IntegerType), OutParam(b, ArrayType([1], StringType))], c, BlockStmt([VarDecl(i, IntegerType, BinExpr(==, Id(a), BinExpr(>=, Id(b), Id(c))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_14(self):
        input = """a : function void (inherit a : integer, out b : array [1] of string) inherit c {
                   a = ((a[10]::{1,2,foo()})+b(0)) ;
                }"""
        expect = """Program([
	FuncDecl(a, VoidType, [InheritParam(a, IntegerType), OutParam(b, ArrayType([1], StringType))], c, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(::, ArrayCell(a, [IntegerLit(10)]), ArrayLit([IntegerLit(1), IntegerLit(2), FuncCall(foo, [])])), FuncCall(b, [IntegerLit(0)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_15(self):
        input = """a : function array [1] of string () inherit c {}"""
        expect = """Program([
	FuncDecl(a, ArrayType([1], StringType), [], c, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_16(self):
        input = """a : array [1] of boolean = {a[a+b, c+d, {},0], true, 1, 1., 10.21e2};"""
        expect = """Program([
	VarDecl(a, ArrayType([1], BooleanType), ArrayLit([ArrayCell(a, [BinExpr(+, Id(a), Id(b)), BinExpr(+, Id(c), Id(d)), ArrayLit([]), IntegerLit(0)]), BooleanLit(True), IntegerLit(1), FloatLit(1.0), FloatLit(1021.0)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_17(self):
        input = """a : function array [1] of string () inherit c { do { return 1; } while ({} == 1);}"""
        expect = """Program([
	FuncDecl(a, ArrayType([1], StringType), [], c, BlockStmt([DoWhileStmt(BinExpr(==, ArrayLit([]), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_18(self):
        input = """a : function array [1] of string () inherit c {do { return foo() + {} ; } while ({} == 1);}"""
        expect = """Program([
	FuncDecl(a, ArrayType([1], StringType), [], c, BlockStmt([DoWhileStmt(BinExpr(==, ArrayLit([]), IntegerLit(1)), BlockStmt([ReturnStmt(BinExpr(+, FuncCall(foo, []), ArrayLit([])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_19(self):
        input = """a : function array [1] of string () inherit c { readInteger(); }"""
        expect = """Program([
	FuncDecl(a, ArrayType([1], StringType), [], c, BlockStmt([CallStmt(readInteger, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_20(self):
        input = """a : integer = {True, true, "true", .e3};"""
        expect = """Program([
	VarDecl(a, IntegerType, ArrayLit([Id(True), BooleanLit(True), StringLit(true), FloatLit(0.0)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_21(self):
        input = """a : function void () { }
a : integer = c;
a : function integer (){
    {
        a : integer;    
    }
    {
        return 1;
    }
    {
    }
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([]))
	VarDecl(a, IntegerType, Id(c))
	FuncDecl(a, IntegerType, [], None, BlockStmt([BlockStmt([VarDecl(a, IntegerType)]), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_22(self):
        input = """a : array [1] of integer = a[1,2,86];"""
        expect = """Program([
	VarDecl(a, ArrayType([1], IntegerType), ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(86)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_23(self):
        input = """a : array [1] of integer = a[1];"""
        expect = """Program([
	VarDecl(a, ArrayType([1], IntegerType), ArrayCell(a, [IntegerLit(1)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_24(self):
        input = """a, b: array [5,5,6] of integer = {a,b,b}, a[1::2];"""
        expect = """Program([
	VarDecl(a, ArrayType([5, 5, 6], IntegerType), ArrayLit([Id(a), Id(b), Id(b)]))
	VarDecl(b, ArrayType([5, 5, 6], IntegerType), ArrayCell(a, [BinExpr(::, IntegerLit(1), IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_25(self):
        input = """a : function void (){
    a[1,2] = a[1,2];
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), ArrayCell(a, [IntegerLit(1), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_26(self):
        input = """a : function void (){
    return a[1];
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_27(self):
        input = """a : function void (){
    a[1] = a[2];
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), ArrayCell(a, [IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_28(self):
        input = """a : function void (){
    a[1] = (a[2,3]);
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), ArrayCell(a, [IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_29(self):
        input = """a : function void (){
    a[1,1] = (a[2,6,7]) + 7;
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(1)]), BinExpr(+, ArrayCell(a, [IntegerLit(2), IntegerLit(6), IntegerLit(7)]), IntegerLit(7)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_30(self):
        input = """a : function void (){
    if (a==(b >= c)) {}
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), BinExpr(>=, Id(b), Id(c))), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_31(self):
        input = """a : function void (){
    if (a==(b >= c)) {} else return {};
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), BinExpr(>=, Id(b), Id(c))), BlockStmt([]), ReturnStmt(ArrayLit([])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_32(self):
        input = """aa : function void (){
    if (a[1,4] == (b >= c)) {}
   
}"""
        expect = """Program([
	FuncDecl(aa, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1), IntegerLit(4)]), BinExpr(>=, Id(b), Id(c))), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_33(self):
        input = """a : function void (){
    for (True = 1, foo(1) >= 2, i -foo()) {}
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(True), IntegerLit(1)), BinExpr(>=, FuncCall(foo, [IntegerLit(1)]), IntegerLit(2)), BinExpr(-, Id(i), FuncCall(foo, [])), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_34(self):
        input = """a : function void (){
    for (a[1] = 1, i >= 2, i -foo()) {}
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(1)]), IntegerLit(1)), BinExpr(>=, Id(i), IntegerLit(2)), BinExpr(-, Id(i), FuncCall(foo, [])), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_35(self):
        input = """a: function integer (inherit out i: integer, i: string) inherit a {
            a[1,a[2]] = {a,a} + a[1,2,{a,a[1]}] + a[2];
        }"""
        expect = """Program([
	FuncDecl(a, IntegerType, [InheritOutParam(i, IntegerType), Param(i, StringType)], a, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), ArrayCell(a, [IntegerLit(2)])]), BinExpr(+, BinExpr(+, ArrayLit([Id(a), Id(a)]), ArrayCell(a, [IntegerLit(1), IntegerLit(2), ArrayLit([Id(a), ArrayCell(a, [IntegerLit(1)])])])), ArrayCell(a, [IntegerLit(2)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_36(self):
        input = """a : function void (){
    for (a[1] = 1, (i :: 2) :: 3 , i -foo()) {}
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(1)]), IntegerLit(1)), BinExpr(::, BinExpr(::, Id(i), IntegerLit(2)), IntegerLit(3)), BinExpr(-, Id(i), FuncCall(foo, [])), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_37(self):
        input = """a : function void (){
    while (i*1) {}
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(*, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_38(self):
        input = """a : function void (){
    do {return 1;} while (a);
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([DoWhileStmt(Id(a), BlockStmt([ReturnStmt(IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_39(self):
        input = """a : function void (){
    do {return 1; break;} while (a);
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([DoWhileStmt(Id(a), BlockStmt([ReturnStmt(IntegerLit(1)), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_40(self):
        input = """a : function void (){
    foo(2+x);
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_41(self):
        input = """a : function void (){
    {
r, s: integer;
r = 2.0;
a, b: array [5] of integer;
s = r * r * myPI;
a[0] = s;
}
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_42(self):
        input = """a : function void (){
    readInteger();
   {
   }
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([CallStmt(readInteger, ), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_43(self):
        input = """a : function void (){
    readInteger();
    writef(a);
    printb(d);
   {
   }
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([CallStmt(readInteger, ), CallStmt(writef, Id(a)), CallStmt(printb, Id(d)), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_44(self):
        input = """a : function void (){
    printInteger(a);
   {
   }
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([CallStmt(printInteger, Id(a)), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_45(self):
        input = """a : function void (){
    printInteger(a);
   {
   }
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([CallStmt(printInteger, Id(a)), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_46(self):
        input = """a : function void (){
    printBoolean(c);
   {
   }
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([CallStmt(printBoolean, Id(c)), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_47(self):
        input = """a : function void (){
    super();
   {
   }
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([CallStmt(super, ), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_48(self):
        input = """a : function void (){
    super({});
   {
   }
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([CallStmt(super, ArrayLit([])), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_49(self):
        input = """a : function void (){
    a : integer = 1;
    continue;
    do {return 1;} while (a > 1);
}
a : function void (){}
"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), ContinueStmt(), DoWhileStmt(BinExpr(>, Id(a), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(1))]))]))
	FuncDecl(a, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_50(self):
        input = """a : function void (){
    call[c] = call(d) :: call[c];
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(call, [Id(c)]), BinExpr(::, FuncCall(call, [Id(d)]), ArrayCell(call, [Id(c)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_51(self):
        input = """foo : boolean = readInter(c,d);"""
        expect = """Program([
	VarDecl(foo, BooleanType, FuncCall(readInter, [Id(c), Id(d)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_52(self):
        input = """foo : boolean = readInteger();"""
        expect = """Program([
	VarDecl(foo, BooleanType, FuncCall(readInteger, []))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_53(self):
        input = """foo : boolean = preventdefault();"""
        expect = """Program([
	VarDecl(foo, BooleanType, FuncCall(preventdefault, []))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_54(self):
        input = """foo : function integer () {
while (a==3) {}
}"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), IntegerLit(3)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_55(self):
        input = """foo : function integer () {
while (a==3) {
    if (a > b) {c : integer = b; return c;}
    else {
        continue;
        break;
        c : integer = b; return c;
    }
}
    {
    c : integer = b; return c;
    }
}
c : integer = b; """
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), IntegerLit(3)), BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([VarDecl(c, IntegerType, Id(b)), ReturnStmt(Id(c))]), BlockStmt([ContinueStmt(), BreakStmt(), VarDecl(c, IntegerType, Id(b)), ReturnStmt(Id(c))]))])), BlockStmt([VarDecl(c, IntegerType, Id(b)), ReturnStmt(Id(c))])]))
	VarDecl(c, IntegerType, Id(b))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_56(self):
        input = """a, b,c : integer;
 foo : function float (a : integer, out c : string) {
   e : integer ;
   e = a + 4 ;
   c = a * d / 2.0 ;
   return c + 1;
}
"""
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(b, IntegerType)
	VarDecl(c, IntegerType)
	FuncDecl(foo, FloatType, [Param(a, IntegerType), OutParam(c, StringType)], None, BlockStmt([VarDecl(e, IntegerType), AssignStmt(Id(e), BinExpr(+, Id(a), IntegerLit(4))), AssignStmt(Id(c), BinExpr(/, BinExpr(*, Id(a), Id(d)), FloatLit(2.0))), ReturnStmt(BinExpr(+, Id(c), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_57(self):
        input = """a: function array [1] of string (a: string) inherit c {
                print();
            }"""
        expect = """Program([
	FuncDecl(a, ArrayType([1], StringType), [Param(a, StringType)], c, BlockStmt([CallStmt(print, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_58(self):
        input = """a: function array [1] of string (a: string) inherit c {
    b : auto;
}"""
        expect = """Program([
	FuncDecl(a, ArrayType([1], StringType), [Param(a, StringType)], c, BlockStmt([VarDecl(b, AutoType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_59(self):
        input = """a, b: array [5,6] of integer;"""
        expect = """Program([
	VarDecl(a, ArrayType([5, 6], IntegerType))
	VarDecl(b, ArrayType([5, 6], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_60(self):
        input = """a: function array [1] of string (a: string) inherit c {
    {//}
    }
}"""
        expect = """Program([
	FuncDecl(a, ArrayType([1], StringType), [Param(a, StringType)], c, BlockStmt([BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_61(self):
        input = """a: function void (a: array [1] of integer) inherit c {
    {//}
        foo(1);
    }
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [Param(a, ArrayType([1], IntegerType))], c, BlockStmt([BlockStmt([CallStmt(foo, IntegerLit(1))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_62(self):
        input = """a: function void (a: array [1] of integer) inherit c {
    {//}
        a[1] = foo(1);
    }
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [Param(a, ArrayType([1], IntegerType))], c, BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), FuncCall(foo, [IntegerLit(1)]))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_63(self):
        input = """a : boolean = "helo";"""
        expect = """Program([
	VarDecl(a, BooleanType, StringLit(helo))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_64(self):
        input = """a,b,c : array [1,4,3] of boolean = "helo",1,2;"""
        expect = """Program([
	VarDecl(a, ArrayType([1, 4, 3], BooleanType), StringLit(helo))
	VarDecl(b, ArrayType([1, 4, 3], BooleanType), IntegerLit(1))
	VarDecl(c, ArrayType([1, 4, 3], BooleanType), IntegerLit(2))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_65(self):
        input = """a,b,c : array [1,4,3] of boolean = "helo",true,false;"""
        expect = """Program([
	VarDecl(a, ArrayType([1, 4, 3], BooleanType), StringLit(helo))
	VarDecl(b, ArrayType([1, 4, 3], BooleanType), BooleanLit(True))
	VarDecl(c, ArrayType([1, 4, 3], BooleanType), BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_66(self):
        input = """a : function void (){
a,b,c : array [1,4,3] of boolean = "helo",true,false;
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([1, 4, 3], BooleanType), StringLit(helo)), VarDecl(b, ArrayType([1, 4, 3], BooleanType), BooleanLit(True)), VarDecl(c, ArrayType([1, 4, 3], BooleanType), BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_67(self):
        input = """a : function void (){
    a[1_2_3] = b;
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(123)]), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_68(self):
        input = """a : function void (){
    a[1_2_3.8,87] = b;
}"""
        expect = """Program([
	FuncDecl(a, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [FloatLit(123.8), IntegerLit(87)]), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_69(self):
        input = """main: function void () {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_70(self):
        input = """a, b, c, d: integer = 3, 4, 6, 7;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(4))
	VarDecl(c, IntegerType, IntegerLit(6))
	VarDecl(d, IntegerType, IntegerLit(7))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_71(self):
        input = """a:function string (){a = a;}"""
        expect = """Program([
	FuncDecl(a, StringType, [], None, BlockStmt([AssignStmt(Id(a), Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_72(self):
        input = """x : auto = 1.0; """
        expect = """Program([
	VarDecl(x, AutoType, FloatLit(1.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_73(self):
        input = """a: function auto (a : boolean) {}"""
        expect = """Program([
	FuncDecl(a, AutoType, [Param(a, BooleanType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_74(self):
        input = """a: boolean;"""
        expect = """Program([
	VarDecl(a, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_75(self):
        input = """        fact: function integer ( fact : integer) {
 
            if (a==2) a=2; else
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) do {for (a=2,a>3,a+1) return 1;} while(a==2);
           {} continue; return _12; {break;}
        }
        a : integer = 1_3_1.;
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(fact, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(2)), AssignStmt(Id(a), IntegerLit(2)), ForStmt(AssignStmt(Id(a), IntegerLit(9123)), FuncCall(foo, [ArrayLit([])]), BinExpr(+, ArrayLit([]), IntegerLit(1122)), DoWhileStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(>, Id(a), IntegerLit(3)), BinExpr(+, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(1)))])))), BlockStmt([]), ContinueStmt(), ReturnStmt(Id(_12)), BlockStmt([BreakStmt()])]))
	VarDecl(a, IntegerType, FloatLit(131.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_76(self):
        input = """        fact: function integer ( a : integer) {
            break;
            if (a==2) a=2; else
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) do {for (a=2,a>3,a+1) return 1;} while(a==2);
           {} continue; return _12; {break;}
        }
        a : integer = 1_3_1.;
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType)], None, BlockStmt([BreakStmt(), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), AssignStmt(Id(a), IntegerLit(2)), ForStmt(AssignStmt(Id(a), IntegerLit(9123)), FuncCall(foo, [ArrayLit([])]), BinExpr(+, ArrayLit([]), IntegerLit(1122)), DoWhileStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(>, Id(a), IntegerLit(3)), BinExpr(+, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(1)))])))), BlockStmt([]), ContinueStmt(), ReturnStmt(Id(_12)), BlockStmt([BreakStmt()])]))
	VarDecl(a, IntegerType, FloatLit(131.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_77(self):
        input = """        fact: function integer ( a : integer) {
            break;
            if (a==2)
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) do {for (a=2,a>3,a+1) return 1;} while(a==2);
           {} continue; return _12; {break;}
        }
        a : integer = 1_3_1.;
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType)], None, BlockStmt([BreakStmt(), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), ForStmt(AssignStmt(Id(a), IntegerLit(9123)), FuncCall(foo, [ArrayLit([])]), BinExpr(+, ArrayLit([]), IntegerLit(1122)), DoWhileStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(>, Id(a), IntegerLit(3)), BinExpr(+, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(1)))])))), BlockStmt([]), ContinueStmt(), ReturnStmt(Id(_12)), BlockStmt([BreakStmt()])]))
	VarDecl(a, IntegerType, FloatLit(131.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_78(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) do {for (a=2,a>3,a+1) return 1;} while(a==2);
           {} continue; return ; {break;}
        }
        a : integer = 1_3_1.;
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType)], None, BlockStmt([BreakStmt(), ForStmt(AssignStmt(Id(a), IntegerLit(9123)), FuncCall(foo, [ArrayLit([])]), BinExpr(+, ArrayLit([]), IntegerLit(1122)), DoWhileStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(>, Id(a), IntegerLit(3)), BinExpr(+, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(1)))]))), BlockStmt([]), ContinueStmt(), ReturnStmt(), BlockStmt([BreakStmt()])]))
	VarDecl(a, IntegerType, FloatLit(131.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_79(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) do {for (a=2,a>3,a+1) return 1;} while(a==2);
           
        }
        a : integer = 1_3_1.;
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType)], None, BlockStmt([BreakStmt(), ForStmt(AssignStmt(Id(a), IntegerLit(9123)), FuncCall(foo, [ArrayLit([])]), BinExpr(+, ArrayLit([]), IntegerLit(1122)), DoWhileStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(>, Id(a), IntegerLit(3)), BinExpr(+, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(1)))])))]))
	VarDecl(a, IntegerType, FloatLit(131.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_80(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) do {for (a=2,a>3,a+1) return 1;} while(a==2);
           
        }
        a : integer = 1_3_1.;
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType)], None, BlockStmt([BreakStmt(), ForStmt(AssignStmt(Id(a), IntegerLit(9123)), FuncCall(foo, [ArrayLit([])]), BinExpr(+, ArrayLit([]), IntegerLit(1122)), DoWhileStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(>, Id(a), IntegerLit(3)), BinExpr(+, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(1)))])))]))
	VarDecl(a, IntegerType, FloatLit(131.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_81(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) return 1_5.;
           
        }
        a : integer = 1_3_1.;
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType)], None, BlockStmt([BreakStmt(), ForStmt(AssignStmt(Id(a), IntegerLit(9123)), FuncCall(foo, [ArrayLit([])]), BinExpr(+, ArrayLit([]), IntegerLit(1122)), ReturnStmt(FloatLit(15.0)))]))
	VarDecl(a, IntegerType, FloatLit(131.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_82(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) return 1_5.;
           
        }
        a,c : integer = 1_3_1., 12;
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType)], None, BlockStmt([BreakStmt(), ForStmt(AssignStmt(Id(a), IntegerLit(9123)), FuncCall(foo, [ArrayLit([])]), BinExpr(+, ArrayLit([]), IntegerLit(1122)), ReturnStmt(FloatLit(15.0)))]))
	VarDecl(a, IntegerType, FloatLit(131.0))
	VarDecl(c, IntegerType, IntegerLit(12))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_83(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) return 1_5.;
        }
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType)], None, BlockStmt([BreakStmt(), ForStmt(AssignStmt(Id(a), IntegerLit(9123)), FuncCall(foo, [ArrayLit([])]), BinExpr(+, ArrayLit([]), IntegerLit(1122)), ReturnStmt(FloatLit(15.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_84(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) return 1_5;
        }
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType)], None, BlockStmt([BreakStmt(), ForStmt(AssignStmt(Id(a), IntegerLit(9123)), FuncCall(foo, [ArrayLit([])]), BinExpr(+, ArrayLit([]), IntegerLit(1122)), ReturnStmt(IntegerLit(15)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_85(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1) return 1;
        }
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType)], None, BlockStmt([BreakStmt(), ForStmt(AssignStmt(Id(a), IntegerLit(9123)), FuncCall(foo, [ArrayLit([])]), BinExpr(+, ArrayLit([]), IntegerLit(1)), ReturnStmt(IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_86(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=2 ,foo({}) ,{}+1) return 1;
        }
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType)], None, BlockStmt([BreakStmt(), ForStmt(AssignStmt(Id(a), IntegerLit(2)), FuncCall(foo, [ArrayLit([])]), BinExpr(+, ArrayLit([]), IntegerLit(1)), ReturnStmt(IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_87(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for ( a = 2, c :: 4 ,d) return 1;
        }
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType)], None, BlockStmt([BreakStmt(), ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(::, Id(c), IntegerLit(4)), Id(d), ReturnStmt(IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_88(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for ( a=1,2>1 ,{1}+1) return 1;
        }
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType)], None, BlockStmt([BreakStmt(), ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(>, IntegerLit(2), IntegerLit(1)), BinExpr(+, ArrayLit([IntegerLit(1)]), IntegerLit(1)), ReturnStmt(IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_89(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a = 2  ,a > foo(1), a - c) return 1;
        }
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType)], None, BlockStmt([BreakStmt(), ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(>, Id(a), FuncCall(foo, [IntegerLit(1)])), BinExpr(-, Id(a), Id(c)), ReturnStmt(IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_90(self):
        input = """a: function integer (b: string) inherit a {
            a[1,a[0]] = 2;
        }"""
        expect = """Program([
	FuncDecl(a, IntegerType, [Param(b, StringType)], a, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), ArrayCell(a, [IntegerLit(0)])]), IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_91(self):
        input = """        fact: function integer (inherit out a : integer) {
            a[1] = {a(0),a[0], {}};
            {a(0);/*} {*/}
        }
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [InheritOutParam(a, IntegerType)], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), ArrayLit([FuncCall(a, [IntegerLit(0)]), ArrayCell(a, [IntegerLit(0)]), ArrayLit([])])), BlockStmt([CallStmt(a, IntegerLit(0))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_92(self):
        input = """        fact: function integer (inherit out a : integer) {
            a[1] = {a(0),a[0], {}};
            {a(0);} return 1;
        }
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [InheritOutParam(a, IntegerType)], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), ArrayLit([FuncCall(a, [IntegerLit(0)]), ArrayCell(a, [IntegerLit(0)]), ArrayLit([])])), BlockStmt([CallStmt(a, IntegerLit(0))]), ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_93(self):
        input = """        fact: function integer (inherit out a : integer) {
            a[1] = {a(0),a[0], {}};
            a[a(0),a[0], {}] = 1;
        }
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [InheritOutParam(a, IntegerType)], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), ArrayLit([FuncCall(a, [IntegerLit(0)]), ArrayCell(a, [IntegerLit(0)]), ArrayLit([])])), AssignStmt(ArrayCell(a, [FuncCall(a, [IntegerLit(0)]), ArrayCell(a, [IntegerLit(0)]), ArrayLit([])]), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_94(self):
        input = """        fact: function integer (inherit out a : integer) {
            a[1] = {a(0),a[0], {}};
        }
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [InheritOutParam(a, IntegerType)], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), ArrayLit([FuncCall(a, [IntegerLit(0)]), ArrayCell(a, [IntegerLit(0)]), ArrayLit([])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_95(self):
        input = """        fact: function integer () {
            a[1] = {a(0),a[0], {}};
        }
"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), ArrayLit([FuncCall(a, [IntegerLit(0)]), ArrayCell(a, [IntegerLit(0)]), ArrayLit([])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_96(self):
        input = """fact: function integer (n: auto){}"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_97(self):
        input = """        fact: function integer (n: auto) {a=c;}"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, AutoType)], None, BlockStmt([AssignStmt(Id(a), Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_98(self):
        input = """        fact: function integer (n: auto) {return 1;}"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, AutoType)], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_99(self):
        input = """        fact: function integer (n: auto) {
            if (n == 0) return ;
            else return ;
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, AutoType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_100(self):
        input = """foo : function integer () {
while (a==3) {
    if (a > b) {c, d, e, f : integer = b, c, d, a; return c;}
    else {
        continue;
        break;
        c, d, c, c, c : integer; return c;
    }
}
    {
    c, d,v,c,a,a : integer; return c;
    }
}
c,a,s,a,f,d : integer ; """
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), IntegerLit(3)), BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([VarDecl(c, IntegerType, Id(b)), VarDecl(d, IntegerType, Id(c)), VarDecl(e, IntegerType, Id(d)), VarDecl(f, IntegerType, Id(a)), ReturnStmt(Id(c))]), BlockStmt([ContinueStmt(), BreakStmt(), VarDecl(c, IntegerType), VarDecl(d, IntegerType), VarDecl(c, IntegerType), VarDecl(c, IntegerType), VarDecl(c, IntegerType), ReturnStmt(Id(c))]))])), BlockStmt([VarDecl(c, IntegerType), VarDecl(d, IntegerType), VarDecl(v, IntegerType), VarDecl(c, IntegerType), VarDecl(a, IntegerType), VarDecl(a, IntegerType), ReturnStmt(Id(c))])]))
	VarDecl(c, IntegerType)
	VarDecl(a, IntegerType)
	VarDecl(s, IntegerType)
	VarDecl(a, IntegerType)
	VarDecl(f, IntegerType)
	VarDecl(d, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 300))