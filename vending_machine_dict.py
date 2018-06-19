from byotest import *

usd_coins = {
    #key.values
    "value1": 100,
    "value2": 50,
    "value3": 25,
    "value4": 10,
    "value5": 5,
    "value6": 2,
    "value7": 1
}

eur_coins = {
    #key.values
    "value1": 100,
    "value2": 50,
    "value": 20,
    "value3": 10,
    "value4": 5,
    "value5": 2,
    "value6": 1
} #refactoring our code



def get_change(amount, coins=eur_coins):

    change = [] #key.values
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
