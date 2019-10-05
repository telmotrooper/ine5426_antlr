# VARIABLES
ANTLR_PATH = lib/antlr-4.7.2-complete.jar
ANTLR = java -jar $(ANTLR_PATH)
GRUN = java -cp .:$(ANTLR_PATH) org.antlr.v4.gui.TestRig
INPUT = input/example.txt

build:
	@echo "You need Java 8+ and Python 3 installed to build and run this application."
	@$(ANTLR) Expr.g4
	@javac -cp .:$(ANTLR_PATH) Expr*.java
	@echo "Program successfully compiled."
	@echo "To run it, use 'make start'."

gen-diagrams:
	@echo "Generating diagrams..."
	@$(ANTLR) -atn Expr.g4

view-diagram:
	@echo "To view a diagram you need the package graphviz installed."
	@echo -e "On Ubuntu: \u001b[32msudo apt get graphviz\u001b[0m"
	@dot -Tpng $(INPUT).dot -o $(INPUT).png
	@xdg-open $(INPUT).png


clean:
	@echo "Removing old files (if they exist)..."
	@rm -rf .antlr *.dot *.png *.java *.interp *.tokens *.class Expr*.py 2> /dev/null
	@echo "Done."

start:
	@cat $(INPUT) | $(GRUN) Expr program -gui
