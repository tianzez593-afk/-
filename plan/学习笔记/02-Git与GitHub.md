# Git 与 GitHub

> 对应图片里的「Github」和「rollback」。
> 目标：每天都能安全地提交、分支、回滚、推送。

---

## 先记住这几件事

1. Git 是**本地**的版本管理工具，GitHub 是**远程**仓库。
2. `add` 把改动放进暂存区，`commit` 把暂存区保存成一个版本。
3. 分支让你在不破坏主代码的情况下改东西。
4. `revert` 是安全的撤销；`reset --hard` 会丢东西，初学别用。
5. 每次提交只做一件事，写清楚提交信息。

---

## 一、Git 是什么

想象你在写论文：

- 每改一版就复制一个「论文_v1」「论文_v2」「论文_最终版」……
- 最后不知道哪个是最新的，也不敢删。

Git 就是帮你自动做这件事：

- 每次 `commit` 就是一个存档点
- 可以随时回到任何一个存档点
- 可以开分支同时写两个版本
- 可以多人协作，最后合并

---

## 二、第一次配置

```cmd
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

查看配置：

```cmd
git config --list
```

---

## 三、核心概念

```text
工作区（你看到的文件）
   ↓ git add
暂存区（准备提交的改动）
   ↓ git commit
本地仓库（历史版本）
   ↓ git push
远程仓库（GitHub）
```

| 概念 | 作用 |
| --- | --- |
| 工作区 | 你正在编辑的文件 |
| 暂存区 | 你准备这次提交的改动 |
| 本地仓库 | `.git` 文件夹，保存所有历史 |
| 远程仓库 | GitHub 上的仓库 |
| 分支 | 一条独立的开发线 |
| HEAD | 当前所在的提交/分支 |

---

## 四、最常用的 10 个命令

### 1. 初始化

```cmd
git init
```

### 2. 克隆

```cmd
git clone https://github.com/用户名/仓库名.git
```

### 3. 看状态

```cmd
git status
```

> 最常用的命令。不知道发生了什么，先 `git status`。

### 4. 看改动

```cmd
git diff
```

### 5. 暂存

```cmd
git add 文件名
git add .          # 所有改动
```

### 6. 提交

```cmd
git commit -m "说明这次改了什么"
```

好的提交信息：

```text
day01: 完成猜数字游戏
fix: 修复单词统计文件不存在时的崩溃
docs: 补充 README 运行说明
```

不好的提交信息：

```text
update
修改
111
```

### 7. 看历史

```cmd
git log --oneline
git log --oneline --graph --all
```

### 8. 推送

```cmd
git push
```

第一次推送：

```cmd
git push -u origin main
```

### 9. 拉取

```cmd
git pull
```

### 10. 查看远程

```cmd
git remote -v
```

---

## 五、分支

### 为什么要分支

- `main` 保持可用
- 新功能在 `feature/xxx` 上开发
- 做完再合并回 `main`

### 常用命令

```cmd
git branch                  # 查看分支
git branch feature/login    # 新建分支
git switch feature/login    # 切换分支
git switch -c feature/login # 新建并切换
git merge feature/login     # 把该分支合并到当前分支
git branch -d feature/login # 删除已合并的分支
```

### 分支工作流

```text
main
  └── feature/word-count
        ├── commit 1
        ├── commit 2
        └── merge 回 main
```

---

## 六、合并冲突

当两个分支改了同一行，Git 不知道保留哪个，就会冲突。

文件里会出现：

```text
<<<<<<< HEAD
这是 main 的版本
=======
这是 feature 的版本
>>>>>>> feature/word-count
```

解决步骤：

1. 打开文件，手动改成你想要的内容
2. 删掉 `<<<<<<<`、`=======`、`>>>>>>>`
3. `git add 文件`
4. `git commit -m "resolve conflict"`

> 不要慌。冲突只是 Git 在问你「这两个版本留哪个」。

---

## 七、撤销与回滚

### 1. 改坏了，还没 add

```cmd
git restore 文件名
```

### 2. 已经 add，还没 commit

```cmd
git restore --staged 文件名
git restore 文件名
```

### 3. 已经 commit，想撤销这一次

```cmd
git revert 提交号
```

> `revert` 会生成一个新提交，抵消旧提交。安全，推荐。

### 4. 查看提交号

```cmd
git log --oneline
```

### 5. `reset` 的区别（了解即可）

| 命令 | 效果 | 风险 |
| --- | --- | --- |
| `git reset --soft HEAD~1` | 撤销 commit，保留改动 | 低 |
| `git reset --mixed HEAD~1` | 撤销 commit 和 add，保留文件 | 中 |
| `git reset --hard HEAD~1` | 全部丢弃 | 高，初学别用 |

---

## 八、.gitignore

哪些文件不该进 Git：

```text
# Python
__pycache__/
*.pyc
.venv/
venv/

# 数据库
db.sqlite3
*.sqlite3

# 环境变量 / 密钥
.env
.env.*

# 编辑器
.vscode/
.idea/

# 系统
Thumbs.db
.DS_Store
```

### 已经提交了怎么办

```cmd
git rm -r --cached .venv
git commit -m "stop tracking .venv"
```

> `.gitignore` 只对「还没被 Git 跟踪」的文件生效。

---

## 九、连接 GitHub

### 方式 1：先有远程，再克隆

```cmd
git clone https://github.com/用户名/仓库名.git
```

### 方式 2：先有本地，再关联

```cmd
git remote add origin https://github.com/用户名/仓库名.git
git branch -M main
git push -u origin main
```

### 认证问题

GitHub 不再接受账号密码。三种方式：

1. **VS Code 源代码管理面板**：点推送，浏览器登录（最省事）
2. **GitHub Desktop**：图形界面
3. **Personal Access Token**：设置 → Developer settings → Tokens

---

## 十、每天的工作流

```cmd
git pull                 # 先拉最新
# 写代码
git status               # 看改了什么
git diff                 # 看具体改动
git add .                # 暂存
git commit -m "说明"      # 提交
git push                 # 推送
```

---

## 十一、常见错误速查

| 报错 | 原因 | 解决 |
| --- | --- | --- |
| `not a git repository` | 不在仓库目录 | `cd` 到项目目录，或 `git init` |
| `push rejected` | 远程有新提交 | `git pull --rebase` 再 push |
| `CONFLICT` | 合并冲突 | 手动改文件，add，commit |
| `detached HEAD` | 切到了某个提交 | `git switch main` |
| `Authentication failed` | 密码方式失效 | 用 VS Code / Token |
| `src refspec main does not match any` | 还没有提交 | 先 `git add` + `commit` |

---

## 十二、练习

按顺序做完：

1. 新建仓库 `git-practice`
2. 建 `README.md`，提交
3. 新建分支 `feature/notes`
4. 在分支上改 README，提交
5. 切回 `main`，合并分支
6. 故意改坏 README，用 `git restore` 恢复
7. 再故意提交一个错误，用 `git revert` 撤销
8. 推到 GitHub
9. 在 GitHub 网页上改一次 README，本地 `git pull`
10. 制造一次冲突并解决

---

## 十三、自检

- [ ] `add` 和 `commit` 的区别？
- [ ] `branch` 是什么？为什么需要？
- [ ] `merge` 做了什么？
- [ ] `revert` 和 `reset` 的区别？
- [ ] `.gitignore` 什么时候生效？
- [ ] `pull` 和 `push` 的方向？
- [ ] 冲突怎么解决？
- [ ] 怎么查看历史提交？
