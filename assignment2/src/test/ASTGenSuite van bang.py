import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x: integer = 1.2;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, FloatLit(1.2))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_6(self):
        input = """main: function void () {
            printInteger(4);
            continue;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4)), ContinueStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_7(self):
        input = """main: function void() {
            if (x == 1) print(1); else print(x);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), CallStmt(print, IntegerLit(1)), CallStmt(print, Id(x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_8(self):
        input = """pascalTri: function integer(a: integer, b: integer){
            if ((a == 0) || (a == b)) return 1;
            return pascalTri(a - 1, b - 1) + pascalTri(a - 1, b);
        }
        main: function void(){
            input1, input2: integer = 5, 3;
            printInt(pascalTri(input1, input2));
        }
        """
        expect = """Program([
	FuncDecl(pascalTri, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(a), IntegerLit(0)), BinExpr(==, Id(a), Id(b))), ReturnStmt(IntegerLit(1))), ReturnStmt(BinExpr(+, FuncCall(pascalTri, [BinExpr(-, Id(a), IntegerLit(1)), BinExpr(-, Id(b), IntegerLit(1))]), FuncCall(pascalTri, [BinExpr(-, Id(a), IntegerLit(1)), Id(b)])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(input1, IntegerType, IntegerLit(5)), VarDecl(input2, IntegerType, IntegerLit(3)), CallStmt(printInt, FuncCall(pascalTri, [Id(input1), Id(input2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_9(self):
        input = """main: function void(){
            x, y: integer = 5, 3;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), VarDecl(y, IntegerType, IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_10(self):
        input = """main: function void(){
for(i = 0, i < 5, i + 1) {a: integer;}
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(a, IntegerType)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_11(self):
        input = """main: function void(){
if (x == 1)
    if (x == 2)
        if (x == 3) return 3;
        else return x;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), IfStmt(BinExpr(==, Id(x), IntegerLit(2)), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), ReturnStmt(IntegerLit(3)), ReturnStmt(Id(x)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_12(self):
        input = """main: function void(){
if (x == 1)
    if (x == 2)
        {if (x == 3) return 3;}
        else return x;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), IfStmt(BinExpr(==, Id(x), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), ReturnStmt(IntegerLit(3)))]), ReturnStmt(Id(x))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_13(self):
        input = """main: function void(){
if (x == 1) {
    if (x == 2) {
        if (x == 3) return 3;
    }
}        
else return x;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), ReturnStmt(IntegerLit(3)))]))]), ReturnStmt(Id(x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_14(self):
        input = """
swap: function void (out x: integer, out y: integer) {
    temp: integer = x;
    x = y;
    y = temp;
    return;
}
bubbleSort: function void (out a: array[2] of integer, size: integer) {
    i: integer;
    for (i = 1, i < size-1, 1) {
        for (j = i+1, j < size, 1) {
            if (a[i] < a[j]) swap(a[i], a[j]);
        } 
    }
    return;
}
main: function void(){
    n: integer = readInteger();
    a: array[10] of integer = {1,2,3,4,5,6,7,8,9};
    bubbleSort(a, n);
}"""
        expect = """Program([
	FuncDecl(swap, VoidType, [OutParam(x, IntegerType), OutParam(y, IntegerType)], None, BlockStmt([VarDecl(temp, IntegerType, Id(x)), AssignStmt(Id(x), Id(y)), AssignStmt(Id(y), Id(temp)), ReturnStmt()]))
	FuncDecl(bubbleSort, VoidType, [OutParam(a, ArrayType([2], IntegerType)), Param(size, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), BinExpr(-, Id(size), IntegerLit(1))), IntegerLit(1), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(size)), IntegerLit(1), BlockStmt([IfStmt(BinExpr(<, ArrayCell(a, [Id(i)]), ArrayCell(a, [Id(j)])), CallStmt(swap, ArrayCell(a, [Id(i)]), ArrayCell(a, [Id(j)])))]))])), ReturnStmt()]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), VarDecl(a, ArrayType([10], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9)])), CallStmt(bubbleSort, Id(a), Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_15(self):
        input = """
main: function void(){
    n: integer = readInteger();
    str: string = (("a"::"b")::"c")::"d";
    bubbleSort(a, n);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), VarDecl(str, StringType, BinExpr(::, BinExpr(::, BinExpr(::, StringLit(a), StringLit(b)), StringLit(c)), StringLit(d))), CallStmt(bubbleSort, Id(a), Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_16(self):
        input = """
main: function void(){}
foo: function array[1,1,1] of boolean(a: array[1] of string){}
goo: function auto(out b: auto){}
coo: function string(out b: float) inherit goo{}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(foo, ArrayType([1, 1, 1], BooleanType), [Param(a, ArrayType([1], StringType))], None, BlockStmt([]))
	FuncDecl(goo, AutoType, [OutParam(b, AutoType)], None, BlockStmt([]))
	FuncDecl(coo, StringType, [OutParam(b, FloatType)], goo, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_17(self):
        input = """
main: function void() {
    if (x == 1) return;
    else return;
    if (x == -2) return;
    else return;
    if (1 + 1 == 2 * 3) return;
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), ReturnStmt(), ReturnStmt()), IfStmt(BinExpr(==, Id(x), UnExpr(-, IntegerLit(2))), ReturnStmt(), ReturnStmt()), IfStmt(BinExpr(==, BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(*, IntegerLit(2), IntegerLit(3))), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_18(self):
        input = """main:function void() {
    a[1] = 3;
}"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_19(self):
        input = """
a: array[1,2] of integer;
b: array[2,2] of string = {"a", "b", "c", "d"};
main:function void() {
    a[1] = 3;
}"""
        expect = """Program([
	VarDecl(a, ArrayType([1, 2], IntegerType))
	VarDecl(b, ArrayType([2, 2], StringType), ArrayLit([StringLit(a), StringLit(b), StringLit(c), StringLit(d)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_20(self):
        input = """
main: function void() {
    if ((a == b) || (b == a)) return;
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(a), Id(b)), BinExpr(==, Id(b), Id(a))), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_21(self):
        input = """
main: function void() {
    if ((a + 1 < b + (2 * (3/(1||0)) == ((2 * 3) - 6 / 5 % 2)))) return;
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(<, BinExpr(+, Id(a), IntegerLit(1)), BinExpr(+, Id(b), BinExpr(==, BinExpr(*, IntegerLit(2), BinExpr(/, IntegerLit(3), BinExpr(||, IntegerLit(1), IntegerLit(0)))), BinExpr(-, BinExpr(*, IntegerLit(2), IntegerLit(3)), BinExpr(%, BinExpr(/, IntegerLit(6), IntegerLit(5)), IntegerLit(2)))))), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_22(self):
        input = """
main: function void() {
    for (i = 2,1,2) {
        
    }
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), IntegerLit(1), IntegerLit(2), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_23(self):
        input = """
main: function void() {
    while (true) {
        break;
    }
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_24(self):
        input = """
main: function void() {
    do {
        continue;
    } while (false);
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(False), BlockStmt([ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_25(self):
        input = """
main: function void() {
    a[i] = main();
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), FuncCall(main, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_26(self):
        input = """
main: function void() {
    for (i = 1, i < 100, 1) {
        if (n % i == 0) return false;
    }
    return true;
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), IntegerLit(1), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_27(self):
        input = """
main: function array[1] of float() {}
a: integer;
b,c: float;
d,e,f: string = 1,2,3;
g: auto;
h,i,j: array[2,2] of integer = {1,2,3,4}, 1, 1;
"""
        expect = """Program([
	FuncDecl(main, ArrayType([1], FloatType), [], None, BlockStmt([]))
	VarDecl(a, IntegerType)
	VarDecl(b, FloatType)
	VarDecl(c, FloatType)
	VarDecl(d, StringType, IntegerLit(1))
	VarDecl(e, StringType, IntegerLit(2))
	VarDecl(f, StringType, IntegerLit(3))
	VarDecl(g, AutoType)
	VarDecl(h, ArrayType([2, 2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(i, ArrayType([2, 2], IntegerType), IntegerLit(1))
	VarDecl(j, ArrayType([2, 2], IntegerType), IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_28(self):
        input = """
x: integer = 65;
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
        }
"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_29(self):
        input = """
a:array[100] of integer;
min: function integer(a: array[100] of integer) {
    min: integer = a[0];
    for (i = 0, i < 100, 1) {
        if (a[i] < min) min = a[i];
    }
    return a[i];
}
"""
        expect = """Program([
	VarDecl(a, ArrayType([100], IntegerType))
	FuncDecl(min, IntegerType, [Param(a, ArrayType([100], IntegerType))], None, BlockStmt([VarDecl(min, IntegerType, ArrayCell(a, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(100)), IntegerLit(1), BlockStmt([IfStmt(BinExpr(<, ArrayCell(a, [Id(i)]), Id(min)), AssignStmt(Id(min), ArrayCell(a, [Id(i)])))])), ReturnStmt(ArrayCell(a, [Id(i)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_30(self):
        input = """
a,b: integer = 129,123;
add: function integer(out b:integer, out a:integer) {
    return a+b;
}
"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(129))
	VarDecl(b, IntegerType, IntegerLit(123))
	FuncDecl(add, IntegerType, [OutParam(b, IntegerType), OutParam(a, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_31(self):
        input = """
key: integer = 129;
hash: function integer(inherit out a: integer) {
    return key % a;
}
"""
        expect = """Program([
	VarDecl(key, IntegerType, IntegerLit(129))
	FuncDecl(hash, IntegerType, [InheritOutParam(a, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(%, Id(key), Id(a)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_32(self):
        input = """
key: integer = 129;
hash: function integer(inherit key: integer) {
    return key || key;
}
"""
        expect = """Program([
	VarDecl(key, IntegerType, IntegerLit(129))
	FuncDecl(hash, IntegerType, [InheritParam(key, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(||, Id(key), Id(key)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_33(self):
        input = """
day: integer = readInteger();
DayOfWeek: function string(inherit day:integer) {
    if (day == 0) return "Sunday";
    else if (day == 1) return "Monday";
    else if (day == 1) return "Tuesday";
    else if (day == 1) return "Wednesday";
    else if (day == 1) return "Thursday";
    else if (day == 1) return "Friday";
    else if (day == 1) return "Saturday";
}
"""
        expect = """Program([
	VarDecl(day, IntegerType, FuncCall(readInteger, []))
	FuncDecl(DayOfWeek, StringType, [InheritParam(day, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(day), IntegerLit(0)), ReturnStmt(StringLit(Sunday)), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Monday)), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Tuesday)), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Wednesday)), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Thursday)), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Friday)), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Saturday)))))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_34(self):
        input = """
day: integer = readInteger();
DayOfWeek: function string(inherit day:integer) {
    if (day == 0) return "Sunday";
    if (day == 1) return "Monday";
    if (day == 1) return "Tuesday";
    if (day == 1) return "Wednesday";
    if (day == 1) return "Thursday";
    if (day == 1) return "Friday";
    if (day == 1) return "Saturday";
}
"""
        expect = """Program([
	VarDecl(day, IntegerType, FuncCall(readInteger, []))
	FuncDecl(DayOfWeek, StringType, [InheritParam(day, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(day), IntegerLit(0)), ReturnStmt(StringLit(Sunday))), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Monday))), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Tuesday))), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Wednesday))), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Thursday))), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Friday))), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Saturday)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_35(self):
        input = """
month: integer = readInteger();
DayOfWeek: function string(inherit month:integer) {
    a: array[12] of string = {"Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
    return a[month];
}
"""
        expect = """Program([
	VarDecl(month, IntegerType, FuncCall(readInteger, []))
	FuncDecl(DayOfWeek, StringType, [InheritParam(month, IntegerType)], None, BlockStmt([VarDecl(a, ArrayType([12], StringType), ArrayLit([StringLit(Jan), StringLit(Feb), StringLit(Mar), StringLit(Apr), StringLit(Jun), StringLit(Jul), StringLit(Aug), StringLit(Sep), StringLit(Oct), StringLit(Nov), StringLit(Dec)])), ReturnStmt(ArrayCell(a, [Id(month)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_36(self):
        input = """
year: integer = readInteger();
isLeapYear: function boolean(inherit year:integer) {
    return (year % 4 == 0) && ((year % 100 != 0) || (year % 400 == 0));
}
toString: function string(flag: boolean) {
    if (flag) printString("Is \\\"leap year\\\"");
    else printString("Is not \\\"leap year\\\"");
}
"""
        expect = """Program([
	VarDecl(year, IntegerType, FuncCall(readInteger, []))
	FuncDecl(isLeapYear, BooleanType, [InheritParam(year, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(&&, BinExpr(==, BinExpr(%, Id(year), IntegerLit(4)), IntegerLit(0)), BinExpr(||, BinExpr(!=, BinExpr(%, Id(year), IntegerLit(100)), IntegerLit(0)), BinExpr(==, BinExpr(%, Id(year), IntegerLit(400)), IntegerLit(0)))))]))
	FuncDecl(toString, StringType, [Param(flag, BooleanType)], None, BlockStmt([IfStmt(Id(flag), CallStmt(printString, StringLit(Is \\"leap year\\")), CallStmt(printString, StringLit(Is not \\"leap year\\")))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_37(self):
        input = """
x: boolean = true;
main: function integer(inherit x:integer) {
    if (x) if (x) if (x) if (x) if (x) if (x) if (x) break; else break; else break; else break;
}
"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	FuncDecl(main, IntegerType, [InheritParam(x, IntegerType)], None, BlockStmt([IfStmt(Id(x), IfStmt(Id(x), IfStmt(Id(x), IfStmt(Id(x), IfStmt(Id(x), IfStmt(Id(x), IfStmt(Id(x), BreakStmt(), BreakStmt()), BreakStmt()), BreakStmt())))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_38(self):
        input = """
x: boolean = true;
main: function integer(inherit x:integer) {
    while (true) break;
}
"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	FuncDecl(main, IntegerType, [InheritParam(x, IntegerType)], None, BlockStmt([WhileStmt(BooleanLit(True), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_39(self):
        input = """
x: boolean = true;
main: function integer(inherit x:integer) {
    a = b;
    a[i] = b[i];
    a[i] = b;
    b = a[i];
}
"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	FuncDecl(main, IntegerType, [InheritParam(x, IntegerType)], None, BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(ArrayCell(a, [Id(i)]), ArrayCell(b, [Id(i)])), AssignStmt(ArrayCell(a, [Id(i)]), Id(b)), AssignStmt(Id(b), ArrayCell(a, [Id(i)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_40(self):
        input = """
x: boolean = true;
main: function integer(inherit x:integer) {
    a = b - a;
    b = a - b;
    lst = a + b;
    return lst/x;
}
"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	FuncDecl(main, IntegerType, [InheritParam(x, IntegerType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(b), Id(a))), AssignStmt(Id(b), BinExpr(-, Id(a), Id(b))), AssignStmt(Id(lst), BinExpr(+, Id(a), Id(b))), ReturnStmt(BinExpr(/, Id(lst), Id(x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_41(self):
        input = """
x: boolean = true;
main: function integer(inherit x:integer) {}
y,z: string = true, 1;
foo: function float(inherit y: string) inherit main {}
"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	FuncDecl(main, IntegerType, [InheritParam(x, IntegerType)], None, BlockStmt([]))
	VarDecl(y, StringType, BooleanLit(True))
	VarDecl(z, StringType, IntegerLit(1))
	FuncDecl(foo, FloatType, [InheritParam(y, StringType)], main, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_42(self):
        input = """
x: boolean = true;
main: function integer(inherit x:integer) {}
y,z: string = true, 1;
foo: function float(inherit y: string) inherit main {
    for (i = y, i < z, i) {
        while (i) {
            if (z) {
                do {
                    return h;
                }
                while (y != z);
            }
        }
    }
}
"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	FuncDecl(main, IntegerType, [InheritParam(x, IntegerType)], None, BlockStmt([]))
	VarDecl(y, StringType, BooleanLit(True))
	VarDecl(z, StringType, IntegerLit(1))
	FuncDecl(foo, FloatType, [InheritParam(y, StringType)], main, BlockStmt([ForStmt(AssignStmt(Id(i), Id(y)), BinExpr(<, Id(i), Id(z)), Id(i), BlockStmt([WhileStmt(Id(i), BlockStmt([IfStmt(Id(z), BlockStmt([DoWhileStmt(BinExpr(!=, Id(y), Id(z)), BlockStmt([ReturnStmt(Id(h))]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_43(self):
        input = """
pi: float = .234e3;
abc: float = pi + 1;
"""
        expect = """Program([
	VarDecl(pi, FloatType, FloatLit(234.0))
	VarDecl(abc, FloatType, BinExpr(+, Id(pi), IntegerLit(1)))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_44(self):
        input = """
pi: float = 3.1415926e1;
abc: float = pi + 1;
isinstance: boolean = type(a) == type(b);
"""
        expect = """Program([
	VarDecl(pi, FloatType, FloatLit(31.415926))
	VarDecl(abc, FloatType, BinExpr(+, Id(pi), IntegerLit(1)))
	VarDecl(isinstance, BooleanType, BinExpr(==, FuncCall(type, [Id(a)]), FuncCall(type, [Id(b)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_45(self):
        input = """
str:string = "Hello"::"World" + {"!"};
"""
        expect = """Program([
	VarDecl(str, StringType, BinExpr(::, StringLit(Hello), BinExpr(+, StringLit(World), ArrayLit([StringLit(!)]))))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_46(self):
        input = """
a:auto = 123;
b:auto = a;
main:function void() {print(b);}
"""
        expect = """Program([
	VarDecl(a, AutoType, IntegerLit(123))
	VarDecl(b, AutoType, Id(a))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_47(self):
        input = """
interface: function integer() {}

foo:function integer(n:integer) inherit inteface {}
"""
        expect = """Program([
	FuncDecl(interface, IntegerType, [], None, BlockStmt([]))
	FuncDecl(foo, IntegerType, [Param(n, IntegerType)], inteface, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_48(self):
        input = """
plus: function integer(a: integer, b:integer) {return a+b;}

fplus: function float(a: float, b:float) {return a+b;}

splus: function string(a: string, b:string) {return a::b;}
"""
        expect = """Program([
	FuncDecl(plus, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(fplus, FloatType, [Param(a, FloatType), Param(b, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(splus, StringType, [Param(a, StringType), Param(b, StringType)], None, BlockStmt([ReturnStmt(BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_49(self):
        input = """
plus: function integer(a: integer, b:integer) {return a+b;}

fplus: function float(a: float, b:float) inherit plus{return a+b;}

splus: function string(a: string, b:string) inherit plus{return a::b;}
"""
        expect = """Program([
	FuncDecl(plus, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(fplus, FloatType, [Param(a, FloatType), Param(b, FloatType)], plus, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(splus, StringType, [Param(a, StringType), Param(b, StringType)], plus, BlockStmt([ReturnStmt(BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_50(self):
        input = """
plus: function integer(a: integer, b:integer) {return a+b;}

fplus: function float(a: float, b:float) inherit plus{return a+b;}

splus: function string(a: string, b:string) inherit plus{return a::b;}
"""
        expect = """Program([
	FuncDecl(plus, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(fplus, FloatType, [Param(a, FloatType), Param(b, FloatType)], plus, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(splus, StringType, [Param(a, StringType), Param(b, StringType)], plus, BlockStmt([ReturnStmt(BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_51(self):
        input = """
haha:function string(){return "haha";}
"""
        expect = """Program([
	FuncDecl(haha, StringType, [], None, BlockStmt([ReturnStmt(StringLit(haha))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_51(self):
        input = """x: integer = foo();"""
        expect = """Program([
	VarDecl(x, IntegerType, FuncCall(foo, []))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_52(self):
        input = """x, y, z: integer = a[2], "a[2]", {2};"""
        expect = """Program([
	VarDecl(x, IntegerType, ArrayCell(a, [IntegerLit(2)]))
	VarDecl(y, IntegerType, StringLit(a[2]))
	VarDecl(z, IntegerType, ArrayLit([IntegerLit(2)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_53(self):
        input = """x: integer = 1.2;
        a, b: float = x,x;"""
        expect = """Program([
	VarDecl(x, IntegerType, FloatLit(1.2))
	VarDecl(a, FloatType, Id(x))
	VarDecl(b, FloatType, Id(x))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_54(self):
        input = """main: function void () {foo();
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_55(self):
        input = """main: function void () {
            printInteger(isinstance(a, b));
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(isinstance, [Id(a), Id(b)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_56(self):
        input = """main: function void () {
            printInteger(4);
            continue;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4)), ContinueStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_57(self):
        input = """main: function void() {
            if (x == 1) print(1); else print(x);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), CallStmt(print, IntegerLit(1)), CallStmt(print, Id(x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_58(self):
        input = """pascalTri: function integer(a: integer, b: integer){
            if ((a == 0 || a) == b) return 1;
            return pascalTri(a - 1, b - 1) + pascalTri(a - 1, b);
        }
        main: function void(){
            input1, input2: integer = 5, 3;
            printInt(pascalTri(input1, input2));
        }
        """
        expect = """Program([
	FuncDecl(pascalTri, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(==, Id(a), BinExpr(||, IntegerLit(0), Id(a))), Id(b)), ReturnStmt(IntegerLit(1))), ReturnStmt(BinExpr(+, FuncCall(pascalTri, [BinExpr(-, Id(a), IntegerLit(1)), BinExpr(-, Id(b), IntegerLit(1))]), FuncCall(pascalTri, [BinExpr(-, Id(a), IntegerLit(1)), Id(b)])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(input1, IntegerType, IntegerLit(5)), VarDecl(input2, IntegerType, IntegerLit(3)), CallStmt(printInt, FuncCall(pascalTri, [Id(input1), Id(input2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_59(self):
        input = """main: function void(){
            x, y: integer = 5, 3;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(5)), VarDecl(y, IntegerType, IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_60(self):
        input = """main: function void(){
for(i = 0, i < 5, i + 1) {a: integer;}
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(a, IntegerType)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_61(self):
        input = """main: function void(){
if (x == 1)
    if (x == 2)
        if (x == 3) return 3;
        else return x;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), IfStmt(BinExpr(==, Id(x), IntegerLit(2)), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), ReturnStmt(IntegerLit(3)), ReturnStmt(Id(x)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_62(self):
        input = """main: function void(){
if (x == 1)
    if (x == 2)
        {if (x == 3) return 3;}
        else return x;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), IfStmt(BinExpr(==, Id(x), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), ReturnStmt(IntegerLit(3)))]), ReturnStmt(Id(x))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_63(self):
        input = """main: function void(){
if (x == 1) {
    if (x == 2) {
        if (x == 3) return 3;
    }
}        
else return x;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(3)), ReturnStmt(IntegerLit(3)))]))]), ReturnStmt(Id(x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_64(self):
        input = """
swap: function void (out x: integer, out y: integer) {
    temp: integer = x;
    x = y;
    y = temp;
    return;
}
bubbleSort: function void (out a: array[1] of integer, size: integer) {
    i: integer;
    for (i = 1, i < size-1, 1) {
        for (j = i+1, j < size, 1) {
            if (a[i] < a[j]) swap(a[i], a[j]);
        } 
    }
    return;
}
main: function void(){
    n: integer = readInteger();
    a: array[10] of integer = {1,2,3,4,5,6,7,8,9};
    bubbleSort(a, n);
}"""
        expect = """Program([
	FuncDecl(swap, VoidType, [OutParam(x, IntegerType), OutParam(y, IntegerType)], None, BlockStmt([VarDecl(temp, IntegerType, Id(x)), AssignStmt(Id(x), Id(y)), AssignStmt(Id(y), Id(temp)), ReturnStmt()]))
	FuncDecl(bubbleSort, VoidType, [OutParam(a, ArrayType([1], IntegerType)), Param(size, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), BinExpr(-, Id(size), IntegerLit(1))), IntegerLit(1), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(size)), IntegerLit(1), BlockStmt([IfStmt(BinExpr(<, ArrayCell(a, [Id(i)]), ArrayCell(a, [Id(j)])), CallStmt(swap, ArrayCell(a, [Id(i)]), ArrayCell(a, [Id(j)])))]))])), ReturnStmt()]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), VarDecl(a, ArrayType([10], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9)])), CallStmt(bubbleSort, Id(a), Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_65(self):
        input = """
main: function void(){
    n: integer = readInteger();
    str: string = (("a"::"b")::"c")::"d";
    bubbleSort(a, n);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(readInteger, [])), VarDecl(str, StringType, BinExpr(::, BinExpr(::, BinExpr(::, StringLit(a), StringLit(b)), StringLit(c)), StringLit(d))), CallStmt(bubbleSort, Id(a), Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_66(self):
        input = """
main: function void(){}
foo: function array[2] of string(a: array[1] of float){}
goo: function auto(out b: auto){}
coo: function string(out b: float) inherit goo{}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(foo, ArrayType([2], StringType), [Param(a, ArrayType([1], FloatType))], None, BlockStmt([]))
	FuncDecl(goo, AutoType, [OutParam(b, AutoType)], None, BlockStmt([]))
	FuncDecl(coo, StringType, [OutParam(b, FloatType)], goo, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_67(self):
        input = """
main: function void() {
    if (x == 1) return;
    else return;
    if (x == -2) return;
    else return;
    if (1 + 1 == 2 * 3) return;
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), ReturnStmt(), ReturnStmt()), IfStmt(BinExpr(==, Id(x), UnExpr(-, IntegerLit(2))), ReturnStmt(), ReturnStmt()), IfStmt(BinExpr(==, BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(*, IntegerLit(2), IntegerLit(3))), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_68(self):
        input = """main:function void() {
    a[1] = 3;
}"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_69(self):
        input = """
a: array[1,2] of integer;
b: array[2,2] of string = {"a", "b", "c", "d"};
main:function void() {
    a[1] = 3;
}"""
        expect = """Program([
	VarDecl(a, ArrayType([1, 2], IntegerType))
	VarDecl(b, ArrayType([2, 2], StringType), ArrayLit([StringLit(a), StringLit(b), StringLit(c), StringLit(d)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_70(self):
        input = """
main: function void() {
    if ((a == b) || (b == a)) return;
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(a), Id(b)), BinExpr(==, Id(b), Id(a))), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_71(self):
        input = """
main: function void() {
    if ((a + 1 < b + (2 * (3/(1||0)) == ((2 * 3) - 6 / 5 % 2)))) return;
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(<, BinExpr(+, Id(a), IntegerLit(1)), BinExpr(+, Id(b), BinExpr(==, BinExpr(*, IntegerLit(2), BinExpr(/, IntegerLit(3), BinExpr(||, IntegerLit(1), IntegerLit(0)))), BinExpr(-, BinExpr(*, IntegerLit(2), IntegerLit(3)), BinExpr(%, BinExpr(/, IntegerLit(6), IntegerLit(5)), IntegerLit(2)))))), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_72(self):
        input = """
main: function void() {
    for (i = 2,1,2) {
        
    }
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), IntegerLit(1), IntegerLit(2), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_73(self):
        input = """
main: function void() {
    while (true) {
        break;
    }
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_74(self):
        input = """
main: function void() {
    do {
        continue;
    } while (false);
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(False), BlockStmt([ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_75(self):
        input = """
main: function void() {
    a[i] = main();
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), FuncCall(main, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_76(self):
        input = """
main: function void() {
    for (i = 1, i < 100, 1) {
        if (n % i == 0) return false;
    }
    return true;
}
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), IntegerLit(1), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_77(self):
        input = """
main: function void() {}
a: integer;
b,c: float;
d,e,f: string = 1,2,3;
g: auto;
h,i,j: array[2,2] of integer = {1,2,3,4}, a, b;
"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	VarDecl(a, IntegerType)
	VarDecl(b, FloatType)
	VarDecl(c, FloatType)
	VarDecl(d, StringType, IntegerLit(1))
	VarDecl(e, StringType, IntegerLit(2))
	VarDecl(f, StringType, IntegerLit(3))
	VarDecl(g, AutoType)
	VarDecl(h, ArrayType([2, 2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(i, ArrayType([2, 2], IntegerType), Id(a))
	VarDecl(j, ArrayType([2, 2], IntegerType), Id(b))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_78(self):
        input = """
x: integer = 65;
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
        }
"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_79(self):
        input = """
a:array[100] of integer;
min: function integer(a: array[1] of integer) {
    min: integer = a[0];
    for (i = 0, i < 100, 1) {
        if (a[i] < min) min = a[i];
    }
    return a[i];
}
"""
        expect = """Program([
	VarDecl(a, ArrayType([100], IntegerType))
	FuncDecl(min, IntegerType, [Param(a, ArrayType([1], IntegerType))], None, BlockStmt([VarDecl(min, IntegerType, ArrayCell(a, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(100)), IntegerLit(1), BlockStmt([IfStmt(BinExpr(<, ArrayCell(a, [Id(i)]), Id(min)), AssignStmt(Id(min), ArrayCell(a, [Id(i)])))])), ReturnStmt(ArrayCell(a, [Id(i)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_80(self):
        input = """
a,b: integer = 129,123;
add: function integer(out b:integer, out a:integer) {
    return a+b;
}
"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(129))
	VarDecl(b, IntegerType, IntegerLit(123))
	FuncDecl(add, IntegerType, [OutParam(b, IntegerType), OutParam(a, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_81(self):
        input = """
key: integer = 129;
hash: function integer(inherit out a: integer) {
    return key % a;
}
"""
        expect = """Program([
	VarDecl(key, IntegerType, IntegerLit(129))
	FuncDecl(hash, IntegerType, [InheritOutParam(a, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(%, Id(key), Id(a)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_82(self):
        input = """
key: integer = 129;
hash: function integer(inherit key: integer) {
    return key || key;
}
"""
        expect = """Program([
	VarDecl(key, IntegerType, IntegerLit(129))
	FuncDecl(hash, IntegerType, [InheritParam(key, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(||, Id(key), Id(key)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_83(self):
        input = """
day: integer = readInteger();
DayOfWeek: function string(inherit day:integer) {
    if (day == 0) return "Sunday";
    else if (day == 1) return "Monday";
    else if (day == 1) return "Tuesday";
    else if (day == 1) return "Wednesday";
    else if (day == 1) return "Thursday";
    else if (day == 1) return "Friday";
    else if (day == 1) return "Saturday";
}
"""
        expect = """Program([
	VarDecl(day, IntegerType, FuncCall(readInteger, []))
	FuncDecl(DayOfWeek, StringType, [InheritParam(day, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(day), IntegerLit(0)), ReturnStmt(StringLit(Sunday)), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Monday)), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Tuesday)), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Wednesday)), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Thursday)), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Friday)), IfStmt(BinExpr(==, Id(day), IntegerLit(1)), ReturnStmt(StringLit(Saturday)))))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_84(self):
        input = """
str:function string(a: string) {
    a = "Hello world \\n";
}
"""
        expect = """Program([
	FuncDecl(str, StringType, [Param(a, StringType)], None, BlockStmt([AssignStmt(Id(a), StringLit(Hello world \\n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_85(self):
        input = """
month: integer = readInteger();
DayOfWeek: function string(inherit month:integer) {
    a: array[12] of string = {"Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
    return a[month];
}
"""
        expect = """Program([
	VarDecl(month, IntegerType, FuncCall(readInteger, []))
	FuncDecl(DayOfWeek, StringType, [InheritParam(month, IntegerType)], None, BlockStmt([VarDecl(a, ArrayType([12], StringType), ArrayLit([StringLit(Jan), StringLit(Feb), StringLit(Mar), StringLit(Apr), StringLit(Jun), StringLit(Jul), StringLit(Aug), StringLit(Sep), StringLit(Oct), StringLit(Nov), StringLit(Dec)])), ReturnStmt(ArrayCell(a, [Id(month)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_86(self):
        input = """
year: integer = readInteger();
isLeapYear: function boolean(inherit year:integer) {
    return (year % 4 == 0) && ((year % 100 != 0) || (year % 400 == 0));
}
"""
        expect = """Program([
	VarDecl(year, IntegerType, FuncCall(readInteger, []))
	FuncDecl(isLeapYear, BooleanType, [InheritParam(year, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(&&, BinExpr(==, BinExpr(%, Id(year), IntegerLit(4)), IntegerLit(0)), BinExpr(||, BinExpr(!=, BinExpr(%, Id(year), IntegerLit(100)), IntegerLit(0)), BinExpr(==, BinExpr(%, Id(year), IntegerLit(400)), IntegerLit(0)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_87(self):
        input = """
x: boolean = true;
main: function integer(inherit x:integer) {
    if (x) if (x) if (x) if (x) if (x) if (x) if (x) break;
}
"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	FuncDecl(main, IntegerType, [InheritParam(x, IntegerType)], None, BlockStmt([IfStmt(Id(x), IfStmt(Id(x), IfStmt(Id(x), IfStmt(Id(x), IfStmt(Id(x), IfStmt(Id(x), IfStmt(Id(x), BreakStmt())))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_88(self):
        input = """
x: boolean = true;
main: function integer(inherit x:integer) {
    while (true) break;
}
"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	FuncDecl(main, IntegerType, [InheritParam(x, IntegerType)], None, BlockStmt([WhileStmt(BooleanLit(True), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_89(self):
        input = """
x: boolean = true;
main: function integer(inherit x:integer) {
    a = b;
    a[i] = b[i];
    a[i] = b;
    b = a[i];
}
"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	FuncDecl(main, IntegerType, [InheritParam(x, IntegerType)], None, BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(ArrayCell(a, [Id(i)]), ArrayCell(b, [Id(i)])), AssignStmt(ArrayCell(a, [Id(i)]), Id(b)), AssignStmt(Id(b), ArrayCell(a, [Id(i)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_90(self):
        input = """
x: boolean = true;
main: function integer(inherit x:integer) {
    a = b - a;
    b = a - b;
    lst = a + b;
    return lst/x;
}
"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	FuncDecl(main, IntegerType, [InheritParam(x, IntegerType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(b), Id(a))), AssignStmt(Id(b), BinExpr(-, Id(a), Id(b))), AssignStmt(Id(lst), BinExpr(+, Id(a), Id(b))), ReturnStmt(BinExpr(/, Id(lst), Id(x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_91(self):
        input = """
x: boolean = true;
main: function integer(inherit x:integer) {}
y,z: string = true, 1;
foo: function float(inherit y: string) inherit main {}
"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	FuncDecl(main, IntegerType, [InheritParam(x, IntegerType)], None, BlockStmt([]))
	VarDecl(y, StringType, BooleanLit(True))
	VarDecl(z, StringType, IntegerLit(1))
	FuncDecl(foo, FloatType, [InheritParam(y, StringType)], main, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_92(self):
        input = """
x: boolean = true;
main: function integer(inherit x:integer) {}
y,z: string = true, 1;
foo: function float(inherit y: string) inherit main {
    for (i = y, i < z, i) {
        while (i) {
            if (z) {
                do {
                    return h;
                }
                while (y != z);
            }
        }
    }
}
"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	FuncDecl(main, IntegerType, [InheritParam(x, IntegerType)], None, BlockStmt([]))
	VarDecl(y, StringType, BooleanLit(True))
	VarDecl(z, StringType, IntegerLit(1))
	FuncDecl(foo, FloatType, [InheritParam(y, StringType)], main, BlockStmt([ForStmt(AssignStmt(Id(i), Id(y)), BinExpr(<, Id(i), Id(z)), Id(i), BlockStmt([WhileStmt(Id(i), BlockStmt([IfStmt(Id(z), BlockStmt([DoWhileStmt(BinExpr(!=, Id(y), Id(z)), BlockStmt([ReturnStmt(Id(h))]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_93(self):
        input = """
pi: float = .e3;
abc: float = pi + 1;
"""
        expect = """Program([
	VarDecl(pi, FloatType, FloatLit(0.0))
	VarDecl(abc, FloatType, BinExpr(+, Id(pi), IntegerLit(1)))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_94(self):
        input = """
pi: float = 1.234e6;
abc: float = pi + 1;
isinstance: boolean = type(a) == type(b);
"""
        expect = """Program([
	VarDecl(pi, FloatType, FloatLit(1234000.0))
	VarDecl(abc, FloatType, BinExpr(+, Id(pi), IntegerLit(1)))
	VarDecl(isinstance, BooleanType, BinExpr(==, FuncCall(type, [Id(a)]), FuncCall(type, [Id(b)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_95(self):
        input = """
str:string = "Hello"::"World" + {"!"};
"""
        expect = """Program([
	VarDecl(str, StringType, BinExpr(::, StringLit(Hello), BinExpr(+, StringLit(World), ArrayLit([StringLit(!)]))))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_96(self):
        input = """
a:auto = 123;
b:auto = a;
main:function void() {print(b);}
"""
        expect = """Program([
	VarDecl(a, AutoType, IntegerLit(123))
	VarDecl(b, AutoType, Id(a))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_97(self):
        input = """
interface: function integer() {}
foo:function integer(n:integer) inherit inteface {}
"""
        expect = """Program([
	FuncDecl(interface, IntegerType, [], None, BlockStmt([]))
	FuncDecl(foo, IntegerType, [Param(n, IntegerType)], inteface, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_98(self):
        input = """
plus: function integer(a: integer, b:integer) {return a+b;}
fplus: function float(a: float, b:float) {return a+b;}
splus: function string(a: string, b:string) {return a::b;}
"""
        expect = """Program([
	FuncDecl(plus, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(fplus, FloatType, [Param(a, FloatType), Param(b, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(splus, StringType, [Param(a, StringType), Param(b, StringType)], None, BlockStmt([ReturnStmt(BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_99(self):
        input = """
main: function void () {
            a:array [2] of integer = {1,2};
            B:integer;
            B = a[0] * a[1];
        }

"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)])), VarDecl(B, IntegerType), AssignStmt(Id(B), BinExpr(*, ArrayCell(a, [IntegerLit(0)]), ArrayCell(a, [IntegerLit(1)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_array_1(self):
        input = """
a:array[1] of integer = a[1] + 1;
"""
        expect = """Program([
	VarDecl(a, ArrayType([1], IntegerType), BinExpr(+, ArrayCell(a, [IntegerLit(1)]), IntegerLit(1)))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
    