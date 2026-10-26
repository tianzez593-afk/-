# 学习进度（每次学习结束前更新）

> 最后更新：2026-10-26 晚
> 这份文件是给「下一次对话」看的。即使聊天记录丢了，也能从这里继续。

---

## 当前位置

- 阶段：0 · 方向体验（10/22 – 11/1）
- 进度：Day 1–5 已完成；下一次是 Day 6（实验 B · 小网页）
- 计划文件：`plan/03-第一阶段-方向体验.md`

---

## 已完成

- [x] Day 1：猜数字 + `try/except` + 3 个问答
- [x] Day 2：单词统计 + Two Sum + Valid Parentheses（自己重写）
- [x] Day 3：Git 分支与回滚（分支、合并、restore、revert、`git-notes.md`）
- [x] Day 4：复盘 + 重写
  - 从零重写 `day04/word_count.py`
  - 读通 `/student/` 的 URL → view → 模板调用链
  - 更新第一次能力自评
- [x] Day 5：实验 A · CSV 统计
  - `taste/automation/csv_stats.py`：读 CSV、算总分 / 平均分、写 `result.csv`
  - `taste/automation/notes.md`：5 行实验感受

---

## 下次开始：Day 6 · 实验 B · 小网页（Flask）

> 开始前先读这份文件，再跑 `git status` / `git log --oneline`。

参考：`plan/03-第一阶段-方向体验.md` 的「第 6 天」

- [ ] 安装 Flask：
  ```bash
  pip install flask
  ```
- [ ] 新建 `taste/web/app.py`
  - 首页 `/`：一个表单，输入名字
  - `/hello`：接收名字并显示「你好，XXX」
- [ ] 运行 `python taste/web/app.py`
- [ ] 浏览器打开 `http://127.0.0.1:5000`，试试点提交
- [ ] 记录 2 个感受：
  - 看到网页出现时，有没有成就感？
  - 你更想改页面样式，还是更想改背后的逻辑？
- [ ] 提交：
  ```bash
  git add .
  git commit -m "day06: 实验 B Flask 小网页"
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
9. CSV：`DictReader` / `DictWriter` / `newline=""`

---

## 下次对话怎么继续

1. 先读这份文件
2. 跑 `git status` / `git log --oneline` 确认真实状态
3. 从「下次开始」第一条做起，一次只做一步
4. 每完成一项，把 `[ ]` 改成 `[x]`
