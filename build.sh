#!/usr/bin/env bash

echo "Removing old files (if they exist)..."

rm *.java *.interp *.tokens 2> /dev/null

echo "Generating .java files..."

antlr4 Expr.g4

echo "Generating .class files..."

javac -cp antlr-4.7.2-complete.jar Expr*.java
