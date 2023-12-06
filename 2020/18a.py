#!/usr/bin/env python3
def ParseInput(postProcess=lambda x:x):
    global Input, InputFromFile
    lines = []

    if InputFromFile:
        fin = open(Input)
        lines = [ line.strip('\n') for line in fin.readlines() ]
        fin.close()
    else:
        lines = Input.strip('\n').split('\n')

    return list(map(postProcess, lines))
import pprint
pp = pprint.PrettyPrinter(indent=2, width=120)

def IsNum(token):
    return type(token) == int
def IsOp(token):
    return (token == "+") or (token == "*")

Lines = ParseInput()

def EvalExpr(expr):
    tokenStack = list()
    for token in expr.replace(' ', ''):
        tokenStack.append(int(token) if token.isdigit() else token)
        EvalTokenStack(tokenStack)
        print("Token=", token, ", Expr: ", sep='', end='') if Debug else None
        pp.pprint(tokenStack) if Debug else None
    return tokenStack.pop()

def EvalTokenStack(tokenStack):
    if tokenStack[-1] == ")":
        tokenStack.pop(-3)  # Remove the opening parens
        tokenStack.pop(-1)  # Remove the closing parens
    elif (len(tokenStack) >= 3) and IsNum(tokenStack[-1]) and IsOp(tokenStack[-2]) and IsNum(tokenStack[-3]):
        operand2 = tokenStack.pop(-1)
        operator = tokenStack.pop(-1)
        operand1 = tokenStack.pop(-1)

        if operator == "+":
            tokenStack.append(operand1 + operand2)
        elif operator == "*":
            tokenStack.append(operand1 * operand2)
    else:
        return

    EvalTokenStack(tokenStack)

exprSum = 0
for expr in Lines:
    result = EvalExpr(expr)
    print(expr, "=", result) if Debug else None
    exprSum += result

print(exprSum)
