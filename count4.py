"""
The function can no be refactored to make it more Pythonic.  The numbered
lines below are what have been removed. After each removal of the code,
we check to see the code stil runs and returns the correct result.
"""

# This helper function repaces the two individual checks below
# to see if a number is even.  The removed code is labled 2).
def is_even(number):
    return number % 2 == 0


def even_number_of_evens(numbers):
    
    # step 1 checs to see if there is a number and returns false for no number
    # 1) if numbers == []:
    # 1)   return False
    
    # step 2 checks if there is an even number, but returns false 
    # because we want more than one even number.
    # 1) else:
   
    evens = 0
    
    # step 2 does a count to see if there are 2 even numbers    
    for n in numbers:
        # 2) if n % 2 == 0:
        if is_even(n):
            evens += 1
            
    # step 4 checks to see if the even number when divided by itself is 0,
    # that the this number answer is forced to false.  This way any other odd 
    # number can be evaluated a false as well.
    if evens == 0:
        return False
    else:
        # 2) return evens % 2 == 0
        return is_even(evens)
        
    """
    Lines 23 to 38 can be further reduced:
    evens = sum([1 for n in numbers if is_even(n)])
    return False if evens == 0 else is_even(evens)
    """
    
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([8]) == False, "One Even Numbers"
assert even_number_of_evens([2, 8]) == True, "Two Even Numbers"
assert even_number_of_evens([1, 3, 9]) == False, "Three odd Numbers"


print("All tests passed!")