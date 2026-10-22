# LeetCode 题解

## 1. Two Sum

- 思路：暴力版用两层循环枚举所有两数组合；优化版用字典记录「已见过的值 → 下标」，对每个数查 `target - num` 是否出现过。
- 复杂度：暴力 O(n²) 时间 / O(1) 空间；字典 O(n) 时间 / O(n) 空间。
- 易错点：内层从 `i + 1` 开始，避免重复和重复使用同一个元素；返回的是下标，不是数值。

```python
# 优化版关键代码
need = target - num
if need in seen:
    return [seen[need], i]
seen[num] = i
```

## 20. Valid Parentheses

- 思路：用栈。左括号入栈；遇到右括号时检查栈顶是否为对应的左括号，匹配则弹出，不匹配或栈空则返回 `False`；最后栈为空才算合法。
- 复杂度：O(n) 时间 / O(n) 空间。
- 易错点：右括号出现时栈可能为空；最后必须检查栈是否为空（例如 `"("` 不合法）。

```python
# 关键代码
if ch in "([{":
    stack.append(ch)
elif not stack or stack[-1] != pairs[ch]:
    return False
else:
    stack.pop()
```
