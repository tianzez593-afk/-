# LeetCode 刷题指南

> 对应图片里的「面试 LC easy / medium」「learning curve」。
> 目标：2027 年 3 月前累计 100 题左右：60 easy + 40 medium。

---

## 先记住这几件事

1. **按题型刷，不按题号刷。** 同一类题连做 5–8 道，才能形成套路。
2. **一道题最多想 20 分钟**，想不出来就看题解。
3. **看完题解必须关掉重写**，否则等于没做。
4. **错题隔天重做，7 天后再做一次。**
5. **写题解**：思路、复杂度、易错点，各 1 行。

---

## 一、刷题的正确流程

```text
读题（2 分钟）
  → 想思路（10 分钟）
    → 有思路：写代码（10–20 分钟）→ 测试 → 记录
    → 没思路：看题解（10 分钟）→ 关掉 → 重写 → 记录
  → 第二天重做
  → 第七天再重做
```

### 不要做的事

- 不要一边看题解一边抄
- 不要只追求数量，不复习
- 不要随机刷题
- 不要一开始就刷 hard

---

## 二、题型顺序

| 顺序 | 题型 | 为什么先学 |
| --- | --- | --- |
| 1 | 数组 / 字符串 / 哈希 | 最基础，面试必考 |
| 2 | 双指针 | 套路固定，容易建立信心 |
| 3 | 滑动窗口 | 高频，模板清晰 |
| 4 | 栈 / 队列 | 结构简单，常与其他题结合 |
| 5 | 链表 | 指针操作，面试常手写 |
| 6 | 二分查找 | 边界容易错，需要专门练 |
| 7 | 二叉树 | 递归入门，高频 |
| 8 | 堆 / Top K | 套路固定 |
| 9 | 图 / BFS / DFS | 网格题、遍历题 |
| 10 | 动态规划 | 最难，放后面 |
| 11 | 回溯 | 模板固定，练熟即可 |
| 12 | 贪心 / 区间 | 了解常见套路 |

---

## 三、题单（约 55 题）

### 1. 数组 / 字符串 / 哈希（8 题）

| 题号 | 题目 | 难度 |
| --- | --- | --- |
| 1 | Two Sum | easy |
| 217 | Contains Duplicate | easy |
| 242 | Valid Anagram | easy |
| 49 | Group Anagrams | medium |
| 347 | Top K Frequent Elements | medium |
| 128 | Longest Consecutive Sequence | medium |
| 238 | Product of Array Except Self | medium |
| 36 | Valid Sudoku | medium |

### 2. 双指针（5 题）

| 题号 | 题目 | 难度 |
| --- | --- | --- |
| 125 | Valid Palindrome | easy |
| 167 | Two Sum II | medium |
| 15 | 3Sum | medium |
| 11 | Container With Most Water | medium |
| 283 | Move Zeroes | easy |

### 3. 滑动窗口（4 题）

| 题号 | 题目 | 难度 |
| --- | --- | --- |
| 121 | Best Time to Buy and Sell Stock | easy |
| 3 | Longest Substring Without Repeating Characters | medium |
| 424 | Longest Repeating Character Replacement | medium |
| 567 | Permutation in String | medium |

### 4. 栈（4 题）

| 题号 | 题目 | 难度 |
| --- | --- | --- |
| 20 | Valid Parentheses | easy |
| 155 | Min Stack | medium |
| 150 | Evaluate Reverse Polish Notation | medium |
| 739 | Daily Temperatures | medium |

### 5. 链表（5 题）

| 题号 | 题目 | 难度 |
| --- | --- | --- |
| 206 | Reverse Linked List | easy |
| 21 | Merge Two Sorted Lists | easy |
| 141 | Linked List Cycle | easy |
| 19 | Remove Nth Node From End of List | medium |
| 143 | Reorder List | medium |

### 6. 二分查找（4 题）

| 题号 | 题目 | 难度 |
| --- | --- | --- |
| 704 | Binary Search | easy |
| 35 | Search Insert Position | easy |
| 33 | Search in Rotated Sorted Array | medium |
| 153 | Find Minimum in Rotated Sorted Array | medium |

### 7. 二叉树（7 题）

