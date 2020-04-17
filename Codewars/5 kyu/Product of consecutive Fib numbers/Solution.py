def productFib(prod):
    fib = [0, 1]
    curr = 0
    mult = []
    tot = 0
    flag = None
    
    while tot < prod:
        curr = fib[-1] + fib[-2]
        fib.append(curr)
        tot = fib[-1] * fib[-2]
        mult.append(tot)

    if prod == 0:
        flag = True
    elif len(mult) == 0:
        flag = False
    elif mult[-1] == prod:
        flag = True
    else:
        flag = False

    return [fib[-2], fib[-1], flag]
