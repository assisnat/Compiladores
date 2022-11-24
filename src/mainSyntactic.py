from syntacticAnalyzer import *
import sys

filename = 'test.txt'
file = open(filename, "r")

analyzer = SlrParse(file)
analyzer.analyze()