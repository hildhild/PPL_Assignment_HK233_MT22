import unittest
from TestUtils import TestParser

# py run.py test ParserSuite
# py run.py test ASTGenSuite
class ParserSuite(unittest.TestCase):
    def test_short_vardecl11(self):
        input = """x: integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))
    
    def test_short_vardecl(self):
        """Test short variable declaration"""
        input = """delta: integer = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_full_vardecl(self):
        """Test full variable declaration"""
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_simple_program_with_UnExpr(self):
        """Test simple program"""
        input = """x:float = -5; 
        y: auto = !true;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_array_decl(self): 
        """Test simple program"""
        input = """a: array [4] of string;
        b: array[5] of float = {1.1,2.3,4.5}; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test_array_decl_string_and_float(self): 
        """Test simple program"""
        input = """a: array [16,16] of string = {"I", "Love","You"};
        b: array[5] of float = {1e2,10.21e2}; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_6(self):
        # Test declaration array
        input = """test1, test2 : array [3,4] of boolean;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_stringdecl(self):
        input = """x,y : string = "268","LTK";  """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_array_decl_int_and_boolean(self): 
        """Test simple program"""
        input = """a: array [16,16] of integer = {2_8, 1,2022,k};
        b: array[5] of boolean = {true,false,true}; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 209))
    def test_inherit_program(self): 
        """Simple program"""
        input = """dbs: function void () inherit dsa {
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_simple_program_with_stmt(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_inherit_program_with_variable(self): 
        """Simple program"""
        input = """dbs: function void (inherit a: integer, out b: float, inherit out c: auto) inherit dsa {
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 212))
    def test_inherit_program_with_array(self): 
        """Simple program"""
        input = """dbs: function array [5] of integer () inherit dsa {
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 213))
    def test_inherit_program_with_arrayParam(self): 
        """Simple program"""
        input = """dbs: function array [5] of integer (inherit a: array [9] of boolean) inherit dsa {
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 214))
    def test_inherit_program_with_arrayParam_and_stmt(self): 
        """Simple program"""
        input = """dbs: function array [5] of integer (inherit a: array [9] of boolean) inherit dsa {
            x:integer = -4;
            return a; 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 215))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 216))
    def test_program_with_for_stmt_2(self): 
        """Simple program"""
        input = """z: function boolean (inherit a: boolean) inherit dsa {
            for (i = 1, i < 10, i + 1) printInteger(i); 
            x:integer = !true;
            return a; 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_ifstmt(self): 
        """Simple program"""
        input = """_tester: function integer (inherit i: integer) inherit dsa {
            i:integer = 15 - 7 + 9;
            if (i%2==0) i = i + 1; 
            return i; 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 218))
    def test_ifstmt_withblock(self): 
        """Simple program"""
        input = """_tester: function integer (out i: integer) inherit dsa {
            i:integer = 15 - 7 + 9;
            if (i%2==0) {
                printInteger(i); 
            } 
            return i; 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 219))
    def test_ifelsestmt(self): 
        """Simple program"""
        input = """_tester: function integer (inherit i: integer) inherit dsa {
            i:integer = 15 - 7 + 9;
            if (i%2==0) i = i + 1;
            else i = i - 1; 
            return i; 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 220))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 221))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 222))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 223))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 224))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 225))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 226))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 227))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 228))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 229))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 230))
    def test_complicated_expr(self): 
        """Simple program"""
        input = """
        main: function void () {
                delta: integer = 3+34*30/5*16/4*2/2+19%4+2%2;
                printInt(delta);
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 231))
    def test_complicated_compareExpr(self): 
        """Simple program"""
        input = """
        main: function void () {
                a:integer = 100; 
                if (a % 7 == (3*2)) printString("True");
                else printString("False");  
                return 0; 
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_2DArray(self): 
        """Simple program"""
        input = """
        print2D: function void (arr: array[5,5] of integer) {
            for (i = 0, i < 5, i +1)
                for (j = 0, j < 5, j + 1)
                    printInteger(arr[i,j]); 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_2DArray_if(self): 
        """Simple program"""
        input = """
        print2D: function void (arr: array[5,5] of integer) {
            for (i = 0, i < 5, i +1)
                for (j = 0, j < 5, j + 1)
                    if (arr[i,j] == 4) break;  
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 234))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_SCOPE(self): 
        """Simple program"""
        input = """
        main: function void (){
            a:string = "HCMUT"::"K20";
            printString(a); 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 236))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_more_complex_program_with_variable(self):
        """More complex program"""
        input =	"""
foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

