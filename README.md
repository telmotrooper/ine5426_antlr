# Analisadores Léxico e Sintático para Linguagem CC-2019-2

É necessário ter Java versão 8 ou superior instalado para utilizar essa aplicação e, caso queira visualizar os diagramas de transição, o pacote `graphviz`.

## Comandos

* `make` - compila a aplicação e gera os diagramas de transição
* `make clean` - remove os arquivos temporários
* `make start` - executa o analisador léxico e o sintático em cima do arquivo `input/example.txt`
* `make start INPUT=program1.txt` - executa o analisador léxico e o sintático em cima do arquivo `program1.txt` (qualquer programa CC-2019-2 pode ser colocado em INPUT)
* `make view-diagram INPUT=diagrams/CC20192Lexer.IF.dot` - mostra o diagrama de transição especificado por INPUT (requer o pacote `graphviz` instalado)
