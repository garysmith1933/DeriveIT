def areAnagrams(s, t):
    letters = 'abcdefghijklmnopqrstuvwxyz'

    cs = {l:0 for l in letters}
    ct = {l:0 for l in letters}

    for char in s:
        cs[char] += 1
    

    for char in t:
        ct[char] += 1

    return cs == ct

# Time O(N + M) len of s and len of t
# Space O(1) really its 2*26 which sums up to O(1)