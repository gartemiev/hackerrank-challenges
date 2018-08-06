def miniMaxSum(arr):
    arrsum = sum(arr)
    res = [arrsum - i for i in arr]
    print(min(res), max(res))