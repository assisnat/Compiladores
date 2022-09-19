from Tokens import *

class reader():
    def __init__(self, file):
        self.file = file
        self.column = 0
        self.line = 0
        self.actualLine = file.readline()
        print("%04d" %(self.line+1), end='  ')
        print(self.actualLine, end = '')

    def Line(self):
        return self.actualLine[self.column:]

    def nextLine(self):
        self.line += 1
        self.column = 0
        self. actualLine = self.file.readline()
        if self.actualLine == '': return
        print("%04d" %(self.line+1), end='  ')
        print(self.actualLine, end = '')
    def nextToken(self):
        k = self.findToken()
        while not k :
            k = self.findToken()
        return k

    def findToken(self):
        atomics = [' ', '{', '}', '(', ')', '[', ']', ':', '\n', ';', '+', '-', '*', '/', '%', '^', ',', '>', '<', '=','~','|']
        composites = ['>=', '<=', '==', '<>','=>','::']
        isString, isCharacter, newtoken = False, False, ''
        initialColumn = self.column
        if self.Line() == '' :
            return Token(defineTokenCategory(''), newtoken, self.line, initialColumn)
        lines = self.actualLine[self.column:]
        z = 0
        while z < len(lines) and lines[z] == ' ' :
            z += 1
        self.column += z
        initialColumn = self.column
        lines = self.actualLine[self.column:]

        for character in lines :

            if character == ' ' and not isString and not isCharacter:
                self.column += 1
                if newtoken == '' :
                    continue
                return Token(defineTokenCategory(newtoken), newtoken, self.line, initialColumn)

            elif isString and character == '"' :
                self.column += 1
                newtoken += character
                return Token(defineTokenCategory(newtoken), newtoken, self.line, initialColumn)

            elif isCharacter and character == "'" :
                self.column += 1
                newtoken += character
                return  Token(defineTokenCategory(newtoken), newtoken, self.line, initialColumn)

            elif newtoken == '"' :
                isString = True

            elif newtoken + character in composites and not isString and not isCharacter:
                self.column += 1
                newtoken += character
                return Token(defineTokenCategory(newtoken), newtoken, self.line, initialColumn)

            elif newtoken in atomics and not isString and not isCharacter:
                return Token(defineTokenCategory(newtoken), newtoken, self.line, initialColumn)

            elif character in atomics and not isString and not isCharacter:
                if newtoken != '':
                    return Token(defineTokenCategory(newtoken), newtoken, self.line, initialColumn)

            newtoken += character
            self.column += 1

        self.nextLine()