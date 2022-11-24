from lexicalAnalyzer import *
import sys

class SlrParse():
    def __init__(self, filename):
        self.table = self.getTable()
        self.actions = self.getActions()
        self.stack = [0]
        self.myreader = reader(filename)

    def getTable(self):
        op = open("SLR.csv", 'r').read()
        op = op.split('\n')
        op = op[2:]
        t = []
        for i in op:
            o = i.split(",")
            t.append(o[1:])
        table = {}
        k = t.pop(0)
        for i in k:
            table[i] = []
        for i in t:
            for j in k:
                table[j].append(i.pop(0))
        return table

    def getActions(self):
        op = open("Actions.txt", 'r').read()
        op = op.split('\n')
        t = []
        for i in op:
            i = i.split()
            if i:
                t.append(i)
        return  t

    def analyze(self):
         tk = self.myreader.nextToken()
         token = tk.token.name.lower()
         while True:
             if len(self.stack) > 2 and self.stack[1] == 'INICIAL':break
             if token == "Error":
                print(f"Erro léxico! linha {tk.line} coluna {tk.column}")
                break
             if  token == "EOF": token = "$"
             action = self.table[token][self.stack[-1]] #pega acao na tabela
             print(action)
             if(action[0] == "s"):
                 self.stack.append(token) #empilha token
                 self.stack.append(int(action[1:])) #empilha valor
                 print(tk)
                 tk = self.myreader.nextToken()
                 token = tk.token.name
                 
             elif(action[0] == "r"):
                 #print("          " + str(self.actions[ int(action[1:]) ]))  # imprimir producao
                 n = 2 * (len(self.actions[ int(action[1:]) ])-1) #num de simbolos no lado direito da producao
                 print("          ", end="")
                 print(self.actions[ int(action[1:]) ][0] + " = ", end = '')
                 for i in self.actions[ int(action[1:]) ][1:] :
                     print(i, end = ' ')
                 print("")
                 for i in range(n):
                     self.stack.pop(-1)  #desempilha as producoes que serao reduzidas
                 y = self.stack[-1] #novo topo -> numero empilhado anteriormente
                 x = self.actions[ int(action[1:]) ][0] #simbolo do lado esquerdo da producao reduzida
                 self.stack.append( x ) #empilha o simbolo do lado esquerdo da producao
                 self.stack.append( int(self.table[x][y]) ) #empilha o valor da transicao
                 
             else:
                 print("ERRO")
        #print("              " + str(token))  # listando tokens