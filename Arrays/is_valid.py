def isValid(s):
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        
        l += 1
        r -= 1
    
    return True

# Time O(N)
# Space O(1)