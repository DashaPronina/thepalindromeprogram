def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

s = input("Введите строку: ")
print(is_palindrome(s))