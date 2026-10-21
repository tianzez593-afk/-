# Agent 开发入门

> 对应图片里的「Agent」「数据写死」「枚举」「dataset」「bug」「figure out」「判断能力」。
> 目标：理解 Agent 的核心循环，能做出一个带工具调用和数据库的小项目。

---

## 先记住这几件事

1. Agent = 大模型 + 工具 + 循环 + 记忆。
2. 核心不是「模型多聪明」，是「怎么把工具接进来、怎么控制循环」。
3. 先手写循环，再用框架。不要一上来学 LangChain。
4. 数据从写死 → 枚举 → dataset → 数据库，一步一步演进。
5. 每次工具调用都要记录：工具名、参数、结果、耗时。

---

## 一、Agent 是什么

普通聊天：

```text
用户 → 模型 → 回答
```

Agent：

```text
用户 → 模型 → 判断要不要用工具
                ├─ 要 → 执行工具 → 把结果给模型 → 再判断
                └─ 不要 → 直接回答
```

### 四个组成部分

| 部分 | 作用 |
| --- | --- |
| LLM | 理解意图、决定下一步 |
| Tools | 查数据库、算数、搜网页、发邮件 |
| Loop | 最多循环 N 次，防止死循环 |
| Memory | 保存对话、工具结果、用户偏好 |

---

## 二、最小 Agent（假模型）

> 先不接 API，不花钱，把循环跑通。

```python
def fake_llm(messages):
    """假模型：根据最后一条消息返回固定结构。"""
    last = messages[-1]["content"]

    if "天气" in last:
        return {"type": "tool", "name": "weather", "args": {"city": "北京"}}
    if "计算" in last:
        return {"type": "tool", "name": "calculate", "args": {"expr": "1+2*3"}}
    return {"type": "answer", "content": f"你说的是：{last}"}


def weather(city):
    return f"{city}：晴，25 度"


def calculate(expr):
    # 只允许数字和 + - * /，防止执行任意代码
    allowed = set("0123456789+-*/(). ")
    if not set(expr) <= allowed:
        return "表达式不合法"
    return str(eval(expr))


TOOLS = {
    "weather": weather,
    "calculate": calculate,
}


def run_agent(user_input, max_steps=5):
    messages = [{"role": "user", "content": user_input}]

    for step in range(max_steps):
        reply = fake_llm(messages)
        print(f"[第 {step + 1} 步] 模型返回：{reply}")

        if reply["type"] == "answer":
            return reply["content"]

        tool_name = reply["name"]
        args = reply["args"]
        tool = TOOLS.get(tool_name)

        if tool is None:
            result = f"没有工具 {tool_name}"
        else:
            result = tool(**args)

        messages.append({"role": "tool", "content": result, "name": tool_name})

    return "达到最大步数，停止"


if __name__ == "__main__":
    while True:
        text = input("你：")
        if text == "退出":
            break
        print("Agent：", run_agent(text))
```

### 你要理解的三件事

1. `messages` 是对话历史，模型靠它判断下一步。
2. 工具调用后，结果要**追加回 messages**，模型才能继续。
3. `max_steps` 防止死循环。

---

## 三、工具设计

### 工具三要素

```text
名字：唯一、动词开头，比如 get_weather
参数：JSON Schema，说明类型和含义
返回值：字符串 / JSON，模型能读懂
```

### 工具 schema 示例

```json
{
  "name": "get_weather",
  "description": "查询指定城市的天气",
  "parameters": {
    "type": "object",
    "properties": {
      "city": {
        "type": "string",
        "description": "城市名，例如：北京"
      }
    },
    "required": ["city"]
  }
}
```

### 好工具的标准

- 只做一件事
- 参数少
- 返回结构稳定
- 出错时返回错误信息，不抛异常给模型

---

## 四、数据演进：写死 → 枚举 → dataset → 数据库

这是你笔记里最重要的一条工程思路。

### 第 1 步：写死在代码里

```python
SKILLS = ["Python", "MySQL", "Redis"]
```

问题：改一次要改代码、重新部署。

### 第 2 步：用枚举 / 常量集中管理

```python
from enum import StrEnum

class SkillCategory(StrEnum):
    CS = "cs"
    CODING = "coding"
    TOOLS = "tools"
    AGENT = "agent"
```

好处：避免魔法字符串，IDE 能提示。

### 第 3 步：放到 dataset（JSON / CSV）

`skills.json`：

```json
[
  {"name": "Python", "category": "coding", "target": 3},
  {"name": "MySQL", "category": "agent", "target": 3}
]
```

代码读取：

```python
import json

with open("skills.json", encoding="utf-8") as f:
    skills = json.load(f)
```

好处：数据和代码分离，非程序员也能改。

### 第 4 步：放进数据库

```sql
CREATE TABLE skill (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    target_level TINYINT NOT NULL
);
```

好处：支持增删改查、多用户、权限。

> 每一步都解决上一阶段的问题。不要一上来就上数据库。

---

## 五、接真实大模型 API

### 通用流程

