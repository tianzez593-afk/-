# 学习进度（每次学习结束前更新）

> 最后更新：2026-10-23 晚
> 这份文件是给「下一次对话」看的。即使聊天记录丢了，也能从这里继续。

---

## 当前位置

- 阶段：0 · 方向体验（10/22 – 11/1）
- 进度：Day 1、Day 2、Day 3 已完成；下一次是 Day 4（复盘 + 重写）
- 计划文件：`plan/03-第一阶段-方向体验.md`

---

## 已完成

- [x] Day 1：猜数字 + `try/except` + 3 个问答
- [x] Day 2：单词统计 + Two Sum + Valid Parentheses（自己重写）
- [x] Day 3：Git 分支与回滚
  - 新建 `practice-git` 分支
  - 分支上提交、切回 `main`、`git merge`（Fast-forward）
  - `git restore` 撤销未提交修改
  - `git revert` 撤销已提交的错误
  - `git-notes.md` 回答 4 个问题

---

## 下次开始：Day 4 · 复盘 + 重写

> 开始前先读这份文件，再跑 `git status` / `git log --oneline`。

参考：`plan/03-第一阶段-方向体验.md` 的「第 4 天」

- [ ] 60 分钟：从零重写下面之一（**不看昨天的代码**）
  - 猜数字游戏
  - 单词统计
- [ ] 30 分钟：读代码（如果 `E:\LMS` 在）
  - 找到 `config/urls.py`，挑一个 URL
  - 顺着找到 `views.py` 里的函数
  - 写下：`URL → 哪个函数 → 做了什么 → 用到哪个模板/服务`
- [ ] 20 分钟：填 `plan/08-能力自评与复盘.md` 的第一次自评
- [ ] 10 分钟：提交
  ```bash
  git add .
  git commit -m "day04: 复盘 + 重写"
  git push origin main
  ```

---

## 已知薄弱点（后面补）

1. 变量作用域：局部变量 vs 全局变量
2. `return` vs `print`；没有 `return` 会得到 `None`
3. 字典读写：`counts[word]`、`in`、`+=`
4. 异常：`ValueError` / `FileNotFoundError`
5. 缩进和相对路径（在哪个目录运行命令）
6. 栈操作：`append` / `pop` / `stack[-1]`
7. Git：merge 的方向、`revert` vs `reset`、`add` vs `commit`

---

## 下次对话怎么继续

1. 先读这份文件
2. 跑 `git status` / `git log --oneline` 确认真实状态
3. 从「下次开始」第一条做起，一次只做一步
4. 每完成一项，把 `[ ]` 改成 `[x]`
