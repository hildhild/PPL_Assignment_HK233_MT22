# remaked by Le Dinh Huy

import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_a(self):
        """test"""
        input = """
            VoTien : boolean = true && "true" || 1; 
            VoTien : integer = 1 && 2 && 3 || 4 || 4;
            VoTien : integer = 1 + 2 - 2 + 3 && 3;
            VoTien : integer = 1 / 2 * 3 % 4;
            VoTien : integer = 1 / 2 / 2 * 3 % 4;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200)) 

    def test_declared(self): # test case 201 -> 220
        """declared"""    
        
        #! biến
        input = """ 
            VoTien : integer;
            
            //VO Tien
            VoTien : integer = 0;
            a: array [122,15] of boolean;
            a: array [122,15] of boolean = 1 + 1 / 2 * 3;
            b: array [3] of string;
            /* 12 
            */
            
            b : array [3] of string =  2 :: " tring";
            i: float = 0;
            i:integer;
            i:integer = 0;
            // VO Tien;
             
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))   
        
        # input = """ 
        #     var VoTien
        # """
        # expect = "Error on line 2 col 23: \n"
        # self.assertTrue(TestParser.test(input, expect, 202))   
        
#         input = """ 
#             dynamic VoTien[5] <- 3
#         """
#         expect = "Error on line 2 col 26: ["
#         self.assertTrue(TestParser.test(input, expect, 203))         

        input = """ 
            a : array ["string"] of boolean;
            a : array [[1,2]] of boolean;
            a : array [1+1] of boolean;
        """
        expect = "Error on line 2 col 23: string"
        self.assertTrue(TestParser.test(input, expect, 204))   
        
        input = """ 
            a: array [1,] of boolean;
        """
        expect = "Error on line 2 col 24: ]"
        self.assertTrue(TestParser.test(input, expect, 205)) 

#         input = """ 
#             var a[1]
#         """
#         expect = "Error on line 2 col 17: ["
#         self.assertTrue(TestParser.test(input, expect, 206))  
        
         
        
#         #! hàm và declaration_statement
        input = """ 
            main: function float () {
                return a;
            }
            main: function void (f1 : integer) {
                return;
            }
            main: function void (f1: integer = c) {
                return;
            }
        """
        expect = "Error on line 8 col 45: ="
        self.assertTrue(TestParser.test(input, expect, 207))       
        
        # input = """ 
        #     func main()
        #     ## VO Tien
        #     func main() func main(dynamic a) ## VO Tien
        # """
        # expect = "Error on line 4 col 24: func"
        # self.assertTrue(TestParser.test(input, expect, 208))  

        # input = """ 
        #     func main(var a)
        # """
        # expect = "Error on line 2 col 22: var"
        # self.assertTrue(TestParser.test(input, expect, 209))                 

#         #! lỗi comment và newline
#         input = """ 
#             ##12
#             ##12
            
#             func main(number a) var c <- 1
#         """
#         expect = "Error on line 5 col 32: var"
#         self.assertTrue(TestParser.test(input, expect, 210))   
        
#         input = """ 
#             func main(string a) 
#                 begin 
#                     break ## 12
#                 end
#             func main(dynamic a) 
#         """
#         expect = "Error on line 6 col 22: dynamic"
#         self.assertTrue(TestParser.test(input, expect, 211))    

#         input = """ 
#             func main(number a[1,2,3]) ##12
#                 break
#         """
#         expect = "Error on line 3 col 16: break"
#         self.assertTrue(TestParser.test(input, expect, 212))    
        
        input = """ 
            //12
            main : function void (a:integer) //14
            {
                //12
                break;
                
            }
            //12
            /*12*/
            main: function void (a:integer) {
                continue;
            }
            //12        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))                  

        input = """ 
            // 12
            
            a: boolean = 1 ;// 12
            // 12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))   
        
#         input = """var a <- 1"""
#         expect = "Error on line 1 col 10: <EOF>"
#         self.assertTrue(TestParser.test(input, expect, 215))  

#         input = """func main(number a) """
#         expect = "Error on line 1 col 20: <EOF>"
#         self.assertTrue(TestParser.test(input, expect, 216))  
                                   
    def test_Expression(self):
#         """Expression"""
#         #! nối chuỗi không có tính kết hợp
        input = """  VoTien : string = "Vo" :: "Tien" ;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
        
        input = """ VoTien : string = "Vo" :: 1 :: "Tien" 
        """
        expect = "Error on line 1 col 29: ::"
        self.assertTrue(TestParser.test(input, expect, 212))
        
#         #! so sánh không có tính kết hợp
        input = """ 
            Vo : boolean = true > "true";
            Vo : boolean = true >= "true";
            Vo : boolean = true == "true";
            Vo : boolean = true < "true";
            Vo : boolean = true <= "true";
            Vo : boolean = true >= "true" :: 1 >2;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
        
        input = """ VoTien : float = true > x >= z ;
        """
        expect = "Error on line 1 col 27: >="
        self.assertTrue(TestParser.test(input, expect, 214))
        
