import unittest
from TestUtils import TestAST
from AST import *
# py run.py test ParserSuite
# py run.py test ASTGenSuite
class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl11(self):
        input = """x: integer;"""
        expect = """Program([
	VarDecl(x, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    
    def test_short_vardecl(self):
        """Test short variable declaration"""
        input = """delta: integer = 3;"""
        expect = """Program([
	VarDecl(delta, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_full_vardecl(self):
        """Test full variable declaration"""
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(4))
	VarDecl(c, IntegerType, IntegerLit(6))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))
    def test_simple_program_with_UnExpr(self):
        """Test simple program"""
        input = """x:float = -5; 
        y: auto = !true;"""
        expect = """Program([
	VarDecl(x, FloatType, UnExpr(-, IntegerLit(5)))
	VarDecl(y, AutoType, UnExpr(!, BooleanLit(True)))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))
    def test_array_decl(self): 
        """Test simple program"""
        input = """a: array [4] of string;
        b: array[5] of float = {1.1,2.3,4.5}; """
        expect = """Program([
	VarDecl(a, ArrayType([4], StringType))
	VarDecl(b, ArrayType([5], FloatType), ArrayLit([FloatLit(1.1), FloatLit(2.3), FloatLit(4.5)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))
    def test_array_decl_string_and_float(self): 
        """Test simple program"""
        input = """a: array [16,16] of string = {"I", "Love","You"};
        b: array[5] of float = {1e2,10.21e2}; """
        expect = """Program([
	VarDecl(a, ArrayType([16, 16], StringType), ArrayLit([StringLit(I), StringLit(Love), StringLit(You)]))
	VarDecl(b, ArrayType([5], FloatType), ArrayLit([FloatLit(100.0), FloatLit(1021.0)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
    def test_6(self):
        # Test declaration array
        input = """test1, test2 : array [3,4] of boolean;"""
        expect = """Program([
	VarDecl(test1, ArrayType([3, 4], BooleanType))
	VarDecl(test2, ArrayType([3, 4], BooleanType))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
    def test_stringdecl(self):
        input = """x,y : string = "268","LTK";  """
        expect = """Program([
	VarDecl(x, StringType, StringLit(268))
	VarDecl(y, StringType, StringLit(LTK))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
    def test_array_decl_int_and_boolean(self): 
        """Test simple program"""
        input = """a: array [16,16] of integer = {2_8, 1,2022,k};
        b: array[5] of boolean = {true,false,true}; """
        expect = """Program([
	VarDecl(a, ArrayType([16, 16], IntegerType), ArrayLit([IntegerLit(28), IntegerLit(1), IntegerLit(2022), Id(k)]))
	VarDecl(b, ArrayType([5], BooleanType), ArrayLit([BooleanLit(True), BooleanLit(False), BooleanLit(True)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))
    def test_inherit_program(self): 
        """Simple program"""
        input = """dbs: function void () inherit dsa {
        }"""
        expect = """Program([
	FuncDecl(dbs, VoidType, [], dsa, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
    def test_simple_program_with_stmt(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
    def test_inherit_program_with_variable(self): 
        """Simple program"""
        input = """dbs: function void (inherit a: integer, out b: float, inherit out c: auto) inherit dsa {
        }"""
        expect = """Program([
	FuncDecl(dbs, VoidType, [InheritParam(a, IntegerType), OutParam(b, FloatType), InheritOutParam(c, AutoType)], dsa, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
    def test_inherit_program_with_array(self): 
        """Simple program"""
        input = """dbs: function array [5] of integer () inherit dsa {
        }"""
        expect = """Program([
	FuncDecl(dbs, ArrayType([5], IntegerType), [], dsa, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))
    def test_inherit_program_with_arrayParam(self): 
        """Simple program"""
        input = """dbs: function array [5] of integer (inherit a: array [9] of boolean) inherit dsa {
        }"""
        expect = """Program([
	FuncDecl(dbs, ArrayType([5], IntegerType), [InheritParam(a, ArrayType([9], BooleanType))], dsa, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))
    def test_inherit_program_with_arrayParam_and_stmt(self): 
        """Simple program"""
        input = """dbs: function array [5] of integer (inherit a: array [9] of boolean) inherit dsa {
            x:integer = -4;
            return a; 
        }"""
        expect = """Program([
	FuncDecl(dbs, ArrayType([5], IntegerType), [InheritParam(a, ArrayType([9], BooleanType))], dsa, BlockStmt([VarDecl(x, IntegerType, UnExpr(-, IntegerLit(4))), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
    def test_program_with_for_stmt_1(self): 
        """Simple program"""
        input = """z: function string (inherit a: boolean) inherit dsa {
            for (i = 1, i < 10, i + 1) {
                printInteger(i); 
                break; 
            }
            x:integer = !true;
            return a; 
        }"""
        expect = """Program([
	FuncDecl(z, StringType, [InheritParam(a, BooleanType)], dsa, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, Id(i)), BreakStmt()])), VarDecl(x, IntegerType, UnExpr(!, BooleanLit(True))), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
    def test_program_with_for_stmt_2(self): 
        """Simple program"""
        input = """z: function boolean (inherit a: boolean) inherit dsa {
            for (i = 1, i < 10, i + 1) printInteger(i); 
            x:integer = !true;
            return a; 
        }"""
        expect = """Program([
	FuncDecl(z, BooleanType, [InheritParam(a, BooleanType)], dsa, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printInteger, Id(i))), VarDecl(x, IntegerType, UnExpr(!, BooleanLit(True))), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
    def test_ifstmt(self): 
        """Simple program"""
        input = """_tester: function integer (inherit i: integer) inherit dsa {
            i:integer = 15 - 7 + 9;
            if (i%2==0) i = i + 1; 
            return i; 
        }"""
        expect = """Program([
	FuncDecl(_tester, IntegerType, [InheritParam(i, IntegerType)], dsa, BlockStmt([VarDecl(i, IntegerType, BinExpr(+, BinExpr(-, IntegerLit(15), IntegerLit(7)), IntegerLit(9))), IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
    def test_ifstmt_withblock(self): 
        """Simple program"""
        input = """_tester: function integer (out i: integer) inherit dsa {
            i:integer = 15 - 7 + 9;
            if (i%2==0) {
                printInteger(i); 
            } 
            return i; 
        }"""
        expect = """Program([
	FuncDecl(_tester, IntegerType, [OutParam(i, IntegerType)], dsa, BlockStmt([VarDecl(i, IntegerType, BinExpr(+, BinExpr(-, IntegerLit(15), IntegerLit(7)), IntegerLit(9))), IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(printInteger, Id(i))])), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))
    def test_ifelsestmt(self): 
        """Simple program"""
        input = """_tester: function integer (inherit i: integer) inherit dsa {
            i:integer = 15 - 7 + 9;
            if (i%2==0) i = i + 1;
            else i = i - 1; 
            return i; 
        }"""
        expect = """Program([
	FuncDecl(_tester, IntegerType, [InheritParam(i, IntegerType)], dsa, BlockStmt([VarDecl(i, IntegerType, BinExpr(+, BinExpr(-, IntegerLit(15), IntegerLit(7)), IntegerLit(9))), IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
    def test_ifelsestmt_withBlock(self): 
        """Simple program"""
        input = """_tester: function integer (inherit i: integer) inherit dsa {
            i:integer = 15 - 7 + 9;
            if (i%2==0) {
                i = i * 2 / 0 + 2 * 2; 
            }
            else {
                i = i * 2 + 0 * 2 / 3; 
            }
            return i; 
        }"""
        expect = """Program([
	FuncDecl(_tester, IntegerType, [InheritParam(i, IntegerType)], dsa, BlockStmt([VarDecl(i, IntegerType, BinExpr(+, BinExpr(-, IntegerLit(15), IntegerLit(7)), IntegerLit(9))), IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(i), BinExpr(+, BinExpr(/, BinExpr(*, Id(i), IntegerLit(2)), IntegerLit(0)), BinExpr(*, IntegerLit(2), IntegerLit(2))))]), BlockStmt([AssignStmt(Id(i), BinExpr(+, BinExpr(*, Id(i), IntegerLit(2)), BinExpr(/, BinExpr(*, IntegerLit(0), IntegerLit(2)), IntegerLit(3))))])), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
    def test_ifelsestmt_noBlockelse(self): 
        """Simple program"""
        input = """_tester: function integer (inherit i: integer) inherit dsa {
            i:integer = 15 - 7 + 9;
            if (i%2==0) {
                while (i > 1) i = i - 1; 
            }
            else i = i * 2 + 0 * 2 / 3; 
            return i; 
        }"""
        expect = """Program([
	FuncDecl(_tester, IntegerType, [InheritParam(i, IntegerType)], dsa, BlockStmt([VarDecl(i, IntegerType, BinExpr(+, BinExpr(-, IntegerLit(15), IntegerLit(7)), IntegerLit(9))), IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([WhileStmt(BinExpr(>, Id(i), IntegerLit(1)), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1))))]), AssignStmt(Id(i), BinExpr(+, BinExpr(*, Id(i), IntegerLit(2)), BinExpr(/, BinExpr(*, IntegerLit(0), IntegerLit(2)), IntegerLit(3))))), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))
    def test_ifelsestmt_noBlocktrue(self): 
        """Simple program"""
        input = """_tester: function integer (inherit i: integer) inherit dsa {
            i:integer = 15 - 7 + 9;
            if (i%2==0) while (i > 1) i = i - 1; 
            else {
                printInteger(i); 
                return i;
            } 
            return i; 
        }"""
        expect = """Program([
	FuncDecl(_tester, IntegerType, [InheritParam(i, IntegerType)], dsa, BlockStmt([VarDecl(i, IntegerType, BinExpr(+, BinExpr(-, IntegerLit(15), IntegerLit(7)), IntegerLit(9))), IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), WhileStmt(BinExpr(>, Id(i), IntegerLit(1)), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))), BlockStmt([CallStmt(printInteger, Id(i)), ReturnStmt(Id(i))])), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
    def test_whileLoop(self): 
        """Simple program"""
        input = """_t3st3r: function integer (inherit out i: integer) inherit dsa {
            i:integer = 15 - 7 + 9;
            while (i == 0) i = i + 1; 
            while (i > 9) {
                i = readInteger();
                return i;  
            }
            return i * 20 + 4; 
        }"""
        expect = """Program([
	FuncDecl(_t3st3r, IntegerType, [InheritOutParam(i, IntegerType)], dsa, BlockStmt([VarDecl(i, IntegerType, BinExpr(+, BinExpr(-, IntegerLit(15), IntegerLit(7)), IntegerLit(9))), WhileStmt(BinExpr(==, Id(i), IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))), WhileStmt(BinExpr(>, Id(i), IntegerLit(9)), BlockStmt([AssignStmt(Id(i), FuncCall(readInteger, [])), ReturnStmt(Id(i))])), ReturnStmt(BinExpr(+, BinExpr(*, Id(i), IntegerLit(20)), IntegerLit(4)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
    def test_doWhileLoop(self): 
        """Simple program"""
        input = """_t3st3r: function integer (inherit out i: integer) inherit dsa {
            i:integer = 15 - 7 + 9;
            do {
                i = i * 2; 
            }
            while (i < 100); 
            return (i / 2) * -4 - 5;  
        }"""
        expect = """Program([
	FuncDecl(_t3st3r, IntegerType, [InheritOutParam(i, IntegerType)], dsa, BlockStmt([VarDecl(i, IntegerType, BinExpr(+, BinExpr(-, IntegerLit(15), IntegerLit(7)), IntegerLit(9))), DoWhileStmt(BinExpr(<, Id(i), IntegerLit(100)), BlockStmt([AssignStmt(Id(i), BinExpr(*, Id(i), IntegerLit(2)))])), ReturnStmt(BinExpr(-, BinExpr(*, BinExpr(/, Id(i), IntegerLit(2)), UnExpr(-, IntegerLit(4))), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))
    def test_doWhileLoop_if(self): 
        """Simple program"""
        input = """_t3st3r: function integer (inherit out i: integer) inherit dsa {
            i:integer = 15 - 7 + 9;
            do {
                i = i * 2;
                if (i == 64) break;
            }
            while (i < 100); 
            return (i / 2) * -4 - 5;  
        }"""
        expect = """Program([
	FuncDecl(_t3st3r, IntegerType, [InheritOutParam(i, IntegerType)], dsa, BlockStmt([VarDecl(i, IntegerType, BinExpr(+, BinExpr(-, IntegerLit(15), IntegerLit(7)), IntegerLit(9))), DoWhileStmt(BinExpr(<, Id(i), IntegerLit(100)), BlockStmt([AssignStmt(Id(i), BinExpr(*, Id(i), IntegerLit(2))), IfStmt(BinExpr(==, Id(i), IntegerLit(64)), BreakStmt())])), ReturnStmt(BinExpr(-, BinExpr(*, BinExpr(/, Id(i), IntegerLit(2)), UnExpr(-, IntegerLit(4))), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
    def test_doWhileLoop_indexop(self): 
        """Simple program"""
        input = """_t3st3r: function integer (inherit out i: integer) inherit dsa {
            a: array [5] of integer;
            i: integer = 0; 
            do {
                a[i] = 0; 
                i = i + 1; 
            }
            while (i < 5); 
            return (i / 2) * -4 - 5;  
        }"""
        expect = """Program([
	FuncDecl(_t3st3r, IntegerType, [InheritOutParam(i, IntegerType)], dsa, BlockStmt([VarDecl(a, ArrayType([5], IntegerType)), VarDecl(i, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(<, Id(i), IntegerLit(5)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(BinExpr(-, BinExpr(*, BinExpr(/, Id(i), IntegerLit(2)), UnExpr(-, IntegerLit(4))), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
    def test_doWhileLoop_indexop2(self): 
        """Simple program"""
        input = """_t3st3r: function integer (inherit out i: auto) inherit dsa {
            a: array [5] of integer;
            i: integer = 0; 
            do {
                a[i] = 0; 
                i = i + 1; 
            }
            while (i < 5);
            a[2] = a[1] + 19 * 4 - 2/1; 
            return a[2];
        }"""
        expect = """Program([
	FuncDecl(_t3st3r, IntegerType, [InheritOutParam(i, AutoType)], dsa, BlockStmt([VarDecl(a, ArrayType([5], IntegerType)), VarDecl(i, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(<, Id(i), IntegerLit(5)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(-, BinExpr(+, ArrayCell(a, [IntegerLit(1)]), BinExpr(*, IntegerLit(19), IntegerLit(4))), BinExpr(/, IntegerLit(2), IntegerLit(1)))), ReturnStmt(ArrayCell(a, [IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
    def test_doWhileLoop_indexop3(self): 
        """Simple program"""
        input = """_t3st3r: function integer (inherit out i: auto) inherit dsa {
            a: array [5] of integer;
            i: integer = 0; 
            do {
                a[i] = 0; 
                i = i + 1; 
            }
            while (i < 5);
            a[2] = a[1] + 19 * 4; 
            return a[2];
        }"""
        expect = """Program([
	FuncDecl(_t3st3r, IntegerType, [InheritOutParam(i, AutoType)], dsa, BlockStmt([VarDecl(a, ArrayType([5], IntegerType)), VarDecl(i, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(<, Id(i), IntegerLit(5)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(+, ArrayCell(a, [IntegerLit(1)]), BinExpr(*, IntegerLit(19), IntegerLit(4)))), ReturnStmt(ArrayCell(a, [IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
    def test_callExpr_2param(self): 
        """Simple program"""
        input = """
        gcd: function integer (a: integer, b: integer) {
            if (b == 0) return a; 
            return gcd(b, a % b); 
        }
        main: function void (inherit out i: integer){
            a,b: integer = -(-15),60;
            return gcd(a,b); 
        }"""
        expect = """Program([
	FuncDecl(gcd, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(b), IntegerLit(0)), ReturnStmt(Id(a))), ReturnStmt(FuncCall(gcd, [Id(b), BinExpr(%, Id(a), Id(b))]))]))
	FuncDecl(main, VoidType, [InheritOutParam(i, IntegerType)], None, BlockStmt([VarDecl(a, IntegerType, UnExpr(-, UnExpr(-, IntegerLit(15)))), VarDecl(b, IntegerType, IntegerLit(60)), ReturnStmt(FuncCall(gcd, [Id(a), Id(b)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
    def test_complicated_expr(self): 
        """Simple program"""
        input = """
        main: function void () {
                delta: integer = 3+34*30/5*16/4*2/2+19%4+2%2;
                printInt(delta);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(3), BinExpr(/, BinExpr(*, BinExpr(/, BinExpr(*, BinExpr(/, BinExpr(*, IntegerLit(34), IntegerLit(30)), IntegerLit(5)), IntegerLit(16)), IntegerLit(4)), IntegerLit(2)), IntegerLit(2))), BinExpr(%, IntegerLit(19), IntegerLit(4))), BinExpr(%, IntegerLit(2), IntegerLit(2)))), CallStmt(printInt, Id(delta))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))
    def test_complicated_compareExpr(self): 
        """Simple program"""
        input = """
        main: function void () {
                a:integer = 100; 
                if (a % 7 == (4 >= 7)) printString("True");
                else printString("False");  
                return 0; 
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(100)), IfStmt(BinExpr(==, BinExpr(%, Id(a), IntegerLit(7)), BinExpr(>=, IntegerLit(4), IntegerLit(7))), CallStmt(printString, StringLit(True)), CallStmt(printString, StringLit(False))), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))
    def test_2DArray(self): 
        """Simple program"""
        input = """
        print2D: function void (arr: array[5,5] of integer) {
            for (i = 0, i < 5, i +1)
                for (j = 0, j < 5, j + 1)
                    printInteger(arr[i,j]); 
        }"""
        expect = """Program([
	FuncDecl(print2D, VoidType, [Param(arr, ArrayType([5, 5], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(5)), BinExpr(+, Id(j), IntegerLit(1)), CallStmt(printInteger, ArrayCell(arr, [Id(i), Id(j)]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
    def test_2DArray_if(self): 
        """Simple program"""
        input = """
        print2D: function void (arr: array[5,5] of integer) {
            for (i = 0, i < 5, i +1)
                for (j = 0, j < 5, j + 1)
                    if (arr[i,j] == 4) break;  
        }"""
        expect = """Program([
	FuncDecl(print2D, VoidType, [Param(arr, ArrayType([5, 5], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(5)), BinExpr(+, Id(j), IntegerLit(1)), IfStmt(BinExpr(==, ArrayCell(arr, [Id(i), Id(j)]), IntegerLit(4)), BreakStmt())))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
    def test_2DArray_init(self): 
        """Simple program"""
        input = """
        print2D: function void (arr: array[3,3] of integer) {
            for (i = 0, i < 5, i +1)
                for (j = 0, j < 5, j + 1)
                    printInteger(arr[i,j]); 
        }
         main: function void () {
                arr: array [3,3] of integer; 
                print2D(arr);
        }
        """
        expect = """Program([
	FuncDecl(print2D, VoidType, [Param(arr, ArrayType([3, 3], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(5)), BinExpr(+, Id(j), IntegerLit(1)), CallStmt(printInteger, ArrayCell(arr, [Id(i), Id(j)]))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([3, 3], IntegerType)), CallStmt(print2D, Id(arr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
    def test_SCOPE(self): 
        """Simple program"""
        input = """
        main: function void (){
            a:string = "HCMUT"::"K20";
            printString(a); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, BinExpr(::, StringLit(HCMUT), StringLit(K20))), CallStmt(printString, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
    def test_doWhileLoop_continue(self): 
        """Simple program"""
        input = """_t3st3r: function integer (inherit out i: integer) inherit dsa {
            i:integer = 15 - 7 + 9;
            do {
                i = i * 2; 
                if (i < 64) continue; 
                else break; 
            }
            while (i < 100); 
            return i;  
        }"""
        expect = """Program([
	FuncDecl(_t3st3r, IntegerType, [InheritOutParam(i, IntegerType)], dsa, BlockStmt([VarDecl(i, IntegerType, BinExpr(+, BinExpr(-, IntegerLit(15), IntegerLit(7)), IntegerLit(9))), DoWhileStmt(BinExpr(<, Id(i), IntegerLit(100)), BlockStmt([AssignStmt(Id(i), BinExpr(*, Id(i), IntegerLit(2))), IfStmt(BinExpr(<, Id(i), IntegerLit(64)), ContinueStmt(), BreakStmt())])), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
    def program_with_for_loop69(self): 
        """More complex program"""
        input =	"""x: integer = 65;
        fact: function integer (n: integer) {
            n = 0; 
            for (i = 0, i < 69, i = i +1){
               n = n + i; 
            }
            for (integer i = n, i >= 0, i = i - 1) printInteger(i)
            return n; 
        }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
    def test_callexpr_global(self): 
        """Simple program"""
        input = """
                dbs: function integer () inherit dsa {
                return 1; 
        }
            x: integer = dbs(); 
        """
        expect = """Program([
	FuncDecl(dbs, IntegerType, [], dsa, BlockStmt([ReturnStmt(IntegerLit(1))]))
	VarDecl(x, IntegerType, FuncCall(dbs, []))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
    def test_MINUS_Unexpr(self): 
        """Simple program"""
        input = """
                dbs: function integer () inherit dsa {
                return 1; 
        }
            x: integer = -dbs(); 
        """
        expect = """Program([
	FuncDecl(dbs, IntegerType, [], dsa, BlockStmt([ReturnStmt(IntegerLit(1))]))
	VarDecl(x, IntegerType, UnExpr(-, FuncCall(dbs, [])))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))
    def test_NOT_Unexpr(self): 
        """Simple program"""
        input = """
                dbs: function integer () inherit dsa {
                return 1; 
        }
            x: integer = !dbs(); 
        """
        expect = """Program([
	FuncDecl(dbs, IntegerType, [], dsa, BlockStmt([ReturnStmt(IntegerLit(1))]))
	VarDecl(x, IntegerType, UnExpr(!, FuncCall(dbs, [])))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))
    def test_MINUS_Unexpr_inExpr(self): 
        """Simple program"""
        input = """
                dbs: function integer () inherit dsa {
                return 1; 
        }
            x: integer = 25 * 7 + -dbs(); 
        """
        expect = """Program([
	FuncDecl(dbs, IntegerType, [], dsa, BlockStmt([ReturnStmt(IntegerLit(1))]))
	VarDecl(x, IntegerType, BinExpr(+, BinExpr(*, IntegerLit(25), IntegerLit(7)), UnExpr(-, FuncCall(dbs, []))))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))
    def test_SubExpr_Global(self): 
        """Simple program"""
        input = """
                dbs: function integer () inherit dsa {
                return 1; 
        }
            x: integer = (25 + 7) * 4; 
        """
        expect = """Program([
	FuncDecl(dbs, IntegerType, [], dsa, BlockStmt([ReturnStmt(IntegerLit(1))]))
	VarDecl(x, IntegerType, BinExpr(*, BinExpr(+, IntegerLit(25), IntegerLit(7)), IntegerLit(4)))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))
    def test_IndexOp_Global(self): 
        """Simple program"""
        input = """
                a: array[3] of integer = {1,2,3}; 
            x: integer = a[1] * 4; 
        """
        expect = """successful"""
        self.assertTrue(TestAST.test(input, expect, 344))
    def test_IndexOp_Global(self): 
        """Simple program"""
        input = """
                a: array[3] of integer = {1,2,3}; 
            x: integer = a[1] * 4; 
        """
        expect = """Program([
	VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(x, IntegerType, BinExpr(*, ArrayCell(a, [IntegerLit(1)]), IntegerLit(4)))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))
    def test_booltype(self): 
        input = """a: boolean = true;  
        """
        expect = """Program([
	VarDecl(a, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
    def test_blockstmt_in_blockstmt(self): 
        input = """main : function void() {
                printString("This is block 0"); 
                {
                        printString("This is block 1"); 
                }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(This is block 0)), BlockStmt([CallStmt(printString, StringLit(This is block 1))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))
    def test_dowhile_do_nothing(self): 
        input = """main : function void() {
                do {
                
                }
                while (true); 
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))
    def test_while_do_nothing(self): 
        input = """main : function void() {
                while(false){
                
                }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(False), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
    def test_for_do_nothing(self):
        input = """main : function void() {
                for (i = 0, i < 9,i +1) {
                
                }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(9)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
    def test_if_do_nothing(self): 
        input = """main : function void() {
                if (1 > 2) { }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, IntegerLit(1), IntegerLit(2)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
    def test_ifelse_do_nothing(self): 
        input = """main : function void() {
                if (1 > 2) { } else {}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, IntegerLit(1), IntegerLit(2)), BlockStmt([]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))
    def test_for_do_nothing11(self):
        input = """main : function void() {
                a: array [10] of integer; 
                for (a = 0, a[1] < 9, a[1] + 1) {
                }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([10], IntegerType)), ForStmt(AssignStmt(Id(a), IntegerLit(0)), BinExpr(<, ArrayCell(a, [IntegerLit(1)]), IntegerLit(9)), BinExpr(+, ArrayCell(a, [IntegerLit(1)]), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))
    def test_ifelse_do_nothing1111(self): 
        input =	"""x: integer = 65;
        fact: function integer (n: integer) {
            n = 0; 
            while (n < 69){
                printString("Tran Ngoc Bao Duy");
                n = n +1 ; 
                if (n == 68) break; 
            }
            while (n > 67) n = n - 1; 
            return n; 
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(n), IntegerLit(0)), WhileStmt(BinExpr(<, Id(n), IntegerLit(69)), BlockStmt([CallStmt(printString, StringLit(Tran Ngoc Bao Duy)), AssignStmt(Id(n), BinExpr(+, Id(n), IntegerLit(1))), IfStmt(BinExpr(==, Id(n), IntegerLit(68)), BreakStmt())])), WhileStmt(BinExpr(>, Id(n), IntegerLit(67)), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1)))), ReturnStmt(Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
    def test_ifelse_do_nothing11111(self): 
        """More complex program"""
        input =	"""x: integer = 65;
        fact: function integer (n: integer) {
            n = 0; 
            while (n < 69){
                printString("Tran Ngoc Bao Duy");
                n = n +1 ; 
                if (n == 68) break; 
                else continue; 
            }
            while (n > 67) n = n - 1; 
            return n; 
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(n), IntegerLit(0)), WhileStmt(BinExpr(<, Id(n), IntegerLit(69)), BlockStmt([CallStmt(printString, StringLit(Tran Ngoc Bao Duy)), AssignStmt(Id(n), BinExpr(+, Id(n), IntegerLit(1))), IfStmt(BinExpr(==, Id(n), IntegerLit(68)), BreakStmt(), ContinueStmt())])), WhileStmt(BinExpr(>, Id(n), IntegerLit(67)), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1)))), ReturnStmt(Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))
    def test_ifelse_do_nothing111111(self): 
        """More complex program"""
        input =	"""x: integer = 65;
        main: function integer () {
            a: float = 2.0;
            a = 6.9; 
            b: array [2022] of integer;
            b[0] = 0;
            for (b = 0, b[0] < 1, b[0] + 1) b[1] = 0; 
            return 0; 
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(a, FloatType, FloatLit(2.0)), AssignStmt(Id(a), FloatLit(6.9)), VarDecl(b, ArrayType([2022], IntegerType)), AssignStmt(ArrayCell(b, [IntegerLit(0)]), IntegerLit(0)), ForStmt(AssignStmt(Id(b), IntegerLit(0)), BinExpr(<, ArrayCell(b, [IntegerLit(0)]), IntegerLit(1)), BinExpr(+, ArrayCell(b, [IntegerLit(0)]), IntegerLit(1)), AssignStmt(ArrayCell(b, [IntegerLit(1)]), IntegerLit(0))), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    def test_ifelse_do_nothing11112(self): 
        """More complex program"""
        input =	"""x: integer = 65;
        fact: function integer (n: integer) {
            n = 0; 
            while (n < 69){
                printString("Tran Ngoc Bao Duy");
                n = n +1 ; 
                if (n == 68) break; 
                else continue; 
            }
            while (n > 67) n = n - 1; 
            return n; 
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(n), IntegerLit(0)), WhileStmt(BinExpr(<, Id(n), IntegerLit(69)), BlockStmt([CallStmt(printString, StringLit(Tran Ngoc Bao Duy)), AssignStmt(Id(n), BinExpr(+, Id(n), IntegerLit(1))), IfStmt(BinExpr(==, Id(n), IntegerLit(68)), BreakStmt(), ContinueStmt())])), WhileStmt(BinExpr(>, Id(n), IntegerLit(67)), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1)))), ReturnStmt(Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))
    def test_ifelse_do_nothing11113(self): 
        """More complex program"""
        input =	"""
        iOT : function string (inherit SE: integer, inherit out DBS: string, out FS: string) inherit dADN{
                result: string = "CE"; 
                readInteger();
                printString(DBS);
                result = result + "CS"; 
                return result; 
        }
        main: function integer () {
            a: float = 2_8.01 + 11.11;
            b: array [3,3] of float; 
            b: array [2022] of integer; 
            IOT(221,"Oracle","Adafruit MQTT"); 
            for (i = 0, i < 2022, i + 1) b[i] = 0; 
            return 0; 
        }"""
        expect = """Program([
	FuncDecl(iOT, StringType, [InheritParam(SE, IntegerType), InheritOutParam(DBS, StringType), OutParam(FS, StringType)], dADN, BlockStmt([VarDecl(result, StringType, StringLit(CE)), CallStmt(readInteger, ), CallStmt(printString, Id(DBS)), AssignStmt(Id(result), BinExpr(+, Id(result), StringLit(CS))), ReturnStmt(Id(result))]))
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(a, FloatType, BinExpr(+, FloatLit(28.01), FloatLit(11.11))), VarDecl(b, ArrayType([3, 3], FloatType)), VarDecl(b, ArrayType([2022], IntegerType)), CallStmt(IOT, IntegerLit(221), StringLit(Oracle), StringLit(Adafruit MQTT)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2022)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(b, [Id(i)]), IntegerLit(0))), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))
    def test_fundecl_with_arrayParam_stmt(self):
        """More complex program"""
        input = """calYear: function void (a: array [2_8] of integer) {
            printInteger(4); 
            if (a[0,0] < 10) a[0,3] = a[0,1];
            else {
                for (i = 0 , i < 8, i+1) a[0,i] = 2010 + i; 
            } 
        }"""
        expect = """Program([
	FuncDecl(calYear, VoidType, [Param(a, ArrayType([28], IntegerType))], None, BlockStmt([CallStmt(printInteger, IntegerLit(4)), IfStmt(BinExpr(<, ArrayCell(a, [IntegerLit(0), IntegerLit(0)]), IntegerLit(10)), AssignStmt(ArrayCell(a, [IntegerLit(0), IntegerLit(3)]), ArrayCell(a, [IntegerLit(0), IntegerLit(1)])), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(8)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(a, [IntegerLit(0), Id(i)]), BinExpr(+, IntegerLit(2010), Id(i))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
    def test_fundecl_with_arrayParam_calExpr(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
            a: array [2_8] of integer; 
            a[0,0] = 1111; 
            a[0,1] = 2022; 
            a[0,0] = a[0,1] / 2 - 11 + 1000 * 2; 
            printInteger(a[0,0]); 
            return 0; 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4)), VarDecl(a, ArrayType([28], IntegerType)), AssignStmt(ArrayCell(a, [IntegerLit(0), IntegerLit(0)]), IntegerLit(1111)), AssignStmt(ArrayCell(a, [IntegerLit(0), IntegerLit(1)]), IntegerLit(2022)), AssignStmt(ArrayCell(a, [IntegerLit(0), IntegerLit(0)]), BinExpr(+, BinExpr(-, BinExpr(/, ArrayCell(a, [IntegerLit(0), IntegerLit(1)]), IntegerLit(2)), IntegerLit(11)), BinExpr(*, IntegerLit(1000), IntegerLit(2)))), CallStmt(printInteger, ArrayCell(a, [IntegerLit(0), IntegerLit(0)])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))
    def test_comp_expr_if_stmt(self): 
        input = """main: function void () {
            a,b: integer = 0,1; 
            if ((a > b) && (b < 0) || (a < b) && (a == 0)) printString("Saitama Sensei"); 
            else {donothing: integer = 2023;}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), VarDecl(b, IntegerType, IntegerLit(1)), IfStmt(BinExpr(&&, BinExpr(||, BinExpr(&&, BinExpr(>, Id(a), Id(b)), BinExpr(<, Id(b), IntegerLit(0))), BinExpr(<, Id(a), Id(b))), BinExpr(==, Id(a), IntegerLit(0))), CallStmt(printString, StringLit(Saitama Sensei)), BlockStmt([VarDecl(donothing, IntegerType, IntegerLit(2023))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))
# if (a > b && b < 0 || a < b && a == 0) printString("Saitama Sensei"); 
    def test_calc_expr_if_stmt(self): 
        input = """main: function void () {
            a,b: integer = 0,1; 
            if (a < 2023) a = 100 * 7 - 4 + 68 * 120 / 64 % 34;
            else b = 88 - 4 * 7 - 4 * 2 - 4 - 5 / 5 + 1;
            printInteger(a); 
            printInteger(b); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), VarDecl(b, IntegerType, IntegerLit(1)), IfStmt(BinExpr(<, Id(a), IntegerLit(2023)), AssignStmt(Id(a), BinExpr(+, BinExpr(-, BinExpr(*, IntegerLit(100), IntegerLit(7)), IntegerLit(4)), BinExpr(%, BinExpr(/, BinExpr(*, IntegerLit(68), IntegerLit(120)), IntegerLit(64)), IntegerLit(34)))), AssignStmt(Id(b), BinExpr(+, BinExpr(-, BinExpr(-, BinExpr(-, BinExpr(-, IntegerLit(88), BinExpr(*, IntegerLit(4), IntegerLit(7))), BinExpr(*, IntegerLit(4), IntegerLit(2))), IntegerLit(4)), BinExpr(/, IntegerLit(5), IntegerLit(5))), IntegerLit(1)))), CallStmt(printInteger, Id(a)), CallStmt(printInteger, Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))
    def test_scope_expr(self): 
        input = """main: function void () {
            s: string = "HCM"::"UT";
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(s, StringType, BinExpr(::, StringLit(HCM), StringLit(UT)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))
    def test_calc_mixed_expr_if_stmt1(self): 
        input = """
                a:float = 1_000 % 2 + .2E-10  + 8.98;
                b:float = (1 - 1) * 2 / 2 / 2 + 8 % 3 + ---10 * !!!true&&false;
        """
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(+, BinExpr(+, BinExpr(%, IntegerLit(1000), IntegerLit(2)), FloatLit(2e-11)), FloatLit(8.98)))
	VarDecl(b, FloatType, BinExpr(&&, BinExpr(+, BinExpr(+, BinExpr(/, BinExpr(/, BinExpr(*, BinExpr(-, IntegerLit(1), IntegerLit(1)), IntegerLit(2)), IntegerLit(2)), IntegerLit(2)), BinExpr(%, IntegerLit(8), IntegerLit(3))), BinExpr(*, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(10)))), UnExpr(!, UnExpr(!, UnExpr(!, BooleanLit(True)))))), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))
    def test_calc_mixed_expr_if_stmt2(self): 
        input = """main: function void () {
            a,b: integer = 0,1; 
            if (a < 2023) a = 100 * 7 - 4 + 68 * 120 / 64 % 34;
            else b = (1 + 2 == 3) || (3 + 4 >= 8);
            printInteger(a); 
            printInteger(b); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), VarDecl(b, IntegerType, IntegerLit(1)), IfStmt(BinExpr(<, Id(a), IntegerLit(2023)), AssignStmt(Id(a), BinExpr(+, BinExpr(-, BinExpr(*, IntegerLit(100), IntegerLit(7)), IntegerLit(4)), BinExpr(%, BinExpr(/, BinExpr(*, IntegerLit(68), IntegerLit(120)), IntegerLit(64)), IntegerLit(34)))), AssignStmt(Id(b), BinExpr(||, BinExpr(==, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), BinExpr(>=, BinExpr(+, IntegerLit(3), IntegerLit(4)), IntegerLit(8))))), CallStmt(printInteger, Id(a)), CallStmt(printInteger, Id(b))]))
])"""
# b = 1 + 2 == 3 || 3 + 4 >= 8;
        self.assertTrue(TestAST.test(input, expect, 365))
    def test_callexpr(self): 
        input = """
        binToDec: function integer (input: string, out result: integer){
        
        }
        main: function void (){
        a: float = binToDec("1111"); 
        }"""
        expect = """Program([
	FuncDecl(binToDec, IntegerType, [Param(input, StringType), OutParam(result, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FuncCall(binToDec, [StringLit(1111)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))
    def test_subexpr(self): 
        input = """

        main: function void (){
        a: float = (3.01 - 28.01) + (7.03 - 3.01); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, BinExpr(+, BinExpr(-, FloatLit(3.01), FloatLit(28.01)), BinExpr(-, FloatLit(7.03), FloatLit(3.01))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))
    def test_StringChar(self): 
        input = """
        main: function void (){
        checker: boolean = True; 
        if (!checker) printString("Don't look for me"); 
        else printString("Everything Goes On");
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(checker, BooleanType, Id(True)), IfStmt(UnExpr(!, Id(checker)), CallStmt(printString, StringLit(Don't look for me)), CallStmt(printString, StringLit(Everything Goes On)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))
    def test_unaryExpr2(self): 
        input = """

        main: function void (){
        hcmut = 21; 
        hcmut = 21 + -1; 
        printString("HCMUT"::"K20"); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(hcmut), IntegerLit(21)), AssignStmt(Id(hcmut), BinExpr(+, IntegerLit(21), UnExpr(-, IntegerLit(1)))), CallStmt(printString, BinExpr(::, StringLit(HCMUT), StringLit(K20)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))
    def test_calc_mixed_expr_if_stmt3(self): 
        input = """main: function void () {
            a,b: integer = 0,1; 
            if (a < 2023) a = 100 * 7 + -4 + 68/ 64 % 34;
            else b = !(1 + 2 == 3) || 3 + 4 >= 8;
            printInteger(a); 
            printInteger(b); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), VarDecl(b, IntegerType, IntegerLit(1)), IfStmt(BinExpr(<, Id(a), IntegerLit(2023)), AssignStmt(Id(a), BinExpr(+, BinExpr(+, BinExpr(*, IntegerLit(100), IntegerLit(7)), UnExpr(-, IntegerLit(4))), BinExpr(%, BinExpr(/, IntegerLit(68), IntegerLit(64)), IntegerLit(34)))), AssignStmt(Id(b), BinExpr(>=, BinExpr(||, UnExpr(!, BinExpr(==, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3))), BinExpr(+, IntegerLit(3), IntegerLit(4))), IntegerLit(8)))), CallStmt(printInteger, Id(a)), CallStmt(printInteger, Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))
    def test_calc_mixed_expr_if_stmt4(self): 
        input = """main : function void() {
                x : integer ;
                if(x==3){} else {z : integer = 3;}
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([]), BlockStmt([VarDecl(z, IntegerType, IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371)) 
    def test_ArrayCell(self): 
        input = """main : function void() {
                a: array [16,16] of integer; 
                b: integer;
                b = a[15,15]; 
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([16, 16], IntegerType)), VarDecl(b, IntegerType), AssignStmt(Id(b), ArrayCell(a, [IntegerLit(15), IntegerLit(15)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_compare_easy1(self): 
        input = """main : function void() {
                a: integer = 1990; 
                b: float = 19_75e2;  
                if (a >= b) {a = b; }
                if (a <= b) {a = a + 1;}
                if (a == b) {b = b + 1; }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1990)), VarDecl(b, FloatType, FloatLit(197500.0)), IfStmt(BinExpr(>=, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))])), IfStmt(BinExpr(<=, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), IfStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))
    def test_compare_easy2(self): 
        input = """main : function void() {
                a: integer = 1990; 
                b: float = 19_75e2;  
                if (a > b) {a = b; }
                if (a < b) {a = a + 1;}
                if (a != b) {b = b + 1; }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1990)), VarDecl(b, FloatType, FloatLit(197500.0)), IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), Id(b))])), IfStmt(BinExpr(<, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), IfStmt(BinExpr(!=, Id(a), Id(b)), BlockStmt([AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))
    def test_compare_hard1(self): 
        input = """main : function void() {
                a: integer = 2002; 
                b: integer = 2000;  
                c: boolean = (a >= b); 
        }"""
# c: boolean = a >= b <= 2000 == 1968 != 1970 < 2022 > 2023;
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(2002)), VarDecl(b, IntegerType, IntegerLit(2000)), VarDecl(c, BooleanType, BinExpr(>=, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))
    def test_compare_hard2(self): 
        input = """main : function void() {
                a: integer = 2002; 
                b: integer = 2000;  
                c: boolean = a >= (b + 2 / (4 % 4)); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(2002)), VarDecl(b, IntegerType, IntegerLit(2000)), VarDecl(c, BooleanType, BinExpr(>=, Id(a), BinExpr(+, Id(b), BinExpr(/, IntegerLit(2), BinExpr(%, IntegerLit(4), IntegerLit(4))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))
    def test_compare_easy3(self): 
        input = """main : function void() {
                a: integer = 2002; 
                b: array [10] of integer;  
                if (b[0] > a) a = b[0]; 
                else b[0] = a; 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(2002)), VarDecl(b, ArrayType([10], IntegerType)), IfStmt(BinExpr(>, ArrayCell(b, [IntegerLit(0)]), Id(a)), AssignStmt(Id(a), ArrayCell(b, [IntegerLit(0)])), AssignStmt(ArrayCell(b, [IntegerLit(0)]), Id(a)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))
    def test_compare_easy4(self):
        input = """
            x : integer;
            main : function void () {count(1/100,2027*2028+1);}
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(count, BinExpr(/, IntegerLit(1), IntegerLit(100)), BinExpr(+, BinExpr(*, IntegerLit(2027), IntegerLit(2028)), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))
    def test_autoParam(self):
        input = '''
            main : function void (x : auto) {}
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))
    def test_autoFunction(self):
        input = '''
                main : function auto (inherit out x : auto){}
        '''
        expect = """Program([
	FuncDecl(main, AutoType, [InheritOutParam(x, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))
    def test_ArrayStmtIn_Ifstmt1(self):
        input = '''
            arr : array [5,6] of integer;
            x : integer = 1111;
            main : function void() {
                if(x==1111) {
                    arr[3,4] = 5;
                }
                else {
                    arr[0,1] = 1 ;
                }
            }
        '''
        expect = """Program([
	VarDecl(arr, ArrayType([5, 6], IntegerType))
	VarDecl(x, IntegerType, IntegerLit(1111))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1111)), BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(3), IntegerLit(4)]), IntegerLit(5))]), BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))
    def test_ArrayStmt2ParamIn_Ifstmt1(self):
        input = '''
            arr : array [6_4,6_4] of integer;
            x : integer = 11_11;
            main : function void() {
                if(x==1111) {
                    arr[3,4] = arr[1,2];
                }
                else {
                    arr[0,1] = arr[1,0] ;
                }
            }
        '''
        expect = """Program([
	VarDecl(arr, ArrayType([64, 64], IntegerType))
	VarDecl(x, IntegerType, IntegerLit(1111))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1111)), BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(3), IntegerLit(4)]), ArrayCell(arr, [IntegerLit(1), IntegerLit(2)]))]), BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(0), IntegerLit(1)]), ArrayCell(arr, [IntegerLit(1), IntegerLit(0)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))
    def test_VarDeclInIf(self):
        input = '''
            main : function void() {
                p : integer ;
                if(p==3){
                   l : integer ;
                    if(l==4) {ppl222 : integer = 4;}
                }
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(p, IntegerType), IfStmt(BinExpr(==, Id(p), IntegerLit(3)), BlockStmt([VarDecl(l, IntegerType), IfStmt(BinExpr(==, Id(l), IntegerLit(4)), BlockStmt([VarDecl(ppl222, IntegerType, IntegerLit(4))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_VarDeclInIfElse(self):
        input = '''
            main : function void() {
                p : integer ;
                if(p==3){
                    l : integer ;
                    if(l==4) {ppl222 : integer = 4;}
                    else {
                        ppl222 : integer = 5;
                    }
                }
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(p, IntegerType), IfStmt(BinExpr(==, Id(p), IntegerLit(3)), BlockStmt([VarDecl(l, IntegerType), IfStmt(BinExpr(==, Id(l), IntegerLit(4)), BlockStmt([VarDecl(ppl222, IntegerType, IntegerLit(4))]), BlockStmt([VarDecl(ppl222, IntegerType, IntegerLit(5))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_IfelseInIfElse(self):
        "If else in if else"
        input = '''
            main : function void() {
             p :integer ;
                 if(p==3){
                    l : integer ;
                    if(l==4) {ppl222 : integer = 4;}
                    else {
                    ppl222 : integer = 5;
                    }
                } else { ppl222 : integer = 3;}
            }
        '''
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(p, IntegerType), IfStmt(BinExpr(==, Id(p), IntegerLit(3)), BlockStmt([VarDecl(l, IntegerType), IfStmt(BinExpr(==, Id(l), IntegerLit(4)), BlockStmt([VarDecl(ppl222, IntegerType, IntegerLit(4))]), BlockStmt([VarDecl(ppl222, IntegerType, IntegerLit(5))]))]), BlockStmt([VarDecl(ppl222, IntegerType, IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))
    def test_CONCATSTRING(self):
        input = """
                x: string = "Everything";
                y: string = "Goes On";
                z: string = x::y;
        """
        expect = """Program([
	VarDecl(x, StringType, StringLit(Everything))
	VarDecl(y, StringType, StringLit(Goes On))
	VarDecl(z, StringType, BinExpr(::, Id(x), Id(y)))
])"""
        self.assertTrue(TestAST.test(input,expect,386))
    def test_CONCATSTRING2(self):
        input = """
                x: string = "He asked me: ";
                y: string = "Where is John";
                z: string = x::y;
        """
        expect = """Program([
	VarDecl(x, StringType, StringLit(He asked me: ))
	VarDecl(y, StringType, StringLit(Where is John))
	VarDecl(z, StringType, BinExpr(::, Id(x), Id(y)))
])"""
        self.assertTrue(TestAST.test(input,expect,387))
    def test_STRING_HARD(self): 
        input = """ lolStr:string = "Test escape"; """
        expect = """Program([
	VarDecl(lolStr, StringType, StringLit(Test escape))
])"""
        self.assertTrue(TestAST.test(input,expect,388))
# " Test escape \\b \\f \\r \\n \\t \\' \\\\ "; """
    def test_FLOAT1(self): 
        input = """fl1:float = 4.;
                  fl2:float = .75e1; 
        """
        expect = """Program([
	VarDecl(fl1, FloatType, FloatLit(4.0))
	VarDecl(fl2, FloatType, FloatLit(7.5))
])"""
        self.assertTrue(TestAST.test(input,expect,389))
    def test_arrayAssign(self): 
        input = """
        a: array [3] of integer = {c+d, e*f, true, false};
        """
        expect = """Program([
	VarDecl(a, ArrayType([3], IntegerType), ArrayLit([BinExpr(+, Id(c), Id(d)), BinExpr(*, Id(e), Id(f)), BooleanLit(True), BooleanLit(False)]))
])"""
        self.assertTrue(TestAST.test(input,expect,390))
    def test_arrAssign2(self): 
        input = """
        a,b: array [3] of integer = {c+d, e*f} , {1,2,3};
        """
        expect = """Program([
	VarDecl(a, ArrayType([3], IntegerType), ArrayLit([BinExpr(+, Id(c), Id(d)), BinExpr(*, Id(e), Id(f))]))
	VarDecl(b, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input,expect,391))
    def test_arrAssign3(self): 
        input = """
        a,b: array [3] of integer = c,d;
        """
        expect = """Program([
	VarDecl(a, ArrayType([3], IntegerType), Id(c))
	VarDecl(b, ArrayType([3], IntegerType), Id(d))
])"""
        self.assertTrue(TestAST.test(input,expect,392))
    def test_whileIfInFor(self):
        input = """ 
        getHigh: function integer (inherit out well: integer) {
            while (well > 10) {
            if (well < 15) break;
            else continue; 
            for (i = well, i > 0, i-1) {
                printString("I can do it"); 
                }
            well = well - 1; 
            }
        return well; 
        }"""
        expect = """Program([
	FuncDecl(getHigh, IntegerType, [InheritOutParam(well, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(>, Id(well), IntegerLit(10)), BlockStmt([IfStmt(BinExpr(<, Id(well), IntegerLit(15)), BreakStmt(), ContinueStmt()), ForStmt(AssignStmt(Id(i), Id(well)), BinExpr(>, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printString, StringLit(I can do it))])), AssignStmt(Id(well), BinExpr(-, Id(well), IntegerLit(1)))])), ReturnStmt(Id(well))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))
    def test_DowhileInFor(self):
        input = """ 
        getHigh: function integer (inherit out well: integer) {
            do {
                for (i = well, i > 0, i-1) {
                printString("I can do it"); 
                }
                well = well - 1; 
            }
            while (well > 20);
        return well - 20; 
        }"""
        expect = """Program([
	FuncDecl(getHigh, IntegerType, [InheritOutParam(well, IntegerType)], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(well), IntegerLit(20)), BlockStmt([ForStmt(AssignStmt(Id(i), Id(well)), BinExpr(>, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printString, StringLit(I can do it))])), AssignStmt(Id(well), BinExpr(-, Id(well), IntegerLit(1)))])), ReturnStmt(BinExpr(-, Id(well), IntegerLit(20)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))
    def test_getMax(self):
        input = """ 
        getMax: function integer (inherit a: array [4] of integer) {
            max: integer = 0; 
            for (i = 0, i < 4,i + 1){
                if (a[i] > max) max = a[i]; 
            }
            return max; 
        }
        """
        expect = """Program([
	FuncDecl(getMax, IntegerType, [InheritParam(a, ArrayType([4], IntegerType))], None, BlockStmt([VarDecl(max, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(a, [Id(i)]), Id(max)), AssignStmt(Id(max), ArrayCell(a, [Id(i)])))])), ReturnStmt(Id(max))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
    def test_whileInForCallExpr(self):
        input = """ 
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer,delta: array [1] of integer) {
            i: integer; 
            for (i = 0, i < fact(10), i + 1) {
                    while (fact(10) > 69) break; 
                continue; 
            }
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, ArrayType([1], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(fact, [IntegerLit(10)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(>, FuncCall(fact, [IntegerLit(10)]), IntegerLit(69)), BreakStmt()), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
    def test_whileInForCallExpr(self):
        input = """ 
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer,delta: array [1] of integer) {
            i: integer; 
            for (i = 0, i < fact(10), i + 1) {
                    while (fact(10) > 69) break; 
                continue; 
            }
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, ArrayType([1], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(fact, [IntegerLit(10)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(>, FuncCall(fact, [IntegerLit(10)]), IntegerLit(69)), BreakStmt()), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
    def test_whileInFor(self):
        input = """ 
        inc: function void(out n: integer,delta: array [1] of integer) {
            i: integer; 
            for (i = 0, i < delta[11], i + 1) {
                    while (delta[11] < 69) break; 
            }
        }
        main: function void() {
            delta: array [15] of integer; 
            inc(x, delta);
            printInteger(x);
        }"""
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, ArrayType([1], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), ArrayCell(delta, [IntegerLit(11)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(<, ArrayCell(delta, [IntegerLit(11)]), IntegerLit(69)), BreakStmt())]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, ArrayType([15], IntegerType)), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))
    
    def testCallExprInExpr(self):
        input = """ 
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + fact(0);
        }
        """
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), FuncCall(fact, [IntegerLit(0)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))
    
    def test_full_program(self):
        """Test full program"""
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))
    def test_expr_function_with_array_comment(self): 
        input =  """bubbleSort: function void (arr: array [1_0] of integer , size: integer) inherit sort {
        for (i = 0, i < size - 1, i + 1){
        // Last i elements are already in place
        for (j = 0, j < size - i - 1, j + 1)
            if (arr[j] > arr[j + 1]){
                temp: integer = arr[j]; 
                arr[j] = arr[i]; 
                arr[j] = temp; 
            }
        }
}"""
        expect = """Program([
	FuncDecl(bubbleSort, VoidType, [Param(arr, ArrayType([10], IntegerType)), Param(size, IntegerType)], sort, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(size), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), BinExpr(-, BinExpr(-, Id(size), Id(i)), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), IfStmt(BinExpr(>, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), BlockStmt([VarDecl(temp, IntegerType, ArrayCell(arr, [Id(j)])), AssignStmt(ArrayCell(arr, [Id(j)]), ArrayCell(arr, [Id(i)])), AssignStmt(ArrayCell(arr, [Id(j)]), Id(temp))])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
    def test_expr_function_with_array_comment2(self): 
        input =  """bFS: function void (arr: array [1_0,1_0] of integer , size: integer) {
        visited: array [1000] of boolean;
        for (i = 0, i < size - 1, i + 1) visited[i] = false; 
        queue: array [1000] of integer;
        front,rear: integer = 0,0;
        visited[9] = true;
        queue[1] = size;
        while (front != rear){
            s = queue[9];
            front = front + 1; 
            printInteger(s);
        for (adjacent = 0, adjacent < g, adjacent +1)
                {
            if (adj[8,7] && !visited[9]) {
                visited[9] = true;
                queue[9] = adjacent;
                front = front +1; 
            }
        }
    }
}"""
        expect = """Program([
	FuncDecl(bFS, VoidType, [Param(arr, ArrayType([10, 10], IntegerType)), Param(size, IntegerType)], None, BlockStmt([VarDecl(visited, ArrayType([1000], BooleanType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(size), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(visited, [Id(i)]), BooleanLit(False))), VarDecl(queue, ArrayType([1000], IntegerType)), VarDecl(front, IntegerType, IntegerLit(0)), VarDecl(rear, IntegerType, IntegerLit(0)), AssignStmt(ArrayCell(visited, [IntegerLit(9)]), BooleanLit(True)), AssignStmt(ArrayCell(queue, [IntegerLit(1)]), Id(size)), WhileStmt(BinExpr(!=, Id(front), Id(rear)), BlockStmt([AssignStmt(Id(s), ArrayCell(queue, [IntegerLit(9)])), AssignStmt(Id(front), BinExpr(+, Id(front), IntegerLit(1))), CallStmt(printInteger, Id(s)), ForStmt(AssignStmt(Id(adjacent), IntegerLit(0)), BinExpr(<, Id(adjacent), Id(g)), BinExpr(+, Id(adjacent), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, ArrayCell(adj, [IntegerLit(8), IntegerLit(7)]), UnExpr(!, ArrayCell(visited, [IntegerLit(9)]))), BlockStmt([AssignStmt(ArrayCell(visited, [IntegerLit(9)]), BooleanLit(True)), AssignStmt(ArrayCell(queue, [IntegerLit(9)]), Id(adjacent)), AssignStmt(Id(front), BinExpr(+, Id(front), IntegerLit(1)))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
    def testReturnNoExpr(self):
        input = """ 
        fact: function integer (n: integer) {
            if (n == 0) return 1;
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + fact(0);
            return; 
        }
        """
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), FuncCall(fact, [IntegerLit(0)]))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 401))
    def test_e_in_float_with_no_INTPART_andDECPART(self): 
        input = """
        a:float = .e2;
        """
        expect = """Program([
	VarDecl(a, FloatType, FloatLit(0.0))
])"""
        self.assertTrue(TestAST.test(input,expect,402))
    