def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


print(is_valid("()"))        # True
print(is_valid("()[]{}"))    # True
print(is_valid("(]"))        # False
print(is_valid("([)]"))      # False
print(is_valid("{[]}"))      # True
