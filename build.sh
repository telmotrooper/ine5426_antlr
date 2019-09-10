#!/usr/bin/env bash

echo "Removing old files (if they exist)..."

rm *.java *.interp *.tokens

echo "Building application..."

antlr4 Expr.g4
javac Expr*.java
