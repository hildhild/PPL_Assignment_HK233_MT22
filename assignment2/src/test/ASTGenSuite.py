# Student ID: 2113481

import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
        300-309: Types & Literals
        310-324: Declarations
        325-344: Expressions
        345-374: Statements
        375-399: Mixed Cases
    """

    ##### TYPES & LITERALS #####
    def test300_single_atomic_types(self):
        input = """
            x: integer;
            y: float;
            z: string;
            t: boolean;
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, FloatType)
	VarDecl(z, StringType)
	VarDecl(t, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, expect, 300))


    def test302_array_types(self):
        input = """x: array [5] of integer;"""
        expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test303_atomic_types_with_init(self):
        input = """
            x: integer = 5;
            y: float = 5.5e5;
            z: string = "55";
            t: boolean = true;
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(5))
	VarDecl(y, FloatType, FloatLit(550000.0))
	VarDecl(z, StringType, StringLit(55))
	VarDecl(t, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test304_array_types_with_init(self):
        input = """x: array [5] of integer = {1,2,3,4,5};"""
        expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))


    def test306_assign_with_basic_literal(self):
        input = """
            main: function void(){
                a = 1;
                b = 1.1;
                c = "c";
                d = false;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(b), FloatLit(1.1)), AssignStmt(Id(c), StringLit(c)), AssignStmt(Id(d), BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test307_assign_with_array_literal(self):
        input = """main: function void(){
            a = {1,2,3,4};
            b = {};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), AssignStmt(Id(b), ArrayLit([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test308_assign_with_multiD_array_literal(self):
        input = """main: function void(){
            a = {1,{2,{3,4}}};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([IntegerLit(1), ArrayLit([IntegerLit(2), ArrayLit([IntegerLit(3), IntegerLit(4)])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test309_assign_with_mixed_array_literal(self):
        input = """main: function void(){
            a = {"1",2,false,abc,abcd()};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([StringLit(1), IntegerLit(2), BooleanLit(False), Id(abc), FuncCall(abcd, [])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    ##### DECLARATIONS #####
    def test310_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test311_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test312_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test313_full_vardecl_simple_expr(self):
        input = """x, y, z: integer = a, b, c;"""
        expect = """Program([
	VarDecl(x, IntegerType, Id(a))
	VarDecl(y, IntegerType, Id(b))
	VarDecl(z, IntegerType, Id(c))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test314_full_vardecl_complex_expr(self):
        input = """x, y, z: integer = hello(), a+5, !b;"""
        expect = """Program([
	VarDecl(x, IntegerType, FuncCall(hello, []))
	VarDecl(y, IntegerType, BinExpr(+, Id(a), IntegerLit(5)))
	VarDecl(z, IntegerType, UnExpr(!, Id(b)))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test315_empty_funcdecl(self):
        input = """main : function void(){}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test316_simple_empty_params_funcdecl(self):
        input = """main : function void(a:integer,b:string,c:boolean,d:float){}"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, IntegerType), Param(b, StringType), Param(c, BooleanType), Param(d, FloatType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test317_inherit_empty_funcdecl(self):
        input = """main : function void(out a:integer, inherit b:string) inherit supermain{}"""
        expect = """Program([
	FuncDecl(main, VoidType, [OutParam(a, IntegerType), InheritParam(b, StringType)], supermain, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test318_normal_funcdecl(self):
        input = """main : function void(){
                a = a+1;
                print(a);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), CallStmt(print, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test319_inherit_out_funcdecl(self):
        input = """main : function void(inherit out c: float) inherit supermain{}"""
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(c, FloatType)], supermain, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test320_mixed_decl1(self):
        input = """x: integer = 1;
        main : function void(){
            x = x+1;
            }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test321_mixed_decl2(self):
        input = """x: integer;
        main : function void(){
            x: float = 2.0;
            }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(2.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test322_mixed_decl3(self):
        input = """
        getTotal: function integer(x: integer, y:integer){
            return x+y;
        }
        main : function void(){
            x: integer = getTotal(1,2);
            }"""
        expect = """Program([
	FuncDecl(getTotal, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(x), Id(y)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, FuncCall(getTotal, [IntegerLit(1), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test323_mixed_decl4(self):
        input = """x: array [2] of integer = {1,2};
        main : function void(){
            x = {1,2,3};
            }"""
        expect = """Program([
	VarDecl(x, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test324_mixed_decl5(self):
        input = """x: array [2] of integer = {1,2};
        main : function void(x: auto){
            print(x);
            return;
            }"""
        expect = """Program([
	VarDecl(x, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
	FuncDecl(main, VoidType, [Param(x, AutoType)], None, BlockStmt([CallStmt(print, Id(x)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    ##### EXPRESSIONS #####
    def test325_empty_call_expr(self):
        input = """
        main: function void (){
            hello();
            good_boy();
            are_you_ok();
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(hello, ), CallStmt(good_boy, ), CallStmt(are_you_ok, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test326_index_1D_ops(self):
        input = """
        main: function void (){
            a[0] = 5;
            b[1] = "string";
            c[3] = 0.5e6;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(0)]), IntegerLit(5)), AssignStmt(ArrayCell(b, [IntegerLit(1)]), StringLit(string)), AssignStmt(ArrayCell(c, [IntegerLit(3)]), FloatLit(500000.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test327_index_ND_ops(self):
        input = """
        main: function void (){
            b[0,1] = "string";
            c[1,2,3] = 0.5e6;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(b, [IntegerLit(0), IntegerLit(1)]), StringLit(string)), AssignStmt(ArrayCell(c, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), FloatLit(500000.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test328_param_lit_call_expr(self):
        input = """
        main: function void (){
            hello(1);
            good_boy("Sang","Kha");
            are_you_ok(true);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(hello, IntegerLit(1)), CallStmt(good_boy, StringLit(Sang), StringLit(Kha)), CallStmt(are_you_ok, BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test329_param_id_call_expr(self):
        input = """
        main: function void (){
            hello(a);
            good_boy(b,e);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(hello, Id(a)), CallStmt(good_boy, Id(b), Id(e))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test330_nested_func_call(self):
        input = """
        main: function auto (){
            func(func(),5,foo());
        }"""
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([CallStmt(func, FuncCall(func, []), IntegerLit(5), FuncCall(foo, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test331_unary_operator(self):
        input = """
        main: function void (){
            a = -4;
            a = --4;
            a = !true;
            a = b[5];
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), UnExpr(-, IntegerLit(4))), AssignStmt(Id(a), UnExpr(-, UnExpr(-, IntegerLit(4)))), AssignStmt(Id(a), UnExpr(!, BooleanLit(True))), AssignStmt(Id(a), ArrayCell(b, [IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test332_nested_array(self):
        input = """
        main: function void (){
            a = {1,2,3,{4,5,6}};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test333_multivar_array(self):
        input = """
        main: function void (){
            b = a[1,2,3];
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(b), ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test334_binary_operator(self):
        input = """
        main: function void (){
            a = 1*b;
            a = true && false;
            a = a==b;
            a = a!=b;
            a = (a::b);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(*, IntegerLit(1), Id(b))), AssignStmt(Id(a), BinExpr(&&, BooleanLit(True), BooleanLit(False))), AssignStmt(Id(a), BinExpr(==, Id(a), Id(b))), AssignStmt(Id(a), BinExpr(!=, Id(a), Id(b))), AssignStmt(Id(a), BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test335_complex_binary_operator(self):
        input = """
        main: function void (){
            a = a*b*c + a/b/c;
            a = a + b%c + d;
            a = a&&b||a;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(*, BinExpr(*, Id(a), Id(b)), Id(c)), BinExpr(/, BinExpr(/, Id(a), Id(b)), Id(c)))), AssignStmt(Id(a), BinExpr(+, BinExpr(+, Id(a), BinExpr(%, Id(b), Id(c))), Id(d))), AssignStmt(Id(a), BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(a)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test336_complex_binary_operator_with_paren1(self):
        input = """
        main: function void (){
            a = a*b*(c+a)/b/c;
            a = a + (b%c + d);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(/, BinExpr(/, BinExpr(*, BinExpr(*, Id(a), Id(b)), BinExpr(+, Id(c), Id(a))), Id(b)), Id(c))), AssignStmt(Id(a), BinExpr(+, Id(a), BinExpr(+, BinExpr(%, Id(b), Id(c)), Id(d))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test337_complex_binary_operator_with_paren2(self):
        input = """
        main: function void (){
            a = (a&&b) || (a>=b && b);
            a = (a + (-b - c*(d+e)))*5;
            a = a::((b::c)::d);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BinExpr(&&, Id(a), Id(b)), BinExpr(>=, Id(a), BinExpr(&&, Id(b), Id(b))))), AssignStmt(Id(a), BinExpr(*, BinExpr(+, Id(a), BinExpr(-, UnExpr(-, Id(b)), BinExpr(*, Id(c), BinExpr(+, Id(d), Id(e))))), IntegerLit(5))), AssignStmt(Id(a), BinExpr(::, Id(a), BinExpr(::, BinExpr(::, Id(b), Id(c)), Id(d))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test338_numeric_left_to_right(self):
        input = """
        main: function void (){
            a = b*c/d%e;
            a = b+c-d+e;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(%, BinExpr(/, BinExpr(*, Id(b), Id(c)), Id(d)), Id(e))), AssignStmt(Id(a), BinExpr(+, BinExpr(-, BinExpr(+, Id(b), Id(c)), Id(d)), Id(e)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test339_logic_left_to_right(self):
        input = """
        main: function void (){
            a = b&&c||d;
            a = b||c&&d;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BinExpr(&&, Id(b), Id(c)), Id(d))), AssignStmt(Id(a), BinExpr(&&, BinExpr(||, Id(b), Id(c)), Id(d)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test340_relational_nonassoc(self):
        input = """
        main: function void (){
            a = b&&c;
            a = b!=c;
            a = b>=c;
            a = b<=c;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(&&, Id(b), Id(c))), AssignStmt(Id(a), BinExpr(!=, Id(b), Id(c))), AssignStmt(Id(a), BinExpr(>=, Id(b), Id(c))), AssignStmt(Id(a), BinExpr(<=, Id(b), Id(c)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test341_string_nonassoc(self):
        input = """
        main: function void (){
            a = b::c;
            a = b::(c::d);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, Id(b), Id(c))), AssignStmt(Id(a), BinExpr(::, Id(b), BinExpr(::, Id(c), Id(d))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test342_funccall(self):
        input = """
        main: function void (){
            t = getA(a) :: getB(b);
            x: integer = getX(x);
            a[1] = getA1(a[0]);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(t), BinExpr(::, FuncCall(getA, [Id(a)]), FuncCall(getB, [Id(b)]))), VarDecl(x, IntegerType, FuncCall(getX, [Id(x)])), AssignStmt(ArrayCell(a, [IntegerLit(1)]), FuncCall(getA1, [ArrayCell(a, [IntegerLit(0)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test343_full_order1(self):
        input = """
        main: function void (){
            a = -7+6/3/2*3-4%2;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, BinExpr(+, UnExpr(-, IntegerLit(7)), BinExpr(*, BinExpr(/, BinExpr(/, IntegerLit(6), IntegerLit(3)), IntegerLit(2)), IntegerLit(3))), BinExpr(%, IntegerLit(4), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test344_full_order2(self):
        input = """
        main: function void (){
            a = (-a + !b) * e[6] && b  >= 6;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(>=, BinExpr(&&, BinExpr(*, BinExpr(+, UnExpr(-, Id(a)), UnExpr(!, Id(b))), ArrayCell(e, [IntegerLit(6)])), Id(b)), IntegerLit(6)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    ##### STATEMENTS #####
    def test345_scalar_asm(self):
        input = """
        main: function void (){
            a = 5;
            b = "ez";
            c = .2e-3;
            d = {a,b,c,d};
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(5)), AssignStmt(Id(b), StringLit(ez)), AssignStmt(Id(c), FloatLit(0.0002)), AssignStmt(Id(d), ArrayLit([Id(a), Id(b), Id(c), Id(d)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test346_indexops_asm(self):
        input = """
        main: function void (){
            a[0] = 2;
            a[1,2,3] = 1;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(0)]), IntegerLit(2)), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test347_complex_asm(self):
        input = """
        main: function void (){
            a[0] = func(1,2,"3");
            a[1,2] = omg(omg(1));
            ez = ez*2 + 6*(7-func());
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(0)]), FuncCall(func, [IntegerLit(1), IntegerLit(2), StringLit(3)])), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), FuncCall(omg, [FuncCall(omg, [IntegerLit(1)])])), AssignStmt(Id(ez), BinExpr(+, BinExpr(*, Id(ez), IntegerLit(2)), BinExpr(*, IntegerLit(6), BinExpr(-, IntegerLit(7), FuncCall(func, [])))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test348_normal_if(self):
        input = """
        main: function void (){
            if(is_easy("PPL")==true){
                printString("de the co a");
            }
            else{
                printString("hoc lai di em");
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, FuncCall(is_easy, [StringLit(PPL)]), BooleanLit(True)), BlockStmt([CallStmt(printString, StringLit(de the co a))]), BlockStmt([CallStmt(printString, StringLit(hoc lai di em))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test349_if_sequence(self):
        input = """
        main: function void (){
            if(a){
            }
            else if (b){
            }
            else{
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(a), BlockStmt([]), IfStmt(Id(b), BlockStmt([]), BlockStmt([])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test350_if_nested1(self):
        input = """
        main: function void (){
            if(calc_score(score)==9){
                printString("idolll :3");
            }
            else {
                if (calc_score(score)==5){
                    printString("vua du qua mon :))");
                }
                else{
                    printString("doan xem");
                }
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, FuncCall(calc_score, [Id(score)]), IntegerLit(9)), BlockStmt([CallStmt(printString, StringLit(idolll :3))]), BlockStmt([IfStmt(BinExpr(==, FuncCall(calc_score, [Id(score)]), IntegerLit(5)), BlockStmt([CallStmt(printString, StringLit(vua du qua mon :))))]), BlockStmt([CallStmt(printString, StringLit(doan xem))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test351_if_nested2(self):
        input = """
        main: function void (){
            if(rich==true){
                if(nice==true){
                    setState("kind and rich");
                }
                else setState("unkind and rich");
            } 
            else setState("not rich");
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(rich), BooleanLit(True)), BlockStmt([IfStmt(BinExpr(==, Id(nice), BooleanLit(True)), BlockStmt([CallStmt(setState, StringLit(kind and rich))]), CallStmt(setState, StringLit(unkind and rich)))]), CallStmt(setState, StringLit(not rich)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test352_if_oneline(self):
        input = """
        main: function void (){
            if(happy) setHappy(true);
            else setHappy(false);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(happy), CallStmt(setHappy, BooleanLit(True)), CallStmt(setHappy, BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test353_if_oneline_nested(self):
        input = """
        main: function void (){
            if(rich==true)
                if(nice==true)
                    setState("kind and rich");
                else setState("unkind and rich");
            else setState("not rich");
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(rich), BooleanLit(True)), IfStmt(BinExpr(==, Id(nice), BooleanLit(True)), CallStmt(setState, StringLit(kind and rich)), CallStmt(setState, StringLit(unkind and rich))), CallStmt(setState, StringLit(not rich)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test354_normal_loop(self):
        input = """
        main: function void (){
            for(i=get_started(),i<=5,i+2){
                printInteger("Yoooo!");
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), FuncCall(get_started, [])), BinExpr(<=, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([CallStmt(printInteger, StringLit(Yoooo!))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test355_nested_forloop(self):
        input = """
        main: function void (){
            for(i=get_started(), i<5*2, i+2){
                for(j=get_started(), j<5*2, j+1){
                    printInteger(i+j);
                }
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), FuncCall(get_started, [])), BinExpr(<, Id(i), BinExpr(*, IntegerLit(5), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([ForStmt(AssignStmt(Id(j), FuncCall(get_started, [])), BinExpr(<, Id(j), BinExpr(*, IntegerLit(5), IntegerLit(2))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printInteger, BinExpr(+, Id(i), Id(j)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test356_normal_while(self):
        input = """
        main: function void (){
            while(a<5){
                printInteger(a);
                a = a+1;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(5)), BlockStmt([CallStmt(printInteger, Id(a)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test357_nested_while(self):
        input = """
        main: function void (){
            a: integer = 0;
            while(match(a)<10){
                printInteger(a);
                while(match(a)*match(a)<69)
                    printInteger(10-a);
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, FuncCall(match, [Id(a)]), IntegerLit(10)), BlockStmt([CallStmt(printInteger, Id(a)), WhileStmt(BinExpr(<, BinExpr(*, FuncCall(match, [Id(a)]), FuncCall(match, [Id(a)])), IntegerLit(69)), CallStmt(printInteger, BinExpr(-, IntegerLit(10), Id(a))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test358_normal_dowhile(self):
        input = """
        main: function void (){
            do {
                a = a+1;
                b = b-1;
            }
            while(a!=b);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(b), BinExpr(-, Id(b), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test359_nested_dowhile(self):
        input = """
        main: function void (){
            do{ 
                //a = a+1;
                //i: integer = 0;
                do{
                    printInteger(i);
                    i = i+1;
                }
                while(i<a);
            }
            while(a<10);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([DoWhileStmt(BinExpr(<, Id(i), Id(a)), BlockStmt([CallStmt(printInteger, Id(i)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
    
    def test360_break_and_return(self):
        input = """
        main: function void (){
            for(i=1,i<2,i+1){
                if(i==t)
                    break;
                if(i<0)
                    continue;
                else printInteger(i);
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), Id(t)), BreakStmt()), IfStmt(BinExpr(<, Id(i), IntegerLit(0)), ContinueStmt(), CallStmt(printInteger, Id(i)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))
    
#     def test361_mixed_loop(self):
#         input = """
#         main: function void (){
#             for(i=1,i<getMax(),i+1){
#                 while(true){
#                     print("kaka");
#                     do{
#                         print("kuku");
#                     }
#                     while(false);
#                 }
#             }
#         }
#         """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(getMax, [])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([CallStmt(print, StringLit(kaka)), DoWhileStmt(BooleanLit(False), BlockStmt([CallStmt(print, StringLit(kuku))]))]))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 361))
        
    def test362_oneline_loop(self):
        input = """
        main: function void (){
            k: integer = 5;
            for(i=1,i<getMax(),i+1)
                printInteger(i);
            while((k<200) && (k>0))
                k = k + 5;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(k, IntegerType, IntegerLit(5)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(getMax, [])), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printInteger, Id(i))), WhileStmt(BinExpr(&&, BinExpr(<, Id(k), IntegerLit(200)), BinExpr(>, Id(k), IntegerLit(0))), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(5))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))
    
    def test363_normal_call(self):
        input = """
        main: function void (){
            hello();
            hello("Sang");
            hello("Sang","Kha");
            hello(hello("Sang"),"Kha");
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(hello, ), CallStmt(hello, StringLit(Sang)), CallStmt(hello, StringLit(Sang), StringLit(Kha)), CallStmt(hello, FuncCall(hello, [StringLit(Sang)]), StringLit(Kha))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test364_nested_call(self):
        input = """
        main: function void (){
            f(f());
            f(f(f(f(f()))));
            f(f(f(f(f(f())))),f(f(f(f(f())))));
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f, FuncCall(f, [])), CallStmt(f, FuncCall(f, [FuncCall(f, [FuncCall(f, [FuncCall(f, [])])])])), CallStmt(f, FuncCall(f, [FuncCall(f, [FuncCall(f, [FuncCall(f, [FuncCall(f, [])])])])]), FuncCall(f, [FuncCall(f, [FuncCall(f, [FuncCall(f, [FuncCall(f, [])])])])]))]))
])"""    
        self.assertTrue(TestAST.test(input, expect, 364))
    
    def test365_expr_call(self):
        input = """
        main: function void (){   
            f(1*x,_123,"sss"::"aaa",dsa("dsa"),x%5);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f, BinExpr(*, IntegerLit(1), Id(x)), Id(_123), BinExpr(::, StringLit(sss), StringLit(aaa)), FuncCall(dsa, [StringLit(dsa)]), BinExpr(%, Id(x), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))
    
    def test366_normal_block(self):
        input = """
        main: function void (){
            {}
            {
                hello();
            }
            {
                a:integer = 1;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([]), BlockStmt([CallStmt(hello, )]), BlockStmt([VarDecl(a, IntegerType, IntegerLit(1))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test367_normal_return(self):
        input = """
            hello: function void(){
                printString("hello");
            }
            one: function integer(x:integer){
                return 1;
            }
        """
        expect = """Program([
	FuncDecl(hello, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(hello))]))
	FuncDecl(one, IntegerType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))
    
    def test368_complex_return(self):
        input = """
            isOdd: function boolean(x:integer){
                return x!=0;
            }
            getArr: function array [3] of integer (x:integer){
                return {x,x*2,x*3};
            }
        """
        expect = """Program([
	FuncDecl(isOdd, BooleanType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(!=, Id(x), IntegerLit(0)))]))
	FuncDecl(getArr, ArrayType([3], IntegerType), [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(ArrayLit([Id(x), BinExpr(*, Id(x), IntegerLit(2)), BinExpr(*, Id(x), IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))
    
    def test369_single_if(self):
        input = """
        main: function void (){   
            if(a==1) return 1;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))
    
#     def test370_empty_loops(self):
#         input = """
#         main: function void (){   
#             for(i=1,i<5,i+1){}
#             while(true){}
#             do{}while(true);
#         }
#         """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([])), WhileStmt(BooleanLit(True), BlockStmt([])), DoWhileStmt(BooleanLit(True), BlockStmt([]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 370))
    
    def test371_idx_for_loops(self):
        input = """
        main: function void (){   
            for(a[i]=1,i<5,i+1){}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [Id(i)]), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))
    
    def test372_idx_for_loops(self):
        input = """
        main: function void (){   
            for(a[i]=1,i<5,i+1){}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [Id(i)]), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))
    
    

    ##### MIXED CASES #####
    def test375_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test376_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))
    
    def test377_full_decl_program(self):
        input = """
        i: integer = 6;
        main: function void () {
            x: integer = 7;
        }
        j: integer = 8;
        foo: function void () {
            y: integer = 8;
        }
        """
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(6))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(7))]))
	VarDecl(j, IntegerType, IntegerLit(8))
	FuncDecl(foo, VoidType, [], None, BlockStmt([VarDecl(y, IntegerType, IntegerLit(8))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))
    
    def test378_full_stmt_program_1(self):
        input = """main: function void () {
            // cond stmt
            if (a>1){
                a = 1;
            }
            else if (a<1){
                a = 0;
            }
            else{
                a = 0.5;
            }
            // iter stmt
            while(a>0){
                a = a*0.4;
                print(a);
                if (a<1) break;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(1))]), IfStmt(BinExpr(<, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(0))]), BlockStmt([AssignStmt(Id(a), FloatLit(0.5))]))), WhileStmt(BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(*, Id(a), FloatLit(0.4))), CallStmt(print, Id(a)), IfStmt(BinExpr(<, Id(a), IntegerLit(1)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))
    
    def test379_full_stmt_program_2(self):
        input = """main: function void () {
            a: integer;
            if (a>0)
                for(a=10,a>0,a-1)
                    if (a>5) print("a>5");
                    else continue;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), IfStmt(BinExpr(>, Id(a), IntegerLit(0)), ForStmt(AssignStmt(Id(a), IntegerLit(10)), BinExpr(>, Id(a), IntegerLit(0)), BinExpr(-, Id(a), IntegerLit(1)), IfStmt(BinExpr(>, Id(a), IntegerLit(5)), CallStmt(print, StringLit(a>5)), ContinueStmt())))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test380_binary_search(self):
        input = """
            binarySearch: function integer (arr:integer, x:integer, low:integer, high:integer){
                if (low>high) return -1;
                else{
                    mid: integer = (low+high)/2;
                    if (x == arr[mid]) return mid;
                    else if (x > arr[mid]) return binarySearch(arr,x,mid+1,high);
                    else return binarySearch(arr,x,low,mid-1);
                }
            }
        """
        expect = """Program([
	FuncDecl(binarySearch, IntegerType, [Param(arr, IntegerType), Param(x, IntegerType), Param(low, IntegerType), Param(high, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(low), Id(high)), ReturnStmt(UnExpr(-, IntegerLit(1))), BlockStmt([VarDecl(mid, IntegerType, BinExpr(/, BinExpr(+, Id(low), Id(high)), IntegerLit(2))), IfStmt(BinExpr(==, Id(x), ArrayCell(arr, [Id(mid)])), ReturnStmt(Id(mid)), IfStmt(BinExpr(>, Id(x), ArrayCell(arr, [Id(mid)])), ReturnStmt(FuncCall(binarySearch, [Id(arr), Id(x), BinExpr(+, Id(mid), IntegerLit(1)), Id(high)])), ReturnStmt(FuncCall(binarySearch, [Id(arr), Id(x), Id(low), BinExpr(-, Id(mid), IntegerLit(1))]))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test381_interpolation_search(self):
        input = """
            interpolationSearch: function boolean (arr:array [100] of integer, x:integer, n:integer){
                low: integer = 0;
                high: integer = n-1;
                while((low<=high) && (target>=arr[low]) && (target <=arr[high])){
                    pos:integer = low + (((target - arr[low]) * (high - low)) / (arr[high] - arr[low]));
 
                    // Check if the target element is at the calculated position
                    if( arr[pos] == target){
                        return pos;
                    }
            
                    // If the target element is less than the element at the calculated position, search the left half of the list
                    if(arr[pos] > target){
                        high = pos - 1;
                    }
                    else{
                        // If the target element is greater than the element at the calculated position, search the right half of the list
                        low = pos + 1;
                    }
                }
                return -1;
            }
        """
        expect = """Program([
	FuncDecl(interpolationSearch, BooleanType, [Param(arr, ArrayType([100], IntegerType)), Param(x, IntegerType), Param(n, IntegerType)], None, BlockStmt([VarDecl(low, IntegerType, IntegerLit(0)), VarDecl(high, IntegerType, BinExpr(-, Id(n), IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(&&, BinExpr(<=, Id(low), Id(high)), BinExpr(>=, Id(target), ArrayCell(arr, [Id(low)]))), BinExpr(<=, Id(target), ArrayCell(arr, [Id(high)]))), BlockStmt([VarDecl(pos, IntegerType, BinExpr(+, Id(low), BinExpr(/, BinExpr(*, BinExpr(-, Id(target), ArrayCell(arr, [Id(low)])), BinExpr(-, Id(high), Id(low))), BinExpr(-, ArrayCell(arr, [Id(high)]), ArrayCell(arr, [Id(low)]))))), IfStmt(BinExpr(==, ArrayCell(arr, [Id(pos)]), Id(target)), BlockStmt([ReturnStmt(Id(pos))])), IfStmt(BinExpr(>, ArrayCell(arr, [Id(pos)]), Id(target)), BlockStmt([AssignStmt(Id(high), BinExpr(-, Id(pos), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(low), BinExpr(+, Id(pos), IntegerLit(1)))]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test382_selection_sort(self):
        input = """
            selectionSort: function void (out arr:array [100] of integer, n:integer){
                i, j, min_idx: integer;
                // One by one move boundary of
                // unsorted subarray
                for (i = 0, i < n-1, i+1)
                {
                    // Find the minimum element in
                    // unsorted array
                    min_idx = i;
                    for (j = i+1, j < n, j+1)
                    {
                    if (arr[j] < arr[min_idx])
                        min_idx = j;
                    }
                    // Swap the found minimum element
                    // with the first element
                    if (min_idx!=i)
                        swap(arr[min_idx], arr[i]);
                }
            }
        """
        expect = """Program([
	FuncDecl(selectionSort, VoidType, [OutParam(arr, ArrayType([100], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(min_idx, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(min_idx), Id(i)), ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [Id(min_idx)])), AssignStmt(Id(min_idx), Id(j)))])), IfStmt(BinExpr(!=, Id(min_idx), Id(i)), CallStmt(swap, ArrayCell(arr, [Id(min_idx)]), ArrayCell(arr, [Id(i)])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test383_merge_sort(self):
        input = """
            mergeSort: function void (out arr: array [100] of integer, begin:integer, end:integer){
                if (begin >= end)
                    return; // Returns recursively
            
                mid: auto = begin + (end - begin) / 2;
                mergeSort(arr, begin, mid);
                mergeSort(arr, mid + 1, end);
                merge(arr, begin, mid, end);
            }
        """
        expect = """Program([
	FuncDecl(mergeSort, VoidType, [OutParam(arr, ArrayType([100], IntegerType)), Param(begin, IntegerType), Param(end, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(begin), Id(end)), ReturnStmt()), VarDecl(mid, AutoType, BinExpr(+, Id(begin), BinExpr(/, BinExpr(-, Id(end), Id(begin)), IntegerLit(2)))), CallStmt(mergeSort, Id(arr), Id(begin), Id(mid)), CallStmt(mergeSort, Id(arr), BinExpr(+, Id(mid), IntegerLit(1)), Id(end)), CallStmt(merge, Id(arr), Id(begin), Id(mid), Id(end))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test384_quick_sort(self):
        input = """
            quickSort: function void (out arr:array [100] of integer, low:integer, high:integer){
                if (low < high) {
                    /* pi is partitioning index, arr[p] is now
                    at right place */
                    pi:integer = partition(arr, low, high);
            
                    // Separately sort elements before
                    // partition and after partition
                    quickSort(arr, low, pi - 1);
                    quickSort(arr, pi + 1, high);
                }
            }
        """
        expect = """Program([
	FuncDecl(quickSort, VoidType, [OutParam(arr, ArrayType([100], IntegerType)), Param(low, IntegerType), Param(high, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(low), Id(high)), BlockStmt([VarDecl(pi, IntegerType, FuncCall(partition, [Id(arr), Id(low), Id(high)])), CallStmt(quickSort, Id(arr), Id(low), BinExpr(-, Id(pi), IntegerLit(1))), CallStmt(quickSort, Id(arr), BinExpr(+, Id(pi), IntegerLit(1)), Id(high))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test385_heap_sort(self):
        input = """
            heapSort: function void (out arr:array [100] of integer, n:integer){
                // Build heap (rearrange array)
                for (i = N / 2 - 1, i >= 0, i-1)
                    heapify(arr, N, i);
            
                // One by one extract an element
                // from heap
                for (i = N - 1, i > 0, i-1) {
            
                    // Move current root to end
                    swap(arr[0], arr[i]);
            
                    // call max heapify on the reduced heap
                    heapify(arr, i, 0);
                }
            }
        """
        expect = """Program([
	FuncDecl(heapSort, VoidType, [OutParam(arr, ArrayType([100], IntegerType)), Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, BinExpr(/, Id(N), IntegerLit(2)), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), CallStmt(heapify, Id(arr), Id(N), Id(i))), ForStmt(AssignStmt(Id(i), BinExpr(-, Id(N), IntegerLit(1))), BinExpr(>, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(swap, ArrayCell(arr, [IntegerLit(0)]), ArrayCell(arr, [Id(i)])), CallStmt(heapify, Id(arr), Id(i), IntegerLit(0))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test386_insertion_sort(self):
        input = """
            insertionSort: function void (out arr:array [100] of integer, n:integer){
                i, key, j: integer;
                for (i = 1, i < n, i+1)
                {
                    key = arr[i];
                    j = i - 1;
            
                    // Move elements of arr[0..i-1], 
                    // that are greater than key, to one
                    // position ahead of their
                    // current position
                    while ((j >= 0) && (arr[j] > key))
                    {
                        arr[j + 1] = arr[j];
                        j = j - 1;
                    }
                    arr[j + 1] = key;
                }
            }
        """
        expect = """Program([
	FuncDecl(insertionSort, VoidType, [OutParam(arr, ArrayType([100], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(key, IntegerType), VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(key), ArrayCell(arr, [Id(i)])), AssignStmt(Id(j), BinExpr(-, Id(i), IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(>=, Id(j), IntegerLit(0)), BinExpr(>, ArrayCell(arr, [Id(j)]), Id(key))), BlockStmt([AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), ArrayCell(arr, [Id(j)])), AssignStmt(Id(j), BinExpr(-, Id(j), IntegerLit(1)))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), Id(key))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test387_find_depth_tree(self):
        input = """
            findDepthRec: function integer (out arr:array [100] of integer, n:integer, out index:integer){
                if ((index >= n) || (tree[index] == "l"))
                    return 0;
            
                // calc height of left subtree (In preorder
                // left subtree is processed before right)
                index=index+1;
                left: integer = findDepthRec(tree, n, index);
            
                // calc height of right subtree
                index=index+1;
                right: integer = findDepthRec(tree, n, index);
            
                return max(left, right) + 1;
            }
            findDepth: function void (out arr:array [100] of integer, n:integer){
                index: integer = 0;
                return findDepthRec(tree, n, index);
            }
        """
        expect = """Program([
	FuncDecl(findDepthRec, IntegerType, [OutParam(arr, ArrayType([100], IntegerType)), Param(n, IntegerType), OutParam(index, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(>=, Id(index), Id(n)), BinExpr(==, ArrayCell(tree, [Id(index)]), StringLit(l))), ReturnStmt(IntegerLit(0))), AssignStmt(Id(index), BinExpr(+, Id(index), IntegerLit(1))), VarDecl(left, IntegerType, FuncCall(findDepthRec, [Id(tree), Id(n), Id(index)])), AssignStmt(Id(index), BinExpr(+, Id(index), IntegerLit(1))), VarDecl(right, IntegerType, FuncCall(findDepthRec, [Id(tree), Id(n), Id(index)])), ReturnStmt(BinExpr(+, FuncCall(max, [Id(left), Id(right)]), IntegerLit(1)))]))
	FuncDecl(findDepth, VoidType, [OutParam(arr, ArrayType([100], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(index, IntegerType, IntegerLit(0)), ReturnStmt(FuncCall(findDepthRec, [Id(tree), Id(n), Id(index)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test388_lcs(self):
        input = """
            lcs: function integer (out X:array [100] of integer, out Y:array [100] of integer, n:integer, m:integer){
                if ((m == 0) || (n == 0))
                    return 0;
                if (X[m-1] == Y[n-1])
                    return 1 + lcs(X, Y, m-1, n-1);
                else
                    return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));
            }
        """
        expect = """Program([
	FuncDecl(lcs, IntegerType, [OutParam(X, ArrayType([100], IntegerType)), OutParam(Y, ArrayType([100], IntegerType)), Param(n, IntegerType), Param(m, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(m), IntegerLit(0)), BinExpr(==, Id(n), IntegerLit(0))), ReturnStmt(IntegerLit(0))), IfStmt(BinExpr(==, ArrayCell(X, [BinExpr(-, Id(m), IntegerLit(1))]), ArrayCell(Y, [BinExpr(-, Id(n), IntegerLit(1))])), ReturnStmt(BinExpr(+, IntegerLit(1), FuncCall(lcs, [Id(X), Id(Y), BinExpr(-, Id(m), IntegerLit(1)), BinExpr(-, Id(n), IntegerLit(1))]))), ReturnStmt(FuncCall(max, [FuncCall(lcs, [Id(X), Id(Y), Id(m), BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(lcs, [Id(X), Id(Y), BinExpr(-, Id(m), IntegerLit(1)), Id(n)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test389_spiral_matrix(self):
        input = """
            spiralPrint: function void (out X:array [100,100] of integer, n:integer, m:integer){
                i,k,l:integer = -1,0,0;
                /* k - starting row index
                    m - ending row index
                    l - starting column index
                    n - ending column index
                    i - iterator
                */
            
                while ((k < m) && (l < n)) {
                    /* Print the first row from
                        the remaining rows */
                    for (i = l, i < n, i+1) {
                        printString(a[k,i]);
                    }
                    k=k+1;
            
                    /* Print the last column
                    from the remaining columns */
                    for (i = k, i < m, i+1) {
                        printString(a[i,n-1]);
                    }
                    n=n-1;
            
                    /* Print the last row from
                            the remaining rows */
                    if (k < m) {
                        for (i = n - 1, i >= l, i-1) {
                            printString(a[m-1,i]);
                        }
                        m=m-1;
                    }
            
                    /* Print the first column from
                            the remaining columns */
                    if (l < n) {
                        for (i = m - 1, i >= k, i-1) {
                            printString(a[i,l]);
                        }
                        l=l+1;
                    }
                }
            }
        """
        expect = """Program([
	FuncDecl(spiralPrint, VoidType, [OutParam(X, ArrayType([100, 100], IntegerType)), Param(n, IntegerType), Param(m, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType, UnExpr(-, IntegerLit(1))), VarDecl(k, IntegerType, IntegerLit(0)), VarDecl(l, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(&&, BinExpr(<, Id(k), Id(m)), BinExpr(<, Id(l), Id(n))), BlockStmt([ForStmt(AssignStmt(Id(i), Id(l)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printString, ArrayCell(a, [Id(k), Id(i)]))])), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1))), ForStmt(AssignStmt(Id(i), Id(k)), BinExpr(<, Id(i), Id(m)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printString, ArrayCell(a, [Id(i), BinExpr(-, Id(n), IntegerLit(1))]))])), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1))), IfStmt(BinExpr(<, Id(k), Id(m)), BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(>=, Id(i), Id(l)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printString, ArrayCell(a, [BinExpr(-, Id(m), IntegerLit(1)), Id(i)]))])), AssignStmt(Id(m), BinExpr(-, Id(m), IntegerLit(1)))])), IfStmt(BinExpr(<, Id(l), Id(n)), BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, Id(m), IntegerLit(1))), BinExpr(>=, Id(i), Id(k)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printString, ArrayCell(a, [Id(i), Id(l)]))])), AssignStmt(Id(l), BinExpr(+, Id(l), IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))
        
    def test390_random_1_empty(self):
        input = "main: function void(){}"
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))
    
    def test391_random_2_id(self):
        input = """main: function void(){
                a = 1;
                a = b;
                a[0] = 1;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(a), Id(b)), AssignStmt(ArrayCell(a, [IntegerLit(0)]), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))
        
    def test392_random_floatlit1(self):
        input = """main: function void(){
                a = .e23;
                b = 10.21e2;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(b), FloatLit(1021.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))
    
    def test393_random_4_vardecl_single_if(self):
        input = """main: function void(){
                if (n == 1)  {a,b: integer;}
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))
    
#     def test394_random_floatlit2(self):
#         input = """main: function void(){
#                 a = .1e23;
#                 a = .1e-23;
#                 a = -.1e23;
#             }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), FloatLit(1e+22)), AssignStmt(Id(a), FloatLit(1e-24)), AssignStmt(Id(a), UnExpr(-, FloatLit(1e+22)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 394))
    
    def test395_random_stringlit1(self):
        input = """main: function void(){
                a = "abc\txyz";
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(abc	xyz))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
    
    def test396_random_stringlit2(self):
        input = """main: function void(){
                a = "abc\\nxyz";
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(abc\\nxyz))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
    
    def test397_ultimate_001(self):
        input = """main: function void(){
                a = -.e23;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), UnExpr(-, FloatLit(0.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))
    
    def test398_ultimate_002(self):
        input = """a: array [3] of integer;""" 
        expect = """Program([
	VarDecl(a, ArrayType([3], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))
    
    def test399_ultimate_003(self):
        input = """main: function void(){
                a: auto = 6;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, IntegerLit(6))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))
        
    def test400_ultimate_003(self):
        input = """main: function void(){
                if (exp1) 
                if (exp2)
                a();
                else b();
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(exp1), IfStmt(Id(exp2), CallStmt(a, ), CallStmt(b, )))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
    
    def test401_ultimate_003(self):
        input = """a: array[3] of integer = c;
            }"""
        expect = """Program([
	VarDecl(a, ArrayType([3], IntegerType), Id(c))
])"""
        self.assertTrue(TestAST.test(input, expect, 401))
    