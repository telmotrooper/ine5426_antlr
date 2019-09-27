#!/usr/bin/env bash

ANTLR_PATH=./antlr-4.7.2-complete.jar

ANTLR="java -jar $ANTLR_PATH"
GRUN="java -cp .:$ANTLR_PATH org.antlr.v4.gui.TestRig"

echo "You need Java 8+ and Python 3 installed to build and run this application."
echo ""

echo "Removing old files (if they exist)..."

rm -rf .antlr *.java *.interp *.tokens *.class Expr*.py 2> /dev/null

echo "Generating Lexer and Parser..."

$ANTLR -Dlanguage=Python3 Expr.g4

#$ANTLR  -Dlanguage=Python3 CCC20192.g4

# echo "Generating .class files..."

# javac -cp .:$ANTLR_PATH Expr*.java

# echo "Write your expression, press ENTER and then Ctrl+D to see the results."

# $GRUN Expr prog -gui
