from lexicalAnalyzer import *
import sys

filename = 'test.txt'
file = open(filename, "r")

myreader = reader(file)
k = myreader.nextToken()

while k.token.value != TokenCategory.EOF.value :
    print(k)
    k = myreader.nextToken()  
print(k)