import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_2(self):
        input = """delta: integer = 13;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_3(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n <= 1) return 1;
            else return n*fact(n-1);
        }
        inc: function void(out n: integer, delta: integer) {
            return n + delta;
        }
        main: function void() {
            printInteger(fact(3));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_4(self):
        input = """x:integer = 4;
        main: function void() {x = x + 1;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test_5(self):
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = """Error on line 1 col 29: ;"""
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_6(self):
        input = """a, b: array [5] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_7(self):
        input = """main: function void() {super(1+1,2+2);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_8(self):
        input = """main: function void() {
r, s: integer;
r = 2.0;
a, b: array [5] of integer;
s = r * r * myPI;
a[0] = s;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_9(self):
        input = """main: function void() {printString(\"Hello\"::\"World!\");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 209))
    def test_10(self):
        input = """main: function void() {while (i > 1) i = i- 1;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_11(self):
        input = """main: function void() {
        if (1+1 == 2) printString("True");
        else if (1+1 == 3) printString("false");
        else printString("default");
        }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_12(self):
        input = """
        is_prime: function boolean (n: integer) {
            // This function to check is a prime number
            res: boolean = true;
            for (i = 2, i < sqrt(n), i + 1) {
                if (n % i == 0) {
                    res = false;
                    break;
                }
            }
            return res;
        }

        main: function void() {
            for (i = 1, i < 10, i + 1) {
                printString(is_prime(i));
            }
        }

        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 212))
        
    def test_13(self):
        input = """delta: boolean = true;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 213))
    def test_14(self):
        input = """x: integer = 0;
        fact: function integer (n:integer) inherit fac {
            if (n <= 1) return 1;
            return n*fact(n-1);
        }
        main: function void() {
            writeInt(fact(10));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test_15(self):
        input = """a: array [3_2] of string = {"Kangxi", "Yongzheng", "Qianlong"};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
    def test_16(self):
        input = """a: array[4] of integer;
        a[1] = 2; a[2] = 3; a[3] = 4;"""
        expect = "Error on line 2 col 9: ["
        self.assertTrue(TestParser.test(input, expect, 216))
    def test_17(self):
        input = """flag: boolean = (1<2)<3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_18(self):
        input = """main: function void() {
        readInteger();
        printInteger(1);
        readFloat();
        printFloat(1.0);
        readBoolean();
        printBoolean(1);
        readString();
        printString("Hello world");
        super(a+1, 2+2);
        preventDefault();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    
    def test_19(self):
        input = """main: function void() {
readInteger(1);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    
    def test_20(self):
        input = """main: function void() {
readFloat(1);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
        
    def test_21(self):
        input = """main: function void() {
readBoolean(true);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
    #aasdasdf
    def test_22(self):
        test_case = """ str : string = \"123\"; 
        a: integer = 150;
        main: function void() {printString(str + a);}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test_case, expect, 222))

    def test_23(self):
        test_case = """ add: function integer(a: integer, b: integer){
            return a + b;
        }
        main: function void(){
            a, b: integer = 3, 4;
            printInt(a, b);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test_case, expect, 223))

    def test_24(self):
        test_case = """ str: string;
        str = \"abc\";
        index: integer = 2;
        main: function void() {printString(str[index]);}
        """
        expect = "Error on line 2 col 12: ="
        self.assertTrue(TestParser.test(test_case, expect, 224))

    def test_25(self):
        test_case = """ phase1 : string = \"Osmanthus wine \";
        phase2 : string =\"tastes \\n the \\n same \\n as \\n I \\n remember. \\n \";
        main: function void() {printString(phase1::phase2);}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test_case, expect, 225))

    def test_26(self):
        test_case = """a: array [5] of integer;
        main: function void() { printInt(a[5]);}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test_case, expect, 226))

    def test_27_recursion(self):
        test_case = """pascalTri: function integer(a: integer, b: integer){
            if ((a == 0 || a) == b) return 1;
            return pascalTri(a - 1, b - 1) + pascalTri(a - 1, b);
        }
        main: function void(){
            input1, input2: integer = 5, 3;
            printInt(pascalTri(input1, input2));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test_case, expect, 227))

    def test_28_forLoopTest(self):
        test_case = """a: integer = 0;
        main: function void() {
        for (i = 0, i < 5, i <= 1) {
            a = a + 1;
        }
        printInt(a);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test_case, expect, 228))
        
    def test_29_BubbleSort(self):
        test_case = """arr: array [5] of integer;
        arr[0] = 4; arr[1] = 2; arr[2] = 3;
        arr[3] = 10; arr[4] = -5;
        for (i = 0, i < 5, i + 1) {
            for (j = i + 1, j < 5, j + 1){
                if (arr[i] < arr[j]){
                    temp: integer = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        for (i = 0, i < 5, i + 1){
            printInt(arr[i]);
            printString(\" \");
        }
        """
        expect = "Error on line 2 col 11: ["
        self.assertTrue(TestParser.test(test_case, expect, 229))

    def test_30(self):
        input = """main: function void() {
        preventDefault(fatherFunc);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_31(self):
        input = """main: function void() {
        printFloat(1.1,2.2);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_32_float_test(self):
        input = """a, b: float = 1.999999, 2.999999999;
        main: function void() {printFLoat(a + b);}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_33_simpleMath(self):
        input = """main: function void() {
        printInt(5 + 4 / 2 * 7 + 1 * (9 - 9) +);        
        }"""
        expect = "Error on line 2 col 46: )"
        self.assertTrue(TestParser.test(input, expect, 233))
    
    def test_34_funcReturnType(self):
        input = """func: function integer(a: integer, b: integer){
            str: string = \"a + b\";
            return str;
        }
        main: function void(){
            printInt(func(1, 2));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_35_doubleType(self):
        input = """main: function void() {
str: string integer = 123;
}"""
        expect = "Error on line 2 col 12: integer"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_36_quickPower(self):
        input = """pow: function integer(a: integer, b: integer){
            if (b == 0) return 1;
            if (b == 1) return a;
            if (b%2 == 0){
                r: integer = pow(a, b/2);
                return r*r;
            }
            else{
                return a*pow(a,b-1);
            }
        }
        main: function void(){
            printInt(pow(4,10));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_37_negativeIndex(self):
        input = """a: array[3] of integer;
        a[-1] = 10;
        main: function void() {printInt(a[-1])};
        """
        expect = "Error on line 2 col 9: ["
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_38_chainCompare(self):
        input = """a, b, c: integer = 0, 3, 5;
        main: function void() {if ((a < b) < c){
            printInt(1);
        }
        else printInt(0);}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_39_boolCast(self):
        input = """num: integer = 15;
        main: function void() {if (num) num = num+1;
        printInt(num);}        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
        
    def test_40(self):
        input = """main: function void() {while (i) {{a:integer;}}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_41(self):
        input = """x: auto;
        main: function void() {x = \"lemon\";
        x = x + 1;}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_42(self):
        input = """x: auto = 1+a[2]*1<(2<3)/4%5;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))
    
    def test_43(self):
        input = """x: string = \"\\y\" """
        expect = "\y"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_44(self):
        input = """x: auto;
        main: function void() {
        x = \"lemon\";
        x = x + 1;
        x = 1;
        x = 1.1;}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    
    def test_45(self):
        input = """x: boolean = true;
        main: function void() {do {x= (x+1<2)<3;}
        while (x);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_46_pyro_electro(self):
        input = """func: function integer(a: integer, b: integer){
            return a + b;
        }
        func: function integer(a: integer){
            return -a;
        }
        main: function void(){
            printInt(func(1,2));
            printString(\" \\n \");
            printInt(func(1));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_47(self):
        input = """main: function void() {do {} while(x+1);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_48_C_supremacy(self):
        input = """string st = \"123123\";
        """
        expect = "Error on line 1 col 0: string"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_49(self):
        input = """a, b, c: float = 1.4, 2.6, 7;
        for (i = a + b - c, i < a + b + c, i + 0.5){
            printInt(i);
        }
        """
        expect = "Error on line 2 col 8: for" #???
        self.assertTrue(TestParser.test(input, expect, 249))
    
    def test_50(self):
        input = """a : integer = 3.14;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_51(self):
        input = """main: function void(){
            a: array[5] of integer;
            b: array[6] of integer;
            a = b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
    
    def test_52(self):
        input = """func: function array[10007] of float(a: integer){
            arr: array[10007] of float;
            arr[0] = a;
            return arr;
        }
        main: function void(){
            func(10);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
    
    def test_53(self):
        input = """#define fto(i, a, b) for (int i = a; i < b; i++)
        """
        expect = "#"
        self.assertTrue(TestParser.test(input, expect, 253))
    
    def test_54(self):
        input = """ModifyEXP:function void (EXP:integer){
            if (EXP < 0) EXP = 0;
            if (EXP > 900) EXP = 900;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_55(self):
        input = """main: function void(){
            str: string = \"abc\";
            for (i = 0, i < 3, i + 4){
                printString(str[i]);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_56(self):
        input = """int power(int x, int y) {
            int power = 1;
            for (int i = 1; i <= y; i++){
                power *= x;    
            }
            return power;
        }"""
        expect = "Error on line 1 col 4: power"
        self.assertTrue(TestParser.test(input, expect, 256))
    
    def test_57(self):
        input = """int firstMeet(int& EXP1, int& EXP2, const int& E1){
        //Complete this function to gain point on task 1
        if (E1 > 999 || E1 < 0) {
            return -999;
        }"""
        expect = "&"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_58(self):
        input = """int power(int a, int b){
            if (b == 1) return a;
            if (b == 0) return 1;
            if (b%2 == 0){
                int res = power(a, b/2);
                return res*res;
            }
            else{
                return a * power(a, b-1);
            }
        }

        int calc(char str[]) {
            // TODO
            int res = 0;
            for (int i = strlen(str)-1; i >= 0; --i){
                if (str[i] == '1'){
                    res += power(2, strlen(str)-1 - i);
                }
            }
            return res;
        }

        int main(){
            char str[] = "001011" ;
            cout << calc(str);
            return 0;
        }"""
        expect = "'"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_59(self):
        input = """else {
        ModifyEXP(EXP1);
        ModifyEXP(EXP2);
        """
        expect = "Error on line 1 col 0: else"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_60(self):
        input = """case1:boolean = (E1 >= 0) && E1 <= 399;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
    
    def test_61(self):
        input = """x : integer = (3+2)/5*6-13*13/7;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
    
    def test_62(self):
        input = """main:function void() {if (case1) {
            if (E1 >= 0 && (E1 <= 49)) {
                EXP2 += EXP2_case1_1;
            }}
            """
        expect = "Error on line 3 col 21: +"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_63(self):
        input = """str1, str2: string = \"abz\", \"xyc\", 123;"""
        expect = "Error on line 1 col 33: ,"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_64(self):
        input = """str1, str2: string = \"abz\", \"xyc\";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
    
    def test_65(self):
        input = """main: function void(out a: integer){
            a = a + 1;
        }

        main: function void(){
            a: integer = 0;
            main(a);
            printInt(a);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_66(self):
        input = """func: function integer(out str: string){
            printString(str);
        }
        main: function void(){
            st: string = "asdfasdf";
            func(1);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
    
    def test_67(self):
        input = """main: function void() {a : array [1,2,4_5] of string;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))
    
    def test_68(self):
        input = """main: function void () {
        a = b = c;
}"""
        expect = "Error on line 2 col 14: ="
        self.assertTrue(TestParser.test(input, expect, 268))
    
    def test_69_c_supremacy2(self):
        input = """void calSum(string fileName)   {
            // TODO
            ifstream infile;
            infile.open(fileName);
            int res = 0;
            int s = 51531;
            while (infile >> s){
                
                cout << s << " ";
                res += s;
            }
            cout << endl << res;
        }

        int main(){
            string filename = "lmao.txt";
            calSum(filename);

            int a[10];
            cout << endl << sizeof(a)/sizeof(int);


            return 0;
        }"""
        expect = "Error on line 1 col 0: void"
        self.assertTrue(TestParser.test(input, expect, 269))
    
    def test_70(self):
        input = """main: function void() {
        if (x) for (x = 1, x < 2, x+1) x = x+1;        
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_71_c_supremacy(self):
        input = """main: function void(){
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
    
    def test_72(self):
        input = """int main(){
            gen(1);
            cout << res;
            return 0;
        }"""
        expect = "Error on line 1 col 4: main"
        self.assertTrue(TestParser.test(input, expect, 272))
    
    def test_73(self):
        input = """bool isSymmetric(int arr[][1000], int row, int col) {
            for (int i = 0; i < row; ++i){
                for (int j = 0; j < col; ++j){
                    if (arr[i][j] != arr[j][i]) return false;
                }
            }
            return true;
        }"""
        expect = "Error on line 1 col 5: isSymmetric"
        self.assertTrue(TestParser.test(input, expect, 273))
    
    def test_74(self):
        input = """main: function void(){
            arr: array[3,2] of integer;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_75(self):
        input = """main: function void(){
            arr: array[3][2] of integer;
        }"""
        expect = "Error on line 2 col 25: ["
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_76(self):
        input = """main: function void(){
            arr: array[0..3][0..2] of integer;
        }"""
        expect = "Error on line 2 col 23: 0."
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_77(self):
        input = """main: function void(){
            arr: array[10] of array[10] of integer;
        }"""
        expect = "Error on line 2 col 30: array"
        self.assertTrue(TestParser.test(input, expect, 277))
        
    def test_78(self):
        input = """main: function void(){
            arr: array[10] of array[10] of array[1] of integer;
        }"""
        expect = "Error on line 2 col 30: array"
        self.assertTrue(TestParser.test(input, expect, 278))
        
    def test_79(self):
        input = """main: function void(){
            arr: array[10] by float;
        }"""
        expect = "Error on line 2 col 27: by"
        self.assertTrue(TestParser.test(input, expect, 279))
        
    def test_80(self):
        input = """main: function void(){
            arr: array[10] of string;
            a[9] = a[9] + \"10\";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
        
    def test_81(self):
        input = """main: function void(){
            arr: array[10] of string;
            a[9][5];
        }"""
        expect = "Error on line 3 col 16: ["
        self.assertTrue(TestParser.test(input, expect, 281))
        
    def test_82(self):
        input = """main: function void(){
            arr: array[10] of string;
            a[9,5] = 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
        
    def test_83(self):
        input = """main: function void(){
            arr: array[10__1] of string;
            a[9,5] = 1;
        }"""
        expect = "Error on line 2 col 25: __1"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_84(self):
        input = """main: function void(){
            arr: array[10,1,1,1,1,1,1] of string;
            arr[9,0,0,0,0,0,0,0] = 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_85(self):
        input = """main: function void(){
            arr: array[10,1,1,1,1,1,1.1] of string;
            array[9,1,1,1,1,1,1] = 1;"""
        expect = "Error on line 2 col 36: 1.1"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_86(self):
        input = """main: function void(){
            arr: array[10] of bool;
            a[0] = true;
            a[1] = false;
            a[2] = a[0] + a[1];
        }"""
        expect = "Error on line 2 col 30: bool"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_87(self):
        input = """main: function void(){
            arr: array[10,1,1,1,1,1,11] of string = {1,2,3,a,\"b\",true, false, 1.1, 1e2};
            arr[9,1,1,1,1,1,1] = 1;
            }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_88(self):
        input = """main: function void(){
            a: integer = 0;
            b: integer = 1;
            a / 5 = b;
        }"""
        expect = "Error on line 4 col 14: /"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_89(self):
        input = """main: function void(){
            a: integer = 0;
            b: integer = 1;
            a - 6 = 5 = b;
        }"""
        expect = "Error on line 4 col 14: -"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_90(self):
        input = """main: function void(){
            a: integer = 0;
            b: integer = 1;
            a = a - 6 == 5 - b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_91(self):
        input = """main: function void(){
            arr: array[10] of bool;
            a[0] = true;
            a[1] = false;
            a[2] = a[0] + a[1];
        }"""
        expect = "Error on line 2 col 30: bool"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_92(self):
        input = """main: function void(){
            printInt(1/0);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_93(self):
        input = """main: function void(){
            a: integer = 0;
            b: integer = 1;
            a = 6 == (5 <= b) + 1/2 * log(2);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_94(self):
        input = """main: function void(){
            a: integer = 5;
            b: integer = 0;
            c: integer;
            c = a / b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_95(self):
        input = """main: function void(){
            a: string = \"5 = 4\";
            b: string = 0;
            c: integer;
            c = a / b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_96(self):
        input = """main: function void(){
            a: string = \"5 = 4\";
            a: boolean = \"L\";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_97(self):
        input = """a = 1/2;"""
        expect = "Error on line 1 col 2: ="
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_98(self):
        input = """main: function void(){
            b: string = \"5 = 4\" = 
            x: boolean = true;
        }"""
        expect = "Error on line 2 col 32: ="
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_99(self):
        input = """main: function void() {return manip();}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_final(self):
        input = """main: function void() {printString(\"10d cho BTL so 1\");}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))   
