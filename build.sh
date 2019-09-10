#!/usr/bin/env bash

ANTLR_PATH=./antlr-4.7.2-complete.jar

ANTLR="java -jar $ANTLR_PATH"
GRUN="java -cp .:$ANTLR_PATH org.antlr.v4.gui.TestRig"

echo "You need Java installed to run this application."

echo "Removing old files (if they exist)..."

rm -rf .antlr *.java *.interp *.tokens *.class 2> /dev/null

echo "Generating .java files..."

$ANTLR Expr.g4

echo "Generating .class files..."

# javac Expr*.java
javac -cp .:$ANTLR_PATH Expr*.java

echo "Write your expression, press ENTER and then Ctrl+D to see the results."

$GRUN Expr prog -gui
