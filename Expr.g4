grammar Expr;		

program         : statement;
statement       : vardecl;
vardecl					: Type WS+ IDENT ';';
Type						: 'float';

IDENT : [a-zA-Z]+;
WS: [ \t];

// STATEMENT1      : STATEMENT | '&';
// STATEMENT       : VARDECL';' | ATRIBSTAT';' | PRINTSTAT';' | READSTAT';' | 
//                    RETURNSTAT';' | IFSTAT';' | FORSTAT';' | '{'STATELIST'}' | 
// 	           'break'';' | ';';

// VARDECL         : TYPE 'ident' BRACKETS*;
// TYPE            : 'int' | 'float' | 'string';
// BRACKETS        : '['INT']' | '['INT']'BRACKETS;
// ATRIBSTAT       : LVALUE '=' ATRIBEXPRESS;
// ATRIBEXPRESS    : EXPRESSION | ALLOCEXPRESSION;
// PRINTSTAT       : 'print' EXPRESSION;
// READSTAT        : 'read' LVALUE;
// RETURNSTAT      : 'return';
// IFSTAT          : 'if' '('EXPRESSION')' STATEMENT ELSESTAT;
// ELSESTAT        : 'else' STATEMENT | '&';
// FORSTAT         : 'for''('ATRIBSTAT';' EXPRESSION';' ATRIBSTAT')' STATEMENT;
// STATELIST       : STATEMENT STATELIST1;
// STATELIST1      : STATELIST | '&';
// ALLOCEXPRESSION : 'new' TYPE '['EXPRESSION']'BRACKETEXPRESS;
// BRACKETEXPRESS  : '['EXPRESSION']' | '['EXPRESSION']'BRACKETEXPRESS;
// EXPRESSION      : NUMEXPRESSION EXPRESSION1;
// EXPRESSION1     : SIGNAL NUMEXPRESSION | '&';
// SIGNAL          : '<' | '>' | '<=' | '>=' | '==' | '!=';
// NUMEXPRESSION   : TERM ARITHMETIC1;
// ARITHMETIC1     : ARITHSIGNAL1 TERM | ARITHSIGNAL1 TERM ARITHMETIC1;
// ARITHSIGNAL1    : '+' | '-';
// TERM            : UNARYEXPR ARITHMETIC2;
// ARITHMETIC2     : ARITHSIGNAL2 UNARYEXPR | ARITHSIGNAL2 UNARYEXPR ARITHMETIC2;
// ARITHSIGNAL2    : '*' | '%' | '\\';
// UNARYEXPR       : ARITHSIGNAL3 FACTOR;
// ARITHSIGNAL3    : ARITHSIGNAL1 | '&';
// FACTOR          : INT | 'float_constant' | 'string_constant' |
// 		   'null' | LVALUE | '('EXPRESSION')';
// LVALUE          : 'ident' BRACKETEXPRESS;
// INT     : [0-9]+ ;
