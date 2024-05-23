def slidingWindowSum(arr, k):
    i, j = 0, k - 1

    res = []

    while j < len(arr):
        window = arr[i:j + 1]
        res.append(sum(window))
        i += 1
        j += 1
    

    return res