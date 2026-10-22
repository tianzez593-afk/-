# day01：猜数字游戏

## 今天做了什么

- 用 `random.randint(1, 100)` 生成答案
- 用 `while True` + `if / elif / else` 判断「大了 / 小了 / 猜对」
- 用 `try / except ValueError` 处理非数字输入

## 三个问题的回答

1. **`while True` 什么时候结束？**
   猜对的时候。执行 `break` 退出循环。

2. **`int()` 为什么可能报错？**
   输入的不是整数（比如 `abc`）时，字符串无法转换成整数，会抛出 `ValueError`。

3. **如果不用 `break`，程序会怎样？**
   会无限循环下去：猜对了也继续问，永远不结束。

## 记录到的报错

输入 `abc` 时：

```text
ValueError: invalid literal for int() with base 10: 'abc'
```

## 怎么运行

```bash
python day01/guess_number.py
```