#         #! cộng trừ nhân chia và &&/or ::.
        input = """ 
            VoTien : string = true && "true" || 1  ;
            VoTien : string = 1 && 2 && 3 || 4 || 4 ;
            VoTien : string = 1 + 2 - 2 + 3 && 3 ;
            VoTien : string = 1 / 2 * 3 % 4 ;
            VoTien : string = 1 / 2 / 2 * 3 % 4 ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        
        input = """VoTien : boolean = true >= "true" && 1 > 2;
        """
        expect = "Error on line 1 col 39: >"
        self.assertTrue(TestParser.test(input, expect, 216)) 
        
#         #! toán tử not và sign   
        input = """ 
            VoTien : integer = -1 * ! 1;
            VoTien : integer = ! ! !----C;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217)) 
        
        input = """ VoTien : boolean = - ! 1;
        """
        expect = "Error on line 1 col 22: !"
        self.assertTrue(TestParser.test(input, expect, 218)) 
        
#         #! toán tử array
        input = """ 
             VoTien : auto = a[1] + 1;
             VoTien : auto = arr[1,1+2][1][2,3];
             VoTien : auto = arr[1,(1) :: 2,arr[ar[(1*2) && 1]],arr[2]];
             VoTien : auto = a[1] + fun()[1,fun()] ;
             VoTien : auto = 1[1];
        """
        expect = "Error on line 3 col 39: ["
        self.assertTrue(TestParser.test(input, expect, 219))
        
        input = """VoTien : float = a[];
        """
        expect = "Error on line 1 col 19: ]"
        self.assertTrue(TestParser.test(input, expect, 220)) 
        
#         #! hàm 
        input = """ 
             VoTien: auto = a();
             VoTien: auto = a(1,2);
             VoTien: auto = a(x,arr[2])[2];
             VoTien: auto = a(z,k[3] :: 2)[1,2];
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))    
        
        input = """ VoTien: float = a()();
        """
        expect = "Error on line 1 col 20: ("
        self.assertTrue(TestParser.test(input, expect, 222))  
        
#         #! tổng hợp

        input = """ 
             VoTien: auto = a() + --1 / 2 *3 <= 3 :: "v" >= 2;
             VoTien: auto = a(1,2)[1,2,3 :: 2] + false + true;
             VoTien: auto = a(z,k[2,3,"2"] :: 2)[true];
             VoTien: auto = (a :: 3) :: b && (a >= b) < b[1, b[1]];
             VoTien: auto =  {"tr", 2, 3, 4, 5} + {{1, 2 + 2 * 2 / 3, 3},{4, 5, 6}};
             VoTien: auto = a(x,arr[2])[2,3+2,true,false];
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))  

        input = """ VoTien : string = a[1]();
        """
        expect = "Error on line 1 col 23: ("
        self.assertTrue(TestParser.test(input, expect, 224))         
        
    def test_Statements(self): # test 230 -> ::
#         """Statements"""
        
#         #! test assignment_statement
        input = """
        // comment
         main : function void()

            // comment
            {
            aPI = 3.14;
            }
            // comment
            
        // comment
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        
        input = """
         main : function void () {
             
        } 
         main : function void () 
            {
                // comment0
            }
         main : function auto ()
            //comment1
            {
                /* comment2
                
                 comment3*/
                VoTien = 1 + 2 + fun();
                VoTien[1+a] = 1;
                
                // comment4
                VoTien[3+4,2,4] = 1;
                
                // comment5
            }
            // comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231)) 
        
        input = """
         main : function void(){
            aPI + 1 = 3.14;
         
         }
        """
        expect = "Error on line 3 col 16: +"
        self.assertTrue(TestParser.test(input, expect, 232))
        
        input = """
         main : function void(){
            aPI()= 3.14;
         
         }
        """
        expect = "Error on line 3 col 17: ="
        self.assertTrue(TestParser.test(input, expect, 233))
        
        input = """
         main : function void(){
            (aPI)[2]= 3.14;
         
         }
        """
        expect = "Error on line 3 col 12: ("
        self.assertTrue(TestParser.test(input, expect, 234))
                
