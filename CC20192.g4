grammar CC20192;

program           : statement1;

statement1        : statement
                  | funclist
                  | ;

funclist          : funcdef funclist1;

funclist1         : funclist
                  | ;

funcdef           : DEF IDENT OPENPAR paramlist CLOSEPAR OPENBRACE statelist CLOSEBRACE;

paramlist         : vartype IDENT COMMA paramlist
                  | vartype IDENT
                  | ;

statement         : vardecl SEMICOLON
                  | atribstat SEMICOLON
                  | printstat SEMICOLON
                  | readstat SEMICOLON
                  | returnstat SEMICOLON
                  | ifstat
                  | forstat
                  | blockstatement
                  | BREAK SEMICOLON
                  | SEMICOLON;

blockstatement    : OPENBRACE statelist CLOSEBRACE;

vardecl           : vartype IDENT brackets;

vartype           : INT
                  | FLOAT
                  | STRING;

brackets          : OPENBRACKET INT_CONSTANT CLOSEBRACKET brackets
                  | ;

atribstat         : lvalue ATRIB atribexpress;

atribexpress      : expression
                  | allocexpression
                  | funccal;

funccal           : IDENT OPENPAR paramlistcall CLOSEPAR;

paramlistcall     : IDENT COMMA paramlistcall
                  | IDENT
                  | ;

printstat         : PRINT expression;

readstat          : READ lvalue;

returnstat        : RETURN;

ifstat            : IF OPENPAR expression CLOSEPAR blockstatement elsestat;

elsestat          : ELSE blockstatement
                  | ;

forstat           : FOR OPENPAR atribstat SEMICOLON expression SEMICOLON atribstat CLOSEPAR statement;

statelist         : statement statelist1;

statelist1        : statelist
                  | ;

allocexpression   : NEW vartype OPENBRACKET expression CLOSEBRACKET bracketexpress;

bracketexpress    : OPENBRACKET expression CLOSEBRACKET bracketexpress1
                  | ;

bracketexpress1   : bracketexpress
                  | ;

expression        : numexpression expression1;

expression1       : signal numexpression
                  | ;

signal            : LESS
                  | GREATER
                  | LESS_EQ
                  | GREATER_EQ
                  | EQUALS
                  | NOT_EQUALS;

numexpression     : term arithmetic1;

arithmetic1       : arithsignal1 term arithmetic1
                  | ;

arithsignal1      : PLUS
                  | MINUS;

term              : unaryexpr arithmetic2;

arithmetic2       : arithsignal2 unaryexpr arithmetic2
                  | ;

arithsignal2      : MULT
                  | DIV
                  | MODULO;

unaryexpr         : arithsignal3 factor;

arithsignal3      : arithsignal1
                  | ;

factor            : INT_CONSTANT
                  | FLOAT_CONSTANT
                  | STRING_CONSTANT
                  | NULL
                  | lvalue
                  | OPENPAR expression CLOSEPAR;

lvalue            : IDENT bracketexpress;


SEMICOLON       : ';';
COMMA           : ',';
OPENBRACE       : '{';
CLOSEBRACE      : '}';
DEF             : 'def';
BREAK           : 'break';
INT             : 'int';
FLOAT           : 'float';
STRING          : 'string';
OPENBRACKET     : '[';
CLOSEBRACKET    : ']';
INT_CONSTANT    : [0-9]+;
ATRIB           : '=';
PRINT           : 'print';
READ            : 'read';
RETURN          : 'return';
IF              : 'if';
OPENPAR         : '(';
CLOSEPAR        : ')';
ELSE            : 'else';
FOR             : 'for';
NEW             : 'new';
LESS            : '<';
GREATER         : '>';
LESS_EQ         : '<=';
GREATER_EQ      : '>=';
EQUALS          : '==';
NOT_EQUALS      : '!=';
PLUS            : '+';
MINUS           : '-';
MULT            : '*';
DIV             : '\\';
MODULO          : '%';
NULL            : 'null';
IDENT           : [a-zA-Z_][a-zA-Z0-9_]*;
STRING_CONSTANT : '"' .*? '"';
FLOAT_CONSTANT  : ('0'..'9')+ '.' ('0'..'9')+;

WHITESPACE   : (' '|'\t'|'\n'|'\r')+ -> skip;
