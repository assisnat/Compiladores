from syntacticAnalyzer import *
import sys

filename = sys.argv[1]
file = open(filename, "r")

analyzer = SlrParse(file)
analyzer.analyze()