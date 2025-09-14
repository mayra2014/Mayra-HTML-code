def is_palindrome(string):
    lef_pos = 0
    right_pos = len(string) - 1

    while right_pos >= lef_pos:
        if not string[lef_pos] == string[right_pos]:
            return False
        lef_pos += 1
        right_pos -= 1
    return True
print(is_palindrome("madam"))
print(is_palindrome("nurses run"))

            