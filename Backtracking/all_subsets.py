def generateSubsets(nums):
    res, subset, idx = [], [], 0

    def genSub():
        nonlocal res, subset, idx
    
        if idx == len(nums):
            res.append(subset.copy())
            return

        # dont add number
        idx += 1
        genSub()
        idx -= 1

        # add number
        subset.append(nums[idx])
        idx += 1
        genSub()

        # reset after adding number
        idx -= 1
        subset.pop()
        
    genSub()
    return res