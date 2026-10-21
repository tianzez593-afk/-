# day01：猜数字游戏

> 对应：Python 基础 + Git 第一次提交
> 预计：2 小时

---

## 目标

写一个程序：

1. 程序随机想一个 1–100 的数字
2. 用户输入猜测
3. 程序提示「大了」「小了」
4. 猜对后打印用了多少次
5. 输入非数字时不崩溃

---

## 起步骨架

在 `day01/guess_number.py` 里写：

```python
import random

answer = random.randint(1, 100)
tries = 0

print("我想了一个 1-100 的数字。")

while True:
    guess = int(input("猜一个数字："))
    tries += 1

    # 在这里补全：
    # 1. 猜小了 → 打印"小了"
    # 2. 猜大了 → 打印"大了"
    # 3. 猜对了 → 打印"猜对了，你用了 X 次"，然后 break
```

---

## 提示

- 比较大小用 `if / elif / else`
- 结束循环用 `break`
- 打印次数用 f-string：`f"你用了 {tries} 次"`
- 处理非数字：

```python
try:
    guess = int(input("猜一个数字："))
except ValueError:
    print("请输入数字")
    continue
```

---

## 验收标准

- [ ] 正常玩一局，能提示大小
- [ ] 猜对后显示次数并退出
- [ ] 输入 `abc` 不崩溃
- [ ] 每行有注释
- [ ] 提交到 GitHub，提交信息：`day01: 完成猜数字游戏`

---

## 进阶（可选）

1. 限制最多猜 7 次，超过就失败
2. 猜对后问「要不要再来一局」
3. 记录历史最佳成绩（最少次数）

---

## 做完回答 3 个问题

1. `while True` 什么时候结束？
2. `int()` 为什么可能报错？
3. 如果不用 `break`，程序会怎样？

把答案写在 `day01/README.md` 里，3 行就够。
