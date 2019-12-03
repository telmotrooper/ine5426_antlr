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

# build:
# 	@echo -e "(You need Python 3 installed to build and run this application.)"
# 	@$(ANTLR) $(GRAMMAR).g4 -o src -Dlanguage=Python3
# 	@echo -e "Program successfully compiled."
# 	@echo -e "To run it, use $(GREEN)make start$(RESET) or '$(GREEN)make start INPUT=$(YELLOW)file_path$(RESET)'."

help:
	@echo -e "To run the program, use '$(GREEN)make start$(RESET)' or '$(GREEN)make start INPUT=$(YELLOW)file_path$(RESET)'."

start:
	@python3 main.py $(INPUT)
