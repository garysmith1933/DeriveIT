def longestNoDupeLength(s):
    window = set()
    max_len = 0
    i = 0

    for j in range(len(s)):
       
        while s[j] in window:
            window.remove(s[i])
            i += 1
        
        window.add(s[j])
    
        max_len = max(max_len, len(window))

    return max_len
    
    # Time O(N)
    # O(1) - worse case is a string with every letter, which is O(26)