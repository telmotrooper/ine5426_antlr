#!/usr/bin/env bash

ANTLR=./antlr-4.7.2-complete.jar

echo "Removing old files (if they exist)..."

rm -rf .antlr *.java *.interp *.tokens *.class 2> /dev/null

echo "Generating .java files..."

antlr4 Expr.g4

echo "Generating .class files..."

javac Expr*.java
# javac -cp $ANTLR Expr*.java

echo "Write your expression and press Ctrl+D to see the results."

grun Expr prog -gui
# java -cp $ANTLR org.antlr.v4.gui.TestRig Expr prog -gui
