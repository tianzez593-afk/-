# 第三阶段：后端与 Agent（12/28 – 2/21，8 周）

> 目标：做出一个「带数据库 + 带 Agent 功能」的项目，能写进简历、能在面试里讲 10 分钟。
> 前提：完成第二阶段，Python 能独立写 100 行以上。

---

## 一、8 周总表

| 周 | 日期 | 主题 | 本周产出 |
| --- | --- | --- | --- |
| 1 | 12/28–1/3 | Web 后端基础（Django） | 一个能增删改查的页面 |
| 2 | 1/4–1/10 | MySQL + Schema design | 项目库表 + ER 图 |
| 3 | 1/11–1/17 | API 设计 + 登录 + 安全 | 一套 REST API |
| 4 | 1/18–1/24 | Redis + MongoDB | 缓存 + 文档存储实验 |
| 5 | 1/25–1/31 | Agent 基础（假模型） | 手写 Agent 循环 + 工具 |
| 6 | 2/1–2/7 | 接真实大模型 API | 能对话、能调工具的 Agent |
| 7 | 2/8–2/14 | 项目整合 | 「AI 学习助手」v1 |
| 8 | 2/15–2/21 | 测试、日志、部署、打磨 | 项目 v2 + 简历描述 |

> 春节在 2 月 6 日前后，第 6–7 周可以减量，顺延即可。

---

## 二、第 1 周：Web 后端基础

### 为什么选 Django

你已经在 LMS 里见过 Django，继续用它学习成本最低。
Agent 的逻辑可以放在 `services.py` 里，和 Web 层分开。

### 学什么

- Django 项目结构：`settings.py`、`urls.py`、`views.py`、`models.py`
- 路由：URL → 视图函数
- 模板：把数据渲染成 HTML
- ORM：用 Python 类操作数据库
- 表单：接收用户输入
- Admin 后台

### 本周任务

做一个「待办清单」：

1. 新建 Django 项目
2. 建 `Todo` 模型：标题、完成状态、创建时间
3. 页面：列表、新增、标记完成、删除
4. 用 Admin 后台也能管理
5. 写 README：怎么启动

### 验收

- [ ] 能新增一条待办
- [ ] 能标记完成
- [ ] 能删除
- [ ] 数据重启后还在

---

## 三、第 2 周：MySQL + Schema design

### 学什么

- 关系型数据库、表、行、列、主键、外键
- SQL：`CREATE / INSERT / SELECT / UPDATE / DELETE`
- `JOIN`、`GROUP BY`、`ORDER BY`
- 索引：为什么加、什么时候加
- 事务：要么全成功，要么全失败
- Schema design：先画图，再建表

### 项目库表（AI 学习助手）

至少设计这些表：

| 表 | 作用 |
| --- | --- |
| `user` | 用户（可先用 Django 自带） |
| `goal` | 学习目标：岗位、入职日期 |
| `skill` | 能力项：名称、当前分、目标分 |
| `task` | 学习任务：日期、能力、状态 |
| `checkin` | 打卡：任务、时长、备注 |
| `resource` | 学习资源：标题、链接、类型 |
| `conversation` | 一次对话 |
| `message` | 对话中的消息 |
| `tool_call` | Agent 调用了什么工具、结果、耗时 |
| `log` | 系统日志 / 错误 |

### 本周任务

1. 画 ER 图（纸上或 draw.io 都行）
2. 写建表 SQL
3. 在 MySQL 里执行
4. 插入 5 条测试数据
5. 写 5 个查询：
   - 本周完成了多少任务
   - 每个能力项的平均分
   - 连续打卡天数（可以先简化）
   - 每个任务类型花了多少时间
   - 最近 10 条 Agent 工具调用

### 验收

- [ ] 能解释每张表为什么存在
- [ ] 能写出带 `JOIN` 的查询
- [ ] 知道哪个字段该加索引

---

## 四、第 3 周：API 设计 + 登录 + 安全

### 学什么

- REST API：GET / POST / PUT / DELETE
- JSON 请求和响应
- 状态码：200 / 201 / 400 / 401 / 403 / 404 / 500
- 登录与会话
- 常见安全问题：SQL 注入、XSS、CSRF、越权

### 本周任务

1. 用 Django REST Framework 或手写 JSON 视图，提供：
   - `GET /api/tasks/` 任务列表
   - `POST /api/tasks/` 新建任务
   - `PATCH /api/tasks/<id>/` 更新
   - `DELETE /api/tasks/<id>/` 删除
2. 加登录：未登录不能访问
3. 权限：只能操作自己的任务
4. 用 Postman 或 curl 测试每个接口
5. 写 API 文档（Markdown 即可）

### 安全底线

- 不用字符串拼接 SQL
- 模板里不对用户输入用 `|safe`
- 每个查询都带归属条件，例如 `Task.objects.get(id=id, user=request.user)`
- 不在代码里写死密码/密钥，用环境变量

### 验收

- [ ] 每个接口都能用 curl 调通
- [ ] 未登录返回 401
- [ ] 不能操作别人的数据

---

## 五、第 4 周：Redis + MongoDB

### Redis 学什么

- 是什么：内存里的键值数据库
- 常见类型：string、hash、list、set、sorted set
- 用途：缓存、会话、计数器、限流
- 过期时间：`EXPIRE`
- 键名规范：`app:module:id`

### MongoDB 学什么

- 文档数据库：JSON 风格的文档
- 集合（collection）vs 表
- 适合存：结构不固定的日志、对话、工具调用记录
- 基本操作：insert / find / update / delete

### 本周任务