main: function void () {
     printInteger(4);
}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 238))
    def program_with_for_loop(self): 
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 238))
    def test_callexpr_global(self): 
        """Simple program"""
        input = """
                dbs: function integer () inherit dsa {
                return 1; 
        }
            x: integer = dbs(); 
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 239))
    def test_MINUS_Unexpr(self): 
        """Simple program"""
        input = """
                dbs: function integer () inherit dsa {
                return 1; 
        }
            x: integer = -dbs(); 
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_NOT_Unexpr(self): 
        """Simple program"""
        input = """
                dbs: function integer () inherit dsa {
                return 1; 
        }
            x: integer = !dbs(); 
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_MINUS_Unexpr_inExpr(self): 
        """Simple program"""
        input = """
                dbs: function integer () inherit dsa {
                return 1; 
        }
            x: integer = 25 * 7 + -dbs(); 
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_SubExpr_Global(self): 
        """Simple program"""
        input = """
                dbs: function integer () inherit dsa {
                return 1; 
        }
            x: integer = (25 + 7) * 4; 
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_IndexOp_Global(self): 
        """Simple program"""
        input = """
                a: array[3] of integer = {1,2,3}; 
            x: integer = a[1] * 4; 
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_IndexOp_Global(self): 
        """Simple program"""
        input = """
                a: array[3] of integer = {1,2,3}; 
            x: integer = a[1] * 4; 
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_booltype(self): 
        input = """a: boolean = true;  
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 246))
    def test_blockstmt_in_blockstmt(self): 
        input = """main : function void() {
                printString("This is block 0"); 
                {
                        printString("This is block 1"); 
                }
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 247))
    def test_dowhile_do_nothing(self): 
        input = """main : function void() {
                do {
                
                }
                while (true); 
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 248))
    def test_while_do_nothing(self): 
        input = """main : function void() {
                while(false){
                
                }
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 249))
    def test_for_do_nothing(self):
        input = """main : function void() {
                for (i = 0, i < 9,i +1) {
                
                }
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_if_do_nothing(self): 
        input = """main : function void() {
                if (1 > 2) { }
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 251))
    def test_ifelse_do_nothing(self): 
        input = """main : function void() {
                if (1 > 2) { } else {}
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 252))
    def test_for_do_nothing11(self):
        input = """main : function void() {
                a: array [10] of integer; 
                for (a[1] = 0, a[1] < 9, a[1] + 1) {
                }
        }"""
        expect = """Error on line 3 col 22: ["""
        self.assertTrue(TestParser.test(input, expect, 253))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_ifelse_do_nothing111111(self): 
        """More complex program"""
        input =	"""x: integer = 65;
        main: function integer () {
            a: float = 2.0;
            a = 6.9; 
            b: array [2022] of integer;
            b[0] = 0;
            for (b[0] = 0, b[0] < 1, b[0] + 1) b[1] = 0; 
            return 0; 
        }"""
        expect = """Error on line 7 col 18: ["""
        self.assertTrue(TestParser.test(input, expect, 256))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 257))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 258))
    def test_fundecl_with_arrayParam_stmt(self):
        """More complex program"""
        input = """calYear: function void (a: array [2_8] of integer) {
            printInteger(4); 
            if (a[0,0] < 10) a[0,3] = a[0,1];
            else {
                for (i = 0 , i < 8, i+1) a[0,i] = 2010 + i; 
            } 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 259))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 260))
    def test_comp_expr_if_stmt(self): 
        input = """main: function void () {
            a,b: integer = 0,1; 
            if ((a > b) && (b < 0) || (a < b) && (a == 2)) printString("Saitama Sensei"); 
            else {donothing: integer = 2023;}
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 261))
# if (a > b && b < 0 || a < b && a == 0) printString("Saitama Sensei"); 
    def test_calc_expr_if_stmt(self): 
        input = """main: function void () {
            a,b: integer = 0,1; 
            if (a < 2023) a = 100 * 7 - 4 + 68 * 120 / 64 % 34;
            else b = 88 - 4 * 7 - 4 * 2 - 4 - 5 / 5 + 1;
            printInteger(a); 
            printInteger(b); 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 262))
    def test_scope_expr(self): 
        input = """main: function void () {
            s: string = "HCM"::"UT";
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 263))
    def test_calc_mixed_expr_if_stmt1(self): 
        input = """
                a:float = 1_000 % 2 + .2E-10  + 8.98;
                b:float = (1 - 1) * 2 / 2 / 2 + 8 % 3 + ---10 * !!!true&&false;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 264))
    def test_calc_mixed_expr_if_stmt2(self): 
        input = """main: function void () {
            a,b: integer = 0,1; 
            if (a < 2023) a = 100 * 7 - 4 + 68 * 120 / 64 % 34;
            else b = (1 + 2 == 3) || (3 + 4 >= 8);
            printInteger(a); 
            printInteger(b); 
        }"""
        expect = """successful"""
# b = 1 + 2 == 3 || 3 + 4 >= 8;
        self.assertTrue(TestParser.test(input, expect, 265))
    def test_callexpr(self): 
        input = """
        binToDec: function integer (input: string, out result: integer){
        
        }
        main: function void (){
        a: float = binToDec("1111"); 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 266))
    def test_subexpr(self): 
        input = """

        main: function void (){
        a: float = (3.01 - 28.01) + (7.03 - 3.01); 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 267))
    def test_StringChar(self): 
        input = """
        main: function void (){
        checker: boolean = True; 
        if (!checker) printString("Don't look for me"); 
        else printString("Everything Goes On");
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 268))
    def test_unaryExpr2(self): 
        input = """

        main: function void (){
        hcmut = 21; 
        hcmut = 21 + -1; 
        printString("HCMUT"::"K20"); 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 269))
    def test_calc_mixed_expr_if_stmt3(self): 
        input = """main: function void () {
            a,b: integer = 0,1; 
            if (a < 2023) a = 100 * 7 + -4 + 68/ 64 % 34;
            else b = !(1 + 2 == 3) || 3 + 4 >= 8;
            printInteger(a); 
            printInteger(b); 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 270))
    def test_calc_mixed_expr_if_stmt4(self): 
        input = """main : function void() {
                x : integer ;
                if(x==3){} else {z : integer = 3;}
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 271)) 
    def test_ArrayCell(self): 
        input = """main : function void() {
                a: array [16,16] of integer; 
                b: integer;
                b = a[15,15]; 
            }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_compare_easy1(self): 
        input = """main : function void() {
                a: integer = 1990; 
                b: float = 19_75e2;  
                if (a >= b) {a = b; }
                if (a <= b) {a = a + 1;}
                if (a == b) {b = b + 1; }
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 273))
    def test_compare_easy2(self): 
        input = """main : function void() {
                a: integer = 1990; 
                b: float = 19_75e2;  
                if (a > b) {a = b; }
                if (a < b) {a = a + 1;}
                if (a != b) {b = b + 1; }
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 274))
    def test_compare_hard1(self): 
        input = """main : function void() {
                a: integer = 2002; 
                b: integer = 2000;  
                c: boolean = (a >= b); 
        }"""
