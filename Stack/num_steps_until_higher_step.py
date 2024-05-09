def numStepsUntilHigherStep(height):
    stack = []

    res = [float('inf')] * len(height)

    # iterate over height
    # while the current number is greater than the last number in the stack
    # pop the last number
    # calculate the days it has it been, and set that to the corresponding index in the result

    # when done add the current number to the stack,

    for i in range(len(height)):
        step = height[i]

        if stack:
            while stack and step > stack[-1][0]:
                val, idx = stack.pop()
                res[idx] = i - idx
    
        stack.append((step, i))
    
    return res

    # Time O(N)
    # Space O(N)