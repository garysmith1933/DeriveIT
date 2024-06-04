def threeSumSmaller(arr, target):

    largest = float('-inf')

    arr.sort()

    for i in range(len(arr)):
        j, k  = i + 1, len(arr) - 1

        while j < k:
            a = arr[i]
            b = arr[j]
            c = arr[k]

            window = a + b + c

            if window < target:
                largest = max(largest,window)
                j += 1
            
            else: # window is greater
                k -= 1
            
    return largest

# Time O(N*2)
# Space O(1)