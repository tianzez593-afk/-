# day03：Git 分支与回滚

> 对应：Git / rollback
> 预计：1.5 小时

---

## 目标

亲手完成一次：

1. 新建分支
2. 在分支上提交
3. 合并回 main
4. 改坏文件并恢复
5. 撤销一次错误提交

---

## 准备工作

进入你的 `learning-log` 仓库：

```cmd
cd /d E:\learning-log
git status
```

确保工作区是干净的（没有未提交的改动）。

---

## 任务 1：分支

```cmd
git switch -c practice-git
```

在当前仓库新建 `practice-git.md`：

```markdown
# Git 练习
这是 practice-git 分支。
```

提交：

```cmd
git add practice-git.md
git commit -m "practice: 新建分支文件"
```

切回 main：

```cmd
git switch main
```

观察：`practice-git.md` 不见了（因为它只在分支上）。

---

## 任务 2：合并

```cmd
git merge practice-git
```

再 `ls`，文件出现了。

---

## 任务 3：改坏再恢复

1. 打开 `README.md`，随便删掉几行
2. 查看改动：

```cmd
git diff
```

3. 恢复：

```cmd
git restore README.md
```

4. 再 `git status`，确认干净。

---

## 任务 4：撤销已提交的错误

1. 在 `README.md` 里加一行 `这一行是错误提交`
2. 提交：

```cmd
git add README.md
git commit -m "错误提交：测试 revert"
```

3. 查看提交号：

```cmd
git log --oneline
```

4. 撤销：

```cmd
git revert 提交号
```

5. 会弹出一个编辑器，保存退出即可（默认提交信息就行）
6. 查看 `README.md`，那一行应该没了
7. `git log --oneline`，能看到一条 `Revert ...`

---

## 任务 5：推送到 GitHub

```cmd
git push
```

---

## 验收标准

- [ ] 能独立新建、切换、合并分支
- [ ] 能用 `git restore` 恢复未提交的改动
- [ ] 能用 `git revert` 撤销已提交的改动
- [ ] 能说出 `restore` 和 `revert` 的区别
- [ ] GitHub 上能看到 `practice-git.md` 和 revert 记录

---

## 记录

在 `git-notes.md` 里回答：

```markdown
1. add 和 commit 的区别：
2. branch 是什么，为什么需要：
3. merge 做了什么：
4. restore 和 revert 的区别：
5. 冲突是什么，怎么解决：
```

---

## 常见问题

### `git switch` 不认识

旧版本 Git 用：

```cmd
git checkout -b practice-git
git checkout main
```

### revert 后出现编辑器

直接保存退出：

- Vim：按 `Esc`，输入 `:wq`，回车
- Nano：`Ctrl+O`，回车，`Ctrl+X`

### push 失败

先：

```cmd
git pull --rebase
git push
```
