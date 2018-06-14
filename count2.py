def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
      
assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One Uppercase"
assert count_upper_case("a") == 0, "One Lowercase"
assert count_upper_case("&^%$*!") == 0, "Special Characters"
   
print(count_upper_case("A"))
print("All Test Passed")