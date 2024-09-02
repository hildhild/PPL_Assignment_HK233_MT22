// Student ID: 2113481

grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: list_declared EOF;

//! --------------------------  Parser ----------------------- //
//List declarations
list_declared:  declared list_declared |  declared;
declared: function | variable;

//Types
atomic_type: BOOLEAN | INTEGER | FLOAT | STRING;

array_type: ARRAY LSB dimensions RSB OF atomic_type;
dimensions: INT_LIT | INT_LIT COMMA dimensions;

void_type: VOID;
auto_type: AUTO;

var_type: atomic_type | array_type | auto_type;
func_type: var_type | void_type;

//Variables declarations
// variable: list_id COLON var_type (ASSIGN list_exp)? SEMI;
variable returns[n] @init {$n = 0}: list_id COLON var_type (ASSIGN (exp ({ $list_id.text.count(',') > $n }? COMMA exp {$n += 1})*) { $list_id.text.count(',') == $n }?)? SEMI;

list_id: ID | ID COMMA list_id;

//Parameters declarations
parameter: INHERIT? OUT? ID COLON var_type;

//Function declaration
function: ID COLON FUNCTION func_type LP list_param? RP (INHERIT ID)? block_stmt;
list_param: parameter COMMA list_param | parameter;

// Expression
exp: exp0 (CONCAT) exp0 | exp0;
exp0: exp1 (EQUAL | DIFF | LT | GT | LTE | GTE) exp1 | exp1;
exp1: exp1 (AND | OR) exp2 | exp2;
exp2: exp2 (ADD | SUB) exp3 | exp3;
exp3: exp3 (MUL | DIV | MOD) exp4 | exp4;
exp4: NOT exp4 | exp5;
exp5: SUB exp5 | exp6; 
exp6: (ID | func_call) LSB list_exp RSB | operand; 

list_exp: exp COMMA list_exp | exp;

// Operands
operand: ID | literal | LP exp RP | func_call; //có ưu tiên dùng ( ) không

// Literals
literal: INT_LIT | FLOAT_LIT | STR_LIT | BOOL_LIT | arr_lit;

arr_lit: LCB list_exp RCB;  //list_exp được rỗng không

//Function call
func_call: ID LP list_exp? RP;

//Statement
stmt: 
	assign_stmt
	| if_stmt
	| for_stmt 
	| while_stmt
	| do_while_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| call_stmt 
	| block_stmt;

//Assignment Statement
assign_stmt: lhs ASSIGN exp SEMI;
lhs: ID | index_exp; // Left hand side
index_exp: ID LSB list_exp RSB;

//If statement
if_stmt: IF LP exp RP stmt (ELSE stmt)?;

//For statement
for_stmt: FOR LP ID ASSIGN exp COMMA exp COMMA exp RP stmt;

// While statement
while_stmt: WHILE LP exp RP stmt;

//Do-while statement
do_while_stmt: DO stmt WHILE LP exp RP SEMI;

//Break statement
break_stmt: BREAK SEMI;

//Continue statement
continue_stmt: CONTINUE SEMI;

//Return statement
return_stmt: RETURN exp? SEMI;

//Call statement
call_stmt: func_call SEMI;

//Block statement
block_stmt: LCB list_block_component RCB;
block_component: stmt | variable;
list_block_component: block_component list_block_component | ;


//!  -------------------------- end Parser ------------------- //

//! --------------------------  Lexical structure ----------------------- //
//Bool literal
BOOL_LIT: TRUE | FALSE;

//Keywords
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

//Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
DIFF: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
CONCAT: '::';

//Separators
LP: '('; // Left Parenthesis
RP: ')'; // Right Parenthesis
LSB: '['; // Left Square Bracket
RSB: ']'; // Right Square Bracket
POINT: '.'; //Point
COMMA: ','; // Comma
SEMI: ';'; //Semicolon
COLON: ':'; //Colon
LCB: '{'; //Left Curly Bracket
RCB: '}'; //Right Curly Bracket
ASSIGN: '='; //Assign


//IdentifierS
ID: [a-zA-Z_] [a-zA-Z0-9_]*;

//LiteralS
fragment INT_PART: '0' | [1-9]('_'? [0-9])*;
fragment DEC_PART: POINT [0-9]*;
fragment EXP_PART: [eE] [-+]? [0-9]+;
INT_LIT: INT_PART {self.text = self.text.replace('_', '')};
FLOAT_LIT: (INT_PART DEC_PART EXP_PART? | DEC_PART EXP_PART | INT_PART EXP_PART) {self.text = self.text.replace('_', '')};

fragment STR_CHAR: ~[\f\r\n"\\] | ESC_SEQ | '\\"'; 
fragment ESC_SEQ: '\\' [bfrnt'\\];
STR_LIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1]};

//COMMENTS WS
COMMENT: '/*' .*? '*/' -> skip;
INLINE_COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\b\f\r\n]+ -> skip; // skip WS

//Errors
UNCLOSE_STRING: '"' STR_CHAR* (EOF | '\n' | '\r\n') 
{if self.text[-1] == '\n':
	if self.text[-2] == '\r':
		raise UncloseString(self.text[1:-2]);
	else:
		raise UncloseString(self.text[1:-1]);
else:
	raise UncloseString(self.text[1:]);
};

fragment ILLEGAL_ESC: ('\\' ~[bfrnt'"\\]);
ILLEGAL_ESCAPE: '"' STR_CHAR* ILLEGAL_ESC {raise IllegalEscape(self.text[1:])};

ERROR_CHAR: . {raise ErrorToken(self.text)};
//!  -------------------------- end Lexical structure ------------------- //


