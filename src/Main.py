from Analyzer import * #só copiei e colei
import sys

filename = sys.argv[1]
file = open(filename, "r")

myreader = reader(file)
k = myreader.nextToken()

while k.token.value != TokenCategory.EOF.value :
    print(k)
    k = myreader.nextToken()

print(k)