grammar Decaf ;

// Reglas LEXER

fragment LETTER: ('a'..'z'|'A'..'Z'|'_') ;
fragment DIGIT: '0'..'9' ;
 
ID: LETTER (LETTER|DIGIT)* ;
NUM: DIGIT(DIGIT)* ;
CHAR: '\'' ( ~['\r\n\\] | '\\' ['\\] ) '\'' ;
WHITESPACE : [ \t\r\n\f]+  ->channel(HIDDEN) ;

// Reglas PARSER
program:'class' 'Program' '{' (declaration)* '}' ;
declaration: 
      structDeclaration
    | varDeclaration
    | methodDeclaration ; 
varDeclaration: 
      varType ID ';'              
    | varType ID '[' NUM ']' ';'  ;

structDeclaration:'struct' ID '{' (varDeclaration)* '}' ;
varType :
    'int'                   #INT_VARTYPE
    | 'char'                #CHAR_VARTYPE
    | 'boolean'             #BOOL_VARTYPE
    | 'struct' ID           #STRUCT_VARTYPE
    | structDeclaration     #STRUCTDECLARATION_VARTYPE
    | 'void'                #VOID_VARTYPE;              
methodDeclaration: methodType ID '(' (parameter (',' parameter)*)* ')' block ;
methodType: 
      'int'       #INT_METHODTYPE
    | 'char'      #CHAR_METHODTYPE
    | 'boolean'   #BOOL_METHODTYPE
    | 'void'      #VOID_METHODTYPE;
parameter: 
      parameterType ID
    | parameterType ID '[' ']' ;
parameterType: 
      'int' 
    | 'char' 
    | 'boolean' ;
block: '{' (varDeclaration)* (statement)* '}';
statement: 
      'if' '(' expression ')' block ( 'else' block )?       #StatementIF
    | 'while' '('expression')' block                        #StatementWHILE
    | 'return' expression ';'                               #StatementRETURN
    | methodCall ';'                                        #StatementMETHODCALL
    | block                                                 #StatementBLOCK
    | location '=' expression ';'                           #StatementLOCATION;

location: (ID|ID '[' expression ']') ('.' location)? ;
expression 
    : methodCall #expr_mcall
    | location #expr_loc
    | literal #expr_literal
    | '-' expression #expr_minus // Unary Minus Operation
    | '!' expression #expr_not // Unary NOT Operation
    | '('expression')' #expr_parenthesis
    | expression arith_op_fifth expression #expr_arith5 // * / %
    | expression arith_op_fourth expression #expr_arith4 // + -
    | expression arith_op_third expression #expr_arith3 // == != < <= > >=  
    | expression arith_op_second expression #expr_arith2 // &&
    | expression arith_op_first expression #expr_arith1 // ||
    ;

methodCall: ID '(' (expression (',' expression)*)? ')';

// Operaciones precedencia
// Extraido de: https://anoopsarkar.github.io/compilers-class/decafspec.html
rel_op : '<' | '>' | '<=' | '>=';
eq_op : '==' | '!=' ;
arith_op_fifth: '*' | '/' | '%';
arith_op_fourth: '+' | '-';
arith_op_third: rel_op | eq_op;
arith_op_second: '&&';
arith_op_first: '||';

// <arith_op>→'+'| '-'| '*'| '/'| '%'
// <rel_op>→'<'| '>'| '<='| '>='
// <eq_op>→'=='| '!='
// <cond_op>→'&&'| '||'

literal : int_literal | char_literal | bool_literal ;
int_literal : NUM ;
char_literal : '\'' CHAR '\'' ;
bool_literal : 'true' | 'false' ;