# VARIABLES
GRAMMAR = CC20192
ANTLR_PATH = antlr-4.7.2-complete.jar
ANTLR = java -jar $(ANTLR_PATH)
GRUN = java -cp .:../$(ANTLR_PATH) org.antlr.v4.gui.TestRig
INPUT = input/hello.ccc

# ANSI ESCAPE CODES
GREEN = \u001b[32m
YELLOW = \u001b[33m
RESET = \u001b[0m

build:
	@echo -e "(You need Java 8+ and Python 3 installed to build and run this application.)"
	@echo -e "Generating lexer and parser..."
	@$(ANTLR) $(GRAMMAR).g4 -o src
	@$(ANTLR) $(GRAMMAR).g4 -o src -Dlanguage=Python3
	@echo -e "Generating diagrams..."
	@$(ANTLR) $(GRAMMAR).g4 -atn -o diagrams
	@cd diagrams && rm *.interp *.tokens *.java
	@javac -cp .:$(ANTLR_PATH) src/*.java -d ./bin
	@echo -e "Program successfully compiled."
	@echo -e "To run it, use $(GREEN)make start$(RESET) or '$(GREEN)make start INPUT=$(YELLOW)file_path$(RESET)'."


view-diagram:
	@echo -e "To view a diagram you need Graphviz installed (on Ubuntu: $(GREEN)sudo apt get graphviz$(RESET))."
	@echo -e "Converting DOT file to PNG..."
	@dot -Tpng $(INPUT) -o $(INPUT).png
	@echo -e "Showing state transition diagram for \"$(INPUT)\"..."
	@xdg-open $(INPUT).png


clean:
	@echo -e "Removing old files (if they exist)..."
	@rm -rf .antlr bin diagrams src 2> /dev/null
	@rm -rf bin diagrams src 2> /dev/null
	@echo -e "Done."

start:
	@python3 main.py $(INPUT)
	@cd bin && cat ../$(INPUT) | $(GRUN) CC20192 program -gui