#         #! test if_statement 
        input = """
         main : function void()
            {   
                if(1+1) api = 1;
                // comment0
                
                if(1+1) 
                    // comment1
                    
                    api = 1;
                    // comment2
                else api = 1;
                // comment3
                
                if (1) api = 1;
                    // comment1
                else  
                    api = 1;
                    // comment2
                
                if (1) api = 1;
                if (1 :: 2) api = 1;
                if (1) api = 1;
                else api = 1 ;  
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))  
        
        input = """
         main : function void()
            {   
                if (api = 1)
            }
        """
        expect = "Error on line 4 col 24: ="
        self.assertTrue(TestParser.test(input, expect, 236))        
        
#         #! test for break Continue
        input = """
         main : function auto()
            {
            for (i = 1 , i >= 10 , 1 + 1)
                // comment
                
                a = 1;
            // comment
            }
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))    
        
        input = """
         main : function void()
            {
            for (i[1] = true,  i >= 10 , 1 + 1)
                a = 1;
            }
        """
        expect = "Error on line 4 col 18: ["
        self.assertTrue(TestParser.test(input, expect, 238))    

        input = """
         main : function void()
            {
            for (i+1 = a(2) , i >= 10 , 1 + 1)
                a = 1;
            }
        """
        expect = "Error on line 4 col 18: +"
        self.assertTrue(TestParser.test(input, expect, 239)) 
        
        input = """
         main : function void()
        {
            break;
            continue;
            for (i = {0,1} ,  i >= 10 , 1 + 1 :: 3 / 2)
                {
                    break;
                    continue;
                }
                
            for (i = false , i >= 10 , 1) print(1);
            for (i = h , i >= 10 , 1 )
                print(1);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))  
        
        input = """
         main : function void()
            {
            for (i = a[7,16] , i >= 10 , 1 + 1)
            }
        """
        expect = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 241))  
        
        
#         #! return  call_statement
        input = """
         main : function void()
         {
            return 1 + 1;
            }
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

        input = """
         main : function void()
            {
            main();
            }
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
        
        input = """
         main : function void()
        { 
            return ({1,2,3}) + 1;
            return main();
            main(1,2);
            fun();
            main({1,2,3}, 1+2, a, c :: e);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))  
        
        input = """
         main : function void()
         {
            return function();
            }
        """
        expect = "Error on line 4 col 19: function"
        self.assertTrue(TestParser.test(input, expect, 245))      
        
        input = """
         main : function string()
         {
            return break;
            }
        """
        expect = "Error on line 4 col 19: break"
        self.assertTrue(TestParser.test(input, expect, 246)) 
        
