def computerCanWriteString(p, strings):
    n = len(p)
    isWritable = [True]*(n + 1) 

    for i in range(n-1,-1,-1): # i = n-1...0

        idxs = []
        for s in strings:
            if p[i:i+len(s)] == s:
                idxs.append(i+len(s))
        
        isWritable[i] = any(isWritable[idx] for idx in idxs)

    return isWritable[0]