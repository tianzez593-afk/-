# 学习进度（每次学习结束前更新）

> 最后更新：2026-10-24 晚
> 这份文件是给「下一次对话」看的。即使聊天记录丢了，也能从这里继续。

---

## 当前位置

- 阶段：0 · 方向体验（10/22 – 11/1）
- 进度：Day 1–4 已完成；下一次是 Day 5（实验 A · 自动化脚本）
- 计划文件：`plan/03-第一阶段-方向体验.md`

---

## 已完成

- [x] Day 1：猜数字 + `try/except` + 3 个问答
- [x] Day 2：单词统计 + Two Sum + Valid Parentheses（自己重写）
- [x] Day 3：Git 分支与回滚（分支、合并、restore、revert、`git-notes.md`）
- [x] Day 4：复盘 + 重写
  - 不看原代码，从零重写 `day04/word_count.py`
  - 读通 `/student/` 的 URL → view → 模板调用链（`day04/code_reading.md`）
  - 更新第一次能力自评（`plan/08-能力自评与复盘.md`）

---

## 下次开始：Day 5 · 实验 A · 自动化脚本

> 开始前先读这份文件，再跑 `git status` / `git log --oneline`。

参考：`plan/03-第一阶段-方向体验.md` 的「第 5 天」

二选一（建议做 A2 CSV，更能练字典和函数）：

- **A1 批量重命名**
  - 在 `taste/automation/` 放 10 个随便命名的 `.txt`
  - 用 Python 重命名为 `note_01.txt`、`note_02.txt`……
  - 打印每个文件改名前后
- **A2 处理 CSV**
  - 造一个 `scores.csv`：姓名、语文、数学、英语
  - 算出每个人的总分、每科平均分
  - 把结果写到 `result.csv`

完成后：

- [ ] 写 5 行感受
  - 哪一步最顺手？
  - 哪一步最烦？
  - 有没有「还想再做点别的」的冲动？
- [ ] 提交：
  ```bash
  git add .
  git commit -m "day05: 实验 A 自动化脚本"
  git push origin main
  ```

---

## 已知薄弱点（后面补）

1. 变量命名和数据流：变量太多时容易绕，先画数据流再写
2. 字典读写：`counts[word]`、`in`、`+=`
3. 函数没有 `return` 会得到 `None`
4. 异常：`ValueError` / `FileNotFoundError`
5. 缩进和相对路径（在哪个目录运行命令）
6. 栈操作：`append` / `pop` / `stack[-1]`
7. Git：merge 的方向、`revert` vs `reset`、`add` vs `commit`
8. Django：URL → `urls.py` → `views.py` → 模板的查找方法

---

## 下次对话怎么继续

1. 先读这份文件
2. 跑 `git status` / `git log --oneline` 确认真实状态
3. 从「下次开始」第一条做起，一次只做一步
4. 每完成一项，把 `[ ]` 改成 `[x]`
