def staircase(n):
    asterString = ""
    alignFormula = '{:>' + str(n) + '}'
    for i in range(n):
        asterString = asterString + '#'
        print(alignFormula.format(asterString))