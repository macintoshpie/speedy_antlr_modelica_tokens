from antlr4 import FileStream, ParseTreeWalker

from .parser import sa_modelica, modelicaListener

class HelloPrintListener(modelicaListener.modelicaListener):
    def enterEveryRule(self, ctx):
        print(f"{type(ctx).__name__}\n  {ctx.start}, {ctx.stop}")

def print_tokens(filename, use_cpp):
    fs = FileStream(filename)
    sa_modelica.USE_CPP_IMPLEMENTATION = use_cpp
    tree = sa_modelica.parse(fs, 'stored_definition')
    printer = HelloPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