1. 安装 Redis（Windows 可用 Docker 或 WSL；装不上就先看概念）
2. 用 Python 的 `redis` 库：
   - 存一个值、读出来
   - 设置 10 秒过期
   - 做一个计数器
3. 安装 MongoDB（可用 Docker 或云服务）
4. 用 `pymongo` 插入 3 条对话记录并查询
5. 写一页对比：什么时候用 MySQL、Redis、MongoDB

### 验收

- [ ] 能说出三者的区别
- [ ] 能用 Redis 做一次缓存
- [ ] 能用 MongoDB 存和查文档

---

## 六、第 5 周：Agent 基础（假模型）

### 核心循环

```text
用户输入
  → 模型判断
    → 需要工具？→ 执行工具 → 把结果交给模型 → 再判断
    → 不需要 → 直接回答
```

### 本周任务

1. 手写一个 `Agent` 类：

```python
class Agent:
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools

    def run(self, user_input):
        messages = [{"role": "user", "content": user_input}]
        for step in range(5):
            reply = self.llm(messages)
            if reply["type"] == "tool":
                result = self.tools[reply["name"]](**reply["args"])
                messages.append({"role": "tool", "content": result})
            else:
                return reply["content"]
        return "达到最大步数，停止"
```

2. 写两个工具：
   - `get_weather(city)`
   - `calculate(expression)`（只支持加减乘除，注意安全）
3. 用假模型测试：
   - 输入「北京天气」→ 调 `get_weather`
   - 输入「1+2*3」→ 调 `calculate`
4. 打印每一步的 `messages`，观察循环

### 数据演进（对应你笔记里的「数据写死 → 枚举 → dataset」）

| 阶段 | 做法 | 目的 |
| --- | --- | --- |
| 1 | 数据写死在代码里 | 先跑通 |
| 2 | 用枚举/常量集中管理 | 避免魔法值 |
| 3 | 放到 JSON/CSV dataset | 数据和代码分离 |
| 4 | 放进 MySQL/MongoDB | 支持增删改查 |

本周至少做到第 2 步，第 3 步有时间就做。

### 验收

- [ ] 能画出 Agent 循环图
- [ ] 能解释 `messages` 是怎么变化的
- [ ] 能加一个新工具

---

## 七、第 6 周：接真实大模型 API

### 学什么

- API Key 怎么存（环境变量，不写进代码）
- 请求格式：`messages`、`tools`、`tool_choice`
- 函数调用（function calling / tool use）
- 错误处理：超时、限流、返回格式错误
- 成本控制：少发无用上下文、限制步数

### 本周任务

1. 选一个你能访问的大模型 API（任意兼容 OpenAI 格式的都可以）
2. 把第 5 周的假模型替换成真实调用
3. 定义工具 schema（JSON）
4. 处理三种错误：
   - 网络超时
   - API 返回错误码
   - 模型返回的不是合法 JSON
5. 记录每次调用：输入、输出、耗时、token（如果能拿到）

### 验收

- [ ] 能真实对话
- [ ] 能真实调用一个工具
- [ ] 出错时不崩溃，有日志
- [ ] API Key 不在代码里

---

## 八、第 7 周：项目整合「AI 学习助手」

### 项目目标

做一个自己能用的学习助手：

1. 录入目标和能力项
2. 生成/管理每日任务
3. 打卡
4. 和 Agent 对话：
   - 「我今天该学什么？」
   - 「帮我复盘这周」
   - 「解释这道题」
5. Agent 能查数据库里的任务和打卡记录

### 技术结构

```text
Django（页面 + API）
  ├── models.py     目标/能力/任务/打卡/对话/消息
  ├── views.py      页面和 API
  ├── services.py   业务逻辑 + Agent 调用
  └── templates/    页面

MySQL      业务数据
Redis      缓存/会话（可选）
MongoDB    对话和工具调用日志（可选）
```

### 本周任务

1. 把前几周的表接进 Django
2. 做 3 个页面：首页、任务列表、对话页
3. Agent 能读取当前用户的任务和打卡
4. 每次工具调用写一条 `tool_call` 记录
5. README 写清楚：功能、架构图、启动方式

### 验收

- [ ] 能登录
- [ ] 能新增任务
- [ ] 能打卡
- [ ] 能问 Agent「我今天该学什么」，它基于真实数据回答

---

## 九、第 8 周：测试、日志、部署、打磨

### 本周任务

1. 给核心逻辑写 5 个测试
2. 加日志：请求、Agent 调用、错误
3. 把 `DEBUG` 关掉，检查报错页
4. 用 `python manage.py check --deploy` 看安全提示
5. 写简历项目描述：

```text
项目：AI 学习助手
- 基于 Django + MySQL 实现目标、任务、打卡管理
- 接入大模型 API，支持工具调用，Agent 可查询任务数据并给出学习建议
- 使用 Redis 缓存高频查询，MongoDB 记录对话与工具调用日志
- 编写单元测试和日志，处理超时、限流、格式错误
```

### 验收

- [ ] 项目能在一台干净电脑上按 README 跑起来
- [ ] 有测试、有日志、有关键截图
- [ ] 能在 10 分钟内讲清楚项目

---

## 十、阶段验收（2/21 前）

- [ ] 能独立设计 8–10 张表的 Schema
- [ ] 能写 CRUD + JOIN + 索引
- [ ] 能解释 Redis / MongoDB 的适用场景
- [ ] 能画出 Agent 循环，并解释每一步
- [ ] 有一个带数据库 + Agent 的项目
- [ ] 项目有 README、测试、日志
- [ ] 完成第三次能力自评
