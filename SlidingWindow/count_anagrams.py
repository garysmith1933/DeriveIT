def numberOfAnagrams(s, t):
    tCount = {}
    for l in t:
        tCount[l] = tCount.get(l, 0) + 1


    window = {}
    for i in range(len(t)):
        window[s[i]] = window.get(s[i], 0) + 1


    answer = 1 if window == tCount else 0


    for i in range(len(s) - len(t)):
        oldLetter = s[i]
        newLetter = s[i + len(t)]
        window[oldLetter] = window.get(oldLetter, 0) - 1
        window[newLetter] = window.get(newLetter, 0) + 1

        if window[oldLetter] == 0: 
            del window[oldLetter]
        
        if window == tCount:
            answer += 1
    
    return answer

#Time O(N)
#Space O(1) - hashmap only stores letters which is O(26)