# c: boolean = a >= b <= 2000 == 1968 != 1970 < 2022 > 2023;
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 275))
    def test_compare_hard2(self): 
        input = """main : function void() {
                a: integer = 2002; 
                b: integer = 2000;  
                c: boolean = a >= (b + 2 / (4* 2 + 4)); 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 276))
    def test_compare_easy3(self): 
        input = """main : function void() {
                a: integer = 2002; 
                b: array [10] of integer;  
                if (b[0] > a) a = b[0]; 
                else b[0] = a; 
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 277))
    def test_compare_easy4(self):
        input = """
            x : integer;
            main : function void () {count(1/100,2027*2028+1);}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
    def test_autoParam(self):
        input = '''
            main : function void (x : auto) {}
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
    def test_autoFunction(self):
        input = '''
                main : function auto (inherit out x : auto){}
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
    def test_CONCATSTRING(self):
        input = """
                x: string = "Everything";
                y: string = "Goes On";
                z: string = x::y;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_CONCATSTRING2(self):
        input = """
                x: string = "He asked me: ";
                y: string = " \\"Where is John\\" ";
                z: string = x::y;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_STRING_HARD(self): 
        input = """ lolStr:string = " Test escape \\\\ "; """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,288))
# " Test escape \\b \\f \\r \\n \\t \\' \\\\ "; """
    def test_FLOAT1(self): 
        input = """fl1:float = 4.;
                  fl2:float = .75e1; 
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,289))
    def test_arrayAssign(self): 
        input = """
        a: array [3] of integer = {c+d, e*f, true, false};
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,290))
    def test_arrAssign2(self): 
        input = """
        a,b: array [3] of integer = {c+d, e*f} , {1,2,3};
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,291))
    def test_arrAssign3(self): 
        input = """
        a,b: array [3] of integer = c,d;

        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,292))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 300))
    def test_expr_function_with_array_comment(self): 
        input =  """ 
        fact: function integer (n: integer) {
            if ((n == 0) || (n <= 27)) return 1;
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + fact(0);
            return; 
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 9001))
#     def test_expr_function_with_array_comment2(self): 
#         input =  """bFS: function void (arr: array [1_0,1_0] of integer , size: integer) {
#         visited: array [1000] of boolean;
#         for (i = 0, i < size - 1, i + 1) visited[i] = false; 
#         queue: array [1000] of integer;
#         front,rear: integer = 0,0;
#         visited[9] = true;
#         queue[1] = size;
#         while (front != rear){
#             s = queue[9];
#             front = front + 1; 
#             printInteger(s);
#         for (adjacent = 0, adjacent < g, adjacent +1)
#                 {
#             if (adj[8,7] && !visited[9]) {
#                 visited[9] = true;
#                 queue[9] = adjacent;
#                 front = front +1; 
#             }
#         }
#     }
# }"""
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 200))
