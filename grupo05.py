def obtener_nivel_precedencia(op):
    if "**" in op:
        i = op.index('*')
        if i-1 < 0 or i+2 >= len(op):
            return 0
        if op[i-1].isnumeric() and op[i+2].isnumeric():
            return 3
        else:
            return 0
    elif '*' in op:
        i = op.index('*')
        if i-1 < 0 or i+1 >= len(op):
            return 0
        if op[i-1].isnumeric() and op[i+1].isnumeric():
            return 2
        else:
            return 0
    elif '/' in op:
        i = op.index('/')
        if i-1 < 0 or i+1 >= len(op):
            return 0
        if op[i - 1].isnumeric() and op[i + 1].isnumeric():
            return 2
        else:
            return 0
    elif '+' in op:
        i = op.index('+')
        if i-1 < 0 or i+1 >= len(op):
            return 0
        if op[i - 1].isnumeric() and op[i + 1].isnumeric():
            return 2
        else:
            return 0
    elif '-' in op:
        i = op.index('-')
        if i-1 < 0 or i+1 >= len(op):
            return 0
        if op[i - 1].isnumeric() and op[i + 1].isnumeric():
            return 2
        else:
            return 0
    else:
        return 0


def calculator(input_operation):
    input_operation = input_operation.replace(" ", "")
    if input_operation[0] == '(' and input_operation[-1] == ')':
        input_operation = input_operation.removeprefix('(')
        input_operation = input_operation.removesuffix(')')
    parentesis = 0
    parentesis1 = False
    op = ""
    subOp = []
    cont = 0
    for c in input_operation:
        if c == '(':
            parentesis += 1
            parentesis1 = True
            if op != "":
                subOp.append(op)
                op = ""
        elif not parentesis1:
            op = op + c
        if c == ')':
            parentesis -= 1
        if parentesis > 0:
            op = op + c
        elif parentesis1:
            op = op + ')'
            subOp.append(op)
            op = ""
            parentesis1 = False
        if cont == len(input_operation) - 1:
            subOp.append(op)
        cont += 1

    cont = 0
    for op in subOp:
        if not op.__contains__('('):
            subOp.remove(op)
        cont += 1

    mayorPrecedencia = ""
    cont = 0
    for op in subOp:
        if cont == 0:
            mayorPrecedencia = subOp[cont]
        else:
            if obtener_nivel_precedencia(subOp[cont]) > obtener_nivel_precedencia(mayorPrecedencia):
                mayorPrecedencia = subOp[cont]
        cont += 1

    while not mayorPrecedencia[0].isnumeric():
        mayorPrecedencia = mayorPrecedencia.removeprefix(mayorPrecedencia[0])

    while not mayorPrecedencia[-1].isnumeric():
        mayorPrecedencia = mayorPrecedencia.removesuffix(mayorPrecedencia[-1])

    return (eval(input_operation), mayorPrecedencia)


