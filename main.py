#!/usr/bin/env python3

import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    print(tree.toStringTree(recog=parser))
 
if __name__ == '__main__':
    main(sys.argv)
