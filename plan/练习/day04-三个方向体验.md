# day04：三个方向体验

> 对应：找出自己想走的方向
> 时间：3 天，每天 1 小时（也可以一天做完，每项 40 分钟）

---

## 规则

三个小实验都做，不要只做喜欢的那个。
做完再对比，否则你不知道自己错过了什么。

每个实验只做**最小可运行版本**，不要扩展。

---

## 实验 A：自动化脚本

### 任务（40–60 分钟）

二选一：

#### A1. 批量重命名

1. 建一个文件夹 `taste/automation/files/`
2. 放 5 个 `.txt` 文件，名字随便
3. 写 `rename.py`，把它们改成 `note_01.txt` … `note_05.txt`
4. 打印每次改名前后

提示：

```python
import os

folder = "files"
files = sorted(os.listdir(folder))

for index, old_name in enumerate(files, start=1):
    old_path = os.path.join(folder, old_name)
    new_name = f"note_{index:02d}.txt"
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)
    print(f"{old_name} -> {new_name}")
```

#### A2. 处理 CSV

1. 造一个 `scores.csv`：

```csv
姓名,语文,数学,英语
小明,80,90,85
小红,88,76,92
```

2. 用 Python 算每个人的总分、每科平均分
3. 输出到 `result.csv`

提示：

```python
import csv
```

---

## 实验 B：小网页

### 任务（40–60 分钟）

1. 安装 Flask：

```cmd
python -m pip install flask
```

2. 新建 `taste/web/app.py`：

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>我的第一个网页</h1>
    <form action="/hello">
        <input name="name" placeholder="输入你的名字">
        <button>提交</button>
    </form>
    """

@app.route("/hello")
def hello():
    name = request.args.get("name", "陌生人")
    return f"<h1>你好，{name}！</h1>"

if __name__ == "__main__":
    app.run(debug=True)
```

3. 运行：

```cmd
python taste/web/app.py
```

4. 浏览器打开 `http://127.0.0.1:5000`
5. 输入名字，点提交

### 加一个小功能

加一个 `/about` 页面，返回一段自我介绍。

---

## 实验 C：假 Agent

### 任务（40–60 分钟）

新建 `taste/agent/mock_agent.py`：

```python
def fake_llm(prompt):
    if "天气" in prompt:
        return "CALL_TOOL: weather"
    if "时间" in prompt:
        return "CALL_TOOL: time"
    return f"ANSWER: 我不太懂「{prompt}」，但我在学习。"

def weather_tool():
    return "晴，25 度"

def time_tool():
    return "现在是学习时间"

def run_agent(user_input):
    reply = fake_llm(user_input)

    if reply.startswith("CALL_TOOL:"):
        tool_name = reply.split(":")[1].strip()
        if tool_name == "weather":
            result = weather_tool()
        elif tool_name == "time":
            result = time_tool()
        else:
            result = "没有这个工具"

        print(f"[调用工具 {tool_name}] 结果：{result}")
        final = fake_llm(f"工具结果是 {result}，请回答用户")
        print(final)
    else:
        print(reply)

if __name__ == "__main__":
    while True:
        text = input("你：")
        if text == "退出":
            break
        run_agent(text)
```

### 加一个工具

加 `calculator`，能算 `1+2`。

提示：

```python
def calculator_tool(expr):
    return str(eval(expr))
```

> 注意：`eval` 有安全风险，这里只是练习，真实项目不要直接 `eval` 用户输入。

---

## 对比表

做完三个实验，填：

| 问题 | A 自动化 | B 网页 | C Agent |
| --- | --- | --- | --- |
| 做的时候有没有忘记时间？ | | | |
| 卡住时想不想继续？ | | | |
| 做完想不想给别人看？ | | | |
| 愿意周末再做一个吗？ | | | |
| 觉得最难的是什么？ | | | |

---

## 结论模板

```markdown
# 我的方向

- 我选：
- 因为：
- 接下来 3 个月重点学：
- 我暂时不学：
- 两周后如果后悔，我可以怎么调整：
```

---

## 验收标准

- [ ] 三个实验都跑通
- [ ] 每个实验至少改了一个小地方
- [ ] 填完对比表
- [ ] 写下方向结论
- [ ] 提交到 GitHub：`day04: 三个方向体验`
