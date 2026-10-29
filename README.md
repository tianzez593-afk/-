# 学习日志

## 2026-10-22

> 今日投入：未记录（当天分多段学习）

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

> 今日投入：未记录（按提交时间约 90 分钟）

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

## 2026-10-24

> 今日投入：未记录

### 今天任务

- [x] 不看答案，从零重写单词统计
- [x] 读 `E:\LMS` 的 `/student/` 调用链
- [x] 填第一次能力自评

### 卡点记录（边做边记）

1. 变量太多、名字太像，脑子绕不过来
   → 把 `content` 改成 `path`、`count` 改成 `counts`、`i/h` 改成 `word/n`
2. `count[word] in count` 报 `KeyError`
   → 应该先判断 `word in counts`，再取值
3. 字典没有 `.sorted()` 方法
   → 用内置 `sorted(counts.items(), key=lambda x: x[1], reverse=True)`
4. `main()` 里没有真正读文件和统计
   → 按 `path → read_text → count_words → top_n → print` 的顺序补齐
5. 路由有四个 `include(..., "")`，不知道网址归哪个文件
   → 用 `Ctrl + Shift + F` 搜路径字符串，或从 `config/urls.py` 顺着 `include` 找

### 今天学了

- 从零重写：不看原代码，凭记忆写出 word_count
- Django 调用链：URL → `urls.py` → `views.py` → 模板
- 用 `Ctrl + Shift + F` / `Ctrl + P` / `F12` 在项目里定位代码

### 写了什么代码

- `day04/word_count.py`：从零重写单词统计，输出前 10
- `day04/code_reading.md`：`/student/` 的调用链笔记
- `plan/08-能力自评与复盘.md`：更新第一次能力自评

### 明天做什么

- Day 5：实验 A · 自动化脚本
- 二选一：批量重命名文件 / CSV 统计
- 记录 5 行感受：哪步顺手、哪步烦、还想做什么

## 2026-10-26

> 今日投入：90 分钟（17:56–19:26）

### 今天任务

- [x] 实验 A · CSV 统计

### 卡点记录（边做边记）

1. `csv.DictReader` 是什么
   → 把 CSV 第一行当表头，每行变成字典，用 `row["语文"]` 取值
2. `averages[subject] = total / len(rows)` 不理解
   → 先累加该科总分，再除以人数，存进字典
3. `DictWriter` / `writeheader()` / `writerows()` 不熟
   → `DictWriter` 按 `fieldnames` 写字典行；`writeheader()` 写表头；`writerows()` 写全部行

### 今天学了

- `csv.DictReader`：CSV → 字典列表
- `csv.DictWriter`：字典列表 → CSV
- CSV 里的数字读出来是字符串，计算前要 `int()`
- 读写 CSV 时 `open(..., newline="")`

### 写了什么代码

- `taste/automation/scores.csv`：测试数据
- `taste/automation/csv_stats.py`：读 CSV、算总分和平均分、写 `result.csv`
- `taste/automation/result.csv`：计算结果
- `taste/automation/notes.md`：5 行实验感受

### 明天做什么

- Day 6：实验 B · 小网页（Flask）
- 安装 Flask，跑一个表单页
- 记录 2 个感受：看到网页有没有成就感、更想改样式还是逻辑

## 2026-10-27 ~ 2026-10-29（补记）

> 今日投入：未记录

### 这几天做了什么

- 学校 LeetCode：混合方式（部分独立做、部分看题解）
- 具体题号和数量没有记录

### 卡点 / 问题

- 看题解后没有全部关掉重写，容易「看懂了但写不出」
- 这几天没有写日志，导致 LeetCode 的记录缺失

### 改进

- 每天 LeetCode 至少记一条：**题号 + 独立做出 / 看题解**
- 当天没时间做完整任务，也写 1 行日志，不要断

### 明天做什么

- Day 6：实验 B · 小网页（Flask）
- 安装 Flask，跑一个表单页
- LeetCode 继续保持每天 30 分钟，并记录题号

## 2026-10-29

> 今日投入：约 20 分钟（Flask 代码 23:00–23:04，另有安装与调试）

### 今天任务

- [x] 实验 B · Flask 小网页

### 卡点记录（边做边记）

1. `<from>` 拼错，点提交没反应
   → 应该是 `<form action="/hello">`
2. 结束标签写成 `<h1>`，少了斜杠
   → 应该是 `</h1>`
3. `name="name"placeholder` 之间少了空格
   → 补上空格

### 今天学了

- Flask：`Flask(__name__)`、`@app.route`
- 表单：`<form action="/hello">`
- `request.args.get("name", "陌生人")` 取网址参数
- `app.run(debug=True)` 改代码自动重载

### 写了什么代码

- `taste/web/app.py`：首页表单 + `/hello` 页面
- `taste/web/notes.md`：2 个实验感受

### LeetCode

- 学校题目，混合方式（已记在 10/27–10/29 补记）

### 明天做什么

- Day 7：实验 C · 假 Agent（`taste/agent/mock_agent.py`）
- 手写 Agent 循环 + 加一个 `calculator` 工具
- LeetCode 每天 30 分钟，记到 `leetcode/log.md`
