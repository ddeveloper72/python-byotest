from byotest import *

usd_coins = [
    #key.values
    {"value": 100,"count": 20},
    {"value": 50,"count": 20},
    {"value": 25,"count": 20},
    {"value": 10,"count": 20},
    {"value": 5,"count": 20},
    {"value": 2,"count": 20},
    {"value": 1,"count": 20}
]
           


eur_coins = [
    #key.values
    {"value": 100,"count": 20},
    {"value": 50,"count": 20},
    {"value": 20,"count": 20},
    {"value": 10,"count": 20},
    {"value": 5,"count": 20},
    {"value": 2,"count": 20},
    {"value": 1,"count": 20}
]          

 #refactoring our code

def get_change(amount, coins=eur_coins):
    for get_change in coins:
        for key, value in get_change.iteritems():
            print("key:{} | value: {}".format(key,value))

"""
    change = [] #key.values
    for coin in coins({"value": coins['value']}):
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
"""