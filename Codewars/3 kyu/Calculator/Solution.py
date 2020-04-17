class Calculator(object):
    def calculate(self, operation, firstnum, secondnum):
        if '*' in operation: return float(firstnum) * float(secondnum)
        if '/' in operation: return float(firstnum) / float(secondnum)
        if '+' in operation: return float(firstnum) + float(secondnum)
        if '-' in operation: return float(firstnum) - float(secondnum)

    def evaluate(self, query):
        query = query.split(' ')
        operators = ['/', '*', '-', '+']
        for operator in operators:
            while operator in query:
                pos = query.index(operator)
                firstnum = query[pos - 1]
                secondnum = query[pos + 1]
                query[pos - 1] = Calculator().calculate(operator, firstnum, secondnum)
                del query[pos]
                del query[pos]
        return float(query[0])
