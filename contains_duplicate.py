def hasDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        
        seen.add(num)

    return False

#Time O(N)
#Space O(N)