#!/usr/bin/env python3

import sys
from antlr4 import *
from src.CC20192Lexer import CC20192Lexer
from src.CC20192Parser import CC20192Parser
from tabulate import tabulate

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CC20192Lexer(input_stream)

    extra_input_stream = FileStream(argv[1])
    extra_lexer = CC20192Lexer(extra_input_stream)

    table = []

    i = 0
    x = extra_lexer.getAllTokens()
    for token in x:
        table.append([i, token.line, token.column, extra_lexer.symbolicNames[token.type], token.text])
        i += 1

    print("Tabela de símbolos:")
    print(tabulate(table, headers=["Índice", "Linha", "Coluna", "Token", "Lexema"]))
    stream = CommonTokenStream(lexer)

    print("\nLista de tokens:")
    print(stream.getText())

    parser = CC20192Parser(stream)
    tree = parser.program()
    # print("\nParse tree (in text):\n")
    # print(tree.toStringTree(recog=parser))
 
if __name__ == '__main__':
    main(sys.argv)
