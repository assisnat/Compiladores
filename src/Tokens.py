from enum import Enum
from Regex import  *
class TokenCategory(Enum):
    Id, Fun, Val, TypeInt, TypeBool, TypeChar, TypeString, TypeConst, Type, Local, \
    OpArAd, OpArMult, OpArdiv, OpArMod, OpArExp, OpReD, OpReI, OpLogAnd, OpLogOr, OpLogNot,\
    OpConcac, OpAtr, InsSIf, InsSThen, InsSElse, InsInWh, InsInDo, BeginP, EndP,        \
    BeginC, EndC, BeginCh, EndCh, ConstInt, ConstBool, ConstChar, ConstString, SepV,   \
    SepPV, IntTo, IntRate, Out, In, SepPont, EOF = list(range(43))

class Token() :
    def __init__(self, token, value, line, column):
        self.token = token
        self.value = value
        self.line = line
        self.column = column
    def __str__(self):
        return  "              [%04d, %04d] (%04d, %10s) {%s}" %(self.line+1,self.column+1, self.token.value, self.token.name, self.value)



def defineTokenCategory(type) :
    if type == 'output' : return TokenCategory.Out
    if type == 'input' : return TokenCategory.In
    if type == 'int' : return  TokenCategory.TypeInt
    if type == 'bool' : return TokenCategory.TypeBool
    if type == 'char' : return  TokenCategory.TypeChar
    if type == 'String' : return TokenCategory.TypeString
    if type == 'const' : return TokenCategory.TypeConst
    if type == 'type': return TokenCategory.Type
    if type == 'local': return TokenCategory.Local
    if type == '+' or type == '-' : return TokenCategory.OpArAd
    if type == '*' : return  TokenCategory.OpArMult
    if type == '/' : return TokenCategory.OpArdiv
    if type == '%' : return TokenCategory.OpArMod
    if type == '^' : return  TokenCategory.OpArExp
    if type == '>' or type == '>=' or type == '<' or type == '<=' : return  TokenCategory.OpReD
    if type == '==' or type == '<>' : return  TokenCategory.OpReI
    if type == 'andalso' : return TokenCategory.OpLogAnd
    if type == 'orelse' : return TokenCategory.OpLogOr
    if type == 'not' : return TokenCategory.OpLogNot
    if type == '++' : return TokenCategory.OpConcac
    if type == '=' : return TokenCategory.OpAtr
    if type == 'if' : return TokenCategory.InsSIf
    if type == 'then' : return  TokenCategory.InsSThen
    if type == 'else' : return  TokenCategory.InsSElse
    if type == 'while' : return TokenCategory.InsInWh
    if type == 'do' : return TokenCategory.InsInDo
    if type == '(' : return TokenCategory.BeginP
    if type == ')' : return  TokenCategory.EndP
    if type == '[' : return  TokenCategory.BeginC
    if type == ']' : return TokenCategory.EndC
    if type == '{' : return  TokenCategory.BeginCh
    if type == '}' : return  TokenCategory.EndCh
    if type == 'false' or type == 'true' : return TokenCategory.ConstBool
    if type == 'to' : return TokenCategory.IntTo
    if type == 'rate' : return TokenCategory.IntRate
    if isRegex(type, digit) : return TokenCategory.ConstInt
    if isRegex(type, char) : return  TokenCategory.ConstChar
    if isRegex(type, word) : return TokenCategory.ConstString
    if isRegex(type, id) : return  TokenCategory.Id
    if type == ',' : return  TokenCategory.SepV
    if type == ';' : return TokenCategory.SepPV
    if type == ':' : return TokenCategory.SepPont
    if type == "" : return TokenCategory.EOF
    return None
