import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_integer_number_1(self):
        """1. Test integer numbers"""
        self.assertTrue(TestLexer.test("123", "123,<EOF>", 101))
        
    def test_integer_number_2(self):
        self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 102))    
        
    def test_float_number_1(self):
        """2. Test floating number"""
        self.assertTrue(TestLexer.test(".234e1", ".234e1,<EOF>", 103))
        
    def test_float_number_2(self):
        self.assertTrue(TestLexer.test("1.2e3", "1.2e3,<EOF>", 104))
        
    def test_float_number_3(self):
        self.assertTrue(TestLexer.test("7E-10", "7E-10,<EOF>", 105))
        
    def test_float_number_4(self):
        self.assertTrue(TestLexer.test("1_234.567", "1234.567,<EOF>", 106))
        
    def test_float_number_5(self):
        self.assertTrue(TestLexer.test("55.", "55.,<EOF>", 107))
    
    def test_string_literal_1(self):
        test_case = "\"This is an illegal escape \n\""
        solution ="Unclosed String: This is an illegal escape "
        self.assertTrue(TestLexer.test(test_case, solution, 108))
        
    def test_string_literal_2(self):
        test_case = """ "He asked me: \\"Where is John?\\"" """
        solution = """He asked me: \\"Where is John?\\",<EOF>"""
        self.assertTrue(TestLexer.test(test_case, solution, 109))
    
    def test_comment_inline(self):
        """4. Test comment inline"""
        test_case = """//Helo""";
        solution = """<EOF>""";
        self.assertTrue(TestLexer.test(test_case,solution,110))
        
    def test_comment_multiline(self):
        """4. Test comment multiline"""
        test_case = """/* Day
        la dai tieng noi 
        Viet Nam
        */""";
        solution = """<EOF>""";
        self.assertTrue(TestLexer.test(test_case,solution,111))
    
    def test_12(self):
        input = """true"""
        expect = """true,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 112))
        
    def test_13(self):
        input = """\"Hello\"::\"World!\""""
        expect = """Hello,::,World!,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 113))
        
    def test_14(self):
        self.assertTrue(TestLexer.test("\"\\o\"","Illegal Escape In String: \\o", 114))
        
    def test_15(self):
        self.assertTrue(TestLexer.test("What @","What,Error Token @",115))
        
    def test_16(self):
        input = """/*aowoavevqvq*/"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 116))
        
    def test_17(self):
        input = """x: string = \"\\y\" """
        expect = "x,:,string,=,Illegal Escape In String: \y"
        self.assertTrue(TestLexer.test(input, expect, 117))

    def test_18(self):
        input = """123__45"""
        expect = "123,__45,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 118))
    
    def test_19(self):
        input = """156416_ada_1231"""
        expect = "156416,_ada_1231,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 119))
    
    def test_20(self):
        input = """156416__ada 1231"""
        expect = "156416,__ada,1231,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 120))
    
    def test_21(self):
        input = """156416ada1231"""
        expect = "156416,ada1231,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 121))
    
    def test_22(self):
        input = """asd454541505"""
        expect = "asd454541505,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 122))
    
    def test_23(self):
        input = """21312\n\n\n 43_ac"""
        expect = "21312,43,_ac,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 123))
    
    def test_24(self):
        input = """supermario,<,>,64,<EOF>"""
        expect = "supermario,,,<,,,>,,,64,,,<,EOF,>,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 124))
    
    def test_25(self):
        input = """boolean"""
        expect = "boolean,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 125))

    def test_26(self):
        input = """integer"""
        expect = "integer,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 126))
    
    def test_27(self):
        input = """integer int int16 int 32 int64"""
        expect = "integer,int,int16,int,32,int64,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 127))
    
    def test_28(self):
        input = """\94"""
        expect = "Error Token \\"
        self.assertTrue(TestLexer.test(input, expect, 128))
    
    def test_29(self):
        input = """\u0047"""
        expect = "G,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 129))
    
    def test_30(self):
        input = """\x2167"""
        expect = "!,67,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 130))
    
    def test_31(self):
        input = """main(){return omg;}"""
        expect = "main,(,),{,return,omg,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 131))
    
    def test_32(self):
        input = """main: function void(){return bassSLAP;}"""
        expect = "main,:,function,void,(,),{,return,bassSLAP,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 132))
    
    def test_33(self):
        input = """arr: array[1007] of integer;"""
        expect = "arr,:,array,[,1007,],of,integer,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 133))
    
    def test_34(self):
        input = """array : arr[123_1231__2] of azhada"""
        expect = "array,:,arr,[,1231231,__2,],of,azhada,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 134))
    
    def test_35(self):
        input = """1m 0n de4dl1n3"""
        expect = "1,m,0,n,de4dl1n3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 135))
    
    def test_36(self):
        input = """c++ -= 1 * 6 789"""
        expect = "c,+,+,-,=,1,*,6,789,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 136))
    
    def test_37(self):
        input = """c++ -=(/123-12) + 4"""
        expect = "c,+,+,-,=,(,/,123,-,12,),+,4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 137))
    
    def test_38(self):
        input = """adava kedava"""
        expect = "adava,kedava,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 138))
    
    def test_39(self):
        input = """1-21312"""
        expect = "1,-,21312,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 139))
    
    def test_40(self):
        input = """python --version"""
        expect = "python,-,-,version,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 140))
    
    def test_41(self):
        input = """g++ -g -o main main.cpp lmao.cpp -I . -std=c++11"""
        expect = "g,+,+,-,g,-,o,main,main,.,cpp,lmao,.,cpp,-,I,.,-,std,=,c,+,+,11,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 141))
    
    def test_42(self):
        input = """./main input"""
        expect = ".,/,main,input,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 142))
    
    def test_43(self):
        input = """$(filename).cpp"""
        expect = "Error Token $"
        self.assertTrue(TestLexer.test(input, expect, 143))
    
    def test_44(self):
        input = """int** p = new int*;"""
        expect = "int,*,*,p,=,new,int,*,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 144))
    
    def test_45(self):
        input = """bool a, b; if (a + b)"""
        expect = "bool,a,,,b,;,if,(,a,+,b,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 145))
    
    def test_46(self):
        input = """a:array[1] of integer;"""
        expect = "a,:,array,[,1,],of,integer,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 146))
    
    def test_47(self):
        input = """a:array[1_1,2] of integer;"""
        expect = "a,:,array,[,11,,,2,],of,integer,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 147))
    
    def test_48(self):
        input = """a:array[1] of integer = {1,2};"""
        expect = "a,:,array,[,1,],of,integer,=,{,1,,,2,},;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 148))
    
    def test_49(self):
        input = """func: integer[100] of array function void(int)"""
        expect = "func,:,integer,[,100,],of,array,function,void,(,int,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 149))
    
    def test_50(self):
        input = """main: function void() {}"""
        expect = "main,:,function,void,(,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))
    
    def test_51(self):
        input = """|[123123]|"""
        expect = "Error Token |"
        self.assertTrue(TestLexer.test(input, expect, 151))
    
    def test_52(self):
        input = """\\e"""
        expect = "Error Token \\"
        self.assertTrue(TestLexer.test(input, expect, 152))
    
    def test_53(self):
        input = """UwU"""
        expect = "UwU,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 153))
    
    def test_54(self):
        input = """\n"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 154))
    
    def test_55(self):
        input = """\t"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 155))
    
    def test_56(self):
        input = """b: string = \"5 = 4\" ="""
        expect = "b,:,string,=,5 = 4,=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 156))
    
    def test_57(self):
        input = """b:string=5 = 4\" ="""
        expect = "b,:,string,=,5,=,4,Unclosed String:  ="
        self.assertTrue(TestLexer.test(input, expect, 157))
    
    def test_58(self):
        input = """self.assertTrue(TestLexer.test(input, expect, 158))"""
        expect = "self,.,assertTrue,(,TestLexer,.,test,(,input,,,expect,,,158,),),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 158))
    
    def test_59(self):
        input = """def test_59(self):"""
        expect = "def,test_59,(,self,),:,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 159))
    
    def test_60(self):
        input = """Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer"""
        expect = "Set,environment,variable,ANTLR_JAR,to,the,file,antlr,-,4.9,.,2,-,complete,.,jar,in,your,computer,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 160))
    
    def test_61(self):
        input = """functionDeclaration: functionPrototype functionBody;"""
        expect = "functionDeclaration,:,functionPrototype,functionBody,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))
    
    def test_62(self):
        input = """Section 1.10.32 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC"""
        expect = "Section,1.10,.,32,of,de Finibus Bonorum et Malorum,,,written,by,Cicero,in,45,BC,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 162))
    
    def test_63(self):
        input = """Donate Bitcoin: CNwhvgrarV\\6+-pMo 123A24C Djb4tyF"""
        expect = "Donate,Bitcoin,:,CNwhvgrarV,Error Token \\"
        self.assertTrue(TestLexer.test(input, expect, 163))
    
    def test_64(self):
        input = """Lorem 2ipsum adf213dolor sit amet,"""
        expect = "Lorem,2,ipsum,adf213dolor,sit,amet,,,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 164))
    
    def test_65(self):
        input = """:)"""
        expect = ":,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 165))
    
    def test_66(self):
        input = """in fin ity &#8734;"""
        expect = "in,fin,ity,Error Token &"
        self.assertTrue(TestLexer.test(input, expect, 166))
    
    def test_67(self):
        input = """kokomi gud noodle"""
        expect = "kokomi,gud,noodle,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 167))
    
    def test_68(self):
        input = """N1 C1 JUMP PLUNGE"""
        expect = "N1,C1,JUMP,PLUNGE,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 168))
    
    def test_69(self):
        input = """ILLEGAL_ESCAPE: '"' (ESC_SEQUENCE | ~[\r\n\\"])*? ('\\' ~[btfr"'\\])  {raise IllegalEscape(self.text[1:])};"""
        expect = "ILLEGAL_ESCAPE,:,Error Token '"
        self.assertTrue(TestLexer.test(input, expect, 169))
    
    def test_70(self):
        input = """fragment  DECIMALPART: '.' DIGIT*;"""
        expect = "fragment,DECIMALPART,:,Error Token '"
        self.assertTrue(TestLexer.test(input, expect, 170))
    
    def test_71(self):
        input = """/* A C-style comment */"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 171))
    
    def test_72(self):
        input = """Assign:         '='"""
        expect = "Assign,:,Error Token '"
        self.assertTrue(TestLexer.test(input, expect, 172))
    
    def test_73(self):
        input = """HCMC UNIVERSITY OF TECHNOLOGY - VNU-HCM
                FACULTY OF COMPUTER SCIENCE AND ENGINEERING"""
        expect = "HCMC,UNIVERSITY,OF,TECHNOLOGY,-,VNU,-,HCM,FACULTY,OF,COMPUTER,SCIENCE,AND,ENGINEERING,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 173))
    
    def test_74(self):
        input = "// Seperators"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 174))
    
    def test_75(self):
        input = """func(1+1)*2;"""
        expect = "func,(,1,+,1,),*,2,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 175))
    
    def test_76(self):
        input = """return n*fact(n-1);"""
        expect = "return,n,*,fact,(,n,-,1,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 176))
    
    def test_77(self):
        input = """map([1,2,3],lambda: [x] ->x);"""
        expect = "map,(,[,1,,,2,,,3,],,,lambda,:,[,x,],-,>,x,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 177))
    
    def test_78(self):
        input = """k*1 = 2*5"""
        expect = "k,*,1,=,2,*,5,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 178))
    
    def test_79(self):
        input = """2*4<1+3"""
        expect = "2,*,4,<,1,+,3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 179))
    
    def test_80(self):
        input = """EOF"""
        expect = "EOF,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 180))
    
    def test_81(self):
        input = """alahu akba"""
        expect = "alahu,akba,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 181))
    
    def test_82(self):
        input = """Tranh coffee"""
        expect = "Tranh,coffee,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 182))
    
    def test_83(self):
        input = """adfaCaf6 adfHafweUdf 853aT88 67adAf /*dfO"""
        expect = "adfaCaf6,adfHafweUdf,853,aT88,67,adAf,/,*,dfO,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 183))
    
    def test_84(self):
        input = """delete system32"""
        expect = "delete,system32,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 184))
    
    def test_85(self):
        input = """@lexer::header {
            from lexererr import *
        }"""
        expect = "Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 185))
    
    def test_86(self):
        input = """liek and subscraibe1523"""
        expect = "liek,and,subscraibe1523,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 186))
    
    def test_87(self):
        input = """1_234_567 (considered as 1234567 by scanner)"""
        expect = "1234567,(,considered,as,1234567,by,scanner,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 187))
    
    def test_88(self):
        input = """1.234 1.2e3 7E-10"""
        expect = "1.234,1.2e3,7E-10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 188))
    
    def test_89(self):
        input = """\b backspace"""
        expect = "backspace,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 189))
    
    def test_90(self):
        input = """LaTeX (/ltx/ LAH-tekh or /letx/ LAY-tekh"""
        expect = "LaTeX,(,/,ltx,/,LAH,-,tekh,or,/,letx,/,LAY,-,tekh,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 190))
    
    def test_91(self):
        input = """IHDR  9    DVo iCCPICC profile  x=H@_?"AdNDEEjVL.&"""
        expect = "IHDR,9,DVo,iCCPICC,profile,x,=,H,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 191))
    
    def test_92(self):
        input = """ \"hello"""
        expect = "Unclosed String: hello"
        self.assertTrue(TestLexer.test(input, expect, 192))
    
    def test_93(self):
        input = """<!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title></title>
        </head>
            
        </body>
        </html>"""
        expect = "<,!,DOCTYPE,html,>,<,html,>,<,head,>,<,meta,charset,=,utf-8,>,<,meta,name,=,viewport,content,=,width=device-width, initial-scale=1,>,<,title,>,<,/,title,>,<,/,head,>,<,/,body,>,<,/,html,>,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 193))
    
    def test_94(self):
        input = """\"\\"iomaip\""""
        expect = "\\\"iomaip,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 194))
    
    def test_95(self):
        input = """int n, a[maxN], b[maxN];"""
        expect = "int,n,,,a,[,maxN,],,,b,[,maxN,],;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 195))
    
    def test_96(self):
        input = """#include<ios > android>"""
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 196))
    
    def test_97(self):
        input = """struct point{
            int x, y;

            point(int x = 0, int y = 0){
                this->x = x;
                this->y = y;
            }

            double dist(point o){
                int xch = abs(o.x - x);
                int ych = abs(o.y - y);

                return sqrt(xch*xch + ych*ych);
            }
        };"""
        expect = "struct,point,{,int,x,,,y,;,point,(,int,x,=,0,,,int,y,=,0,),{,this,-,>,x,=,x,;,this,-,>,y,=,y,;,},double,dist,(,point,o,),{,int,xch,=,abs,(,o,.,x,-,x,),;,int,ych,=,abs,(,o,.,y,-,y,),;,return,sqrt,(,xch,*,xch,+,ych,*,ych,),;,},},;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 197))
    
    def test_98(self):
        input = """int ccw (point p1, point p2, point p3) {
            int t = p1.x*(p2.y - p3.y) + p2.x*(p3.y - p1.y) + p3.x*(p1.y - p2.y);
            if(!t) return 0;
            if(t < 0) return -1;
            return 1;
        }"""
        expect = "int,ccw,(,point,p1,,,point,p2,,,point,p3,),{,int,t,=,p1,.,x,*,(,p2,.,y,-,p3,.,y,),+,p2,.,x,*,(,p3,.,y,-,p1,.,y,),+,p3,.,x,*,(,p1,.,y,-,p2,.,y,),;,if,(,!,t,),return,0,;,if,(,t,<,0,),return,-,1,;,return,1,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 198))
    
    def test_99(self):
        input = """int n, m, k;
            ll w_mn;
            vector<pair<int, ii> > edge;
            vector<ii> mst;
            int p[maxN];
        """
        expect = "int,n,,,m,,,k,;,ll,w_mn,;,vector,<,pair,<,int,,,ii,>,>,edge,;,vector,<,ii,>,mst,;,int,p,[,maxN,],;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 199))
    
    def test_0(self):
        input = """main: function void() {printString(\"10d cho BTL so 1\");}"""
        expect = "main,:,function,void,(,),{,printString,(,10d cho BTL so 1,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 100))
    
    
    
    
    