# def f(n): # Tabulation
#     fib = {0:1, 1:1}

#     for i in range(2, n+1):
#         fib[i] = fib[i - 1] + fib[i - 2]
    
#     return fib[n]

#     # Time O(N)
#     # Space O(N) 


# def f(n): # Tabulation+

#     prevfib = 1
#     currfib = 1

#     for i in range(2, n+1):
#         temp = currfib
#         currfib = currfib + prevfib
#         prevfib = temp
        
#     return currfib

#     # Time (N)
#     # Space O(1)


memo = {0: 1, 1:1}

def f(n): # memoization

    if n in memo:
        return memo[n]

    else:
        answer = f(n - 1) + f(n - 2)
        memo[n] = answer
        
        return answer

    # Time O(N)
    # Space O(N)
