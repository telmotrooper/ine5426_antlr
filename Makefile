# VARIABLES
ANTLR_PATH = antlr-4.7.2-complete.jar
ANTLR = java -jar $(ANTLR_PATH)
GRUN = java -cp .:$(ANTLR_PATH) org.antlr.v4.gui.TestRig
INPUT = input/example.txt

build:
	@echo "You need Java 8+ installed to build and run this application."
	@echo "Generating lexer and parser..."
	@$(ANTLR) Expr.g4 -o src
	@echo "Generating diagrams..."
	@$(ANTLR) Expr.g4 -atn -o diagrams
	@javac -cp .:$(ANTLR_PATH) src/*.java -d ./bin
	@echo "Program successfully compiled."
	@echo "To run it, use 'make start' or 'make start INPUT=file_path'."


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
