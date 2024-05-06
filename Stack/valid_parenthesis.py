def isValid(s):
    open2Close = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }

    stack = []

    for bracket in s:
        if bracket not in open2Close:
            stack.append(bracket)
            continue
        
        if not stack or open2Close[bracket] != stack[-1]:
            return False
        
        else:
            stack.pop()
    
    return not stack

    # Time O(N)
    # Space O(N)
    