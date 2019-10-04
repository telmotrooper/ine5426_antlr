# VARIABLES
ANTLR_PATH = ./antlr-4.7.2-complete.jar
ANTLR = "java -jar $(ANTLR_PATH)"
GRUN = "java -cp .:$(ANTLR_PATH) org.antlr.v4.gui.TestRig"

default:
	$(ANTLR) -Dlanguage=Python3 Expr.g4

clean:
	rm -rf .antlr *.java *.interp *.tokens *.class Expr*.py 2> /dev/null
