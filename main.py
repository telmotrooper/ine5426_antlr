#!/usr/bin/env python3

import sys
from antlr4 import *
from src.CC20192Lexer import CC20192Lexer
from src.CC20192Parser import CC20192Parser
from src.CC20192Listener import CC20192Listener
from tabulate import tabulate
from database import conn


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CC20192Lexer(input_stream)

    # Essas instâncias são utilizadas apenas para gerar a árvore de símbolos
    extra_input_stream = FileStream(argv[1])
    extra_lexer = CC20192Lexer(extra_input_stream)
    extra_lexer.removeErrorListeners()

    # Montando a árvore de símbolos
    table = []
    i = 0

    token_list = extra_lexer.getAllTokens()
    for token in token_list:
        conn.execute('''
            INSERT INTO symbols(id, line, column, token, lexeme, scope)
            VALUES (?,?,?,?,?, NULL)
        ''', (i, token.line, token.column, extra_lexer.symbolicNames[token.type], token.text))
        conn.commit()

        i += 1

    for row in conn.execute("SELECT * FROM symbols"):
        table.append(row)

    print("Tabela de símbolos:")
    print(tabulate(table, headers=["Índice", "Linha", "Coluna", "Token", "Lexema", "Scope"]))
    stream = CommonTokenStream(lexer)

    print("\n" + "Lista de tokens:")
    print(stream.getText() + "\n")

    parser = CC20192Parser(stream)
    tree = parser.program()

    # print("\nParse tree (in text):\n")
    # print(tree.toStringTree(recog=parser))

    listener = CC20192Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)
