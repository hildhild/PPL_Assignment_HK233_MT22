#Student ID: 2113481

import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    '''
        TESTCASE STRATEGY:
        500-509: VarDecl, AssignStmt, Bin/UnOps
        510-519: ArrayLit/Cell + Local/Global VarDecl
        520-529: IfElseStmt + BlockStmt 
        530-544: For/While/DoWhileStmt(3x3) + Break/Continue(6)
        545-554: (CheckPoint) IfElseStmt & For/While/DoWhileStmt & IndexOperator
        555-574: Func/ParamDecl + CallStmt/FuncCall + ReturnStmt
        575-589: Parameter Passing + Inherit Params
        590-599: Mixed Cases
    '''
    def test500_single_vardecl(self):
        input = """
        main:function void(){
            a: integer = 1;
            printInteger(a);
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test501_multi_vardecl(self):
        input = """
        main:function void(){
            a,b,c: integer = 1,2,3;
            printInteger(b);
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test502_simple_assign(self):
        input = """
        main:function void(){
            a: integer;
            a = 4;
            printInteger(a);
        }
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test503_mixed_vardecl_assign(self):
        input = """
        main:function void(){
            a,b,c: integer = 1,2,3;
            a = 4;
            b = 5;
            c = 6;
            printInteger(a);
            printInteger(b);
            printInteger(c);
        }
        """
        expect = "456"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test504_mixed_type_vardecl_assign1(self):
        input = """
        main:function void(){
            a: integer;
            b: float;
            c: string;
            d: boolean;
            a = 2;
            b = 1.2;
            c = "hw";
            d = false;
            printInteger(a);
            writeFloat(b);
            printString(c);
            printBoolean(d);
        }
        """
        expect = "21.2hwfalse"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test505_simple_bin_op(self):
        input = """
        main:function void(){
            // Integer
            a: integer = 1;
            b: integer = 2;
            b = b/a;
            a = a+b;
            a = a*b;
            b = b%2;
            printInteger(a-1);
            // Boolean
            b1: boolean = true;
            b2: boolean = false;
            b1 = b1 || b2;
            printBoolean(b1 && b2);
            // Integer - Boolean
            printBoolean(b >= a);
            // String
            s1: string = "hello";
            s2: string = "world";
            s1 = (s1::" ")::s2;
            printString(s1);
        }
        """
        expect = "5falsefalsehello world"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test506_simple_un_op(self):
        input = """
        main:function void(){
            a: integer = -1;
            a = -a;
            printInteger(a);
            b: float = 1e2;
            b = -b;
            writeFloat(b);
            c: boolean = true;
            c = !c;
            printBoolean(c);
        }
        """
        expect = "1-100.0false"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    def test507_type_coercion(self):
        input = """
        main:function void(){
            a: integer = 1;
            b: float = 2.0;
            c: float = a+b;
            writeFloat(c);
        }
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    def test508_mixed_ops(self):
        input = """
        main:function void(){
            i: integer = 2;
            b: boolean = true;
            s: string = "str";
            f: float = 9.0;
            f = f*i+f/2;
            s = s::((s::s)::s);
            printInteger(7+i-(-i)*i/2);
            printBoolean((i==i)&&b);
            writeFloat(f);
        }
        """
        expect = "11true22.5"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    def test509_mixed_ops(self):
        input = """
        main:function void(){
            i1,i2,i3: integer = 2*1,3/1,4-0;
            b1,b2: boolean = true && false, true || false;
            s: string = "hi";
            f: float = 9.0*2;
            f = f*i1+f/2;
            s = s::((s::s)::s);
            writeFloat(7.0+i2-(-i1)*i3/2);
            printBoolean((i3>=i2)&&b1);
            writeFloat(f);
        }
        """
        expect = "14.0false45.0"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    def test510_simple_arraylit(self):
        input = """
        main:function void(){
            a: array [5] of integer = {1,2,3,4,5};
            b: array [3] of string = {"1","2","3"};
            c: array [2] of boolean = {true,false};
            d: array [2] of float = {1.0,2.0};
            printInteger(a[1]);
            printString(b[1]);
            printBoolean(c[1]);
            writeFloat(d[1]);
        }
        """
        expect = "22false2.0"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    def test511_multi_arraylit(self):
        input = """
        main:function void(){
            e: array [2,2] of string = {{"1","2"},{"3","4"}};
            f: array [2,2,2] of integer = {{{1,2},{3,4}},{{1,2},{3,4}}};
            printString(e[1,1]);
            printInteger(f[1,1,1]);
        }
        """
        expect = "44"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    def test512_simple_arraycell_left(self):
        input = """
        main:function void(){
            e: array [2,2] of string = {{"1","2"},{"3","4"}};
            e[1,1] = "5";
            printString(e[1,1]);
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    def test513_simple_arraycell_right(self):
        input = """
        main:function void(){
            e: array [2,2,2] of float = {{{1.0,2e5},{3e-4,0.04}},{{-1.5,.3e1},{3_456.0,5.1}}};
            e[0,1,0] = 7.0+e[0,0,0];
            writeFloat(e[0,1,0]);
        }
        """
        expect = "8.0"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    def test514_complex_expr_arraycell(self):
        input = """
        main:function void(){
            f: array [2,2,2] of integer = {{{1+2,2*4},{3-5,4+1}},{{1%1,2/2},{30-6,4+5}}};
            printInteger(f[1,1,1]);
        }
        """
        expect = "9"
        self.assertTrue(TestCodeGen.test(input,expect,514)) 
    def test515_simple_scope(self):
        input = """
        a: integer = 6;
        main:function void(){
            a = a+1;
            printInteger(a);
        }
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input,expect,515)) 
    def test516_override_scope(self):
        input = """
        a: integer = 6;
        main:function void(){
            a: string = "7";
            printString(a);
        }
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input,expect,516))
    def test517_block_scope_1(self):
        input = """
        a: integer = 6;
        main:function void(){
            a: string = "7";
            {
                printString(a);
            }
        }
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    def test518_block_scope_2(self):
        input = """
        a: integer = 6;
        main:function void(){
            a: string = "7";
            {
                a = a::"7";
                printString(a);
            }
            printString(a);
        }
        """
        expect = "7777"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    def test519_block_scope_3(self):
        input = """
        a: integer = 6;
        main:function void(){
            b: integer = 7;
            {
                b = 8;
                {
                    a = 9;
                }
            }
            printInteger(a+b);
        }
        """
        expect = "17"
        self.assertTrue(TestCodeGen.test(input,expect,519))
    def test520_simple_if(self):
        input = """
        main:function void(){
            b: integer = 7;
            if(b>0){
                printString("True");
            }
            else{
                printString("False");
            }
        }
        """
        expect = "True"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    def test521_simple_if_inline(self):
        input = """
        main:function void(){
            b: integer = 7;
            if(b>0)
                printString("True");
            else
                printString("False");
        }
        """
        expect = "True"
        self.assertTrue(TestCodeGen.test(input,expect,521))
    def test522_seq_if(self):
        input = """
        main:function void(){
            b: integer = 7;
            if(b>10)
                printString("x>10");
            else if ((b<=10) && (b>=5))
                printString("5<=x<=10");
            else if (b>=0){
                printString("0<=x<5");
            }
            else{
                printString("x<0");
            }
        }
        """
        expect = "5<=x<=10"
        self.assertTrue(TestCodeGen.test(input,expect,522))
    def test523_seq_if(self):
        input = """
        main:function void(){
            b: integer = 7;
            if(b>0)
                printString("x>0;");
            if ((b<=10) && (b>=5))
                printString("5<=x<=10");
            else if (b>=0){
                printString("0<=x<5");
            }
            else{
                printString("x<0");
            }
        }
        """
        expect = "x>0;5<=x<=10"
        self.assertTrue(TestCodeGen.test(input,expect,523))
    def test524_seq_if(self):
        input = """
        b: integer = 9;
        main:function void(){
            b: integer = 7;
            if(b>10){
                printString("x>10");
            }
            else if ((b<=10) && (b>=5)){
                b = b+1;
                printString("x=8;");
                printString("5<=x<=10");
            }
            else{
                printString("x<5");
            }
        }
        """
        expect = "x=8;5<=x<=10"
        self.assertTrue(TestCodeGen.test(input,expect,524))
    def test525_nested_if_1(self):
        input = """
        main:function void(){
            b: integer = 7;
            if(b>0){
                if(b>10){
                    printString("x>10");
                }
                else if ((b<=10) && (b>=5)){
                    printString("5<=x<=10");
                }
                else{
                    printString("x<5");
                }
            }
            else{
                printString("x<0");
            }
        }
        """
        expect = "5<=x<=10"
        self.assertTrue(TestCodeGen.test(input,expect,525))
    def test526_nested_if_2(self):
        input = """
        main:function void(){
            b: integer = 7;
            if(b<0){
                printString("x<0");
            }
            else{
                if(b>10){
                    printString("x>10");
                }
                else if ((b<=10) && (b>=5)){
                    printString("5<=x<=10");
                }
                else{
                    printString("x<5");
                }
            }
        }
        """
        expect = "5<=x<=10"
        self.assertTrue(TestCodeGen.test(input,expect,526))
    def test527_blocks_if_1(self):
        input = """
        main:function void(){
            b: integer = 7;
            if(b>10){
                printString("x>10");
                {
                    b = b*2;
                }
            }
            else if ((b<=10) && (b>=5)){
                {
                    b = b+1;
                    printString("5<=x<=10;");
                }
                b = b+1;
            }
            else{
                {
                    b = b-6;
                }
                printString("x<5");
            }
            printInteger(b);
        }
        """
        expect = "5<=x<=10;9"
        self.assertTrue(TestCodeGen.test(input,expect,527))
    def test528_blocks_if_2(self):
        input = """
        main:function void(){
            b: integer = 7;
            {
                if(b>10){
                    printString("x>10");
                    {
                        b = b*2;
                    }
                }
                else if ((b<=10) && (b>=5)){
                    {
                        b = b+1;
                        printString("5<=x<=10;");
                    }
                    b = b+1;
                }
                else{
                    {
                        b = b-6;
                    }
                    printString("x<5");
                }
                b = b-1;
            }
            printInteger(b);
        }
        """
        expect = "5<=x<=10;8"
        self.assertTrue(TestCodeGen.test(input,expect,528))
    def test529_mixed_if(self):
        input = """
        main:function void(){
            b: integer = 7;
            {
                if(b>10){
                    printString("x>10");
                    {
                        b = b*2;
                        {
                            b = b-2;
                        }
                    }
                }
                else if ((b<=10) && (b>=5)){
                    {
                        b = b+1;
                        printString("5<=x<=10;");
                        {
                            b = b*1;
                            if(b==8) printString("x=8;");
                        }
                    }
                    b = b+1;
                }
                else{
                    {
                        b = b-6;
                    }
                    printString("x<5");
                }
                b = b-1;
            }
            printInteger(b);
        }
        """
        expect = "5<=x<=10;x=8;8"
        self.assertTrue(TestCodeGen.test(input,expect,529))
    def test530_simple_while(self):
        input = """
        main:function void(){
            b: integer = 5;
            while(b>0){
                printInteger(b);
                b = b-1;
            }
            printInteger(b);
        }
        """
        expect = "543210"
        self.assertTrue(TestCodeGen.test(input,expect,530))
    def test531_while_inline(self):
        input = """
        main:function void(){
            b: integer = 5;
            while(b>0) b=b-1;
            printInteger(b);
        }
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,531))
    def test532_nested_while(self):
        input = """
        main:function void(){
            b: integer = 5;
            while(b>0){
                i:integer = 2;
                while(i>0){
                    i = i-1;
                }
                b = b-1;
            }
            printInteger(b);
        }
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,532))
    def test533_simple_dowhile(self):
        input = """
        main:function void(){
            b: integer = 5;
            do{
                printInteger(b);
                b = b-1;
            }while(b>0);
            printInteger(b);
        }
        """
        expect = "543210"
        self.assertTrue(TestCodeGen.test(input,expect,533))
    def test534_dowhile_inline(self):
        input = """
        main:function void(){
            b: integer = 0;
            do {b=b+1;} while(b<0);
            printInteger(b);
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,534))
    def test535_nested_dowhile(self):
        input = """
        main:function void(){
            b: integer = 5;
            do{
                i:integer = 2;
                do{
                    i = i-1;
                } while(i>0);
                b = b-1;
            } while(b>0);
            printInteger(b);
        }
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,535))
    def test536_simple_for(self):
        input = """
        main:function void(){
            b: integer;
            for(b=0,b<5,b+1){
                printInteger(b);
            }
            printInteger(b);
        }
        """
        expect = "012345"
        self.assertTrue(TestCodeGen.test(input,expect,536))
    def test537_for_inline(self):
        input = """
        b: integer;
        main:function void(){
            for(b=0,b<5,b+1) printInteger(b);
            printInteger(b);
        }
        """
        expect = "012345"
        self.assertTrue(TestCodeGen.test(input,expect,537))
    def test538_nested_while(self):
        input = """
        main:function void(){
            b: integer = 5;
            for(b=5,b>0,b-1){
                i:integer;
                for(i=2,i>0,i-1){
                    b = b-1;
                }
                printInteger(b);
            }
            printInteger(b);
        }
        """
        expect = "30-1"
        self.assertTrue(TestCodeGen.test(input,expect,538))
    def test539_continue1(self):
        input = """
        main:function void(){
            b: integer = 5;
            for(b=5,b>0,b-1){
                if(b%2==0) {
                    continue;
                }
                printInteger(b);
            }
        }
        """
        expect = "531"
        self.assertTrue(TestCodeGen.test(input,expect,539))
    def test540_continue2(self):
        input = """
        main:function void(){
            b: integer = 10;
            while(b<15){
                if(b%3==0)
                    if(b%4==0){
                        b = b+1;
                        continue;
                    }
                printInteger(b);
                b=b+1;
            }
        }
        """
        expect = "10111314"
        self.assertTrue(TestCodeGen.test(input,expect,540))
    def test541_continue3(self):
        input = """
        main:function void(){
            b: integer = 5;
            for(b=2,b>0,b-1){
                i:integer;
                for(i=2,i>0,i-1){
                    if(b==i) continue;
                    else{
                        printInteger(i);
                        printInteger(b);
                    }
                }
            }
        }
        """
        expect = "1221"
        self.assertTrue(TestCodeGen.test(input,expect,541))
    def test542_break1(self):
        input = """
        main:function void(){
            b: integer = 5;
            for(b=5,b>0,b-1){
                if(b%2==0) {
                    break;
                }
                printInteger(b);
            }
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,542))
    def test543_break2(self):
        input = """
        main:function void(){
            b: integer = 10;
            while(b<15){
                if(b%3==0)
                    if(b%4==0){
                        b = b+1;
                        break;
                    }
                printInteger(b);
                b=b+1;
            }
        }
        """
        expect = "1011"
        self.assertTrue(TestCodeGen.test(input,expect,543))
    def test544_break3(self):
        input = """
        main:function void(){
            b: integer = 5;
            for(b=2,b>0,b-1){
                i:integer;
                for(i=2,i>0,i-1){
                    if(b!=i) break;
                    else{
                        printInteger(i);
                        printInteger(b);
                    }
                }
            }
        }
        """
        expect = "22"
        self.assertTrue(TestCodeGen.test(input,expect,544))
    def test545_init_1D_array(self):
        input = """
        main:function void(){
            a: array [5] of integer;
            l: integer = 5;
            i: integer = 0;
            for(i=0,i<l,i+1){
                a[i] = i;
                printInteger(a[i]);
            }
        }
        """
        expect = "01234"
        self.assertTrue(TestCodeGen.test(input,expect,545))
    def test546_init_2D_array(self):
        input = """
        main:function void(){
            a: array [2,3] of integer;
            r,c: integer = 2,3;
            i,j: integer = 0,0;
            for(i=0,i<r,i+1){
                for(j=0,j<c,j+1){
                    a[i,j] = i*j+j;
                    printInteger(a[i,j]);
                }
            }
        }
        """
        expect = "012024"
        self.assertTrue(TestCodeGen.test(input,expect,546))
    def test547_simple_idx_op_1(self):
        input = """
        main:function void(){
            a: array [1] of integer;
            i: integer;
            for(a[0]=3,a[0]>0,a[0]-1){
                printInteger(a[0]);
            }
            printInteger(a[0]);
        }
        """
        expect = "3210"
        self.assertTrue(TestCodeGen.test(input,expect,547))
    def test548_simple_idx_op_2(self):
        input = """
        main:function void(){
            a: array [3] of integer = {1,2,3};
            l,i: integer = 3,0;
            
            for(i=0,i<l,i+1){
                for(a[i]=a[i],a[i]>0,a[i]-1){
                    printInteger(a[i]);
                }
            }
        }
        """
        expect = "121321"
        self.assertTrue(TestCodeGen.test(input,expect,548))
    def test549_simple_idx_op_2(self):
        input = """
        main:function void(){
            a: array [3,3] of integer;
            n,i,j: integer = 3,0,0;
            for(i=0,i<n,i+1){
                for(j=0,j<n,j+1){
                    if(i!=j) continue;
                    a[i,j] = 1;
                }
            }
            for(i=0,i<n,i+1){
                for(j=0,j<n,j+1){
                    printInteger(a[i,j]);
                }
            }
        }
        """
        expect = "100010001"
        self.assertTrue(TestCodeGen.test(input,expect,549))
    def test550_mixed_iffor_1(self):
        input = """
        a: array [5] of integer;
        main:function void(){
            a = {1,2,3,4,5};
            i,l: integer = 0,5;
            for(i=0,i<l,i+1){
                if(a[i]%2==0) printInteger(a[i]);
                else continue;
            }
        }
        """
        expect = "24"
        self.assertTrue(TestCodeGen.test(input,expect,550))
    def test551_mixed_iffor_2(self):
        input = """
        main:function void(){
            i: integer = 0;
            while(true){
                printInteger(i);
                if(i==5) break;
                i=i+1;
            }
        }
        """
        expect = "012345"
        self.assertTrue(TestCodeGen.test(input,expect,551))
    def test552_mixed_iffor_3(self):
        input = """
        main:function void(){
            i: integer = 5;
            if(i>0)
                while(i>0){
                    printInteger(i);
                    i=i-1;
                }
            if(i==0){
                i = 5;
            }
            printInteger(i);
        }
        """
        expect = "543215"
        self.assertTrue(TestCodeGen.test(input,expect,552))
    def test553_mixed_iffor_4(self):
        input = """
        main:function void(){
            i: integer = 3;
            while(i>0){
                if(i%2==0) printInteger(9-i);
                else printInteger(i-9);
                i=i-1;
            }
        }
        """
        expect = "-67-8"
        self.assertTrue(TestCodeGen.test(input,expect,553))
    def test554_mixed_iffor_4(self):
        input = """
        a: array [3] of integer = {1,2,3};
        main:function void(){
            a = {4,5,6};
            l,i: integer = 3,0;
            for(i=0,i<l,i+1){
                if(a[i]==1) printString("Wrong");
                else{
                    printString("Right");
                    break;
                }
            }
            printInteger(i);
        }
        """
        expect = "Right0"
        self.assertTrue(TestCodeGen.test(input,expect,554)) 
    def test555_simple_funcdecl(self):
        input = """
        inc: function integer(i: integer){
            return i+1;
        }
        main:function void(){
            i: integer = 0;
            i = inc(i);
            printInteger(inc(i));
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,555))
    def test556_nested_funcdecl(self):
        input = """
        i: integer = 0;
        inc: function integer(i: integer){
            return i+1;
        }
        double: function integer(i: integer){
            return i*2;
        }
        main:function void(){
            printInteger(double(inc(i)));
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,556))
    def test557_nested_funcdecl(self):
        input = """
        i: integer = 0;
        inc: function integer(i: integer){
            return i+1;
        }
        double: function integer(i: integer){
            return i*2;
        }
        main:function void(){
            printInteger(double(inc(i)));
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,557)) 
    def test558_reversed_nested_funcdecl(self):
        input = """
        i: integer = 0;
        main:function void(){
            printInteger(double(inc(i)));
        }
        inc: function integer(i: integer){
            printInteger(i);
            return i+1;
        }
        double: function integer(i: integer){
            printInteger(i);
            return i*2;
        }
        """
        expect = "012"
        self.assertTrue(TestCodeGen.test(input,expect,558)) 
    def test559_simple_funcall(self):
        input = """
        i: integer = 1;
        main:function void(){
            i = inc(i) + double(i);
            printInteger(i);
        }
        inc: function integer(i: integer){
            return i+1;
        }
        double: function integer(i: integer){
            return i*2;
        }
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,559))
    def test560_complex_funcall(self):
        input = """
        main:function void(){
            i: integer = 1;
            i = (inc(i)*double(i)+inc(i))*double(i);
            printInteger(i);
        }
        inc: function integer(i: integer){
            return i+1;
        }
        double: function integer(i: integer){
            return i*2;
        }
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,560))
    def test561_no_return(self):
        input = """
        main:function void(){
            printHelloWorld();
        }
        printHelloWorld: function void(){
            printString("Hello World!");
        }
        """
        expect = "Hello World!"
        self.assertTrue(TestCodeGen.test(input,expect,561))
    def test562_coerced_return_1(self):
        input = """
        main:function void(){
            a: integer = 1;
            b: integer = 2;
            writeFloat(add(a,b));
        }
        add: function float(a: float, b:float){
            return a+b;
        }
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input,expect,562))
    def test563_coerced_return_2(self):
        input = """
        main:function void(){
            a: float = 1;
            b: integer = 2;
            writeFloat(add(a,b));
        }
        add: function float(a: float, b:integer){
            return a+b;
        }
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input,expect,563))
    def test564_mixed_funcall(self):
        input = """
        main:function void(){
            a: float = 1.0;
            b: float = 2.0;
            writeFloat(add(a*b-b/b+0.6,b-0.2));
        }
        add: function float(a: float, b:float){
            return a+b;
        }
        """
        expect = "3.4"
        self.assertTrue(TestCodeGen.test(input,expect,564))
    def test565_mixed_funcall_ops(self):
        input = """
        isOdd: function boolean(a: integer){
            return a%2==1;
        }
        getString: function string(a: string){
            return "GetString: "::a;
        }
        main:function void(){
            printBoolean(isOdd(7));
            printString(getString("Ez"));
        }
        """
        expect = "trueGetString: Ez"
        self.assertTrue(TestCodeGen.test(input,expect,565))
    def test566_funcall_array1(self):
        input = """
        getSum: function integer (arr: array [5] of integer, size: integer){
            res,i: integer=0,0;
            for(i=0,i<size,i+1){
                res = res + arr[i];
            }
            return res;
        }
        main:function void(){
            nums: array [5] of integer = {1,2,3,4,5};
            printInteger(getSum(nums,5));
        }
        """
        expect = "15"
        self.assertTrue(TestCodeGen.test(input,expect,566))
    def test567_funcall_array2(self):
        input = """
        doubleMap: function void (arr: array [5] of integer, size: integer){
            i: integer;
            for(i=0,i<size,i+1){
                arr[i] = arr[i] * 2;
            }
            printInteger(arr[2]);
        }
        main:function void(){
            nums: array [5] of integer = {1,2,3,4,5};
            doubleMap(nums,5);
        }
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,567))
    def test568_funcall_recursion1(self):
        input = """
        fib: function integer(n: integer){
            if((n==0)||(n==1)) return n;
            return fib(n-1)+fib(n-2);
        }
        main:function void(){
            fib5: integer = fib(6);
            printInteger(fib5);
        }
        """
        expect = "8"
        self.assertTrue(TestCodeGen.test(input,expect,568))
    def test569_funcall_recursion2(self):
        input = """
        findGCD: function integer(a: integer, b:integer){
            if (b == 0) return a;
            return findGCD(b, a % b);
        }
        main:function void(){
            gcd: integer = findGCD(10,24);
            printInteger(gcd);
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,569)) 
    def test570_funcall_idxops(self):
        input = """
        findGCD: function integer(a: integer, b:integer){
            if (b == 0) return a;
            return findGCD(b, a % b);
        }
        main:function void(){
            a: array [2] of integer = {10,24};
            gcd: integer = findGCD(a[0],a[1]);
            printInteger(gcd);
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,570))
    def test571_funcall_manytypes(self):
        input = """
        i: function integer(a: integer){
            return a;
        }
        s: function string(c: string){
            return c;
        }
        f: function float(b:float){
            return b;
        }
        b: function boolean(d: boolean){
            return d;
        }
        
        main:function void(){
            printInteger(i(1)+i(2));
            printString(s("1")::s("2"));
            writeFloat(f(1.0)+f(2.0));
            printBoolean(b(true)||b(false));
        }
        """
        expect = "3123.0true"
        self.assertTrue(TestCodeGen.test(input,expect,571)) 
    def test572_funcall_coercion(self):
        input = """
        i: function integer(a: integer){
            return a;
        }
        s: function string(c: string){
            return c;
        }
        f: function float(b:float){
            return b;
        }
        b: function boolean(d: boolean){
            return d;
        }
        
        main:function void(){
            writeFloat(f(1.0)+i(2));
        }
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input,expect,572))
    def test573_funcall_global(self):
        input = """
        a: float = f(1.0)+i(2);
        i: function integer(a: integer){
            return a;
        }
        s: function string(c: string){
            return c;
        }
        f: function float(b:float){
            return b;
        }
        b: function boolean(d: boolean){
            return d;
        }
        main:function void(){
            writeFloat(a);
        }
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input,expect,573))
    def test574_funcall_blocks(self):
        input = """
        i: function integer(a: integer){
            {
                return a;
            }
        }
        s: function string(c: string){
            return c;
        }
        f: function float(b:float){
            return b;
        }
        b: function boolean(d: boolean){
            return d;
        }
        
        main:function void(){
            a: float;
            {
                a = f(1.0);
                {
                    a = a+i(2);
                }
                writeFloat(a);
            }
        }
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input,expect,574)) 
    def test575_ref_array(self):
        input = """
        inc: function void(a: array[3] of integer, l: integer){
            i: integer;
            for(i=0,i<l,i+1){
                a[i] = a[i]+1;
            }
        }
        
        main:function void(){
            a: array[3] of integer = {1,2,3};
            inc(a,3);
            printInteger(a[2]);
        }
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,575)) 
    def test576_noref_var(self):
        input = """
        inc: function void(i: integer){
            i = i+1;
            return;
        }
        
        main:function void(){
            i: integer = 2;
            inc(i);
            printInteger(i);
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,576))
    def test577_simple_inherit(self):
        input = """
        foo: function void(inherit a: integer) {
            return;
        }
        foo1: function integer (b: integer) inherit foo {
            super(2);
            a = b+1;
            return a;
        }
        main:function void(){
            printInteger(foo1(1));
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,577)) 
    def test578_mixed_inherit_1(self):
        input = """
        foo: function void(inherit a: integer, b: integer, inherit c: integer) {
            return;
        }
        foo1: function integer (b: integer) inherit foo {
            super(1,2,3);
            return a+b+c;
        }
        main:function void(){
            printInteger(foo1(4));
        }
        """
        expect = "8"
        self.assertTrue(TestCodeGen.test(input,expect,578))
    def test579_mixed_inherit_2(self):
        input = """
        foo: function void(a: integer, b: integer) {
            return;
        }
        foo1: function integer (b: integer) inherit foo {
            super(2,3);
            a: integer = 1;
            return a;
        }
        main:function void(){
            printInteger(foo1(1));
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,579)) 
    def test580_empty_inherit(self):
        input = """
        foo: function void() {
            return;
        }
        foo1: function integer (b: integer) inherit foo {
            a: integer = 1;
            return a;
        }
        main:function void(){
            printInteger(foo1(1));
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,580))
    def test581_empty_inherit_2(self):
        input = """
        foo: function void(inherit b: integer) {
            return;
        }
        foo1: function integer (b: integer) inherit foo {
            preventDefault();
            a: integer = 1;
            return a;
        }
        main:function void(){
            printInteger(foo1(1));
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,581)) 
    def test582_test_passbyval(self):
        input = """
        main:function void(){
            j,k: integer = 10,15;
            phil(j,j,j+k); // 10,10,25
            printInteger(j); //<<10
            printInteger(k); //<<15
        }
        phil: function void(a: integer, b: integer, c: integer){
            b = b+5; //b=15
            b = a+c+4; // b=39
            printInteger(a); //<<10
            printInteger(b); //<<39
            printInteger(c); //<<25
        }
        """
        expect = "1039251015"
        self.assertTrue(TestCodeGen.test(input,expect,582))
    def test583_passbyvalue_result1(self):
        input = """
        phil: function void(out a: integer, out b: integer, c: integer){
            b = b+5; 
            b = a+c+4; // b=39
            printInteger(a); //<<10
            printInteger(b); //<<39
            printInteger(c); //<<25
        }
        main:function void(){
            j,k: integer = 10,15;
            phil(j,j,j+k); // 10,10,25
            printInteger(j); // <<39
            printInteger(k); // <<15
        }
        
        """
        expect = "1039253915"
        self.assertTrue(TestCodeGen.test(input,expect,583))
    def test584_passbyvalue_result2(self):
        input = """
        phil: function void(out a: integer, out b: integer, c: integer, out d: string){
            b = b+5; 
            b = a+c+4; // b=39
            printInteger(a); //<<10
            printInteger(b); //<<39
            printInteger(c); //<<25
            d = d::d;
        }
        main:function void(){
            j,k: integer = 10,15;
            s: string = "Hi";
            phil(j,j,j+k,s); // 10,10,25
            printInteger(j); // <<39
            printInteger(k); // <<15
            printString(s); // <<15
        }
        
        """
        expect = "1039253915HiHi"
        self.assertTrue(TestCodeGen.test(input,expect,584))
    def test585_passbyvalue_result3(self):
        input = """
        phil: function integer (out a: integer, out b: integer, c: integer){
            b = b+5; 
            b = a+c+4; // b=39
            printInteger(a); //<<10
            printInteger(b); //<<39
            printInteger(c); //<<25
            return a+b+c;
        }
        main:function void(){
            j,k: integer = 10,15;
            printInteger(phil(j,j,j+k)); // 10,10,25
            printInteger(j); // <<39
            printInteger(k); // <<15
        }
        """
        expect = "103925743915"
        self.assertTrue(TestCodeGen.test(input,expect,585))