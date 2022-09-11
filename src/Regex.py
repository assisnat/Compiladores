import re

digit = re.compile("\d+")
char = re.compile("'\w'", re.ASCII)
word = re.compile("\".*\"", re.ASCII)
id = re.compile("[_a-z][_a-zA-Z\d]*")

def isRegex(num, regex) :
    i = regex.match(num)
    if i == None : return False
    return i.group() == num
