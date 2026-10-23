# 学习进度（每次学习结束前更新）

> 最后更新：2026-10-22 晚
> 这份文件是给「下一次对话」看的。即使聊天记录丢了，也能从这里继续。

---

## 当前位置

- 阶段：0 · 方向体验（10/22 – 11/1）
- 进度：Day 1、Day 2 已完成；明天先自己重写 Valid Parentheses，再进入 Day 3
- 计划文件：`plan/03-第一阶段-方向体验.md`

---

## 已完成

- [x] Day 1：猜数字 + `try/except` + 3 个问答
- [x] Day 2：单词统计 `day02/word_count.py`（读文件 / 词频 / 前 10 / 文件不存在提示）
- [x] LeetCode Two Sum：暴力 O(n²) + 字典 O(n)，两版都通过
- [x] Valid Parentheses：已实现并提交（`10675e1`）——**明天不看答案自己重写**
- [x] 两题题解：`leetcode/notes.md`
- [x] Day 2 已推送到 GitHub

---

## 下次开始（明天）

### 0. 先自己写 Valid Parentheses（约 20 分钟）

- `leetcode/valid_parentheses.py` 已恢复成 **TODO 骨架**（这个改动还没提交）
- [ ] **不看** `leetcode/notes.md`，**不看** git 历史，自己补完 TODO
- [ ] 运行 `python leetcode/valid_parentheses.py`，期望：`True True False False True`
- [ ] 写完后对比答案：`git show 10675e1:leetcode/valid_parentheses.py`
- [ ] 提交：
  ```bash
  git add .
  git commit -m "day02: 自己重写 Valid Parentheses"
  git push origin main
  ```

### 1. 然后进入 Day 3 · Git 分支与回滚

参考：`plan/练习/day03-Git分支与回滚.md`

- [ ] 新建分支 `practice-git`
- [ ] 修改一个文件并提交
- [ ] 切回 `main`，合并分支
- [ ] 故意改坏文件，用 `git restore` 恢复
- [ ] 故意提交一个错误，用 `git revert` 撤销
- [ ] 写 `git-notes.md`，回答 4 个问题：
  - `add` 和 `commit` 的区别？
  - `branch` 是什么？
  - `merge` 做了什么？
  - `revert` 和 `reset` 的区别？
- [ ] LeetCode（时间够再做）：Merge Two Sorted Lists、Best Time to Buy and Sell Stock

---

## 已知薄弱点（后面补）

1. 变量作用域：局部变量 vs 全局变量
2. `return` vs `print`；没有 `return` 会得到 `None`
3. 字典读写：`counts[word]`、`in`、`+=`
4. 异常：`ValueError` / `FileNotFoundError`
5. 缩进和相对路径（在哪个目录运行命令）
6. 栈操作：`append` / `pop` / `stack[-1]`

---

## 下次对话怎么继续

1. 先读这份文件
2. 跑 `git status` / `git log --oneline` 确认真实状态
3. 从「下次开始」第一条做起，一次只做一步
4. 每完成一项，把 `[ ]` 改成 `[x]`
