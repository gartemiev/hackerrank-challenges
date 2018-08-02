######## By using list comprehensions
def plusMinus(arr):
    positive = round(len([i for i in arr if i == abs(i) and i != 0])/len(arr),6)
    negative = round(len([i for i in arr if i != abs(i)])/len(arr),6)
    zero = round(len([i for i in arr if i == 0])/len(arr),6)

    print(positive)
    print(negative)
    print(zero)

######## By using counters
def plusMinus2(arr):
    positive=0
    negative=0
    zero=0
    for i in arr:
        if i == abs(i) and i != 0:
            positive +=1
        elif i != abs(i):
            negative += 1
        else:
            zero += 1

    print(round(positive / len(arr), 6))
    print(round(negative / len(arr), 6))
    print(round(zero / len(arr), 6))