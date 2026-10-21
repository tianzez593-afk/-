# 学习进度（每次学习结束前更新）

> 最后更新：2026-10-22
> 这份文件是给「下一次对话」看的。即使聊天记录丢了，也能从这里继续。

---

## 当前位置

- 阶段：0 · 方向体验（10/22 – 11/1）
- 天数：第 1 天 / 11 天
- 今日日期：2026-10-22
- 计划文件：`plan/03-第一阶段-方向体验.md`

---

## 已经完成

- [x] 环境确认（python / git / code）
- [x] 仓库 clone 到 `E:\learning-log`
- [x] `day01/guess_number.py` 基本逻辑：大了 / 小了 / 猜对 + break
- [x] 第一次 commit + push（`c0ba67f`）
- [x] 学习计划复制进 `plan/`（29 个文件）
- [x] 本地提交 `87914ed day01: 猜数字游戏`（**还没 push**）

---

## Day 1 还差（未完成 → 明天用 10 分钟热身补）

- [ ] 输入 `abc` 不崩溃：给 `int(input(...))` 加 `try/except ValueError`
- [ ] 亲手输入 `abc`，把报错抄到日志里
- [ ] 回答 day01 的 3 个问题，写进 `day01/README.md`
- [ ] 提交并推送剩余改动（README 已在暂存区；`PROGRESS.md`、`plan/` 还未提交）

---

## 已知薄弱点（后面几天补）

1. 变量分不清：`answer` / `guess` / `tries` 各自是什么
2. 不知道 `random` 有什么用
3. 字符串拼接：`str +` 与 f-string
4. 异常处理：`int()` 转换失败会抛 `ValueError`

---

## 下次开始：Day 2 · 2026-10-23（周五）

> 开始前先读这份文件，再跑一次 `git status`。

### 0. 热身 10 分钟：Day 1 收尾
- [ ] 给 `int(input(...))` 加 `try / except ValueError`，输入 `abc` 不崩溃
- [ ] 把 `abc` 的报错抄进 `README.md` 日志
- [ ] 写 `day01/README.md`，回答 3 个问题（while 何时结束 / int 为什么报错 / 不用 break 会怎样）

### 1. 30 分钟：学
- 看 `plan/学习笔记/01-Python基础.md` 的「函数」「文件」「异常」三节
- 重点：`def`、`return`、`with open()`、`try/except`

### 2. 50 分钟：写单词统计
- 新建 `day02/word_count.py`
- 读 `day02/sample.txt`，统计词频，打印前 10
- 逻辑拆成函数；文件不存在时给提示、不崩溃

### 3. 30 分钟：LeetCode
- Two Sum（easy）
- Valid Parentheses（easy）
- 每题写 3 行：思路、复杂度、易错点

### 4. 10 分钟：提交 + 日志
```bash
git add .
git commit -m "day02: 单词统计 + 两道 LeetCode"
git push origin main
```

---

## 下次对话怎么继续

1. 先读这份文件
2. 跑 `git status` / `git log --oneline` 确认真实状态
3. 从「今天还差」第一条开始，一次只做一步
4. 每完成一项，回来把 `[ ]` 改成 `[x]`
