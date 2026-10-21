# Python 基础

> 对应图片里的「Python」。
> 目标：能独立写出 100–300 行的小程序，能解释每一行。

---

## 先记住这几件事

1. Python 用**缩进**表示代码块，不用大括号。
2. 变量不需要声明类型，直接赋值。
3. 列表 `[]`、字典 `{}`、元组 `()`、集合 `set()` 是最常用的容器。
4. 函数用 `def` 定义，用 `return` 返回结果。
5. 文件用 `with open(...) as f` 打开，会自动关闭。
6. 报错不可怕，先看最后一行。

---

## 一、怎么运行 Python

### 方式 1：命令行

```cmd
python hello.py
```

### 方式 2：交互式

```cmd
python
```

然后输入：

```python
>>> print("hello")
hello
```

### 方式 3：VS Code

新建 `.py` 文件，点右上角运行按钮。

---

## 二、变量和类型

```python
name = "小明"      # 字符串 str
age = 18           # 整数 int
height = 1.75      # 浮点数 float
is_student = True  # 布尔值 bool

print(name, age, height, is_student)
print(type(age))   # <class 'int'>
```

### 类型转换

```python
number = int("18")      # 字符串转整数
text = str(18)          # 整数转字符串
price = float("9.9")    # 字符串转浮点数
```

> `int("abc")` 会报 `ValueError`，因为 `"abc"` 不是数字。

### 常用运算

```python
print(7 + 3)    # 10
print(7 - 3)    # 4
print(7 * 3)    # 21
print(7 / 3)    # 2.333...
print(7 // 3)   # 2（整除）
print(7 % 3)    # 1（余数）
print(7 ** 2)   # 49（幂）
```

---

## 三、字符串

```python
s = "Hello, Python"

print(len(s))          # 长度
print(s.upper())       # 转大写
print(s.lower())       # 转小写
print(s.replace("Python", "World"))
print(s.split(", "))   # 按分隔符切成列表
print(s[0])            # 第一个字符
print(s[-1])           # 最后一个字符
print(s[0:5])          # 切片：前 5 个字符
```

### f-string（最常用）

```python
name = "小明"
age = 18
print(f"{name} 今年 {age} 岁")
```

### 常用判断

```python
print("Py" in s)        # True
print(s.startswith("He"))
print(s.endswith("on"))
```

---

## 四、列表、元组、字典、集合

### 列表 list：有序、可修改

```python
fruits = ["apple", "banana", "orange"]

fruits.append("pear")      # 末尾添加
fruits.insert(1, "grape")  # 指定位置插入
fruits.remove("banana")    # 删除指定值
last = fruits.pop()        # 弹出最后一个

print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
print(len(fruits))
```

### 元组 tuple：有序、不可修改

```python
point = (3, 5)
x, y = point
print(x, y)
```

### 字典 dict：键值对

```python
student = {
    "name": "小明",
    "age": 18,
    "score": 90,
}

print(student["name"])
print(student.get("gender", "未知"))  # 没有这个键时返回默认值

student["age"] = 19       # 修改
student["city"] = "北京"  # 新增

for key, value in student.items():
    print(key, value)
```

### 集合 set：去重、无序

```python
numbers = [1, 2, 2, 3, 3, 3]
unique = set(numbers)
print(unique)  # {1, 2, 3}

a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)  # 交集 {2, 3}
print(a | b)  # 并集 {1, 2, 3, 4}
```

### 什么时候用哪个

| 容器 | 特点 | 场景 |
| --- | --- | --- |
| list | 有序、可改、可重复 | 一组按顺序的数据 |
| tuple | 有序、不可改 | 固定的几个值，比如坐标 |
| dict | 键值对、查找快 | 按名字查数据 |
| set | 去重、查找快 | 去重、判断是否存在 |

---

## 五、条件和循环

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

### for 循环

```python
for i in range(5):
    print(i)  # 0 1 2 3 4

fruits = ["apple", "banana"]
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

### while 循环

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

### break 和 continue

```python
for i in range(10):
    if i == 3:
        continue   # 跳过本次
    if i == 6:
        break      # 结束循环
    print(i)
```

---

## 六、函数

```python
def add(a, b):
    return a + b

print(add(2, 3))  # 5
```

### 默认参数

```python
def greet(name, greeting="你好"):
    return f"{greeting}，{name}"

print(greet("小明"))
print(greet("小明", "早上好"))
```

### 任意个参数

```python
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))  # 6
```

### 关键字参数

```python
def create_user(name, age, city="北京"):
    return {"name": name, "age": age, "city": city}

print(create_user(name="小明", age=18))
```

### 作用域

```python
x = 10

def show():
    x = 20      # 这是局部变量
    print(x)