```text
1. 读取 API Key（环境变量）
2. 构造 messages
3. 发送请求，带上 tools 定义
4. 解析返回：
   - 普通文本 → 结束
   - 工具调用 → 执行工具 → 追加结果 → 再请求
5. 限制最大步数
```

### 伪代码

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["API_KEY"], base_url=os.environ.get("BASE_URL"))

def call_llm(messages, tools):
    response = client.chat.completions.create(
        model="你的模型名",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    return response.choices[0].message
```

> 不同厂商的 SDK 不一样，但「messages + tools + 循环」的思路一样。
> 如果你用的是 Anthropic，对应的是 `tools` 和 `tool_use` 内容块。

### API Key 规则

- 放在环境变量，不写进代码
- 不提交到 Git
- 不贴给 AI
- 泄露后立刻吊销

---

## 六、错误处理

Agent 常见错误：

| 错误 | 原因 | 处理 |
| --- | --- | --- |
| 超时 | 网络/模型慢 | 重试 2 次，指数退避 |
| 限流 429 | 请求太快 | 等待后重试 |
| 返回不是 JSON | 模型输出不稳定 | 解析失败就让它重试一次 |
| 工具参数缺字段 | 模型漏了 | 校验参数，返回错误信息 |
| 死循环 | 模型反复调同一工具 | `max_steps` + 重复检测 |
| 工具执行异常 | 数据库/网络问题 | 捕获异常，返回错误文本 |

### 日志要记什么

```text
时间、用户、输入、模型、工具名、参数、结果、耗时、错误
```

---

## 七、项目架构：AI 学习助手

```text
Django（页面 + API）
  ├── models.py      目标/能力/任务/打卡/对话/消息/工具调用
  ├── views.py       页面和 API
  ├── services.py    业务逻辑 + Agent 调用
  └── templates/     页面

MySQL      业务数据
Redis      缓存 / 会话（可选）
MongoDB    对话和工具调用日志（可选）
```

### Agent 可以调用的工具

| 工具 | 作用 |
| --- | --- |
| `get_today_tasks(user_id)` | 查今天的任务 |
| `get_week_stats(user_id)` | 查本周完成率 |
| `get_skill_gaps(user_id)` | 查能力差距 |
| `create_task(user_id, title, date)` | 新建任务 |
| `explain_concept(topic)` | 解释一个概念（内部再调模型） |

### 示例对话

```text
用户：我今天该学什么？
Agent：调用 get_today_tasks(1) → 返回 3 个任务
Agent：调用 get_skill_gaps(1) → Python 差距最大
Agent：建议先做「Python 函数练习」，再做 1 道 LeetCode。
```

---

## 八、判断能力：方案取舍

每做一个技术选择，写 3 行决策记录：

```markdown
## 决策：对话记录存 MySQL 还是 MongoDB？
- 选 MongoDB：对话结构灵活，消息数量大，不需要多表 JOIN。
- 代价：事务能力弱，统计查询不如 SQL 方便。
- 什么时候改：如果需要复杂统计，再加一张 MySQL 汇总表。
```

### 常见取舍

| 选择 | 优点 | 缺点 |
| --- | --- | --- |
| 自己写循环 | 理解深、可控 | 代码多 |
| 用 LangChain | 快、生态好 | 抽象多，出问题难查 |
| MySQL | 事务强、JOIN 方便 | 结构固定 |
| MongoDB | 灵活、易扩展 | 事务弱 |
| Redis 缓存 | 快 | 数据可能不一致 |
| 同步调用 | 简单 | 慢请求会阻塞 |
| 异步队列 | 解耦、可重试 | 复杂度高 |

---

## 九、面试常问

1. Agent 和普通聊天机器人的区别？
2. Agent 的核心循环是什么？
3. 工具调用怎么实现？
4. 怎么防止 Agent 死循环？
5. 怎么控制 token 成本？
6. 工具调用失败怎么处理？
7. 怎么保证模型输出的稳定性？
8. 为什么先手写循环再用框架？
9. 数据从写死到数据库，每一步解决什么问题？
10. 你怎么评估一个 Agent 的效果？

---

## 十、练习

### 练习 1：假 Agent

把上面的 `mock_agent.py` 敲一遍，跑通：

- 「北京天气」→ 调 weather
- 「计算 1+2*3」→ 调 calculate
- 「你好」→ 直接回答

### 练习 2：加工具

加一个 `get_time()` 工具，返回当前时间。

提示：

```python
from datetime import datetime
```

### 练习 3：改数据源

把 `TOOLS` 从写死改成从 `tools.json` 读取。

### 练习 4：接真实 API

- 用环境变量存 Key
- 接一个兼容 OpenAI 格式的 API
- 让它调用 `get_weather`
- 记录每次调用的耗时

### 练习 5：加数据库

- 建 `tool_call` 表
- 每次工具调用写一条记录
- 查最近 10 条

---

## 十一、自检

- [ ] 能画出 Agent 循环图？
- [ ] 能解释 `messages` 的作用？
- [ ] 能说出工具三要素？
- [ ] 能解释为什么要 `max_steps`？
- [ ] 能说出数据演进的 4 个阶段？
- [ ] 能写出一个工具 schema？
- [ ] 能说出至少 3 种 Agent 错误处理？
