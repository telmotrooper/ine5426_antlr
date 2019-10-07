#!/usr/bin/env python3

import sys
from antlr4 import *
from src.CC20192Lexer import CC20192Lexer
from src.CC20192Parser import CC20192Parser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CC20192Lexer(input_stream)
    stream = CommonTokenStream(lexer)

    print("Token list:\n")
    print(stream.getText())

    parser = CC20192Parser(stream)
    tree = parser.program()
    print("\nParse tree (in text):\n")
    print(tree.toStringTree(recog=parser))
 
if __name__ == '__main__':
    main(sys.argv)
