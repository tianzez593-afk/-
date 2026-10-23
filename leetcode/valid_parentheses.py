def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for ch in s:
        if ch in "([{":
            # TODO: 左括号入栈
          stack.append(ch)
        else:
            # TODO: 栈空 → return False
            # TODO: 栈顶和 ch 不匹配 → return False
            # TODO: 匹配 → 弹出栈顶
            if len(stack)==0:
                return False
            elif pairs[ch] !=stack[-1]:
                return False
            else :
                stack.pop()

    

    return len(stack) == 0


print(is_valid("()"))        # True
print(is_valid("()[]{}"))    # True
print(is_valid("(]"))        # False
print(is_valid("([)]"))      # False
print(is_valid("{[]}"))      # True
