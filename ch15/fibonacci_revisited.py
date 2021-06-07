# 15.1 Fibonacci Sequences, Revisited
# See 6.1 for recursive implementation of Fibonacci sequence

# # Figure 15-2 from page 308
def fib_memo(n, memo = None):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if memo == None:
        memo = {}
        
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        memo[n] = result
        return result

def fib_tab(n, to_print = False):
    """Assumes n is an int >= 0
       Returns Fibonacci of n"""
    # create an array with (n+1) elements
    # only first two values matter, the remainder will be overridden
    tab = [1]*(n+1)
    if to_print:
        print(f"tab={tab}")
    
    for i in range(2, n + 1):
        tab[i] = tab[i-1] + tab[i-2]
        if to_print:
            print(f"tab={tab}")
    return tab[n]

# fib(120) = 8,670,007,398,507,948,658,051,921
def test_fib():
    print("Fibonacci using memoization method:")
    print(f"{fib_memo(120):,}")
        
    print()
        
    print("Fibonacci using tabular method:")
    print(f"{fib_tab(120):,}")
    
    print()
    
    print("Fibonacci using tabular method (debugging on):")
    print(fib_tab(10, to_print = True))

# Finger exercise on page 309
# Use tabular method to implement a dynamic programming
# solution that meets the specification
def make_change(coin_array, change, to_print = False):
    """coin_array is a list of positive ints and coin_array[0] = 1
       change is a positive int
       return the minimum number of coins needed to have a set of
          coins the values of which sum to change. Coins may be used
          more than once. 
          Examples:
              make_change([1, 5, 8], 11) --> 3 (1 + 5 + 5)
              make_change([1, 5, 10, 25], 30) --> 2 (5 + 25)
    """
    if to_print:
        print(f"coins={coin_array}")
        print(f"change={change}")
    
    min_coins_count = [0] * (change + 1)
    
    for coin in range(change + 1):
        coin_count = coin 
        
        for i in [coin_val for coin_val in coin_array if coin_val <= coin]:
            if min_coins_count[coin - i] + 1 < coin_count:
                coin_count = min_coins_count[coin - i] + 1
                
        min_coins_count[coin] = coin_count
    
    return min_coins_count[change]

# https://notebook.community/OSU-CS-325/Project_Two_Coin_Change/dynamic-programming/dynamic_programming
def make_change_table(coin_array, change, to_print = False):
    min_coins_used = list(range(change + 1))
    min_coins_count = list(range(change + 1))
    
    for coin in range(change + 1):
        coin_count = coin 
        latest_coin = 1 
        
        for i in [coin_val for coin_val in coin_array if coin_val <= coin]:
            if min_coins_count[coin - i] + 1 < coin_count:
                coin_count = min_coins_count[coin - i] + 1
                latest_coin = i 
                
        min_coins_count[coin] = coin_count
        min_coins_used[coin] = latest_coin
    
    min_count = min_coins_count[change]
    print(f"min_count={min_count}")
    
    min_used = [0] * len(coin_array)
    change_iter = change 
    while change_iter > 0:
        coin_val = min_coins_used[change_iter] 
        p = 0 
        for j in coin_array:
            if coin_val == j:
                min_used[p] += 1
                if to_print:
                    print(f"min_used={min_used}")
            p += 1
            
        change_iter = change_iter - coin_val

    print(f"min_used={min_used} (final)")
    
def test_make_change():
    coin_vals = [1, 5, 8]
    change = 11
    print(f"minimum number of coins = {make_change(coin_vals, change, True)}")
    
    print()
    
    coin_vals = [1, 5, 10, 25]
    change = 30
    print(f"minimum number of coins = {make_change(coin_vals, change, True)}")
    
    # make_change_table(coin_vals, change, True)
    
    
if __name__ == "__main__":
    test_fib()
    # test_make_change()
