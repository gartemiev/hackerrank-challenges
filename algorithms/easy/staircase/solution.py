#with the help of format
def staircase(n):
    for i in range(n):
        print('{:>{wid}}'.format('#'*(i+1), wid=n))

#with the help of rjust
def staircase1(n):
    for i in range(n):
        print(str('#'*(i+1)).rjust(n))