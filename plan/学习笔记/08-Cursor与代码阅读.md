# Cursor 与代码阅读

> 对应图片里的「Cursor：功能 / run / UI / terminal / feature / API-function / 读代码 / 调用关系 / 配置 / 调用 / rollback / error / 二次开发」。
> 目标：能用 AI 加速理解代码，而不是被 AI 代替思考。

---

## 先记住这几件事

1. Cursor 是编辑器 + AI，不是自动写代码的外挂。
2. 读代码的顺序：入口 → 路由 → 视图 → 服务 → 模型 → 模板。
3. 调用关系要画出来，画不出来就是没懂。
4. `rollback` 是后悔药，改坏了先回滚，不要硬修。
5. 二次开发 = 读懂 → 小改 → 测试 → 提交。

---

## 一、Cursor 的主要功能

| 功能 | 怎么用 | 适合做什么 |
| --- | --- | --- |
| Chat | `Ctrl+L` | 问「这段代码在干什么」 |
| Inline Edit | `Ctrl+K` | 选中代码，让它改一小段 |
| Tab 补全 | 直接打字 | 补全重复代码 |
| Terminal | `Ctrl+`` | 在编辑器里跑命令 |
| @Codebase | 在对话里输入 `@Codebase` | 让它检索整个项目 |
| @File | `@文件名` | 只问某个文件 |
| Rules | 项目根目录 `.cursor/rules` | 固定代码规范 |
| Agent 模式 | 让它多步执行 | 较大的改动，但要盯着 |

> 快捷键可能随版本变化，以你安装的版本为准。

---

## 二、怎么问 Cursor 才有效

### 不好的问法

```text
帮我改一下这个项目
这个报错怎么办
```

### 好的问法

```text
请解释 E:\LMS\apps\plans\views.py 里 plan_create 函数的完整流程：
1. 它接收什么请求
2. 调用了哪些函数
3. 数据写到哪张表
4. 最后渲染哪个模板
请引用具体行号。
```

```text
我在 day02/word_count.py 遇到 FileNotFoundError。
我想读取脚本同目录下的 sample.txt。
请解释相对路径是相对于谁，并给出两种修复方式。
不要直接改代码，先解释。
```

### 三条规则

1. **先让它解释，再让它改。**
2. **改完必须自己跑一遍。**
3. **它说的每一句，都要能在代码里找到对应。**

---

## 三、读代码的方法

### 五步法

```text
1. 找入口：URL / main / 按钮点击
2. 找路由：这个 URL 对应哪个函数
3. 找调用链：函数 A 调了 B，B 调了 C
4. 找数据：读/写了哪张表、哪个文件
5. 找输出：返回 JSON 还是渲染模板
```

### 以 LMS 为例

目标：用户点击「新建学习计划」后发生了什么？

```text
1. 入口
   templates/plans/list.html 里的「新建」按钮
   → href="/plans/new/"

2. 路由
   apps/plans/urls.py
   → path("new/", views.plan_create, name="plan_create")

3. 视图
   apps/plans/views.py
   → def plan_create(request)

4. 表单
   apps/plans/forms.py
   → class PlanForm

5. 服务
   apps/plans/services.py
   → save_plan(...)

6. 模型
   apps/plans/models.py
   → StudyPlan.objects.create(...)

7. 模板
   templates/plans/form.html
```

### 画调用图

```text
浏览器
  → urls.py: /plans/new/
    → views.plan_create()
      → forms.PlanForm()
      → services.save_plan()
        → models.StudyPlan.objects.create()
      → render("plans/form.html")
```

> 能画出这张图，才算真的读懂一个请求。

---

## 四、读代码时的提问清单

每读一个函数，问自己：

1. 输入是什么？（参数、请求）
2. 输出是什么？（返回值、页面、JSON）
3. 它依赖谁？（调用了哪些函数/模型）
4. 谁调用它？（上游）
5. 出错会怎样？（异常处理）
6. 数据从哪来，到哪去？

---

## 五、配置与调用关系

### 配置

- `settings.py`：数据库、时区、中间件、模板路径
- `.env`：密钥、数据库密码（不要提交）
- `requirements.txt`：依赖版本
- `urls.py`：路由总表

### 调用关系

```text
URL → View → Service → Model → DB
                 ↓
              Template
```

> 好的项目：View 只收请求，Service 放业务逻辑，Model 管数据。
> 如果 View 里写了 100 行业务逻辑，说明结构有问题。

---

## 六、rollback 与 error

### rollback

改代码前先提交，改坏了：

```cmd
git status
git diff
git restore 文件名          # 撤销未提交的改动
git revert 提交号            # 撤销已提交的改动
```

### error

读报错三步：

1. 看最后一行（错误类型）
2. 找自己的文件（文件名 + 行号）
3. 看那一行在做什么

### 给 Cursor 的报错提问模板

```text
报错如下：
（粘贴完整报错）

我的代码：
（粘贴相关 20 行）

我想做什么：
我已经试过：
请先分析原因，不要直接给完整代码。
```

---

## 七、二次开发

### 什么叫二次开发

在别人的项目上做小改动：

- 加一个字段
- 加一个页面
- 改一个接口
- 修一个 bug

### 步骤

1. **跑起来**：按 README 启动
2. **读一条链路**：从入口追到数据库
3. **找最小改动点**：只改必要的文件
4. **写测试**：至少手动验证
5. **提交**：小步提交，写清楚
6. **回滚预案**：改坏了能恢复

### 练习：给 LMS 加一个字段

例如：给 `StudyPlan` 加一个 `remark` 备注字段。

步骤：

1. 改 `models.py`
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. 改表单 `forms.py`
5. 改模板
6. 运行验证
7. 提交

> 不要一上来改十个文件。一次只改一个功能。

---

## 八、AI 使用红线

| 不要 | 因为 |
| --- | --- |
| 让 AI 生成整个项目 | 你学不到东西，也维护不了 |
| 复制看不懂的代码 | 出 bug 你修不了 |
| 不看报错就问 AI | 失去读报错的能力 |
| 让 AI 改完不测试 | 可能引入新问题 |
| 把密钥贴给 AI | 泄露风险 |

### 一条硬规则

> **你保留的每一行 AI 代码，你都必须能逐行解释。**
> 解释不了，就删掉自己重写。

---

## 九、练习

### 练习 1：读一个请求

在 LMS 里选一个页面，画出：

```text
URL → 路由 → 视图 → 服务 → 模型 → 模板
```

### 练习 2：用 Cursor 解释代码

选中一个函数，问：

```text
请逐行解释这个函数，重点说明：
1. 每个参数是什么
2. 调用了哪些函数
3. 哪里可能出错
```

然后自己验证它说得对不对。

### 练习 3：故意改坏再回滚

1. 改坏一个文件
2. `git diff` 看改了什么
3. `git restore` 恢复
4. 记录过程

### 练习 4：加一个小功能

给 LMS 或你自己的项目加一个小功能，要求：

- 只改 3 个文件以内
- 手动测试通过
- 提交信息写清楚

---

## 十、自检

- [ ] 能说出 Cursor 的 5 个功能？
- [ ] 能画出一个请求的调用链？
- [ ] 能解释 `git restore` 和 `git revert` 的区别？
- [ ] 能读懂报错并定位到自己的文件？
- [ ] 能在一个陌生项目里加一个小功能？
- [ ] 能判断 AI 给的代码哪里不对？
