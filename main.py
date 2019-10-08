#!/usr/bin/env python3

import sys
from antlr4 import *
from src.CC20192Lexer import CC20192Lexer
from src.CC20192Parser import CC20192Parser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CC20192Lexer(input_stream)

    extra_input_stream = FileStream(argv[1])
    extra_lexer = CC20192Lexer(extra_input_stream)

    i = 0
    x = extra_lexer.getAllTokens()
    for token in x:
        print("Índice: {0}".format(i))
        print("Linha: {0} Coluna: {1}".format(token.line, token.column))
        print("Lexema: {0}".format(token.text))
        print("Token: {0}".format(lexer.symbolicNames[token.type]))
        print("---")
        i += 1

    stream = CommonTokenStream(lexer)

    print("Token list:\n")
    print(stream.getText())

    parser = CC20192Parser(stream)
    tree = parser.program()
    # print("\nParse tree (in text):\n")
    # print(tree.toStringTree(recog=parser))
 
if __name__ == '__main__':
    main(sys.argv)
