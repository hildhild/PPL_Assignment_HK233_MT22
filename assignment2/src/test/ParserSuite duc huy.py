import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """a : array [1] of integer = {a[0], true, 1, 1., .e3};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_2(self):
        input = """a : array [1] of array [1] integer = {a[0], true, 1, 1., .e3};"""
        expect = "Error on line 1 col 17: array"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_3(self):
        input = """a : void = {};"""
        expect = "Error on line 1 col 4: void"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_4(self):
        input = """a : array [1] of void = {a[0], true, 1, 1., .e3};"""
        expect = "Error on line 1 col 17: void"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_5(self):
        input = """a : integer = {};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_6(self):
        input = """a,b,c : integer = a, foo(), 15, "hehe";"""
        expect = "Error on line 1 col 30: ,"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_7(self):
        input = """a : integer = {{1},foo({1})};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_8(self):
        input = """a : function void (inherit a : void, out b : array [1] of integer) inherit c {return 1;}"""
        expect = "Error on line 1 col 31: void"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_9(self):
        input = """a : function void (inherit a : integer, out b : array [1] of void) inherit c {return 1;}"""
        expect = "Error on line 1 col 61: void"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_10(self):
        input = """a : function void (inherit a : integer, out b : array [1] of string) inherit c {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_11(self):
        input = """a : function void (inherit a : integer, out b : array [1] of string) inherit c {
                    {
                    }
                    if (a > 2);
                }"""
        expect = "Error on line 4 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_12(self):
        input = """a : function void (inherit a : integer, out b : array [1] of string) inherit c {
                  i : integer = a[5,(a[10]::{1,2,foo()})+b(0)];
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_13(self):
        input = """a : function void (inherit a : integer, out b : array [1] of string) inherit c {
                  i : integer = a == (b >= c);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_14(self):
        input = """a : function void (inherit a : integer, out b : array [1] of string) inherit c {
                   a = ((a[10]::{1,2,foo()})+b(0)) ;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_15(self):
        input = """a : function array [1] of string () inherit c {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_16(self):
        input = """a : function array [1] of string () inherit c { foo() = 1; }"""
        expect = "Error on line 1 col 54: ="
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_17(self):
        input = """a : function array [1] of string () inherit c { do {return 1;} while ({} == 1);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_18(self):
        input = """a : function array [1] of string () inherit c { do {return foo()+{};} while ({} == 1);}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_19(self):
        input = """a : function array [1] of string () inherit c { readInteger(a); }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_20(self):
        input = """a = 5;"""
        expect = "Error on line 1 col 2: ="
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_21(self):
        input = """a : function void () { ; } """
        expect = "Error on line 1 col 23: ;"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_22(self):
        input = """a : array [1] of integer = a[1][2];"""
        expect = "Error on line 1 col 31: ["
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_23(self):
        input = """a : array [1] of integer = a[2];"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_24(self):
        input = """a, b: array [5,5,6] of integer = {a,b,b}, a[1::2];"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_25(self):
        input = """a : function void (){
    a[1][2] = a[1][2];
}"""
        expect = "Error on line 2 col 8: ["
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_26(self):
        input = """a : function void (){
    a[1] = a[1][2];
}"""
        expect = "Error on line 2 col 15: ["
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_27(self):
        input = """a : function void (){
    a[1] = a[2];
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_28(self):
        input = """a : function void (){
    a[1] = a[3];
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_29(self):
        input = """a : function void (){
    (a[1])[3] = (a[2])[3];
}"""
        expect = "Error on line 2 col 4: ("
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_30(self):
        input = """a : function void (){
    if (a==(b >= c)) {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_31(self):
        input = """a : function void (){
    if (a==(b >= c)) {} else return {};
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_32(self):
        input = """a : function void (){
    if (a==(b >= c)) {;} else return {};
}"""
        expect = "Error on line 2 col 22: ;"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_33(self):
        input = """a : function void (){
    for (a[1] = foo(), i >= 2, i -foo()) {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_34(self):
        input = """a : function void (){
    for (a[1] = 1, i >= 2, i -foo()) {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_35(self):
        input = """a: function integer (inherit out i: integer, i: string) inherit a {
            a[1,a[2]] = {a,a} + a[1,2,{a,a[1]}][2];
        }"""
        expect = "Error on line 2 col 47: ["
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_36(self):
        input = """a : function void (){
    for (a[1] = 1, (i :: 2) :: 3 , i -foo()) {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_37(self):
        input = """a : function void (){
    while (i*1) {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_38(self):
        input = """a : function void (){
    do {return 1;} while (a);
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_39(self):
        input = """a : function void (){
    do {return 1; break;} while (a);
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_40(self):
        input = """a : function void (){
    foo(2+x);
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_42(self):
        input = """a : function void (){
    readInteger();
   {
   }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_43(self):
        input = """a : function void (){
    readInteger(a,b);
   {
   }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_44(self):
        input = """a : function void (){
    printInteger(a);
   {
   }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_45(self):
        input = """a : function void (){
    printInteger();
   {
   }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_46(self):
        input = """a : function void (){
    printBoolean();
   {
   }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_47(self):
        input = """a : function void (){
    super();
   {
   }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_48(self):
        input = """a : function void (){
    super({});
   {
   }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_49(self):
        input = """a : function void (){
    a : function void (){}
   {
   }
}"""
        expect = "Error on line 2 col 8: function"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_50(self):
        input = """a : function void (){
    call(c) + call(d) = 1;
}"""
        expect = "Error on line 2 col 12: +"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_51(self):
        input = """foo(a) = {}"""
        expect = "Error on line 1 col 3: ("
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_52(self):
        input = """{}"""
        expect = "Error on line 1 col 0: {"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_53(self):
        input = """if (a>3) return 1;"""
        expect = "Error on line 1 col 0: if"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_54(self):
        input = """while (a==3) {}"""
        expect = "Error on line 1 col 0: while"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_55(self):
        input = """super(a)"""
        expect = "Error on line 1 col 5: ("
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_56(self):
        input = """a, b,c : integer;
 foo : function float (a : integer, out c : string) {
   e : integer ;
   e = a + 4 ;
   c = a * d / 2.0 ;
   return c + 1;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_57(self):
        input = """a: function array [1] of string (a: string) inherit c {
                print();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_58(self):
        input = """a: function array [1] of string (a: string) inherit c {
    b : auto;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_59(self):
        input = """a, b: array [5,6] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_60(self):
        input = """a: function array [1] of string (a: string) inherit c {
    {//}
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_61(self):
        input = """a: function void (a: array [1] of integer) inherit c {
    {//}
        foo(1);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_62(self):
        input = """a: function void (a: array [1] of integer) inherit c {
    {//}
        a[1] = foo(1);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_63(self):
        input = """a : boolean = "helo";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_64(self):
        input = """a,b,c : array [1,4,3] of boolean = "helo",1,2;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_65(self):
        input = """a,b,c : array [1,4,3] of boolean = "helo",true,false;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_66(self):
        input = """a : function void (){
a,b,c : array [1,4,3] of boolean = "helo",true,false;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_67(self):
        input = """a : function void (){
    a[1_2_3] = b;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_68(self):
        input = """a : function void (){
    a[1_2_3.8,87] = b;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_69(self):
        input = """main: function void () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_70(self):
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_71(self):
        input = """a:function string (){a = a;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_72(self):
        input = """x : auto = 1.0 """
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_73(self):
        input = """a: function auto (a : boolean) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_74(self):
        input = """a: boolean;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_75(self):
        input = """        fact: function integer ( fact : integer) {

            if (a=2) a=2; else
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) do {for (a=2,a>3,a+1) return 1;} while(a==2);
           {} continue; return _12; {break;}
        }
        a : integer = 1_3_1.;
"""
        expect = "Error on line 3 col 17: ="
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_76(self):
        input = """        fact: function integer ( a : integer) {
            break;
            if (a==2) a=2; else
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) do {for (a=2,a>3,a+1) return 1;} while(a==2);
           {} continue; return _12; {break;}
        }
        a : integer = 1_3_1.;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_77(self):
        input = """        fact: function integer ( a : integer) {
            break;
            if (a==2)
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) do {for (a=2,a>3,a+1) return 1; }while(a==2);
           {} continue; return _12; {break;}
        }
        a : integer = 1_3_1.;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_78(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) do {for (a=2,a>3,a+1) return 1;} while(a==2);
           {} continue; return ; {break;}
        }
        a : integer = 1_3_1.;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_79(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) do {for (a=2,a>3,a+1) return 1;} while(a==2);

        }
        a : integer = 1_3_1.;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_80(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) do {for (a=2,a>3,a+1) return 1;} while(a=2);

        }
        a : integer = 1_3_1.;
"""
        expect = "Error on line 3 col 88: ="
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_81(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) return 1_5.;

        }
        a : integer = 1_3_1.;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_82(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) return 1_5.;

        }
        a : integer = 1_3_1., 12;
"""
        expect = "Error on line 6 col 28: ,"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_83(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) return 1_5.;
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_84(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) return 1_5;
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_85(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1) return 1;
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_86(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=2 ,foo({}) ,{}+1) return 1;
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_87(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for ( , ,) return 1;
        }
"""
        expect = "Error on line 3 col 18: ,"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_88(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for ( a=1,2>1 ,{1}+1) return 1;
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_89(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for ( ; ; ;) return 1;
        }
"""
        expect = "Error on line 3 col 18: ;"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_90(self):
        input = """a: function integer (b: string) inherit a {
            a[1,a[0]] = 2;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_91(self):
        input = """        fact: function integer (inherit out a : integer) {
            a[1] = {a(0),a[0], {}};
            {a(0);/*} {*/}
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_92(self):
        input = """        fact: function integer (inherit out a : integer) {
            a[1] = {a(0),a[0], {}};
            {a(0);} return 1;
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_93(self):
        input = """        fact: function integer (inherit out a : integer) {
            a[1] = {a(0),a[0], {}};
            {a(0),a[0], {}} = 1;
        }
"""
        expect = "Error on line 3 col 17: ,"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_94(self):
        input = """        fact: function integer (inherit out a : integer) {
            a[1] = {a(0),a[0], {}};
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_95(self):
        input = """        fact: function integer () {
            a[1] = {a(0),a[0], {}};
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_96(self):
        input = """        fact: function integer (n: auto)"""
        expect = "Error on line 1 col 40: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_97(self):
        input = """        fact: function integer (n: auto) a=c;"""
        expect = "Error on line 1 col 41: a"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_98(self):
        input = """        fact: function integer (n: auto) return 1;"""
        expect = "Error on line 1 col 41: return"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_99(self):
        input = """        fact: function integer (n: auto) {
            if (n == 0) return ;
            else return ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_100(self):
        input = """        fact: function integer (n: void) {
            if (n == 0) return 1;
            else return ;
        }"""
        expect = "Error on line 1 col 35: void"
        self.assertTrue(TestParser.test(input, expect, 300))
