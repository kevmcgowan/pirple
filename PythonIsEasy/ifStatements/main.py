def check_equality(param1, param2, param3):
    if param1 == param2 or param1 == param3 or param2 == param3:
        return True
    else:
        return False

# Test cases
print(check_equality(1, 2, 3))       # Should return False
print(check_equality(1, 1, 3))       # Should return True
print(check_equality("test", 2, 2))  # Should return True
print(check_equality("a", "b", "a")) # Should return True
print(check_equality(5, 6, 7))       # Should return False
