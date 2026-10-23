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

## 2026-10-23

### 今天任务

- [x] 不看答案，自己重写 Valid Parentheses
- [x] Day 3：Git 分支与回滚
- [x] 写 `git-notes.md`

### 卡点记录（边做边记）

> 格式：想做什么 → 现象/报错 → 试过什么 → 怎么解决的。

1. 不知道「入栈」是什么意思
   → 搞清了 `append`（入栈）/ `pop`（出栈）/ `stack[-1]`（看栈顶）
2. 右括号比较对象写错：用了 `ch != stack[-1]`
   → 应该用 `pairs[ch] != stack[-1]`
3. 匹配成功后写了 `return stack[-1]`
   → 应该用 `stack.pop()`，继续循环而不是结束函数
4. `key=lambda x: x[1]` 不懂
   → `key` 是排序依据，`x[1]` 表示按次数排
5. `main()` 和 `if __name__ == "__main__"` 不懂
   → 意思是「只有直接运行这个文件时才执行 main()」
6. 切回 `main` 后，分支上的文件不见了
   → 文件还在 `practice-git` 的提交里，切回分支就能看到
7. 不理解 merge 的方向
   → 在哪个分支上执行，就是把别的分支合进「当前分支」
8. `revert` 和 `reset` 分不清
   → `revert` 新增提交抵消旧提交（安全）；`reset` 移动指针、改写历史（危险）
9. `add` 和 `commit` 的区别
   → `add` 放进暂存区，`commit` 才真正存档

### 今天学了

- 栈：`append` / `pop` / `stack[-1]`
- `sorted` 的 `key` 参数和 `lambda`
- `main()` 与 `if __name__ == "__main__"`
- Git 分支：`switch -c` / `merge`（Fast-forward）
- `git restore`：撤销未提交的修改
- `git revert`：新增提交，抵消已提交的修改

### 写了什么代码

- `leetcode/valid_parentheses.py`：不看答案自己重写，5 个测试通过
- `day03/branch_practice.txt`：分支练习文件
- `git-notes.md`：4 个 Git 问题的回答

### 明天做什么

- Day 4：复盘 + 重写
- 选猜数字或单词统计，从零重写一遍
- 读 `E:\LMS` 的一个 URL → views 调用链（如果环境在）
- 填 `plan/08-能力自评与复盘.md` 的第一次自评
