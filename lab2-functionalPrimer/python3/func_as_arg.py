def listFunc(a, ):
    return [i for i in range(a, b)] #Create list of ints from 1 to 5, Haskell equivalent [1..5]

def applicatorFunc(inpFunc, a, bs):
    if s=='s':
        return sum(inpFunc(a, b))
    else:
        return sum(inpFunc(a,b))/(b - a + 1)

print(applicatorFunc(listFunc, 'a', 1, 10)) #Call applicatorFunc with inpFunc and 'a' as args