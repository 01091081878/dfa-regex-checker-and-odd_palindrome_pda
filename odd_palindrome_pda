def is_odd_palindrome_pda(string):
    if len(string) % 2 == 0:
        return False

    stack = []
    mid = len(string) // 2
    for i in range(mid):
        stack.append(string[i])

    for i in range(mid + 1, len(string)):
        if string[i] != stack.pop():
            return False

    return True

print(is_odd_palindrome_pda("abcba"))
print(is_odd_palindrome_pda("racecar"))
print(is_odd_palindrome_pda("abcdcba"))
print(is_odd_palindrome_pda("abccba"))
print(is_odd_palindrome_pda("a"))
print(is_odd_palindrome_pda(""))