show()          # 20
print(x)        # 10
```

> 函数里修改全局变量要用 `global`，但初学阶段尽量少用。

---

## 七、文件读写

### 读文件

```python
with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(text)
```

### 按行读

```python
with open("sample.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### 写文件

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("你好\n")
    f.write("第二行\n")
```

> `"w"` 会覆盖原文件；想追加用 `"a"`。

### 路径

```python
import os

print(os.getcwd())                    # 当前工作目录
print(os.path.exists("sample.txt"))   # 文件是否存在
```

> 相对路径是相对于「运行命令的目录」，不是脚本所在目录。这是新手最常踩的坑。

---

## 八、异常处理

```python
try:
    number = int(input("请输入数字："))
    print(10 / number)
except ValueError:
    print("你输入的不是数字")
except ZeroDivisionError:
    print("不能除以 0")
finally:
    print("程序结束")
```

### 主动抛异常

```python
def set_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    return age
```

### 常见异常

| 异常 | 原因 |
| --- | --- |
| `ValueError` | 值不对，比如 `int("abc")` |
| `TypeError` | 类型不对，比如 `"a" + 1` |
| `KeyError` | 字典没有这个键 |
| `IndexError` | 列表越界 |
| `FileNotFoundError` | 文件不存在 |
| `ZeroDivisionError` | 除以 0 |

---

## 九、类（先会用即可）

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"我叫 {self.name}，今年 {self.age} 岁"

    def __str__(self):
        return self.introduce()


s = Student("小明", 18)
print(s.introduce())
print(s)
```

### 三个关键词

- `class`：定义类
- `__init__`：创建对象时自动执行
- `self`：指对象自己

> 初学阶段不用学继承、多态。先把「类 = 数据 + 方法」用熟。

---

## 十、模块、虚拟环境、pip

### 导入模块

```python
import math
from datetime import datetime
from collections import Counter

print(math.sqrt(16))
print(datetime.now())
print(Counter("hello"))
```

### 自己的模块

`tools.py`：

```python
def add(a, b):
    return a + b
```

`main.py`：

```python
from tools import add

print(add(1, 2))
```

### 虚拟环境

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

激活后命令行前面有 `(.venv)`。

### 安装包

```cmd
pip install requests
pip freeze > requirements.txt
pip install -r requirements.txt
```

> 每个项目一个虚拟环境，不要把包装到系统 Python 里。

---

## 十一、新手最常踩的 12 个坑

1. 缩进混用 Tab 和空格 → 统一 4 个空格。
2. 忘记冒号：`if x > 0` 少了 `:`。
3. `=` 和 `==` 混用。
4. 字符串和数字直接相加：`"1" + 1` 报错。
5. 列表越界：`lst[10]` 但长度只有 3。
6. 字典用不存在的键：用 `.get()`。
7. 文件路径错：打印 `os.getcwd()`。
8. 忘记关闭文件：用 `with open`。
9. 修改列表时遍历它：先复制一份。
10. 函数里没有 `return`，结果拿到 `None`。
11. 变量名拼错：Python 不会提醒你，只会 `NameError`。
12. 认为 `input()` 返回数字：它永远返回字符串，要 `int()`。

---

## 十二、练习（做完再往下）

### 基础

1. 输入两个数，输出和、差、积、商。
2. 判断奇偶数。
3. 打印 1–100 中能被 3 整除的数。
4. 输入 5 个数，求平均值。
5. 反转一个字符串。
6. 判断回文。
7. 统计一句话里每个字出现的次数。
8. 打印九九乘法表。
9. 判断闰年。
10. 打印斐波那契数列前 20 项。

### 函数

11. 写 `is_prime(n)` 判断质数。
12. 写 `average(*numbers)`。
13. 写 `safe_int(text)`，失败返回 `None`。
14. 写 `count_words(text)`，返回字典。
15. 写 `read_file(path)`，文件不存在返回 `None`。

### 文件

16. 读一个文本文件，统计行数、单词数、字符数。
17. 把一个列表写进文件，每行一个。
18. 读 CSV，算每列平均值。

### 类

19. 写 `BankAccount` 类：存款、取款、查余额。
20. 写 `PhoneBook` 类：增、删、查。

---

## 十三、自检

能不看笔记回答，才算学会：

- [ ] `list` 和 `tuple` 的区别？
- [ ] `dict` 的 `.get()` 和 `[]` 有什么区别？
- [ ] `break` 和 `continue` 的区别？
- [ ] 函数没有 `return` 会返回什么？
- [ ] `with open` 的好处是什么？
- [ ] `try/except` 什么时候用？
- [ ] 虚拟环境解决了什么问题？
- [ ] 相对路径是相对于谁？
