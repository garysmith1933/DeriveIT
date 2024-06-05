def hasOverlap(intervals):
    # sort it
    intervals.sort(key=lambda i: i[0])

    i, j = 0, 1

    while j < len(intervals):
        interval1 = intervals[i]
        interval2 = intervals[j]

        if overlapping(interval1, interval2): return True

        j += 1
        i += 1
    
    return False
    

def overlapping(interval1, interval2):
    # check for overlap
    return interval1[1] > interval2[0]


# Time O(n log n) # have to sort intervals 
# O(1)