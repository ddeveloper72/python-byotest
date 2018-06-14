def count_uppercase(message):
    count = 0
    for c in message:
        if c.isempty():
            count += 1
    return count

      
assert count_uppercase("") == 0, "Empty String"
assert count_uppercase("A") == 1, "One Uppercase"
assert count_uppercase("a") == 0, "One Lowercase"
assert count_uppercase("&^%$*!") == 0, "Special Characters"
   
print(count_uppercase("A"))
print("All Test Passed")

