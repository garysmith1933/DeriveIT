# def slidingWindowSum(arr, k):
#     i, j = 0, k - 1

#     res = []

#     while j < len(arr):
#         window = arr[i:j + 1]
#         res.append(sum(window))
#         i += 1
#         j += 1
    

#     return res

def slidingWindowSum(arr, k):

    curr_sum = sum(arr[:k])
    res = [curr_sum]
    
    for i in range(len(arr) - k):
        curr_sum -= arr[i] # removes first number from current window
        curr_sum += arr[i + k] #adds next number to current window

        res.append(curr_sum)
    
    return res

    #Time O(N)
    # Space O(n - k)