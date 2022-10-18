from enum import Enum
from Regex import  *
class TokenCategory(Enum):
    Id, Fun,Fn, Val, TypeInt, TypeBool, TypeChar, TypeString, TypeConst, Type, List, Local, Infix, Nonfix, End, Of,\
    Bar, Arrow, OpArAd, DoubleP, OpMinus, OpArMult, OpArdiv, OpArMod, OpArExp, OpReD, OpReI, And, OpLogAndAlso, OpLogOr, OpLogNot,\
    At, Abs, Mod, Div, OpAtr, InsSIf, InsSThen, InsSElse, InsInWh, InsInCase, InsInDo, BeginP, EndP,        \
    BeginC, EndC, BeginCh, EndCh, ConstInt, ConstBool, ConstChar, ConstString, Asp, SepV,   \
    SepPV, In, SepPont, EOF, Error= list(range(59))

class Token() :
    def __init__(self, token, value, line, column):
        self.token = token
        self.value = value
        self.line = line
        self.column = column
    def __str__(self):
        return  "              [%04d, %04d] (%04d, %10s) {%s}" %(self.line+1,self.column+1, self.token.value, self.token.name, self.value)

def defineTokenCategory(type) :
    if type == 'in' : return TokenCategory.In
    if type == 'val': return TokenCategory.Val
    if type == 'int' : return  TokenCategory.TypeInt
    if type == 'bool' : return TokenCategory.TypeBool
    if type == 'char' : return  TokenCategory.TypeChar
    if type == 'string' : return TokenCategory.TypeString
    if type == 'const' : return TokenCategory.TypeConst
    if type == 'type': return TokenCategory.Type
    if type == 'list': return TokenCategory.List
    if type == 'local': return TokenCategory.Local
    if type == 'end': return TokenCategory.End
    if type == 'of': return TokenCategory.Of
    if type == 'infix': return TokenCategory.Infix
    if type == 'nonfix': return TokenCategory.Nonfix
    if type == 'fn': return TokenCategory.Fn
    if type == 'fun': return TokenCategory.Fun
    if type == '|': return TokenCategory.Bar
    if type == '+' or type == '-' : return TokenCategory.OpArAd
    if type == '~': return TokenCategory.OpMinus
    if type == '*' : return  TokenCategory.OpArMult
    if type == '/' : return TokenCategory.OpArdiv
    if type == '%' : return TokenCategory.OpArMod
    if type == '^' : return  TokenCategory.OpArExp
    if type == '=>': return TokenCategory.Arrow
    if type == '::': return TokenCategory.DoubleP
    if type == 'div': return TokenCategory.Div
    if type == 'mod': return TokenCategory.Mod
    if type == 'abs': return TokenCategory.Abs
    if type == '@': return TokenCategory.At
    if type == '>' or type == '>=' or type == '<' or type == '<=' : return  TokenCategory.OpReD
    if type == '==' or type == '<>' : return  TokenCategory.OpReI
    if type == 'andalso' : return TokenCategory.OpLogAndAlso
    if type == 'and': return TokenCategory.And
    if type == 'orelse' : return TokenCategory.OpLogOr
    if type == 'not' : return TokenCategory.OpLogNot
    if type == '=' : return TokenCategory.OpAtr
    if type == 'if' : return TokenCategory.InsSIf
    if type == 'then' : return  TokenCategory.InsSThen
    if type == 'else' : return  TokenCategory.InsSElse
    if type == 'while' : return TokenCategory.InsInWh
    if type == 'do' : return TokenCategory.InsInDo
    if type == 'case': return TokenCategory.InsInCase
    if type == '(' : return TokenCategory.BeginP
    if type == ')' : return  TokenCategory.EndP
    if type == '[' : return  TokenCategory.BeginC
    if type == ']' : return TokenCategory.EndC
    if type == '{' : return  TokenCategory.BeginCh
    if type == '}' : return  TokenCategory.EndCh
    if type == 'false' or type == 'true' : return TokenCategory.ConstBool
    if isRegex(type, digit) : return TokenCategory.ConstInt
    if isRegex(type, char) : return  TokenCategory.ConstChar
    if isRegex(type, word) : return TokenCategory.ConstString
    if isRegex(type, id) : return  TokenCategory.Id
    if type == ',' : return  TokenCategory.SepV
    if type == ';' : return TokenCategory.SepPV
    if type == ':' : return TokenCategory.SepPont
    if type == "'" : return TokenCategory.Asp
    if type == "" : return TokenCategory.EOF
    return TokenCategory.Error