| 题号 | 题目 | 难度 |
| --- | --- | --- |
| 104 | Maximum Depth of Binary Tree | easy |
| 226 | Invert Binary Tree | easy |
| 100 | Same Tree | easy |
| 110 | Balanced Binary Tree | easy |
| 543 | Diameter of Binary Tree | easy |
| 102 | Binary Tree Level Order Traversal | medium |
| 98 | Validate Binary Search Tree | medium |

### 8. 堆 / Top K（2 题）

| 题号 | 题目 | 难度 |
| --- | --- | --- |
| 215 | Kth Largest Element in an Array | medium |
| 347 | Top K Frequent Elements | medium |

### 9. 图 / BFS / DFS（3 题）

| 题号 | 题目 | 难度 |
| --- | --- | --- |
| 200 | Number of Islands | medium |
| 133 | Clone Graph | medium |
| 207 | Course Schedule | medium |

### 10. 动态规划（5 题）

| 题号 | 题目 | 难度 |
| --- | --- | --- |
| 70 | Climbing Stairs | easy |
| 198 | House Robber | medium |
| 300 | Longest Increasing Subsequence | medium |
| 322 | Coin Change | medium |
| 139 | Word Break | medium |

### 11. 回溯（3 题）

| 题号 | 题目 | 难度 |
| --- | --- | --- |
| 78 | Subsets | medium |
| 39 | Combination Sum | medium |
| 46 | Permutations | medium |

### 12. 区间 / 贪心（3 题）

| 题号 | 题目 | 难度 |
| --- | --- | --- |
| 56 | Merge Intervals | medium |
| 57 | Insert Interval | medium |
| 55 | Jump Game | medium |

---

## 四、Python 常用模板

> 模板是拐杖，先理解再用。不要背模板去套所有题。

### 1. 双指针

```python
def two_pointers(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        # 根据条件移动 left 或 right
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return []
```

### 2. 滑动窗口

```python
def sliding_window(s):
    left = 0
    window = {}
    best = 0

    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1

        while not valid(window):
            window[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best
```

### 3. 哈希表

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []
```

### 4. 栈

```python
def is_valid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack
```

### 5. 二叉树递归

```python
def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

### 6. BFS

```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()
        for nxt in neighbors(node):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
```

### 7. 二分查找

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 8. 动态规划

```python
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
```

---

## 五、题解模板

```markdown
## 1. Two Sum

- 难度：easy
- 题型：哈希表
- 思路：遍历数组，用字典记录「值 → 下标」，对每个数查 target - num 是否出现过。
- 时间复杂度：O(n)
- 空间复杂度：O(n)
- 易错点：要先查再存，避免同一个元素用两次。
- 关键代码：
```python
seen = {}
for i, num in enumerate(nums):
    if target - num in seen:
        return [seen[target - num], i]
    seen[num] = i
```
```

---

## 六、复习计划

| 时间 | 做什么 |
| --- | --- |
| 当天 | 做完记录题解 |
| 第二天 | 重做一遍，不看题解 |
| 第 7 天 | 再重做一遍 |
| 第 30 天 | 挑错题抽查 |

### 错题标记

```text
[ ] 第一次独立做出
[ ] 第二次独立做出
[ ] 第三次独立做出
```

三次都独立做出，才算掌握。

---

## 七、常见错误

| 错误 | 后果 | 改法 |
| --- | --- | --- |
| 没看清题目就写 | 白写 | 先用自己的话复述题目 |
| 边界没考虑 | 空数组、单元素、重复元素出错 | 写完先测边界 |
| 死循环 | 提交超时 | 检查指针移动 |
| 复杂度太高 | 超时 | 先想暴力，再优化 |
| 只看不写 | 眼会手不会 | 关掉题解重写 |
| 只刷不复习 | 做了就忘 | 隔天、7 天重做 |

---

## 八、自检

- [ ] 能不能说出「哈希表」适合解决什么问题？
- [ ] 双指针什么时候用？
- [ ] 滑动窗口的 `left` 什么时候移动？
- [ ] 递归终止条件怎么写？
- [ ] BFS 和 DFS 的区别？
- [ ] 动态规划的状态和转移怎么找？
- [ ] 能不能在 20 分钟内独立写出 Two Sum？
