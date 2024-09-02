#Student ID: 2113481

import unittest
from TestUtils import TestChecker

class CheckerSuite(unittest.TestCase):
    '''
        400-404: No Entry Point
        405-419: Redeclared (Variable/ Parameter/ Function)
        420-429: Undeclared Identifier/Function
        430-444: Type Mismatch In Expression
        445-449: IllegalArrayLiteral
        450-464: Type Mismatch In Statement
        465-469: MustInLoop
        470-479: InvalidStatementInFunction
        480-484: Invalid Variable/Parameter
        485-499: Mixed Cases
    '''
    def test_no_entry_point_1(self):
        input = """a: integer;"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 400))
    
    def test_no_entry_point_2(self):
        input = """a: function void(){}"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_no_entry_point_3(self):
        input = """main: function float(){}"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test_no_entry_point_4(self):
        input = """main: function void(){}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test_no_entry_point_5(self):
        input = """bkool: function void(){}"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 404))
    
    def test_redecl_var_1(self):
        input = """main: function void(){
                a: integer;
                a: float;
            }"""
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test_redecl_var_2(self):
        input = """main: function void(){
                a: integer;
                b: float;
                c: string;
                b: string;
            }"""
        expect = """Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test_redecl_var_3(self):
        input = """ a: integer;
        main: function void(){
                a: float;
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test_redecl_var_4(self):
        input = """ a: integer;
        main: function void(){
                a: float;
                {
                    a: string;
                }
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))
    
    def test_redecl_var_5(self):
        input = """ a,b: integer;
        main: function void(){
                a: float;
            }
            b: float;"""
        expect = """Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test_redecl_var_6(self):
        input = """main: function void(){}
            c: function void(){}
            c: integer;"""
        expect = """Redeclared Variable: c"""
        self.assertTrue(TestChecker.test(input, expect, 410))
    
    def test_redecl_func_1(self):
        input = """main: function void(){}
            c: integer;
            c: function void(){}
            """
        expect = """Redeclared Function: c"""
        self.assertTrue(TestChecker.test(input, expect, 411))
    
    def test_redecl_func_2(self):
        input = """main: function void(){}
            c: function auto(){}
            c: function void(){}
            """
        expect = """Redeclared Function: c"""
        self.assertTrue(TestChecker.test(input, expect, 412))
   
    def test_redecl_func_3(self):
        input = """main: function void(){
            main: integer;
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 413))
    
    def test_redecl_func_4(self):
        input = """main: function void(){}
            foo: function integer(a: integer){
                a: boolean;
            }
            """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 414))
    
    def test_redecl_func_5(self):
        input = """main: function void(){}
            foo: function integer(a: integer){}
            a: string;
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))
    
    def test_redecl_param_1(self):
        input = """main: function void(){}
            foo: function integer(a: integer, a:string){
            }
            """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 416))
    
    def test_redecl_param_2(self):
        input = """main: function void(){}
            foo: function integer(foo: integer){
            }
            """
        # expect = """Redeclared Parameter: foo"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 417)) #khong loi vi khac scope
    
    def test_redecl_param_3(self):
        input = """main: function void(){}
            foo: function integer(main: integer){
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 418))
    
    def test_redecl_param_4(self):
        input = """main: function void(){}
            foo: function integer(a: integer){
            }
            a: function integer(foo: integer){
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 419))
    
    def test_undecl_var_1(self):
        input = """main: function void(){
            a = 2;
        }
            """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 420))
    
    def test_undecl_var_2(self):
        input = """a: integer;
        main: function void(){
            a = 2;
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))
    
    def test_undecl_var_3(self):
        input = """main: function void(){
            a: integer;
            a = 2;
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test_undecl_var_4(self):
        input = """main: function void(){
            {
                a: integer;
            }
            a = 2;
        }
            """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 423))
    
    def test_undecl_var_5(self):
        input = """main: function void(){}
            foo: function void(a:integer){
                a = 2;
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 424))
    
    def test_undecl_func_1(self):
        input = """main: function void(){
            foo();
        }
            """
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test_undecl_func_2(self):
        input = """main: function void(){
            a: integer;
            a = foo() + 5;
        }
            """
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 426))
    
    def test_undecl_func_3(self):
        """forward invocation"""
        input = """
        foo: function integer(){
            return 1;
        }
        main: function void(){
            a: integer;
            a = foo() + 5;
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 427))
    
    def test_undecl_func_4(self):
        """backward invocation"""
        input = """
        main: function void(){
            a: integer;
            a = foo() + 5;
        }
        foo: function integer(){
            return 1;
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 428))
    
    def test_undecl_func_5(self):
        """backward inheritance"""
        input = """
        main: function void(){
            a: integer;
            a = foo() + 5;
        }
        foo: function integer() inherit barrr{
            preventDefault();
            return 1;
        }
        bar: function integer(){
            return 2;
        }
            """
        expect = """Undeclared Function: barrr"""
        self.assertTrue(TestChecker.test(input, expect, 429))
    
    def test_tmme_a1(self):
        input = """
        main: function void(){
            a: array [5] of integer;
            b: integer;
            b = a[5];
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test_tmme_a2(self):
        input = """
        main: function void(){
            a: integer;
            b: integer;
            b = a[5];
        }
            """
        expect = """Type mismatch in expression: ArrayCell(a, [IntegerLit(5)])"""
        self.assertTrue(TestChecker.test(input, expect, 431))
    
    def test_tmme_a3(self):
        input = """
        main: function void(){
            a: array [5,5] of integer;
            b: integer;
            b = a[1.0,"1"];
        }
            """
        # expect = """Type mismatch in expression: FloatLit(1.0)"""
        expect = "Type mismatch in expression: ArrayCell(a, [FloatLit(1.0), StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test_tmme_b1_implicit(self):
        input = """
        main: function void(){
            a: integer;
            b: float;
            // a + b: float; a: integer
            a = a + b;
        }
            """
        expect = """Type mismatch in statement: AssignStmt(Id(a), BinExpr(+, Id(a), Id(b)))"""
        self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test_tmme_b2_implicit(self):
        input = """
        main: function void(){
            a: integer;
            b: float;
            // float -> integer:OK
            b = a;
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 434))
    
    def test_tmme_b3_implicit(self):
        input = """
        main: function void(){
            a: float = 1;
            b: float = a + 2;
            c: integer = 2.3;
        }
            """
        # expect = """Type mismatch in Variable Declaration: FloatLit(2.3)"""
        expect = """Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FloatLit(2.3))"""
        self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test_tmme_b4_unary(self):
        input = """
        main: function void(){
            a: string;
            a = -a;
        }
            """
        expect = """Type mismatch in expression: UnExpr(-, Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test_tmme_b5_unary(self):
        input = """
        main: function void(){
            a: integer;
            a = !a;
        }
            """
        expect = """Type mismatch in expression: UnExpr(!, Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test_tmme_b6_binary(self):
        input = """
        main: function void(){
            a: integer;
            b: float;
            b = a + b; // valid
            a = a + b; // invalid
        }
            """
        expect = """Type mismatch in statement: AssignStmt(Id(a), BinExpr(+, Id(a), Id(b)))"""
        self.assertTrue(TestChecker.test(input, expect, 438)) 
    
    def test_tmme_b7_binary(self):
        input = """
        main: function void(){
            a: integer;
            b: float;
            c: integer;
            d: string;
            e: string;
            d = d :: e; // valid
            b = a % c; // valid
            a = a % b; // invalid: a % b
        }
            """
        expect = """Type mismatch in expression: BinExpr(%, Id(a), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 439))
    
    def test_tmme_b8_binary(self):
        input = """
        main: function void(){
            a: integer;
            b: boolean;
            c: boolean;
            b = (b && c) || c; // valid
            b = a && b; // invalid: a && b
        }
            """
        expect = """Type mismatch in expression: BinExpr(&&, Id(a), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 440))
    
    # def test_tmme_b9_binary(self):
    #     input = """
    #     main: function void(){
    #         a: integer;
    #         b: integer;
    #         c: boolean;
    #         d: boolean;
    #         e: float;
    #         c = b > e;
    #         c = e <= b;
    #         d = b == e; // invalid: b==e. UPDATE: valid
    #     }
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 441))
    
    def test_tmme_c1_void_funccall(self):
        input = """
        main: function void(){
            a: integer = 2;
            a = foo() + 2;
        }
        foo: function void(){
            return;
        }
            """
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test_tmme_c2_param_typ(self):
        input = """
        main: function void(){
            a: integer = 2;
            b: float = 2.1;
            a = foo(b,a) + 2;
        }
        foo: function integer(a: integer, b: float){
            return a+b;
        }
            """
        expect = """Type mismatch in expression: FuncCall(foo, [Id(b), Id(a)])"""
        self.assertTrue(TestChecker.test(input, expect, 443))
    
    def test_tmme_c3_param_len(self):
        input = """
        main: function void(){
            a: integer = 2;
            b: float = 2.1;
            a = foo(a,b) + 2;
        }
        foo: function integer(a: integer, b: float, c: integer){
            return a+b+c;
        }
            """
        expect = """Type mismatch in expression: FuncCall(foo, [Id(a), Id(b)])"""
        self.assertTrue(TestChecker.test(input, expect, 444))
    
    def test_ial_1(self):
        input = """
        main: function void(){
            a: array [5] of integer;
            a = {1,2.0};
        }
            """
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(2.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test_ial_2(self):
        input = """
        b1: float;
        main: function void(){
            a: array [5] of boolean;
            b1: boolean;
            b2: boolean;
            a = {b1,b2};
        }
            """
        expect = """Type mismatch in statement: AssignStmt(Id(a), ArrayLit([Id(b1), Id(b2)]))"""
        self.assertTrue(TestChecker.test(input, expect, 446))
        
    def test_ial_3(self):
        input = """
        a: array [5] of integer;
        main: function void(){
            i1: integer = 25;
            f2: float = 25.0;
            a = {i1,f2};
        }
            """
        expect = """Illegal array literal: ArrayLit([Id(i1), Id(f2)])"""
        self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test_ial_4(self):
        input = """
        main: function void(){
            a: array [5,5] of integer;
            a = {{1,2},{1,2,3},{1,2,"3"}};
        }
            """
        expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2), StringLit(3)])])"""
        self.assertTrue(TestChecker.test(input, expect, 448))
        
    def test_ial_5(self):
        input = """
        main: function void(){
            a: array [5] of float;
            s: string;
            a[3] = 2.5;
            a[2] = 5;
            a[1] = s;
        }
            """
        expect = """Type mismatch in statement: AssignStmt(ArrayCell(a, [IntegerLit(1)]), Id(s))"""
        self.assertTrue(TestChecker.test(input, expect, 449))
        
    def test_tmms_condexpr_1(self):
        input = """
        main: function void(){
            b: boolean;
            i: integer;
            while(b){}
            if(b){}
            do{}while(b);
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test_tmms_condexpr_2(self):
        input = """
        main: function void(){
            b: boolean;
            i: integer;
            while(i){}
            if(b){}
            do{}while(b);
        }
            """
        expect = """Type mismatch in statement: WhileStmt(Id(i), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input, expect, 451))
    
    def test_tmms_condexpr_3(self):
        input = """
        main: function void(){
            b1: boolean;
            b2: boolean;
            i1: integer;
            i2: integer;
            while(i1 == i2){}
            if(i1){}
            do{}while(b1);
        }
            """
        expect = """Type mismatch in statement: IfStmt(Id(i1), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test_tmms_condexpr_4(self):
        input = """
        main: function void(){
            b1: boolean;
            b2: boolean;
            i: integer;
            while(b1&&b2){}
            if(b1||b2){}
            do{}while(i);
        }
            """
        expect = """Type mismatch in statement: DoWhileStmt(Id(i), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test_tmms_forexpr_1(self):
        input = """
        main: function void(){
            b: boolean;
            i: integer;
            for(i=0,i<10,i+1){}
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test_tmms_forexpr_2(self):
        input = """
        main: function void(){
            b: boolean;
            i: integer;
            for(b=true,i<10,i*2){}
        }
            """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(b), BooleanLit(True)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(*, Id(i), IntegerLit(2)), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test_tmms_forexpr_3(self):
        input = """
        main: function void(){
            b: boolean;
            i: integer;
            for(i=0,i<10,i<10){}
        }
            """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test_tmms_forexpr_4(self):
        input = """
        main: function void(){
            b: boolean;
            i: integer;
            for(i=0,i+1,i<10){}
        }
            """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(+, Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test_tmms_asm_1(self):
        input = """
        v: function void(){}
        main: function void(){
            b: boolean;
            i: integer;
            v = v;
        }
            """
        expect = """Undeclared Identifier: v"""
        self.assertTrue(TestChecker.test(input, expect, 458))  #bien khong co kieu void, lhs cua assign phai la kieu khac void hoac array
    
    def test_tmms_asm_2(self):
        input = """
        main: function void(){
            b: boolean;
            a: array [5] of integer;
            a = {1,2,3,4,5};
        }
            """
        expect = """Type mismatch in statement: AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))"""
        self.assertTrue(TestChecker.test(input, expect, 459))
    
    # def test_tmms_func_1(self):
    #     input = """
    #     foo: function auto(){
    #         return 0;
    #     }
    #     main: function void(){
    #         i: integer;
    #         f: float;
    #         f = f+i;
    #         foo(); // foo: auto (general) -> int (return - not auto anymore) != void (CallStmt) => INVALID !!
    #         f = f+foo(i);
    #         i = i+f;
    #     }
    #         """
    #     expect = """Type mismatch in expression: FuncCall(foo, [Id(i)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 460))
        
    def test_tmms_func_2(self):
        input = """
        foo: function auto(a:auto,b:auto,c:auto){
            return 0.0; // foo->float
        }
        bar: function void(){}
        main: function void(){
            i: integer;
            f: float;
            f = foo(i,f,f)+f; // infer: foo->float,a->integer,b->float,c->float
            f = foo(1,"2",3.0); // invalid: param 2 mismatch
        }
            """
        expect = """Type mismatch in expression: FuncCall(foo, [IntegerLit(1), StringLit(2), FloatLit(3.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 461))
    
    def test_tmms_func_3(self):
        input = """
        foo: function auto(a:auto,b:auto,c:auto){
            return 0.0;
        }
        main: function void(){
            i: integer;
            f: float;
            f = f+i;
            f = foo(i,f,f)+f; // infer: foo->float (return),a->integer,b->float,c->float
            foo(1,2.0,3.0); // invalid: foo is not void
        }
            """
        # expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(1), FloatLit(2.0), FloatLit(3.0))"
        expect =""
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test_tmms_func_4(self):
        input = """
        foo: function auto(a:auto,b:auto,c:auto,d:integer){
            return 0;
        }
        main: function void(){
            i: integer;
            f: float;
            f = f+i;
            {
                f = foo(i,f,f,i); // infer: foo->float,a->integer,b->float,c->float
            }
            foo(1,2.0,3.0,1); // invalid: foo is not void
        }
            """
        # expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(1), FloatLit(2.0), FloatLit(3.0), IntegerLit(1))"
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 463))
    
    def test_tmms_func_5(self):
        input = """
        foo: function auto(a:auto,b:auto,c:auto,d:integer){
            a = 5;
            return a; // foo->integer
        }
        main: function void(){
            f: auto = foo(1,2,3,4); // f->float
            f = f + "wrong";
        }
            """
        expect = """Type mismatch in expression: BinExpr(+, Id(f), StringLit(wrong))"""
        self.assertTrue(TestChecker.test(input, expect, 464))
        
    def test_mil_1(self):
        input = """
        main: function void(){
            while(true){
                continue;
                break;
            }
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test_mil_2(self):
        input = """
        main: function void(){
            while(true){
                continue;
            }
            break;
        }
            """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test_mil_3(self):
        input = """
        main: function void(){
            do{
                break;
            }
            while(true);
            continue;
        }
            """
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test_mil_4(self):
        input = """
        main: function void(){
            i: integer;
            for(i=0,i<10,i+1){
                continue;
                {
                    break;
                }
            }
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test_mil_5(self):
        input = """
        main: function void(){
            i: integer;
            for(i=0,i<10,i+1){
                continue;
            }
            {
                break;
            }
        }
            """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 469))
    
    def test_ifs_normal_super(self):
    
        input = """
        foo: function void(inherit a: integer){}
        mid: function void(){}
        main: function void() inherit foo{
            super(1);
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 470))
    
    def test_ifs_normal_preventDefault(self):
        input = """
        foo: function void(a: integer){}
        mid: function void(){}
        main: function void() inherit foo{
            preventDefault();
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 471))
    
    def test_ifs_block_stmt(self):
        input = """
        foo: function void(a: integer){}
        mid: function void(){}
        main: function void() inherit foo{
            {
                super(1);
            }
            preventDefault();
        }
            """
        expect = """Invalid statement in function: main"""
        self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test_ifs_inherit_parent(self):
        input = """
        foo: function void(inherit a: integer,b: auto, inherit c: integer){}
        mid: function void(){}
        main: function void() inherit foo{
            super(1,2,3);
            a = a+1;
            c = c+1;
            b = b+1;
        }
            """
        expect = """Undeclared Identifier: b"""
        self.assertTrue(TestChecker.test(input, expect, 473))
        
    def test_ifs_inherit_grandparent(self):
        input = """
        main: function void(){}
        goo: function void(c: integer) inherit bar{
            super(2);
            c = b + a;
        }
        bar: function void(inherit b: integer) inherit foo{
            super(1);
        }
        foo: function void(inherit a: integer){}
            """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 474))
    
    def test_ifs_redecl_var(self):
        input = """
        main: function void(){}
        goo: function void(c: integer) inherit bar{
            super(2);
            a: integer;
            c = a + b;
        }
        bar: function void(inherit b: integer) inherit foo{
            super(1);
        }
        foo: function void(inherit a: integer){}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))
    
    def test_ifs_redecl_param(self):
        input = """
        main: function void(){}
        goo: function void(b: integer) inherit bar{
            super(2);
            c = a + b;
        }
        bar: function void(inherit b: integer) inherit foo{
            super(1);
        }
        foo: function void(inherit a: integer){}
            """
        expect = """Invalid Parameter: b"""
        self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test_ifs_auto_inherit_empty(self):
        input = """
        main: function void(){}
        go: function void(b: integer) inherit bar{
            b = a;
        }
        bar: function void() inherit foo{
            super(1);
        }
        foo: function void(inherit a: integer){}
            """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 477))
    
    def test_ifs_block_inherit_empty(self):
        input = """
        main: function void(){}
        go: function void(b: integer) inherit bar{
            preventDefault();
            b = a;
        }
        bar: function void() inherit foo{
            super(1);
        }
        foo: function void(inherit a: integer){}
            """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 478))
    
    def test_ifs_mixed_inherit(self):
        input = """
        main: function void(){}
        go: function void(b: integer) inherit bar{
            b = a;
        }
        bar: function void() inherit foo{
            super(1);
        }
        foo: function void(inherit a: integer) inherit zar{
            preventDefault();
        }
        zar: function void(inherit b: integer){}
            """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 479))
    
    def test_invalid_var(self):
        input = """
        main: function void(){
            a: auto;
        }
            """
        expect = """Invalid Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 480))
    
    def test_infer_var(self):
        input = """
        main: function void(){
            a: auto = 10;
            b: auto = "100";
            c: auto = a<10;
            printInteger(a);
            printString(b);
            printBoolean(c);
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test_infer_func_1(self):
        
        input = """
        foo: function auto(a: integer, b: integer){}
        main: function void(){
            a: float = foo(1,2);
            writeFloat(foo(1,2));
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))
        
    def test_infer_func_2(self):
        input = """
        foo: function auto(a: integer, b: integer){}
        main: function void(){
            a: float = foo(1,2) + 1;
            printInteger(foo(1,2));
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 483))
    
    # def test_infer_func_3(self):
    #     input = """
    #     foo: function auto(a: integer, b: integer){}
    #     main: function void(){
    #         foo(1,2);
    #         a: float = foo(1,2) + 1;
    #     }
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 484))
    
    def test_invalid_param_1(self):
        input = """
        foo: function auto(a: integer){}
        main: function void(a: integer) inherit foo{
            super(1);
        }
            """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 485))
    
    def test_invalid_param_2(self):
        input = """
        foo: function auto(inherit a: integer){}
        main: function void(a: integer) inherit foo{
            super(1);
        }
            """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 486))
    
    ## TESTS from BKeL
    def test_array_decl(self):
        input = """
        foo: function string(a: integer){}
        main: function void(){
            a: array [3] of integer = {1,2};
        }
            """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))"""
        self.assertTrue(TestChecker.test(input, expect, 487)) 
        
    def test_array_asm(self):
        input = """
        foo: function string(a: integer){}
        main: function void(){
            a: array [2,3] of integer;
            a[1,2,3] = 1;
        }
            """
        expect = """Type mismatch in expression: ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])"""
        self.assertTrue(TestChecker.test(input, expect, 488))
        
    # def test_out_param(self):
    #     input = """
    #     foo: function void(out x: integer){}
    #     main: function void(){
    #         foo(2);
    #     }
    #         """
    #     expect = """Type mismatch in statement: CallStmt(foo, IntegerLit(2))"""
    #     self.assertTrue(TestChecker.test(input, expect, 489))
    
    def test_array_as_param(self):
        input = """
        foo1: function auto(){}
        foo2: function auto(){}
        main: function void(){
            a: array [2] of integer = { foo1(), foo2() };
            printInteger(foo1());
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))
    
    # def test_array_cell_nonatomic(self):
    #     input = """
    #     main: function void(){
    #         a: array[1,2,3] of integer;
    #         x: integer = a[1];
    #     }
    #         """
    #     expect = """Type mismatch in Variable Declaration: ArrayCell(a, [IntegerLit(1)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 491))
    
    # def test_super_in_empty_parent(self):
    #     input = """
    #     x: function void(){}
    #     main: function void(){
    #         super();
    #     }
    #         """
    #     expect = """Invalid statement in function: super"""
    #     self.assertTrue(TestChecker.test(input, expect, 492))
        
    def test_nonatomic_cell_init(self):
        input = """
        x: function void(){}
        main: function void(){
            a: array[2,3] of integer;
            b: array[3] of integer = a[0];
            c: array[5] of integer = a[0];
        }
            """
        expect = """Type mismatch in Variable Declaration: VarDecl(c, ArrayType([5], IntegerType), ArrayCell(a, [IntegerLit(0)]))"""
        self.assertTrue(TestChecker.test(input, expect, 493))
    
    # def test_func_id(self):
    #     input = """
    #     foo: function integer(){}
    #     a: auto = foo;
    #     main: function void(){
    #     }
    #         """
    #     expect = """Undeclared Identifier: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 494))
        
    def test_array_id(self):
        input = """
        foo: function integer(){}
        main: function void(){
            a[0] = 5;
        }
            """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 495)) 
        
    def test_undecl_mismatch_param(self):
        input = """
        main: function void(){
            
        }
        a: auto = foo(1, 2);
        foo: function auto() { }
            """
        expect = """Type mismatch in expression: FuncCall(foo, [IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 496))
    
    def test_infer_subscript(self):
        input = """
        main: function void(){
            a: array[3,4] of integer;
            a[foo(), 1+4] = 222;
            a[1,2] = bar();
            printInteger(foo());
            printInteger(bar());
        }
        foo: function auto(){}
        bar: function auto(){}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 497))
    
    def test_coercion_array_intfloat(self):
        input = """
        main: function void(){
            a: array[4] of float = {1,2,3,4};
        }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498)) 
    
    def test_return_after(self):
        input = """
        foo: function auto (a: auto, b: integer){
            if (b>0){
                return a; //-> auto
            }
            return "a"; //-> string
            return 1; //-> dont care
        }
        main: function void(){
            printString(foo(1,2));
        }
        
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))
    
    def test_func_pass(self):
        input = """
            main: function void() {
                c: auto = { {1 , 2}, { 1,1.5} };
            }
            """
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(1.5)])"""
        self.assertTrue(TestChecker.test(input, expect, 4000))
    
    def test_4001(self):
        input = """
            goo: function auto() {}
            foo : function auto(b:auto) {
                a : auto = {{1,2},{goo(),4},{3,4}, b};
                a[4,4] = 1;
                return;
            }
            main:function void() {
                return;
            }
            """
        expect = ""
        
        self.assertTrue(TestChecker.test(input, expect, 4001))
        
    def test_4002(self):
        input = """
            goo: function auto() {}
            foo : function auto(b:auto) {
                a: integer;
                a = printInteger();
            }
            main:function void() {
                return;
            }
            """
        expect = "Type mismatch in expression: FuncCall(printInteger, [])"
        
        self.assertTrue(TestChecker.test(input, expect, 4002)) 

    def test_huy(self):
        input = """
            foo : function integer(b:auto) {
                return 0.1;
            }
            main:function void() {
                return;
            }
            """
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(0.1))"
        self.assertTrue(TestChecker.test(input, expect, 500)) 
        
    def test_huy1(self):
        input = """
            inc: function void (out n: integer, n: float) inherit foo{
                super(0.1, 1);
                n: string = 124;
            }
            foo: function auto (inherit n: float, b: integer){}
            """
        expect = "Redeclared Parameter: n"
        self.assertTrue(TestChecker.test(input, expect, 501)) 
    
    # def test_huy2(self):
    #     input = """
    #         foo: function auto (a: auto, b: auto) {

    #             c = a == b;

    #             d = a + b;

    #             return d;

    #         }
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 502)) 
    
    def test_huy3(self):
        input = """
            foo: function float (x : integer) {

    x: float = x + x;

    return x;

}
            """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 503)) 
        
    def test_huy4(self):
        input = """
            x: function float (x : integer) {

    x: float = x + x;

    return x;

}
            """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 504)) 
        
    def test_huy5(self):
        input = """
            main: function void () {
            a: string = "1";
            b: string = "1";
            if (a == b){
                printInteger(4);
            }
        }
            """
        expect = "Type mismatch in expression: BinExpr(==, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 505)) 
    
    def test_huy6(self):
        input = """
            f2: function integer(p1: integer,  p2: integer) inherit f1{
    super(1, 2);
}
f1: function integer(inherit p1: integer, inherit p2: integer) inherit f0{
    super(2);
}
f0: function float(inherit out p0: integer){}
main: function void(){}
            """
        expect = "Invalid Parameter: p1"
        self.assertTrue(TestChecker.test(input, expect, 506)) 
        
    def test_huy7(self):
        input = """
            f2: function integer(p1: integer,  p2: integer) inherit f1{
    super(1, 2);
}
f1: function integer(inherit p1: integer, inherit p1: integer) {
}
main: function void(){}
            """
        expect = "Redeclared Parameter: p1"
        self.assertTrue(TestChecker.test(input, expect, 507)) 
    
    def test_huy8(self):
        input = """
            foo: function auto(){}
main: function void(){
    a: float = -foo();
    b: string = foo();
}
            """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, StringType, FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 508)) 
    
    def test_huy9(self):
        input = """
            foo: function auto(){}
main: function void(){
    a: float = -foo();
    b: float = foo() + 1.2;
}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 509)) 
        
    def test_huy10(self):
        input = """
            x: array[4] of integer = foo(10);
            foo: function array[4] of integer (n: integer) {
                return {n, n+1, n+2,n+3} ;
            }
            main: function void(){}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 510))     
        
    def test_huy11(self):
        input = """
            x: array[4] of integer = foo(10);
            foo: function array[2, 2] of integer (n: integer) {
                return {n,n+1,n+2,n+3};
            }
            main: function void(){}
            """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, ArrayType([4], IntegerType), FuncCall(foo, [IntegerLit(10)]))"
        self.assertTrue(TestChecker.test(input, expect, 511))     
    
    def test_huy12(self):
        input = """
            x: array[4] of integer = foo(10);
            foo: function array[4] of integer (n: float) {
                return {n, n+1, n+2, n+3} ;
            }
            main: function void(){}
            """
        expect = "Type mismatch in statement: ReturnStmt(ArrayLit([Id(n), BinExpr(+, Id(n), IntegerLit(1)), BinExpr(+, Id(n), IntegerLit(2)), BinExpr(+, Id(n), IntegerLit(3))]))"
        self.assertTrue(TestChecker.test(input, expect, 512))   
    
    def test_huy13(self):
        input = """
            foo: function void (b: auto, c: auto){
                a : string =b+c;
            }
            main: function void(){}
            """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(+, Id(b), Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 513))   
        
        
    def test_huy14(self):
        input = """
            foo: function auto (){
                return 1;
            }
            main: function void(){
                a:float = foo() ;
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 514))   
    
    def test_huy15(self):
        input = """
            main: function void(){
                if ( 1+3.2 ==true) {
                    return;
                }
            }
            """
        expect = "Type mismatch in expression: BinExpr(==, BinExpr(+, IntegerLit(1), FloatLit(3.2)), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 515))   
        
    def test_return_after1(self):
        input = """
        foo: function auto (a: auto, b: integer){
            return "1";
            if (b>0){
                return a; //-> auto
                return 1;
            }
            return "a"; 
            return 1; //-> dont care
        }
        main: function void(){
            printString(foo("1",2));
        }
        
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 520))
    
    def test_return_after2(self):
        input = """
        foo: function auto (a: auto, b: integer){
            return "1";
            if (b>0){
                return 1;
            }
        }
        main: function void(){
            printString(foo("1",2));
        }
        
            """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 521))
    
    def test_return_after3(self):
        input = """
        foo: function auto (a: auto, b: integer){
            return "1";
            if (b>0){
                return "2";
                return true;
            }
        }
        main: function void(){
            printString(foo("1",2));
        }
        
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 522))
    
    def test_return_after4(self):
        input = """
        foo: function auto (a: auto, b: integer){
            return "1";
            if (b>0){
                return "2";
                return true;
            }
            else{
                return 1;
            }
        }
        main: function void(){
            printString(foo("1",2));
        }
        
            """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 523))
    
    def test_return_after5(self):
        input = """
        foo: function auto (a: auto, b: integer){
            return "1";
            if (b>0){
                return "2";
                return true;
            }
            else{
                return "1";
                return 1;
            }
        }
        main: function void(){
            printString(foo("1",2));
        }
        
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 524))