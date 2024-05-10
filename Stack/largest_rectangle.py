def biggestTreasureChest(arr):
    stack = []
    maxArea = 0 

    for i in range(len(arr)):
        leftmostIdx = i

        while stack and stack[-1][1] >= arr[i]:
            j,h = stack.pop()
            leftmostIdx = j
            area = (i - j) * h
            print(i, area, leftmostIdx)
            maxArea = max(maxArea, area)

        
        stack.append((leftmostIdx, arr[i]))

    
    for j, h in stack:
        area = (len(arr) - j) * h
        maxArea = max(maxArea, area)
    

    return maxArea


    # Time O(N)
    # Space O(N)
