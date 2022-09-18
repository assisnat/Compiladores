from Tokens import *

class reader():
    def __init__(self, file):
        self.file = file
        self.collumn = 0
        self.line = 0
        self.actualLine = file.readline()
        print("%04d" %(self.line+1), end='  ')
        print(self.actualLine, end = '')

    def Line(self):
        return self.actualLine[self.collumn:]

    def nextLine(self):
        self.line += 1
        self.collumn = 0
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
        atomics = [' ', '{', '}', '(', ')', '[', ']', ':', '\n', ';', '+', '-', '*', '/', '%', '^', ',', '>', '<', '=', '!']
        composites = ['>=', '<=', '==', '!=', '++']
        isString,isCharacter, newtoken = False,False, ''
        inicialCollum = self.collumn
        if self.Line() == '' :
            return Token(defineTokenCategory(''), newtoken, self.line, inicialCollum)
        lines = self.actualLine[self.collumn:]
        z = 0
        while z < len(lines) and lines[z] == ' ' :
            z += 1
        self.collumn += z
        inicialCollum = self.collumn
        lines = self.actualLine[self.collumn:]

        for character in lines :

            if character == ' ' and not isString and not isCharacter:
                self.collumn += 1
                if newtoken == '' :
                    continue
                return Token(defineTokenCategory(newtoken), newtoken, self.line, inicialCollum)

            elif isString and character == '"' :
                self.collumn += 1
                newtoken += character
                return Token(defineTokenCategory(newtoken), newtoken, self.line, inicialCollum)

            elif isCharacter and character == "'" :
                self.collumn += 1
                newtoken += character
                return  Token(defineTokenCategory(newtoken), newtoken, self.line, inicialCollum)

            elif newtoken == '"' :
                isString = True

            elif newtoken + character in composites and not isString and not isCharacter:
                self.collumn += 1
                newtoken += character
                return Token(defineTokenCategory(newtoken), newtoken, self.line, inicialCollum)

            elif newtoken in atomics and not isString and not isCharacter:
                return Token(defineTokenCategory(newtoken), newtoken, self.line, inicialCollum)

            elif character in atomics and not isString and not isCharacter:
                if newtoken != '':
                    return Token(defineTokenCategory(newtoken), newtoken, self.line, inicialCollum)

            newtoken += character
            self.collumn += 1

        self.nextLine()