from byotest import *

usd_coins = {
            #key.value
    "One_Dollar": 100,
    "Fifty_cent": 50,
    "Quater": 25,
    "Ten_cent": 10,
    "Five_cent": 5,
    "Two_cent": 2,
    "One_cent": 1
}

eur_coins = {
          #key.value
    "One_Euro": 100,
    "Fifty_cent": 50,
    "Tewnty_cent": 20,
    "Ten_cent": 10,
    "Five_cent": 5,
    "Two_cent": 2,
    "One_cent": 1
} #refactoring our code



def get_change(amount, coins=eur_coins):
    
    """
    refactoring our code
    if amount == 0:
        return []

    if amount in coins:
        return [amount]
    """
    change = []  #key.value
    for coin in coins.values():
        while coin <= amount:
            amount -= coin
            change.append(coin)

    return change

test_are_equal(get_change(0),[])
test_are_equal(get_change(1),[1])
test_are_equal(get_change(2),[2])
test_are_equal(get_change(5),[5])
test_are_equal(get_change(10),[10])
test_are_equal(get_change(20),[20])
test_are_equal(get_change(50),[50])
test_are_equal(get_change(100),[100])
test_are_equal(get_change(3),[2,1])
test_are_equal(get_change(7),[5,2])
test_are_equal(get_change(9), [5,2,2])
test_are_equal(get_change(35, usd_coins), [25,10])


print("All tests pass!")
