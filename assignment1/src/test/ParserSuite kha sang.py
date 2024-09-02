import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
        200-209: Single Cases
        210-219: Type
        220-229: Declaration
        230-249: Expressions
        250-279: Statements
        280-299: Mixed Cases
    """

    # Single Cases
    def test200_simple_program(self):
        """Simple program: int main() {}"""
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))

    def test201_complex_program(self):
        input = """
            x : integer = 65;
            
            fact : function integer (n:integer) {
                if(n==0) return true;
                else return n*fact(n-1);
            }
            
            inc:function void (out n:integer,delta:integer) {
                n=n+delta;
            }
            main : function void () {
                delta:integer = fact(3);
                inc(x,delta);
                printInteger(x);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test202_conditionals_without_brackets(self):
        input = """
        main: function void (){
            if(a == "1") print(a);
            else print("Nothing");
            
            if(a == 1){
                a = a+1;
            }
            else{
                a = a-1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test203_conditionals_with_brackets(self):
        input = """  
        main: function void (){
            if(a == 1){
                a = a+1;
            }
            else{
                a = a-1;
            }
        }         
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test204_for_loops(self):
        input = """
        main: function void (){
            for(i=1,i<5,i+1){
                print(i);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test205_while_loops(self):
        input = """
        main: function void (){
            while(i<5){
                print(i);
                i=i+1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test206_dowhile_loops(self):
        input = """
        main: function void (){
            do {
                print(i);
                i=i+1;
            } while(i<5);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test207_kw_loops(self):
        input = """
        main: function void (){
            for(i=1,i<5,i+1){
                if(i<3) continue;
                if(i==4) break;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test208_loops_and_conditionals(self):
        input = """
        main: function void (){
            for(i=1,i<5,i+1){
                if(i>3) print(i);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test209_block(self):
        input = """
        main: function void (){
            {
                r, s: integer;
                r = 2.0;
                a, b: array [50] of integer;
                s = r * r * myPI;
                a[0] = s;
            }
        }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    # Type
    def test210_bool_type(self):
        input = """
        void_func: function void () {
            a: boolean = true;
            b: boolean = false;
            printBoolean(!a);
            printBoolean(a&&b);
            printBoolean(a||b);
            printBoolean(a==b);
            printBoolean(a!=b);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test211_arith_int_type(self):
        input = """
        void_func: function void () {
            a: integer = 1_234;
            b: integer = -5_678;
            printInteger(a+b);
            printInteger(a-b);
            printInteger(a*b);
            printInteger(a/b);
            printInteger(a%b);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test212_arith_float_type(self):
        input = """
        void_func: function void () {
            a: integer = 1_234e-12;
            b: integer = -5_678.5e+2;
            writeFloat(a+b);
            writeFloat(a-b);
            writeFloat(a*b);
            writeFloat(a/b);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test213_relation_numeric_type(self):
        input = """
        void_func: function void () {
            a: integer = 5;
            b: float = 5.1;
            printBoolean(a>b);
            printBoolean(a>=b);
            printBoolean(a<b);
            printBoolean(a<=b);
            printBoolean(a!=b);
            printBoolean(a==b);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test214_string_type(self):
        input = """
        void_func: function void () {
            a: string = "Hello";
            b: string = "World";
            printString(a::b);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test215_array_type(self):
        input = """
        void_func: function void () {
            a: array [5] of integer;
            printInteger(a[0]);
            printInteger(a[2]);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test216_multidim_array_type(self):
        input = """
        void_func: function void () {
            a: array [5,2] of integer;
            printInteger(a[0,1]);
            printInteger(a[3,0]);
            printInteger(a[3,1]);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test217_void_and_auto_type(self):
        input = """
            void_func: function void () {
                return;
            }
            auto_func: function auto (a:integer) {
                return a*a;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test218_invalid_array_size_1(self):
        input = """
        void_func: function void () {
            a: array [5_123,0] of integer;
            printInteger(a[0,1]);
            printInteger(a[3,0]);
            printInteger(a[3,1]);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test219_invalid_array_size_1(self):
        input = """
            a: array [5.2] of float;
            printInteger(a[0]);
            printInteger(a[2]);
        """
        expect = "Error on line 2 col 22: 5.2"
        self.assertTrue(TestParser.test(input, expect, 219))

    # Declaration
    def test220_global_variables(self):
        input = """
            a: integer;
            b: float;
            c: string;
            d: boolean;
            e: auto;
            f: array [5] of float;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test221_init_global_variables(self):
        input = """
            a: integer = 5;
            b: float = 7.3;
            c: string = "cool";
            d: boolean = true;
            e: auto = 7e6;
            e: string = getString();
            g: string = c;
            h: string = g::c;
            i: boolean= d && true;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test222_init_multi_variables(self):
        input = """
            a1,a2,a3: integer = a[5],6,7;
            b1,b2,b3: float = 7.3,3.5e7,0.9;
            c1,c2: string = "cool","cool.test";
            d1,d2: boolean = true,false;
            e1,e2: auto = 7e6,"boyy";
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test223_nonparam_function_decl(self):
        input = """
            empty_function: function void () {
                printInteger(5);
            }
            return_function: function integer () {
                return 5;
            }
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test224_nonparam_function_decl(self):
        input = """
            empty_function: function void (a:integer, b:integer) {
                printInteger(a+b);
                return ;
            }
            return_function: function integer (a:integer, b:integer) {
                return a+b;
            }
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test225_local_var_function(self):
        input = """
            empty_function: function void (a:integer, b:integer) {
                local: integer = 5;
                return local+a+b;
            }
            return_function: function integer (a:integer, b:integer) {
                local: integer = 5;
                return local+a+b;
            }
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test226_complex_function(self):
        input = """
            empty_function: function void (a:integer, b:integer) {
                local: integer = 5;
                return local+a+b;
            }
            return_function: function integer (out a:integer, b:integer) inherit empty_function{
                local: integer = 5;
                return local+a+b;
            }
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test227_noblock_function(self):
        input = """
            empty_function: function void (a:integer, b:integer)
                local: integer = 5;
                return local+a+b;
        """
        expect = "Error on line 3 col 16: local"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test228_unclosed_function(self):
        input = """
            empty_function: function void (a:integer, b:integer){
                local: integer = 5;
                return local+a+b;
            )
        """
        expect = "Error on line 5 col 12: )"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test229_notequal_init_var(self):
        input = """a,b,c:integer = 5,6,7,8;"""
        expect = "Error on line 1 col 21: ,"
        self.assertTrue(TestParser.test(input, expect, 229))

    # EXPRESSIONS
    def test230_index_1D_ops(self):
        input = """
        main: function void (){
            a[0] = 5;
            b[1] = "string";
            c[3] = 0.5e6;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test231_index_ND_ops(self):
        input = """
        main: function void (){
            b[0,1] = "string";
            c[1,2,3] = 0.5e6;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test232_empty_call_expr(self):
        input = """
        main: function void () {
            hello();
            good_boy();
            are_you_ok();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test233_param_lit_call_expr(self):
        input = """
        main: function void () {
            hello(1);
            good_boy("Sang","Kha");
            are_you_ok(true);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test234_missing_param_call_expr(self):
        input = """
        main: function void (){
            hello(a,b,);
        }
        """
        expect = "Error on line 3 col 22: )"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test235_missing_comma_call_expr(self):
        input = """
        main: function void (){
            hello(1"wrong");
        }
        """
        expect = "Error on line 3 col 19: wrong"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test236_unexpected_comma_call_expr(self):
        input = """
        main: function void (){
            hello(a,b,,);
        }
        """
        expect = "Error on line 3 col 22: ,"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test237_param_id_call_expr(self):
        input = """
        main: function void (){
            hello(a);
            good_boy(b,e);
            are_you_ok(c,d,f);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test238_unclosing_paren_array(self):
        input = """
        main: function void (){
            a[0 = 5;
        }
        """
        expect = "Error on line 3 col 16: ="
        self.assertTrue(TestParser.test(input, expect, 238))

    def test239_unexpected_paren_array(self):
        input = """
        main: function void (){
            a[0]] = 5;
        }
        """
        expect = "Error on line 3 col 16: ]"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test240_nested_func_call(self):
        input = """
        main: function auto (){
            func(func(),5,foo());
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test241_unary_operator(self):
        input = """
        main: function void (){
            a = -4;
            a = --4;
            a = !true;
            a = !!true;
            a = !!!true;
            a = !!!!!!!!(True && False);
            a = ------------ (1 + 2 * 3 - 4 + 5 / 6 - 7);
            a =  !(1 + 2 * 3 - 4 + 5 / 6 - 7);
            a = b[5];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test242_nested_array(self):
        input = """
        main: function void (){
            a = {1,2,3,{4,5,6}};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test243_multivar_array(self):
        input = """
        main: function void (){   
            bc(a[1,2,3]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test244_unclosed_nested_array(self):
        input = """
        main: function void (){
            func(func(,5);
        }
        """
        expect = "Error on line 3 col 22: ,"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test245_binary_operator(self):
        input = """
        main: function void (){
            a = 1*b;
            a = 1+b;
            a = 1-b;
            a = b/2;
            a = true && false;
            a = true || false;
            a = a==b;
            a = a!=b;
            a = a::b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test246_complex_binary_operator(self):
        input = """
        main: function void (){ 
            a = a*b*c + a/b/c;
            a = a + b%c + d;
            a = a&&b || a>=b && b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test247_complex_binary_operator_with_paren(self):
        input = """
        main: function void (){
            a = a*b*(c+a)/b/c;
            a = a + (b%c + d);
            a = (a&&b) || (a>=b && b);
            a = (a + (-b - c*(d+e)))*5;
            a = a::((b::c)::d);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test248_missing_unary(self):
        input = """
        main: function void (){
            a = 8--;
        }
        """
        expect = "Error on line 3 col 19: ;"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test249_missing_binary(self):
        input = """
        main: function void (){
            a = 8*8-9/;
        }
        """
        expect = "Error on line 3 col 22: ;"
        self.assertTrue(TestParser.test(input, expect, 249))

    # Statements
    def test250_scalar_asm(self):
        input = """
        main: function void (){
            a = 5;
            b = "ez";
            c = .2e-3;
            d = {a,b,c,d};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test251_idxops_asm(self):
        input = """
        main: function void (){
            a[0] = 2;
            a[1,2,3] = 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test252_complex_asm(self):
        input = """
        main: function void (){
            a[0] = func(1,2,"3");
            a[1,2] = omg(omg(1));
            ez = ez*2 + 6*(7-func());
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test253_too_many_asm_id(self):
        input = """
        main: function void (){
            a,b = 5;
        }
        """
        expect = "Error on line 3 col 16: ="
        self.assertTrue(TestParser.test(input, expect, 253))

    def test254_normal_if(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test255_if_3case(self):
        input = """
        main: function void (){
            if(calc_score(score)==9){
                printString("idolll :3");
            }
            else if (calc_score(score)==5){
                printString("vua du qua mon :))");
            }
            else if(calc_score(score)==13){
                printString("hoc lai di cung");
            }
            else{
                printString("doan xem");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test256_if_oneline(self):
        input = """
        main: function void (){
            if(happy) setHappy(true);
            else setHappy(false);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test257_if_forgotten_curly(self):
        input = """
        main: function void (){
            if(happy && print==true) 
                setHappy(true);
                printString("happyyyy");
            else setHappy(false);
        }
        """
        expect = "Error on line 6 col 12: else"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test258_nested_if(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test259_nested_if_oneline(self):
        input = """
        main: function void (){
            if(rich==true)
                if(nice==true)
                    setState("kind and rich");
                else setState("unkind and rich");
            else setState("not rich");
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test260_normal_loop(self):
        input = """
        main: function void (){
            for(i=get_started(),i<=5,i+2){
                printInteger("Yoooo!");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test261_nested_forloop(self):
        input = """
        main: function void (){
            for(i=get_started(), i<5*2, i+2){
                for(j=get_started(), j<5*2, j+1){
                    printInteger(i+j);
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test262_normal_while(self):
        input = """
        main: function void (){
            while(a<5){
                printInteger(a);
                a = a+1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test263_nested_while(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test264_normal_dowhile(self):
        input = """
        main: function void (){
            do {
                a = a+1;
                b = b-1;
            }
            while(a!=b);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test265_nonblock_dowhile(self):
        input = """
        main: function void (){
            do 
                a = a+1;
            while(a<10);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test266_nested_dowhile(self):
        input = """
        main: function void (){
            do{ 
                a = a+1;
                i: integer = 0;
                do{
                    printInteger(i);
                    i = i+1;
                }
                while(i<a);
            }
            while(a<10);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test267_break_continue_loop(self):
        input = """
        main: function void (){
            for(i=1,i<getMax(),i+1){
                if(i==threshold)
                    break;
                if(i<0)
                    continue;
                else printInteger(i);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test268_mixed_loop(self):
        input = """
        main: function void (){
            for(i=1,i<getMax(),i+1){
                while(true){
                    print("kaka");
                    do{
                        print("kuku");
                    }
                    while(false);
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test269_oneline_loop(self):
        input = """
        main: function void (){
            k: integer = 5;
            for(i=1,i<getMax(),i+1)
                printInteger(i);
            while((k<200) && (k>0))
                k = k + 5;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test270_normal_call(self):
        input = """
        main: function void (){
            
            hello();
            hello("Sang");
            hello("Sang","Kha");
            hello(hello("Sang"),"Kha");
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test271_nested_call(self):
        input = """
        main: function void (){
            f(f());
            f(f(f(f(f()))));
            f(f(f(f(f(f())))),f(f(f(f(f())))));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test272_expr_call(self):
        input = """
        main: function void (){   
            f(1*x,_123,"sss"::"aaa",dsa("dsa"),x%5);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test273_normal_block(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test274_unclose_block(self):
        input = """
        main: function void(){
            {
                hello();
                a:integer = 1;
            {
                hello();
                a:integer = 1;
            }
        }
        """
        expect = "Error on line 11 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test275_normal_return(self):
        input = """
            hello: function void(){
                printString("hello");
            }
            one: function integer(x:integer){
                return 1;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test276_complex_return(self):
        input = """
            isOdd: function boolean(x:integer){
                return x!=0;
            }
            getArr: function array [3] of integer (x:integer){
                return {x,x*2,x*3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test277_invalid_return(self):
        input = """
            mismatchRet: function void(){
                return return;
            }
        """
        expect = "Error on line 3 col 23: return"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test278_return_not_in_func(self):  # problem: can not solve this with lexer
        input = """
            missingRet: function void(){
                print("hello");
            }
            return 1;
        """
        expect = "Error on line 5 col 12: return"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test279_empty_program(self):
        input = """
        
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 279))

    # Mixed
    def test280_binary_search(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test281_interpolation_search(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test282_selection_sort(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test283_merge_sort(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test284_quick_sort(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test285_heap_sort(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test286_insertion_sort(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test287_find_depth_tree(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test288_lcs(self):
        input = """
            lcs: function int (out X:array [100] of integer, out Y:array [100] of integer, n:integer, m:integer){
                if (m == 0 || n == 0)
                    return 0;
                if (X[m-1] == Y[n-1])
                    return 1 + lcs(X, Y, m-1, n-1);
                else
                    return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test288_lcs(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test289_spiral_matrix(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test290_unparen_for_nonassoc_relop(self):
        input = """
            main: function void (){    
                while(a>5 && a<10){
                    "something"
                }
            }
        """
        expect = "Error on line 3 col 30: <"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test291_comment_before_block(self):
        input = """
            main: function void (){
                while((a>5) && (a<10))/*this is a comment*/{
                    a = 7.5;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test292_return_if_stmt(self):
        input = """
            main: function void () {
                return (if (a>5) {});
            }
        """
        expect = "Error on line 3 col 24: if"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test293_call_if_stmt(self):
        input = """
            main: function void () {
                if_call((if (a>5) {}),"007")
            }
        """
        expect = "Error on line 3 col 25: if"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test294_wrong_indexing_stmt(self):
        input = """
            main: function void () {
                printInt(a[1][2]); // parser can't catch this error?
            }
        """
        expect = "Error on line 3 col 29: ["
        self.assertTrue(TestParser.test(input, expect, 294))

    def test295_wrong_param_stmt(self):
        input = """
            isOdd: function boolean(x,y:integer){
                return x%y!=0;
            }
        """
        expect = "Error on line 2 col 37: ,"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test296_wrong_complex_indexing_stmt(self):
        input = """
            main: function void () {
                printInt(a[1*2+3,2+2/1]);
                printInt(a[1||2]);
                a: array ["a"] of integer;
            }
        """
        expect = "Error on line 5 col 26: a"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test297_unparen_for_nonassoc_string(self):
        input = """
            main: function void () {
                printString(a::b::c);
            }
        """
        expect = "Error on line 3 col 32: ::"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test298_funcall_as_operands(self):
        input = """
            main: function void () {
                nc(getString(a)::getString(b));
                lc(getInt(1)+getInt(2)*getInt(3));
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    # def test299_array_init(self):
    #     input = """
    #         main: function void () {
    #             a,b,c: array [5] of integer = {1,2,3},{3,4,5},{5,6,7,8},{};
    #         }
    #     """
    #     expect = "Error on line 3 col 71: ,"
    #     self.assertTrue(TestParser.test(input, expect, 299))
