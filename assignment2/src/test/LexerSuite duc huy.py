import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_l1(self):
        self.assertTrue(TestLexer.test("\"abc \\n \\f 's def", "Unclosed String: abc \\n \\f 's def", 101))

    def test_l2(self):
        self.assertTrue(TestLexer.test("\"abc \'", "Unclosed String: abc \'", 102))

    def test_l3(self):
        self.assertTrue(TestLexer.test("\"unclosed \\n string", "Unclosed String: unclosed \\n string", 103))

    def test_l4(self):
        self.assertTrue(TestLexer.test("aCb234", "aCb234,<EOF>", 104))

    def test_l5(self):
        self.assertTrue(TestLexer.test("array[5]", "array,[,5,],<EOF>", 105))

    def test_l6(self):
        self.assertTrue(TestLexer.test("a+b-c*d/e", "a,+,b,-,c,*,d,/,e,<EOF>", 106))

    def test_l7(self):
        self.assertTrue(TestLexer.test("\"abc \q'", "Illegal Escape In String: abc \q", 107))

    def test_l8(self):
        self.assertTrue(TestLexer.test("? = a", "Error Token ?", 108))

    def test_l9(self):
        self.assertTrue(TestLexer.test("a >= b", "a,>=,b,<EOF>", 109))

    def test_l10(self):
        self.assertTrue(TestLexer.test("a&&b||c", "a,&&,b,||,c,<EOF>", 110))

    def test_l11(self):
        self.assertTrue(TestLexer.test("if(a>b) a=2;", "if,(,a,>,b,),a,=,2,;,<EOF>", 111))

    def test_l12(self):
        self.assertTrue(TestLexer.test("a+2==b*3", "a,+,2,==,b,*,3,<EOF>", 112))

    def test_l13(self):
        self.assertTrue(TestLexer.test("\"abc\"", "abc,<EOF>", 113))

    def test_l14(self):
        self.assertTrue(TestLexer.test("inta", "inta,<EOF>", 114))

    def test_l15(self):
        self.assertTrue(TestLexer.test("if 5 > 3 then a = b + 1;", "if,5,>,3,then,a,=,b,+,1,;,<EOF>", 115))

    def test_l16(self):
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 116))

    def test_l17(self):
        self.assertTrue(TestLexer.test("false", "false,<EOF>", 117))

    def test_l18(self):
        self.assertTrue(TestLexer.test("do a = a + 1; while (a < 10)", "do,a,=,a,+,1,;,while,(,a,<,10,),<EOF>", 118))

    def test_l19(self):
        self.assertTrue(TestLexer.test("/*This is a comment*/", "<EOF>", 119))

    def test_l20(self):
        self.assertTrue(TestLexer.test("//This is a comment", "<EOF>", 120))

    def test_l21(self):
        self.assertTrue(TestLexer.test("0x123", "0,x123,<EOF>", 121))

    def test_l22(self):
        self.assertTrue(TestLexer.test("1.2e-3", "1.2e-3,<EOF>", 122))

    def test_l23(self):
        self.assertTrue(TestLexer.test("1.2e-3.4", "1.2e-3,.,4,<EOF>", 123))

    def test_l24(self):
        self.assertTrue(TestLexer.test("123_456", "123456,<EOF>", 124))

    def test_l25(self):
        self.assertTrue(TestLexer.test("1_2.3_4e-5_6", "12.3,_4e,-,56,<EOF>", 125))

    def test_l26(self):
        self.assertTrue(TestLexer.test("false abc true", "false,abc,true,<EOF>", 126))

    def test_l27(self):
        self.assertTrue(TestLexer.test('{"a", "b", "c"}', "{,a,,,b,,,c,},<EOF>", 127))

    def test_l28(self):
        self.assertTrue(TestLexer.test("[", "[,<EOF>", 128))

    def test_l29(self):
        self.assertTrue(TestLexer.test("]", "],<EOF>", 129))

    def test_l30(self):
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", 130))

    def test_l31(self):
        self.assertTrue(TestLexer.test("if else for while", "if,else,for,while,<EOF>", 131))

    def test_l32(self):
        self.assertTrue(TestLexer.test("!=", "!=,<EOF>", 132))

    def test_l33(self):
        self.assertTrue(TestLexer.test("a_1 b_2 c_3 d_4 e_5 f_6 g_7 h_8 i_9 j_10",
                                       "a_1,b_2,c_3,d_4,e_5,f_6,g_7,h_8,i_9,j_10,<EOF>",
                                       133))

    def test_l34(self):
        self.assertTrue(TestLexer.test("array[]", "array,[,],<EOF>", 134))

    def test_l35(self):
        self.assertTrue(TestLexer.test("{1, 2, 3, 4}", "{,1,,,2,,,3,,,4,},<EOF>", 135))

    def test_l36(self):
        self.assertTrue(TestLexer.test("abc // this is a comment", "abc,<EOF>", 136))

    def test_l37(self):
        self.assertTrue(TestLexer.test("/* this is a comment */ abc", "abc,<EOF>", 137))

    def test_l38(self):
        self.assertTrue(TestLexer.test("continue; break;", "continue,;,break,;,<EOF>", 138))

    def test_l39(self):
        self.assertTrue(TestLexer.test("0o10", "0,o10,<EOF>", 139))

    def test_l40(self):
        self.assertTrue(TestLexer.test("0o18", "0,o18,<EOF>", 140))

    def test_l41(self):
        self.assertTrue(TestLexer.test("0x19", "0,x19,<EOF>", 141))

    def test_l42(self):
        self.assertTrue(TestLexer.test("0x1g", "0,x1g,<EOF>", 142))

    def test_l43(self):
        self.assertTrue(TestLexer.test("0x", "0,x,<EOF>", 143))

    def test_l44(self):
        self.assertTrue(TestLexer.test("0o", "0,o,<EOF>", 144))

    def test_l45(self):
        self.assertTrue(TestLexer.test("0.", "0.,<EOF>", 145))

    def test_l46(self):
        self.assertTrue(TestLexer.test(".0", ".,0,<EOF>", 146))

    def test_l47(self):
        self.assertTrue(TestLexer.test("1e5", "1e5,<EOF>", 147))

    def test_l48(self):
        self.assertTrue(TestLexer.test("1e", "1,e,<EOF>", 148))

    def test_l49(self):
        self.assertTrue(TestLexer.test("1.e5", "1.e5,<EOF>", 149))

    def test_l50(self):
        self.assertTrue(TestLexer.test(".1e5", ".1e5,<EOF>", 150))

    def test_l51(self):
        self.assertTrue(TestLexer.test("a += 5;", "a,+,=,5,;,<EOF>", 151))

    def test_l52(self):
        self.assertTrue(TestLexer.test("a -= 5;", "a,-,=,5,;,<EOF>", 152))

    def test_l53(self):
        self.assertTrue(TestLexer.test("a *= 5;", "a,*,=,5,;,<EOF>", 153))

    def test_l54(self):
        self.assertTrue(TestLexer.test("a /= 5;", "a,/,=,5,;,<EOF>", 154))

    def test_l55(self):
        self.assertTrue(TestLexer.test("a %= 5;", "a,%,=,5,;,<EOF>", 155))

    def test_l56(self):
        self.assertTrue(TestLexer.test("a == 5;", "a,==,5,;,<EOF>", 156))

    def test_l57(self):
        self.assertTrue(TestLexer.test("a != 5;", "a,!=,5,;,<EOF>", 157))

    def test_l58(self):
        self.assertTrue(TestLexer.test("a > 5;", "a,>,5,;,<EOF>", 158))

    def test_l59(self):
        self.assertTrue(TestLexer.test("a >= 5;", "a,>=,5,;,<EOF>", 159))

    def test_l60(self):
        self.assertTrue(TestLexer.test("a < 5;", "a,<,5,;,<EOF>", 160))

    def test_l61(self):
        self.assertTrue(TestLexer.test("a <= 5;", "a,<=,5,;,<EOF>", 161))

    def test_l62(self):
        self.assertTrue(TestLexer.test("a[12]", "a,[,12,],<EOF>", 162))

    def test_l63(self):
        self.assertTrue(TestLexer.test("a[3+4]", "a,[,3,+,4,],<EOF>", 163))

    def test_l64(self):
        self.assertTrue(TestLexer.test("a[3*4-1]", "a,[,3,*,4,-,1,],<EOF>", 164))

    def test_l65(self):
        self.assertTrue(TestLexer.test("a[b[2]]", "a,[,b,[,2,],],<EOF>", 165))

    def test_l66(self):
        self.assertTrue(TestLexer.test("a+b*c/d-e%g", "a,+,b,*,c,/,d,-,e,%,g,<EOF>", 166))

    def test_l67(self):
        self.assertTrue(TestLexer.test("a=b=c=5", "a,=,b,=,c,=,5,<EOF>", 167))

    def test_l68(self):
        self.assertTrue(TestLexer.test("a+=5", "a,+,=,5,<EOF>", 168))

    def test_l69(self):
        self.assertTrue(TestLexer.test("a==b", "a,==,b,<EOF>", 169))

    def test_l70(self):
        self.assertTrue(TestLexer.test("a!=b", "a,!=,b,<EOF>", 170))

    def test_l71(self):
        self.assertTrue(TestLexer.test("a>b", "a,>,b,<EOF>", 171))

    def test_l72(self):
        self.assertTrue(TestLexer.test("a>=b", "a,>=,b,<EOF>", 172))

    def test_l73(self):
        self.assertTrue(TestLexer.test("a<b", "a,<,b,<EOF>", 173))

    def test_l74(self):
        self.assertTrue(TestLexer.test("a<=b", "a,<=,b,<EOF>", 174))

    def test_l75(self):
        self.assertTrue(TestLexer.test("a&&b||c", "a,&&,b,||,c,<EOF>", 175))

    def test_l76(self):
        self.assertTrue(TestLexer.test("a&&!b||c", "a,&&,!,b,||,c,<EOF>", 176))

    def test_l77(self):
        self.assertTrue(
            TestLexer.test("if (a<b) { c=d; } else { c=e; }", "if,(,a,<,b,),{,c,=,d,;,},else,{,c,=,e,;,},<EOF>", 177))

    def test_l78(self):
        self.assertTrue(
            TestLexer.test("if (a<b) { if (b<c) { c=d; } }", "if,(,a,<,b,),{,if,(,b,<,c,),{,c,=,d,;,},},<EOF>", 178))

    def test_l79(self):
        self.assertTrue(TestLexer.test("while (a<b) { a=a+1; }", "while,(,a,<,b,),{,a,=,a,+,1,;,},<EOF>", 179))

    def test_l80(self):
        self.assertTrue(TestLexer.test("var a, b, c: integer;", "var,a,,,b,,,c,:,integer,;,<EOF>", 180))

    def test_l81(self):
        self.assertTrue(TestLexer.test("if a == 5 then b = 6;", "if,a,==,5,then,b,=,6,;,<EOF>", 181))

    def test_l82(self):
        self.assertTrue(TestLexer.test("a && b;", "a,&&,b,;,<EOF>", 182))

    def test_l83(self):
        self.assertTrue(TestLexer.test("for i := 0 to n do = sum + i;", "for,i,:,=,0,to,n,do,=,sum,+,i,;,<EOF>", 183))

    def test_l84(self):
        self.assertTrue(TestLexer.test("a := (5 + 3) * 2 - 1;", "a,:,=,(,5,+,3,),*,2,-,1,;,<EOF>", 184))

    def test_l85(self):
        self.assertTrue(TestLexer.test("/* hehe */ hello", "hello,<EOF>", 185))

    def test_l86(self):
        self.assertTrue(TestLexer.test("/* lay het */ lay het */", "lay,het,*,/,<EOF>", 186))

    def test_l87(self):
        self.assertTrue(TestLexer.test("ac //chu", "ac,<EOF>", 187))

    def test_l88(self):
        self.assertTrue(TestLexer.test("// /* */ */", "<EOF>", 188))

    def test_l89(self):
        self.assertTrue(TestLexer.test("/* // */", "<EOF>", 189))

    def test_l90(self):
        self.assertTrue(TestLexer.test("/*//*/ */ ", "*,/,<EOF>", 190))

    def test_l91(self):
        self.assertTrue(TestLexer.test("//hello hehe", "<EOF>", 191))

    def test_l92(self):
        self.assertTrue(TestLexer.test("if (a == 5) b = 3;", "if,(,a,==,5,),b,=,3,;,<EOF>", 192))

    def test_l93(self):
        self.assertTrue(TestLexer.test("a = b && c || d;", "a,=,b,&&,c,||,d,;,<EOF>", 193))

    def test_l94(self):
        self.assertTrue(TestLexer.test("out(print(5));", "out,(,print,(,5,),),;,<EOF>", 194))

    def test_l95(self):
        self.assertTrue(TestLexer.test("\"This is a string.\"", "This is a string.,<EOF>", 195))

    def test_l96(self):
        self.assertTrue(TestLexer.test("""//haha
haha""",
                                       "haha,<EOF>", 196))

    def test_l97(self):
        self.assertTrue(TestLexer.test("a[5] = 3;", "a,[,5,],=,3,;,<EOF>", 197))

    def test_l98(self):
        self.assertTrue(TestLexer.test("int arr[10];", "int,arr,[,10,],;,<EOF>", 198))

    def test_l99(self):
        self.assertTrue(
            TestLexer.test("function foo(): void { return; }", "function,foo,(,),:,void,{,return,;,},<EOF>", 199))

    def test_l100(self):
        self.assertTrue(
            TestLexer.test("do { i = i + 1; } while (i < 10);", "do,{,i,=,i,+,1,;,},while,(,i,<,10,),;,<EOF>", 200))
