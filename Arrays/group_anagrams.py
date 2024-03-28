def groupAnagrams(strs):
    # count are keys, values are words
    groups = {}

    for word in strs:
        letters = [0] * 26
        for char in word:
            letter = ord(char) - ord('a')
            letters[letter] += 1

        
        group = tuple(letters)
        
        if group not in groups:
            groups[group] = []
        groups[group].append(word)

    return groups.values()
    #Time O(N + M) - size of array, average length of each string
    # Space O(N + M) - returns n strings, with m average size.