#         #! return  block
        input = """
         main : function float()
            {
                {
                    {
                        x = 1;
                    }
                    
                    {
                        return true;
                    }
                    
                    return false;
                }
                
                {}
                return true;
            }
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
     
    # def test_NewLine(self): # test 250 -> ::
    #     """new line"""
    #     input = """ aPI : auto = 3.14;"""
    #     expect = "Error on line 1 col 15: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 250))          
  
    def test_Source_Code(self): # test 270 -> ::
        """Source_Code"""
        input = """
         areDivisors : function void(num1:auto,  num2: string){
            return (num1 % num2 == 0 :: num2 % num1 == 0);
         }
         main : function auto()
            {
                 num1 : float = readNumber();
                 num2 : float = readNumber();
                if (areDivisors(num1, num2)) printString("Yes");
                else printString("No");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))   
        
        
        input = """
             isPrime : function void(x: integer){}
             main: function auto()
                {
                     x : auto = readNumber();
                    if (isPrime(x)) printString("Yes");
                    else printString("No");
                }
            isPrime : function void (x : float)
            {
            if (x <= 1) return false;
             i : auto = 2;
            for (i = 1 , i > x / 2 , 1)
            {
            if (x % i == 0) return false;
            }
            return true;
            
            
            for (i = {0} , i > x / 2 , 1 + 1) { c : auto = 1;}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))  

        input = """
         a : function integer() {return 1;} // 12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))   
        
        input = """
             x : auto = x ; x: auto = y;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273)) 
        
        input = """
        a : function void()
        {}
        
        a : function void()
        {

            x : integer = x;
            
        }
        
        a : function auto()
        {}
        a : function float() { 
        }
        a : function void() { 
        //123
        }
        a : function auto() { /* comment*/
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))  
        

        input = """    
        a : function boolean()
        {
            break continue;
        }
        """
        expect = "Error on line 4 col 18: continue"
        self.assertTrue(TestParser.test(input, expect, 275)) 
        
        input = """    
        a : function auto()
        {
            return 1 break;
        }
        """
        expect = "Error on line 4 col 21: break"
        self.assertTrue(TestParser.test(input, expect, 276))   
        
        input = """    
        a : function void()
        {
            if (x <= 1) return false;
            if (x <= 1 )
                return false ;
        } // comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))  
        
        input = """    
        a : function void()
        fun();
        """
        expect = "Error on line 3 col 8: fun"
        self.assertTrue(TestParser.test(input, expect, 278))  
        
        input = """    
        a : function void()
            if x <= 1 return false;
        """
        expect = "Error on line 3 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 279))  
        
        input = """    
        a : function boolean(){
            return; if x <= 1 return false;
            }
        """
        expect = "Error on line 3 col 23: x"
        self.assertTrue(TestParser.test(input, expect, 280))  
        
        # input = """    
        # a : function void()
        # {
        #     return ;
        # }
        # a : auto = {};
        # """
        # expect = "Error on line 4 col 18: ]"
        # self.assertTrue(TestParser.test(input, expect, 281))  
        
        input = """    
        a : function void (a : array [1+1] of integer){};
        """
        expect = "Error on line 2 col 39: +"
        self.assertTrue(TestParser.test(input, expect, 282))  
        
        input = """    
            a : auto = a[1][1];
        """
        expect = "Error on line 2 col 27: ["
        self.assertTrue(TestParser.test(input, expect, 283))  
        
        input = """    
            a : auto = 1[1];
        """
        expect = "Error on line 2 col 24: ["
        self.assertTrue(TestParser.test(input, expect, 284))  
        
        input = """
        """
        expect = "Error on line 2 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 285)) 
        
        input = """    
        a : function void()
            {
                a[1][2] = 1;
            }
        """
        expect = "Error on line 4 col 20: ["
        self.assertTrue(TestParser.test(input, expect, 286)) 
        
        
        input = """    
            a : auto = {1,2,3}{1};
        """
        expect = "Error on line 2 col 30: {"
        self.assertTrue(TestParser.test(input, expect, 287)) 
        

        input = """    
            a : array [1+1] of string;
        """
        expect = "Error on line 2 col 24: +"
        self.assertTrue(TestParser.test(input, expect, 288)) 
        
        input = """    
        a : function void()
            { a = 1;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289)) 
        
        input = """    
        a : function auto()
            {
            } c : auto = 1;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))    
        
        input = """    
        a : function void()
            {
                c()[1] = 1;
            }
        """
        expect = "Error on line 4 col 19: ["
        self.assertTrue(TestParser.test(input, expect, 291))      
        
        input = """    
        a : function void()
            {
                c = (1)[1];
            }
        """
        expect = "Error on line 4 col 23: ["
        self.assertTrue(TestParser.test(input, expect, 292))    
        
        input = """    
        a : function auto()
            {
                 c: auto = 1 c : auto = 1;
            }
        """
        expect = "Error on line 4 col 29: c"
        self.assertTrue(TestParser.test(input, expect, 293))      
        
        
        input = """    
        a : function void()
            {
                VoTien[] = 1;
            }
        """
        expect = "Error on line 4 col 23: ]"
        self.assertTrue(TestParser.test(input, expect, 294))     
        
        input = """    
        a : function void()
            {
                1 = 2;
            }
        """
        expect = "Error on line 4 col 16: 1"
        self.assertTrue(TestParser.test(input, expect, 295))     
        
        input = """    
            a : function string(s : array ["2"] of string);
        """
        expect = "Error on line 2 col 43: 2"
        self.assertTrue(TestParser.test(input, expect, 296))
        
        input = """    
            c : auto = a();
            [1];
        """
        expect = "Error on line 3 col 12: ["
        self.assertTrue(TestParser.test(input, expect, 297))     
        
        input = """    
            a : function void()
            {
                fun() fun();
            }
        """
        expect = "Error on line 4 col 22: fun"
        self.assertTrue(TestParser.test(input, expect, 298))    
        

        input = """    
            a : array [1][2] of integer = 1;
        """
        expect = "Error on line 2 col 25: ["
        self.assertTrue(TestParser.test(input, expect, 300))    
        
        input = """  
            a : integer = func()[1]  ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 301))    
        
        input = """    
            a : float = fun()["1" + 2 * 3];
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 302))   
        
        input = """    
            a : function void()
            {
                if ( 1 return true;
            }
        """
        expect = "Error on line 4 col 23: return"
        self.assertTrue(TestParser.test(input, expect, 303))    
        
        input = """    
            a : function void()
            {
                if (1  {return true};
            }
        """
        expect = "Error on line 4 col 23: {"
        self.assertTrue(TestParser.test(input, expect, 304))  
        
        input = """    
            a : function void()
            {
                a : function void() {return 1.0;}
            }
        """
        expect = "Error on line 4 col 20: function"
        self.assertTrue(TestParser.test(input, expect, 305))  
        
        input = """    
            a : function void()
            {
                if 1  return true;
            }
        """
        expect = "Error on line 4 col 19: 1"
        self.assertTrue(TestParser.test(input, expect, 306))  
        
        input = """    
            a : function void()
            {
                if (1)  return true;
                else return true;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 307))  
        
        input = """    
            a : function void()
            {
                if (1)  return true;
                else 1 return true;
            }
        """
        expect = "Error on line 5 col 21: 1"
        self.assertTrue(TestParser.test(input, expect, 308))  
                
        
                              