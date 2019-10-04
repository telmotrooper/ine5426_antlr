# VARIABLES
ANTLR_PATH = ./antlr-4.7.2-complete.jar
ANTLR = java -jar $(ANTLR_PATH)
GRUN = java -cp .:$(ANTLR_PATH) org.antlr.v4.gui.TestRig
INPUT = ./example_program.txt

default:
	@echo "You need Java 8+ and Python 3 installed to build and run this application."
	@$(ANTLR) -Dlanguage=Python3 Expr.g4
	@echo "Program successfully compiled."
	@echo "To run it, use 'make start'."

clean:
	@echo "Removing old files (if they exist)..."
	@rm -rf .antlr *.java *.interp *.tokens *.class Expr*.py 2> /dev/null
	@echo "Done."

start:
	python3 ./main.py $(INPUT)
