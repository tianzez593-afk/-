# 学习日志

## 2026-10-22

### 今天学了

- Git：`clone` → `add` → `commit` → `push` 的完整流程
- Python：函数、文件读写、异常处理、字典统计
- LeetCode：Two Sum（暴力 + 字典优化）、Valid Parentheses（栈）

### 今天新接触的代码

**Git**

- `git status` / `git log --oneline` / `git remote -v`
- `git rm --cached`（取消暂存）
- `.gitignore`（忽略 `__pycache__/`、`*.pyc`）

**Python 基础**

- `import random`、`random.randint(1, 100)`
- `int(input(...))`、`str(tries)`
- `while True` / `if / elif / else` / `break` / `continue`
- `try / except ValueError` / `except FileNotFoundError` / `raise`
- f-string：`f"你用了 {tries} 次"`
- `def`、默认参数、`*numbers`、`return`、`sum()`
- 局部变量 vs 全局变量

**文件**

- `with open(path, "r"/"w"/"a", encoding="utf-8") as f`
- `f.read()`、`f.write()`、`\n`
- `import os`、`os.getcwd()`、`os.path.exists()`

**字典 / 排序**

- `{}`、`counts[word]`、`word in counts`、`counts[word] += 1`
- `.items()`
- `sorted(..., key=lambda x: x[1], reverse=True)`
- 切片 `[:10]`

**LeetCode**

- 双重循环：O(n²)
- 字典记录「值 → 下标」：O(n)
- `enumerate(nums)`：同时拿下标和值
- 栈：`stack.append()` / `stack.pop()` / `stack[-1]`

### 写了什么代码

- `day01/guess_number.py`：猜数字，加了 `try/except`，输入 `abc` 不崩溃
- `day02/word_count.py`：读文件、统计词频、打印前 10、文件不存在时提示
- `leetcode/two_sum.py`：Two Sum，暴力 O(n²) + 字典 O(n) 两版
- `leetcode/valid_parentheses.py`：Valid Parentheses，用栈判断括号配对
- `leetcode/notes.md`：两题各 3 行题解（思路 / 复杂度 / 易错点）

### Git 常用命令

```bash
git clone https://github.com/tianzez593-afk/learning-log.git
git add .
git commit -m "修改的内容"
git push origin main
```

### 卡在哪

- 字典的键值读写、`lambda`、`enumerate`
- 函数没有 `return` 会得到 `None`
- 缩进和相对路径（要看清楚在哪个目录运行命令）
- 栈的 `append` / `pop` / `stack[-1]` 还需要多练

### 明天做什么

- Day 3：Git 分支与回滚（`plan/练习/day03-Git分支与回滚.md`）
- 新建分支、提交、合并、`restore`、`revert`
- LeetCode：Merge Two Sorted Lists、Best Time to Buy and Sell Stock
