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

def EvalTokenStack(tokenStack):
    # pp.pprint(tokenStack) if Debug else None

    # Evaluate the expression within the parentheses and replace it with the result
    if tokenStack[-1] == ")":
        matchingOpenParenIdx = len(tokenStack) - tokenStack[::-1].index("(") - 1
        parenExprVal = EvalTokenStack(tokenStack[matchingOpenParenIdx+1:-1]).pop()
        del tokenStack[matchingOpenParenIdx:]
        tokenStack.append(parenExprVal)
        return tokenStack

    # Evaluate all + operations recursively
    if "+" in tokenStack:
        opIdx = tokenStack.index("+")
        operand1 = tokenStack[opIdx-1]
        operand2 = tokenStack[opIdx+1]
        del tokenStack[opIdx-1:opIdx+2]
        tokenStack.insert(opIdx-1, operand1 + operand2)
        return EvalTokenStack(tokenStack)
    else:
        # No more additions, evaluate multiplications left-to-right
        product = 1
        for i in tokenStack:
            if i != "*":
                product *= i
        return [product]

def EvalExpr(expr):
    tokenStack = list()
    for token in expr.replace(' ', ''):
        tokenStack.append(int(token) if token.isdigit() else token)
        if token == ")":
            tokenStack = EvalTokenStack(tokenStack)
        print("Token=", token, ", Expr: ", sep='', end='') if Debug else None
        pp.pprint(tokenStack) if Debug else None

    tokenStack = EvalTokenStack(tokenStack)
    return tokenStack.pop()

Lines = ParseInput()
exprSum = 0
for expr in Lines:
    result = EvalExpr(expr)
    print(expr, "=", result) if Debug else None
    exprSum += result

print(exprSum)
