grammar CCC20192;

// sintático

program           : statement1;

statement1        : statement 
                  | ;

statement         : vardecl SEMICOLON 
                  | atribstat SEMICOLON
                  | printstat SEMICOLON
                  | readstat SEMICOLON
                  | returnstat SEMICOLON
                  | ifstat SEMICOLON
                  | forstat SEMICOLON
                  | OPENBRACE statelist CLOSEBRACE
                  | BREAK SEMICOLON
                  | SEMICOLON;

vardecl           : vartype IDENT brackets;

vartype           : INT
                  | FLOAT
                  | STRING;

brackets          : OPENBRACKET INT_CONSTANT CLOSEBRACKET
                  | OPENBRACKET INT_CONSTANT CLOSEBRACKET brackets;
                  | ;

atribstat         : lvalue ATRIB atribexpress;

atribexpress      : expression
                  | allocexpression;

printstat         : PRINT expression;

readstat          : READ lvalue;

returnstat        : RETURN;

ifstat            : IF OPENPAR expression CLOSEPAR statement elsestat;

elsestat          : ELSE statement
                  | ;

forstat           : FOR OPENPAR atribstat SEMICOLON expression SEMICOLON atribstat CLOSEPAR statement;

statelist         : statement statelist1;

statelist1        : statelist
                  | ;

allocexpression   : NEW vartype OPENBRACKET expression CLOSEBRACKET bracketexpress;

bracketexpress    : OPENBRACKET expression CLOSEBRACKET
                  | OPENBRACKET expression CLOSEBRACKET bracketexpress;

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

arithmetic1       : arithsignal1 term
                  | arithsignal1 term arithmetic1;

arithsignal1      : PLUS
                  | MINUS;

term              : unaryexpr arithmetic2;

arithmetic2       : arithsignal2 unaryexpr
                  | arithsignal2 unaryexpr arithmetic2;

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

// lexico

SEMICOLON       : ';';
OPENBRACE       : '{';
CLOSEBRACE      : '}';
BREAK           : 'break';
IDENT           : [a-zA-Z0-9]+;
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
FLOAT_CONSTANT  : [0-9+.0.9+];
STRING_CONSTANT : [a-zA-Z0-9]*;
NULL            : 'null';

WHITESPACE   : (' '|'\t'|'\n'|'\r')+ -> skip ;



