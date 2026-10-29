# 学习进度（每次学习结束前更新）

> 最后更新：2026-10-29 晚
> 这份文件是给「下一次对话」看的。即使聊天记录丢了，也能从这里继续。

---

## 当前位置

- 阶段：0 · 方向体验（10/22 – 11/1）
- 进度：Day 1–6 已完成；下一次是 Day 7（实验 C · 假 Agent）
- LeetCode：每天 30 分钟；学校题目按混合方式做
- 计划文件：`plan/03-第一阶段-方向体验.md`

> LeetCode 每做一题都记到 `leetcode/log.md`：题号 + 独立做出 / 看题解。

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
- [x] Day 6：实验 B · Flask 小网页
  - `taste/web/app.py`：首页表单 + `/hello`
  - `taste/web/notes.md`：感受记录

---

## 下次开始：Day 7 · 实验 C · 假 Agent

> 开始前先读这份文件，再跑 `git status` / `git log --oneline`。

参考：`plan/03-第一阶段-方向体验.md` 的「第 7 天」

- [ ] 新建 `taste/agent/mock_agent.py`
- [ ] 手写 Agent 循环：
  - `fake_llm(prompt)`：按关键词返回固定结果
  - `weather_tool()` / `time_tool()`
  - `run_agent(user_input)`：模型判断 → 调工具 → 把结果交回模型
- [ ] 试三个输入：`今天天气怎么样`、`现在几点`、`你好`
- [ ] 加一个新工具 `calculator`，能算 `1+2`
- [ ] 记录 2 个感受：
  - 这个循环有意思吗？
  - 更想研究「让模型更聪明」，还是「把工具接进来」？
- [ ] LeetCode 每天 30 分钟，记到 `leetcode/log.md`
- [ ] 提交：
  ```bash
  git add .
  git commit -m "day07: 实验 C 假 Agent"
  git push origin main
  ```

---

## 然后：Day 8 · 选方向

参考：`plan/03-第一阶段-方向体验.md` 的「第 8 天」

- [ ] 填 A/B/C 对比表：
  - 做的时候有没有忘记时间？
  - 卡住时想不想继续？
  - 做完想不想给别人看？
  - 愿意周末再做一个吗？
- [ ] 三选一：后端 / AI 应用 Agent / 自动化数据分析
- [ ] 写一页方向说明：`direction.md`
  - 我选：
  - 因为：
  - 接下来 3 个月重点学：
  - 我暂时不学：

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
10. HTML：标签拼写（`form`）、结束标签 `</h1>`

---

## 下次对话怎么继续

1. 先读这份文件
2. 跑 `git status` / `git log --oneline` 确认真实状态
3. 从「下次开始」第一条做起，一次只做一步
4. 每完成一项，把 `[ ]` 改成 `[x]`
