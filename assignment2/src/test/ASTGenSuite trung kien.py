import unittest
from TestUtils import TestAST
from AST import *

 
class ASTGenSuite(unittest.TestCase):
    def test_0(self):
        input = """x: integer;"""
        expect = """Program([
	VarDecl(x, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_1(self):
        input = """x: integer; y: float; z: boolean; t:string; """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, FloatType)
	VarDecl(z, BooleanType)
	VarDecl(t, StringType)
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_2(self):
        input = """x, y, z: integer = 1, 2, 3; """
        expect ="""Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_3(self): #done
        input = """x, y, z: integer = 1, 2, 3;
        k,l: string = "Trung","Kien";
        m,n: boolean = true, false;
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(k, StringType, StringLit(Trung))
	VarDecl(l, StringType, StringLit(Kien))
	VarDecl(m, BooleanType, BooleanLit(True))
	VarDecl(n, BooleanType, BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_4(self):
        input = """
        tes1, test2 : array [3,4] of string;
        """
        expect = """Program([
	VarDecl(tes1, ArrayType([3, 4], StringType))
	VarDecl(test2, ArrayType([3, 4], StringType))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_5(self):
        input = """
            x: integer = 65;
            func1: function integer (n: integer){
                return n/50 * 2;
            }
            main: function void () {
                delta: integer = mess(7);
                printInteger(delta);
            }
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(func1, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, BinExpr(/, Id(n), IntegerLit(50)), IntegerLit(2)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(mess, [IntegerLit(7)])), CallStmt(printInteger, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_6(self):
        input = """
            add: function integer (n: integer){
                sum: integer= 0;
                for (i = 0, i<=n, i+1){
                        sum = sum + i;
                    }
                    return sum;
                }
            main: function void () {
                delta: integer = add(10);
                printInteger(delta);
            }
        """
        expect = """Program([
	FuncDecl(add, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i)))])), ReturnStmt(Id(sum))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(add, [IntegerLit(10)])), CallStmt(printInteger, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_7(self):
        input = """
            x: integer = 65;
                fact: function integer (n:integer){
                    if (n == 0) return 1;
                    else return n * fact(n-1);
                }
            inc: function void (out n: integer, delta: integer){
                n = n + delta;
            }
            main: function void () {
                delta: integer = fact(3);
                inc(x,delta);
                printInteger(x);
            }
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_8(self):
        input = """
            main: function void () {
                i: integer = 10;
                while (i!=0){
                    i = i - 1;
                }
                return  i;
            }
        """
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(10)), WhileStmt(BinExpr(!=, Id(i), IntegerLit(0)), BlockStmt([AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))])), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_9(self):
        input = """
            main: function void () {
                i: integer = 10;
                while (i>20){
                    i = i + 2;
                }
                return  i;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(10)), WhileStmt(BinExpr(>, Id(i), IntegerLit(20)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))])), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_10(self):
        input = """
            voidA: function integer (n: integer){
                return n%10;
            }
            voidB: function void (out n: integer, delta:integer){
                n = n + voidA(delta);
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInteger(x);
            }
        """
        expect = """Program([
	FuncDecl(voidA, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(%, Id(n), IntegerLit(10)))]))
	FuncDecl(voidB, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), FuncCall(voidA, [Id(delta)])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, IntegerLit(5)), CallStmt(voidB, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_11(self):
        input = """
            main: function void () {
                delta: string = "Kien";
                printString(delta);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, StringType, StringLit(Kien)), CallStmt(printString, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_12(self):
        input = """
            main: function void () {
                delta: float = 3.45;
                printFloat(delta);
            }
        """
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, FloatType, FloatLit(3.45)), CallStmt(printFloat, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_13(self):
        input = """
            main: function void () {
                delta: float = 3.45;
                printFloat(delta);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, FloatType, FloatLit(3.45)), CallStmt(printFloat, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_14(self):
        input = """
            main: function void () {
                delta: boolean = true;
                printBoolean(delta);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, BooleanType, BooleanLit(True)), CallStmt(printBoolean, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_15(self):
        input = """
            main: function void () {
                b: array [5] of integer;
                b[4] = 3;
                printIntegert(b[4]);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(ArrayCell(b, [IntegerLit(4)]), IntegerLit(3)), CallStmt(printIntegert, ArrayCell(b, [IntegerLit(4)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_16(self):
        input = """
            main: function void () {
                delta: integer = 1+22*33*35*16/4*2/2-4*4+5%2;
                printInteger(delta);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, BinExpr(+, BinExpr(-, BinExpr(+, IntegerLit(1), BinExpr(/, BinExpr(*, BinExpr(/, BinExpr(*, BinExpr(*, BinExpr(*, IntegerLit(22), IntegerLit(33)), IntegerLit(35)), IntegerLit(16)), IntegerLit(4)), IntegerLit(2)), IntegerLit(2))), BinExpr(*, IntegerLit(4), IntegerLit(4))), BinExpr(%, IntegerLit(5), IntegerLit(2)))), CallStmt(printInteger, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_17(self):
        input = """
            main: function void () {
                i: integer = 10;
                do{
                    i = i - 1;
                }
                while (i!=0);
                return  i;
            }  
        """
        expect ="""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(10)), DoWhileStmt(BinExpr(!=, Id(i), IntegerLit(0)), BlockStmt([AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))])), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_18(self):
        input = """
            main: function void () {
                i: integer = -10;
                do{
                    i = i - 1;
                }
                while (i!=0);
                return  i;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, UnExpr(-, IntegerLit(10))), DoWhileStmt(BinExpr(!=, Id(i), IntegerLit(0)), BlockStmt([AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))])), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_19(self):
        input = """
            main: function void () {
                delta: float = 130.34e2;
                printFloat(delta);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, FloatType, FloatLit(13034.0)), CallStmt(printFloat, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_20(self):
        input = """
            main: function void () {
                delta: string = "true";
                printString(delta);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, StringType, StringLit(true)), CallStmt(printString, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_21(self):
        input = """
        test: function integer (out x:integer, data:string){
            c : integer;
        }
        """
        expect = """Program([
	FuncDecl(test, IntegerType, [OutParam(x, IntegerType), Param(data, StringType)], None, BlockStmt([VarDecl(c, IntegerType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_22(self):
        input = """
            test: function integer (){
            }
        """
        expect ="""Program([
	FuncDecl(test, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_23(self):
        input = """
            x: float = 10 % 2 + .2E-10 * 12 + 8.98;
            y: boolean =  true||false&&true||false;
        """
        expect = """Program([
	VarDecl(x, FloatType, BinExpr(+, BinExpr(+, BinExpr(%, IntegerLit(10), IntegerLit(2)), BinExpr(*, FloatLit(2e-11), IntegerLit(12))), FloatLit(8.98)))
	VarDecl(y, BooleanType, BinExpr(||, BinExpr(&&, BinExpr(||, BooleanLit(True), BooleanLit(False)), BooleanLit(True)), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_24(self):
        input = """
            x: string = "Trung"::"Kien";
        """
        expect = """Program([
	VarDecl(x, StringType, BinExpr(::, StringLit(Trung), StringLit(Kien)))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_25(self):
        input = """
            x: string = "Trung";
            y: string = "Kien";
            z: string = x::y;
        """
        expect = """Program([
	VarDecl(x, StringType, StringLit(Trung))
	VarDecl(y, StringType, StringLit(Kien))
	VarDecl(z, StringType, BinExpr(::, Id(x), Id(y)))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_26(self):
        input = """
            x: integer = 1/2*3 + 4;
            array_test : array [1,3] of integer;
        """
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, BinExpr(*, BinExpr(/, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)))
	VarDecl(array_test, ArrayType([1, 3], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_27(self):
        input = """
            x: integer= 1/2*3 + 4;
            array_test : array [1,3] of integer;
            y: float = array_test[1+1,x];
        """
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, BinExpr(*, BinExpr(/, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)))
	VarDecl(array_test, ArrayType([1, 3], IntegerType))
	VarDecl(y, FloatType, ArrayCell(array_test, [BinExpr(+, IntegerLit(1), IntegerLit(1)), Id(x)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_28(self):
        input = """
                x:integer = 1/2*3 + 4;
                array_test : array [1,3] of integer;
                y: float = array_test[1+1,x] + 1/100;
        """
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, BinExpr(*, BinExpr(/, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)))
	VarDecl(array_test, ArrayType([1, 3], IntegerType))
	VarDecl(y, FloatType, BinExpr(+, ArrayCell(array_test, [BinExpr(+, IntegerLit(1), IntegerLit(1)), Id(x)]), BinExpr(/, IntegerLit(1), IntegerLit(100))))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_29(self):
        input = """
            test: function integer (){
                arr : array [2,3] of float;
                x = arr [0,1];
           }
        """
        expect = """Program([
	FuncDecl(test, IntegerType, [], None, BlockStmt([VarDecl(arr, ArrayType([2, 3], FloatType)), AssignStmt(Id(x), ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_30(self):
        input = """
            arr : array [2,3] of float;
            test: function integer(out arr : array [2,3] of float){
                arr : array [2,3] of float;
                arr [0,1] = 1*2+1.2-1;
           }
        """
        expect = """Program([
	VarDecl(arr, ArrayType([2, 3], FloatType))
	FuncDecl(test, IntegerType, [OutParam(arr, ArrayType([2, 3], FloatType))], None, BlockStmt([VarDecl(arr, ArrayType([2, 3], FloatType)), AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), BinExpr(-, BinExpr(+, BinExpr(*, IntegerLit(1), IntegerLit(2)), FloatLit(1.2)), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_31(self):
        input = """
            main : function void() {
                continue;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ContinueStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_32(self):
        input = """
            x : integer ;
            main : function void() {
                x : integer ;
                if(x==3) y = 3;
            }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), AssignStmt(Id(y), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_33(self):
        input = """
            x : integer ;
            main : function void() {
                if(x==3) {y :integer= 3;}
            }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([VarDecl(y, IntegerType, IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_34(self):
        input = """
            x : integer ;
            main : function void() {
               if(x==3){break;}
            }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_35(self):
        input = """
            x : integer;
            main : function void() {
               if(x==3){continue;}
            }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))  

    def test_36(self):
        input = """
            x : integer ;
            main : function void() {
                if(x==3) {y :integer = 3;}
                else {y : integer = 34;}
            }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([VarDecl(y, IntegerType, IntegerLit(3))]), BlockStmt([VarDecl(y, IntegerType, IntegerLit(34))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_37(self):
        input = """
            x : integer ;
            main : function void() {
                if(x==3) {y :integer = 3;}
                else {y : integer = 34;}
            }
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([VarDecl(y, IntegerType, IntegerLit(3))]), BlockStmt([VarDecl(y, IntegerType, IntegerLit(34))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_38(self):
        input = """
            arr : array [1,2] of integer;
            x : integer ;
            main : function void() {
                if(x==3) {arr[0,1] = 3;}
                else {arr[0,1] = 4 ;}
            }
        """
        expect = """Program([
	VarDecl(arr, ArrayType([1, 2], IntegerType))
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), IntegerLit(3))]), BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), IntegerLit(4))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_39(self):
        input = """
            arr : array [1,2] of integer;
            main : function void() {
                if(x==3) {arr[0,1] = arr [0,2];}
                else {arr[0,1] = arr[1,2];} 
            }
        """
        expect = """Program([
	VarDecl(arr, ArrayType([1, 2], IntegerType))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), ArrayCell(arr, [IntegerLit(0), IntegerLit(2)]))]), BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), ArrayCell(arr, [IntegerLit(1), IntegerLit(2)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))  

    def test_40(self):
        input = """
            main : function void() {
            x : integer ;
                if(x==3){
                   y : integer ;
                    if(y==4) {z : integer = 4;}
                }
            } 
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([VarDecl(y, IntegerType), IfStmt(BinExpr(==, Id(y), IntegerLit(4)), BlockStmt([VarDecl(z, IntegerType, IntegerLit(4))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_41(self):
        input = """
            main : function void() {
                x : integer ;
                if(x==3){
                    y : integer ;
                    if(y==4) {z : integer = 4;}
                    else {
                        z : integer = 5;
                    }
                }
            }       
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([VarDecl(y, IntegerType), IfStmt(BinExpr(==, Id(y), IntegerLit(4)), BlockStmt([VarDecl(z, IntegerType, IntegerLit(4))]), BlockStmt([VarDecl(z, IntegerType, IntegerLit(5))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_42(self):
        input = """
            main : function void() {
                x :integer ;
                 if(x==3){
                    y : integer ;
                    if(y==4) {z : integer = 4;}
                    else {
                    z : integer = 5;
                    }
                } else { z : integer = 3;}
            }        
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([VarDecl(y, IntegerType), IfStmt(BinExpr(==, Id(y), IntegerLit(4)), BlockStmt([VarDecl(z, IntegerType, IntegerLit(4))]), BlockStmt([VarDecl(z, IntegerType, IntegerLit(5))]))]), BlockStmt([VarDecl(z, IntegerType, IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_43(self):
        input = """
            main : function void() {
                x : integer ;
                if(x==3){}
            }      
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))  

    def test_44(self):
        input = """
            main : function void() {
                x : integer ;
                if(x==3){} else {z : integer = 3;}
            }       
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([]), BlockStmt([VarDecl(z, IntegerType, IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_45(self):
        input = """
            main : function void() {
                for (i = 1, i < 10, i + 1) {
                    printInteger(i);
                }
            }        
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_46(self):
        input = """
            main : function void() {
                x : integer ;
                if(x==3){
                    for (i = 1, i < 10, i + 1) {
                    printInteger(i);
                    }
                } else {z : integer = 3;}
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i))]))]), BlockStmt([VarDecl(z, IntegerType, IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_47(self):
        input = """
            main: function void() {
                for (i = 1, i < 10, i + 1) {
                printInteger(i);
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))  

    def test_48(self):
        input = """
            main : function void() {
                x : integer ;
                {
                    for (i = 1, i < 10, i + 1) {
                        printInteger(i);
                        if(x==3){break;}
                    }
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i)), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([BreakStmt()]))]))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_49(self):
        input = """
            main : function void() {
                x : integer ;
                for (i = 1, i < 10, i + 1) {
                    printInteger(i);
                    if(x==3){break;}
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i)), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([BreakStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_50(self):
        input = """
            main : function void() {
                x : integer ;
                for (i = 1, i < 10, i + 1) {
                    printInteger(i);
                    if(x==3){continue;}
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i)), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([ContinueStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_51(self):
        input = """
            main : function void() {
                x : integer ;
                for (i = 1, i < 10, i + 1) {
                    if(i%2==0){printInteger(i);}
                    else foo(2*i);
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(printInteger, Id(i))]), CallStmt(foo, BinExpr(*, IntegerLit(2), Id(i))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_52(self):
        input = """
            main : function void() {
                x : integer = 5;
                while (x > 0){
                    printInteger(x);
                    x = x - 1;
                }
            }

        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), WhileStmt(BinExpr(>, Id(x), IntegerLit(0)), BlockStmt([CallStmt(printInteger, Id(x)), AssignStmt(Id(x), BinExpr(-, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_53(self):
        input = """
            main : function void() {
                x : integer = 5;
                while (x > 0){
                    if(x%2==0){printInteger(x);}
                    else break;
                    x = x - 1;
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), WhileStmt(BinExpr(>, Id(x), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(x), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(printInteger, Id(x))]), BreakStmt()), AssignStmt(Id(x), BinExpr(-, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_54(self):
        input = """
            main : function void() {
                x : integer = 5;
                while ( x > 0){
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), WhileStmt(BinExpr(>, Id(x), IntegerLit(0)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))  

    def test_55(self):
        input = """
            main : function void() {
                x : integer = 5;
                while (x > 0)  x = x - 1;
            }

        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), WhileStmt(BinExpr(>, Id(x), IntegerLit(0)), AssignStmt(Id(x), BinExpr(-, Id(x), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_56(self):
        input = """
            main : function void() {
                x : integer = 5;
                do {x = x - 1;}
                while (x > 0);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), DoWhileStmt(BinExpr(>, Id(x), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), BinExpr(-, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_57(self):
        input = """
            main : function void() {
                x : integer = 5;
                do {
                    if(x==3) writeInt(x);
                }
                while (x > 0);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), DoWhileStmt(BinExpr(>, Id(x), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), CallStmt(writeInt, Id(x)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_58(self):
        input = """
            main : function void() {
            x : integer= 5;
                do {
                    if(x==3) break;
                    else writeInt(x);
                }
                while (x > 0);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), DoWhileStmt(BinExpr(>, Id(x), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BreakStmt(), CallStmt(writeInt, Id(x)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))  

    def test_59(self):
        input = """
            main : function void() {
                x : integer = 5;
                do {
                    if(x==3) continue;
                    else writeInt(x);
                }
                while (x > 0);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), DoWhileStmt(BinExpr(>, Id(x), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), ContinueStmt(), CallStmt(writeInt, Id(x)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_60(self):
        input = """
            main : function void (x : auto) {}
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_61(self):
        input = """
            main : function void(x: boolean) {    
                    x = y || z || t && x;
                    x = y && z && t && z;
                }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, BooleanType)], None, BlockStmt([AssignStmt(Id(x), BinExpr(&&, BinExpr(||, BinExpr(||, Id(y), Id(z)), Id(t)), Id(x))), AssignStmt(Id(x), BinExpr(&&, BinExpr(&&, BinExpr(&&, Id(y), Id(z)), Id(t)), Id(z)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_62(self):
        input = """
            main : function void(x: float) {    
                    a = x[1+1,2*3] + 10000 ;
                }   
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, FloatType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, ArrayCell(x, [BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(*, IntegerLit(2), IntegerLit(3))]), IntegerLit(10000)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_63(self):
        input = """
            main : function void(x: float) {    
                    a = x[y[1,2],5*6] + 10000 ;
                }   
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, FloatType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, ArrayCell(x, [ArrayCell(y, [IntegerLit(1), IntegerLit(2)]), BinExpr(*, IntegerLit(5), IntegerLit(6))]), IntegerLit(10000)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_64(self):
        input = """
            main : function void(x: float) {    
                    a = x[y[1,2,z[1,t[1,2,3]]],5*6] + 10000 ;
            }   
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, FloatType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, ArrayCell(x, [ArrayCell(y, [IntegerLit(1), IntegerLit(2), ArrayCell(z, [IntegerLit(1), ArrayCell(t, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])])]), BinExpr(*, IntegerLit(5), IntegerLit(6))]), IntegerLit(10000)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_65(self):
        input = """
            main : function void() {    
                if(true){
                    if(1+1*2-8/6%2==3){
                        continue;
                        }
                    }
                    else{
                        break;
                    }
                }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(==, BinExpr(-, BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(1), IntegerLit(2))), BinExpr(%, BinExpr(/, IntegerLit(8), IntegerLit(6)), IntegerLit(2))), IntegerLit(3)), BlockStmt([ContinueStmt()]))]), BlockStmt([BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))  

    def test_66(self):
        input = """
            main : function string() {    
                return "QA cute";
            }
        """
        expect = """Program([
	FuncDecl(main, StringType, [], None, BlockStmt([ReturnStmt(StringLit(QA cute))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_67(self):
        input = """
            main : function void() {
                a : array[2,3] of integer;
                arr[0,0] = 1;
                arr[0,1] = 2;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 3], IntegerType)), AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(0)]), IntegerLit(1)), AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_68(self):
        input = """
            main : function void() {
                return;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_69(self):
        input = """
            main : function void() {
                x:string = "Quynh Anh";
                a : array[1,1] of string;
                a[2*2-4,1-1] = "xinh dep";
                y: string = a[0,0];
                z:string = a::b;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, StringLit(Quynh Anh)), VarDecl(a, ArrayType([1, 1], StringType)), AssignStmt(ArrayCell(a, [BinExpr(-, BinExpr(*, IntegerLit(2), IntegerLit(2)), IntegerLit(4)), BinExpr(-, IntegerLit(1), IntegerLit(1))]), StringLit(xinh dep)), VarDecl(y, StringType, ArrayCell(a, [IntegerLit(0), IntegerLit(0)])), VarDecl(z, StringType, BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))  

    def test_70(self):
        input = """
            main : function void(){
                if(true){
                    a: integer;
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([VarDecl(a, IntegerType)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_71(self):
        input = """
            main : function void(){
                if (a + b > c){
                    x:integer;
                }
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, BinExpr(+, Id(a), Id(b)), Id(c)), BlockStmt([VarDecl(x, IntegerType)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_72(self):
        input = """
            main : function void() {
                    x = y::z;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(::, Id(y), Id(z)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_73(self):
        input = """
            main : function void(){ 
                    x = y <= z;
                    x = y >= z;
                    x = y < z;
                    x = y > z;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(<=, Id(y), Id(z))), AssignStmt(Id(x), BinExpr(>=, Id(y), Id(z))), AssignStmt(Id(x), BinExpr(<, Id(y), Id(z))), AssignStmt(Id(x), BinExpr(>, Id(y), Id(z)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_74(self):
        input = """
            main : function void() {    
                    x = y || z || t && x;
                    x = y && z && t && z;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(&&, BinExpr(||, BinExpr(||, Id(y), Id(z)), Id(t)), Id(x))), AssignStmt(Id(x), BinExpr(&&, BinExpr(&&, BinExpr(&&, Id(y), Id(z)), Id(t)), Id(z)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_75(self):
        input = """
            main : function void() {    
                a, b, c: integer = 1,2,3;
                x, y, z: integer = 1,2,3;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType, IntegerLit(3)), VarDecl(x, IntegerType, IntegerLit(1)), VarDecl(y, IntegerType, IntegerLit(2)), VarDecl(z, IntegerType, IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_76(self):
        input = """
            main : function void() {    
                _Kien_ : float = 1>3||true&&false;
                a: array[1,10] of integer;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(_Kien_, FloatType, BinExpr(>, IntegerLit(1), BinExpr(&&, BinExpr(||, IntegerLit(3), BooleanLit(True)), BooleanLit(False)))), VarDecl(a, ArrayType([1, 10], IntegerType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))  

    def test_77(self):
        input = """
            test : function integer (num:integer)  {
                if( num == 1){
                    return 1;
                }
                else {
                    return 0;
                }
            }
            main : function void() {
                printInteger(test(5));
            }
        """
        expect = """Program([
	FuncDecl(test, IntegerType, [Param(num, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(num), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([ReturnStmt(IntegerLit(0))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(test, [IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_78(self):
        input = """
            a,b,c : float;
            main : function void() {    
                x = y && z && t || c || r;
            }
        """
        expect = """Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(c, FloatType)
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(||, BinExpr(||, BinExpr(&&, BinExpr(&&, Id(y), Id(z)), Id(t)), Id(c)), Id(r)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_79(self):
        input = """
            main : function void() {    
                x = y * !z * t / !!g % k + !h - !!!i % m;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(-, BinExpr(+, BinExpr(%, BinExpr(/, BinExpr(*, BinExpr(*, Id(y), UnExpr(!, Id(z))), Id(t)), UnExpr(!, UnExpr(!, Id(g)))), Id(k)), UnExpr(!, Id(h))), BinExpr(%, UnExpr(!, UnExpr(!, UnExpr(!, Id(i)))), Id(m))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_80(self):
        input = """
            main : function void() {    
                x = !y - z[86,1_2_3] + t[1,2] * m[0,a+b+c];
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, BinExpr(-, UnExpr(!, Id(y)), ArrayCell(z, [IntegerLit(86), IntegerLit(123)])), BinExpr(*, ArrayCell(t, [IntegerLit(1), IntegerLit(2)]), ArrayCell(m, [IntegerLit(0), BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))  

    def test_81(self):
        input = """
            main : function void(args: string) {}
            foo: function boolean(a:string, b: string){
                return a == b;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(args, StringType)], None, BlockStmt([]))
	FuncDecl(foo, BooleanType, [Param(a, StringType), Param(b, StringType)], None, BlockStmt([ReturnStmt(BinExpr(==, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_82(self):
        input = """
            foo: function integer(x:integer,y:integer) {
                if(x + 2 == 3){
                    break;
                }
                else{
                    x = x*2;
                    y = y*2;
                }
                return x + y;
            }
            main : function void() {    
                printInteger(foo(2,3));
            }
        """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(+, Id(x), IntegerLit(2)), IntegerLit(3)), BlockStmt([BreakStmt()]), BlockStmt([AssignStmt(Id(x), BinExpr(*, Id(x), IntegerLit(2))), AssignStmt(Id(y), BinExpr(*, Id(y), IntegerLit(2)))])), ReturnStmt(BinExpr(+, Id(x), Id(y)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(foo, [IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_83(self):
        input = """
            main : function void() {    
                return 0;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_84(self):
        input = """
            getString: function string(x: string) {
                return x;
            }
            upperCase: function string(y: string) {
                    return y;
                }
            main : function void() {    
                a:string = getString("QA")::upperCase("cute");
            }
        """
        expect = """Program([
	FuncDecl(getString, StringType, [Param(x, StringType)], None, BlockStmt([ReturnStmt(Id(x))]))
	FuncDecl(upperCase, StringType, [Param(y, StringType)], None, BlockStmt([ReturnStmt(Id(y))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, BinExpr(::, FuncCall(getString, [StringLit(QA)]), FuncCall(upperCase, [StringLit(cute)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_85(self):
        input = """
            test : function integer(x:integer,y:integer,z:integer) {    
                if (x + y + z >= 2) {
                    return x+y+z;
                }
                else {
                    return 0;
                }
            }
            main : function void() {    
                a: integer = test(1,2,3);
                printInteger(a);
            }
            
        """
        expect = """Program([
	FuncDecl(test, IntegerType, [Param(x, IntegerType), Param(y, IntegerType), Param(z, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)), IntegerLit(2)), BlockStmt([ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))]), BlockStmt([ReturnStmt(IntegerLit(0))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(test, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])), CallStmt(printInteger, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_86(self):
        input = """
            main : function void() {    
                if(true){
                    break;
                }
                else{
                    continue;
                }
                return;    
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([BreakStmt()]), BlockStmt([ContinueStmt()])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_87(self):
        input = """
            main: function void () {
                a: boolean = true;
                readBoolean(a);
                printBoolean(s || true && false);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType, BooleanLit(True)), CallStmt(readBoolean, Id(a)), CallStmt(printBoolean, BinExpr(&&, BinExpr(||, Id(s), BooleanLit(True)), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))  

    def test_88(self):
        input = """
            main : function void() {    
                
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_89(self):
        input = """
            sum: function integer(x:integer, y:integer,z:integer){
                return x + y + z;
            } 
            main : function void() {    
                printInteger(sum(1,2,3));
            }
        """
        expect = """Program([
	FuncDecl(sum, IntegerType, [Param(x, IntegerType), Param(y, IntegerType), Param(z, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(sum, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_90(self):
        input = """
            sumOdd: function integer(arr: array[100] of integer, n: integer ){
                sum: integer = 0;
                for(i = 0 , i < n , i + 1){
                    if(i%2 == 0) {
                        sum = sum + i;
                    }
                }
                return sum;
            } 
            main : function void() {
               arr: array[10] of integer;
               printInteger(sumOdd(arr,10));
            }   
                
        """
        expect = """Program([
	FuncDecl(sumOdd, IntegerType, [Param(arr, ArrayType([100], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i)))]))])), ReturnStmt(Id(sum))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10], IntegerType)), CallStmt(printInteger, FuncCall(sumOdd, [Id(arr), IntegerLit(10)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_91(self):
        input = """
            main: function void () {
                x : integer = 5;
                do{
                    x = x - 1;
                }
                while (i>=0);
                return  x;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), DoWhileStmt(BinExpr(>=, Id(i), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), BinExpr(-, Id(x), IntegerLit(1)))])), ReturnStmt(Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))  

    def test_92(self):
        input = """
            main: function void () {
                x : string = "";
                n : integer = 5;
                do{
                    x = x::"a";
                    n = n - 1 ;
                }
                while (n>=0);
                printString(x);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, StringLit()), VarDecl(n, IntegerType, IntegerLit(5)), DoWhileStmt(BinExpr(>=, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), BinExpr(::, Id(x), StringLit(a))), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1)))])), CallStmt(printString, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_93(self):
        input = """
            main: function void () {
                x : string = "";
                n : integer = 5;
                do{
                    x = x::"a";
                    n = n - 1;
                }
                while(n>=0);
                printString(x);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, StringLit()), VarDecl(n, IntegerType, IntegerLit(5)), DoWhileStmt(BinExpr(>=, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), BinExpr(::, Id(x), StringLit(a))), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1)))])), CallStmt(printString, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_94(self):
        input = """
            main: function void () {
                x : string = "";
                n : integer = 5;
                while(n>=0){
                    x = x::"a";
                    n = n - 1;
                }
                printString(x);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, StringLit()), VarDecl(n, IntegerType, IntegerLit(5)), WhileStmt(BinExpr(>=, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), BinExpr(::, Id(x), StringLit(a))), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1)))])), CallStmt(printString, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))
    def test_95(self):
        input = """
            main : function void() {
                x,y : integer = 100, 1*2*4-6;
                if (x < y) x = 9 + 3; 
                printInteger(x);
                printInteger(y);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(100)), VarDecl(y, IntegerType, BinExpr(-, BinExpr(*, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(4)), IntegerLit(6))), IfStmt(BinExpr(<, Id(x), Id(y)), AssignStmt(Id(x), BinExpr(+, IntegerLit(9), IntegerLit(3)))), CallStmt(printInteger, Id(x)), CallStmt(printInteger, Id(y))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_96(self):
        input = """
            main : function void(a: float) {
                a =5.0;
                a = a - 1;
                printFloat(x + 1.0);
            }  
            """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, FloatType)], None, BlockStmt([AssignStmt(Id(a), FloatLit(5.0)), AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(1))), CallStmt(printFloat, BinExpr(+, Id(x), FloatLit(1.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_97(self):
        input = """
            main : function void(a: float) {
                a =5.0;
                a = a - 1.7;
                printFloat(x + 1);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, FloatType)], None, BlockStmt([AssignStmt(Id(a), FloatLit(5.0)), AssignStmt(Id(a), BinExpr(-, Id(a), FloatLit(1.7))), CallStmt(printFloat, BinExpr(+, Id(x), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_98(self):
        input = """
            main : function void(a: float) {
                a =5.0;
                a = a - 1.7;
                printFloat(x + 1.0);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, FloatType)], None, BlockStmt([AssignStmt(Id(a), FloatLit(5.0)), AssignStmt(Id(a), BinExpr(-, Id(a), FloatLit(1.7))), CallStmt(printFloat, BinExpr(+, Id(x), FloatLit(1.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))  

    def test_99(self):
        input = """
            main : function void() { 
                arr : array[2,2] of integer;
                arr[1,3] = 6;
                x: integer = arr[1, 3];
                printInteger(x);
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([2, 2], IntegerType)), AssignStmt(ArrayCell(arr, [IntegerLit(1), IntegerLit(3)]), IntegerLit(6)), VarDecl(x, IntegerType, ArrayCell(arr, [IntegerLit(1), IntegerLit(3)])), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))
    def test_100(self):
        input = '''
        main : function void() {
                for( i = 0 , i[0] < 1 , -1){}
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, ArrayCell(i, [IntegerLit(0)]), IntegerLit(1)), UnExpr(-, IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
    def test_101(self): #note
        input = """
            x: float = 10 % 2 + .2E-10 * 12 + 8.98;
            y: boolean =  (true||false)&&true||false;
        """
        expect = """Program([
	VarDecl(x, FloatType, BinExpr(+, BinExpr(+, BinExpr(%, IntegerLit(10), IntegerLit(2)), BinExpr(*, FloatLit(2e-11), IntegerLit(12))), FloatLit(8.98)))
	VarDecl(y, BooleanType, BinExpr(||, BinExpr(&&, BinExpr(||, BooleanLit(True), BooleanLit(False)), BooleanLit(True)), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 401))
    def test_102(self):
        input = """
                a:float = 1_000 % 2 + .2E-10  + 8.98;
                b:float = (1 - 1) * 2 / 2 / 2 + 8 % 3 + ---10 * !!!true&&false;
        """
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(+, BinExpr(+, BinExpr(%, IntegerLit(1000), IntegerLit(2)), FloatLit(2e-11)), FloatLit(8.98)))
	VarDecl(b, FloatType, BinExpr(&&, BinExpr(+, BinExpr(+, BinExpr(/, BinExpr(/, BinExpr(*, BinExpr(-, IntegerLit(1), IntegerLit(1)), IntegerLit(2)), IntegerLit(2)), IntegerLit(2)), BinExpr(%, IntegerLit(8), IntegerLit(3))), BinExpr(*, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(10)))), UnExpr(!, UnExpr(!, UnExpr(!, BooleanLit(True)))))), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input,expect,402))

    def test103(self):
        input = """
                a : integer = 1;
                giaithua: function integer(n: integer){
                    if (n <= 0) return 1;
                    else return giaithua(n - 1) *n;
                }
                a : integer = 1;
                a : integer = 1;

                main: function void(inherit out a : integer, b : float) inherit a{
                    a: integer = giaithua(5);
                    b : integer = 2;
                }
            """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	FuncDecl(giaithua, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, FuncCall(giaithua, [BinExpr(-, Id(n), IntegerLit(1))]), Id(n))))]))
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(a, IntegerType, IntegerLit(1))
	FuncDecl(main, VoidType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], a, BlockStmt([VarDecl(a, IntegerType, FuncCall(giaithua, [IntegerLit(5)])), VarDecl(b, IntegerType, IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 3103))