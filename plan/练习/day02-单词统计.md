# day02：单词统计

> 对应：函数、文件、异常、字典
> 预计：2 小时

---

## 目标

写一个脚本 `day02/word_count.py`：

1. 读取同目录下的 `sample.txt`
2. 统计每个单词出现的次数（忽略大小写）
3. 打印出现次数最多的前 10 个
4. 文件不存在时给出提示，不崩溃
5. 把统计逻辑拆成函数

---

## 示例

`sample.txt`：

```text
Python is easy.
Python is powerful.
I like Python.
```

输出：

```text
python: 3
is: 2
easy: 1
powerful: 1
i: 1
like: 1
```

---

## 起步骨架

```python
from collections import Counter


def read_file(path):
    # 读文件，返回文本；文件不存在返回 None
    pass


def count_words(text):
    # 返回 Counter
    pass


def top_words(counter, n=10):
    # 返回出现次数最多的 n 个
    pass


def main():
    text = read_file("sample.txt")
    if text is None:
        print("文件不存在")
        return

    counter = count_words(text)
    for word, count in top_words(counter):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
```

---

## 提示

- 读文件：

```python
with open(path, "r", encoding="utf-8") as f:
    return f.read()
```

- 捕获文件不存在：

```python
try:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
except FileNotFoundError:
    return None
```

- 分词：`text.lower().split()`
- 统计：`Counter(words)`
- 取前 10：`counter.most_common(10)`

---

## 验收标准

- [ ] 正常文件能统计
- [ ] 文件不存在时打印提示，不崩溃
- [ ] 统计逻辑在函数里
- [ ] 有 `if __name__ == "__main__":`
- [ ] 提交到 GitHub：`day02: 单词统计`

---

## 进阶（可选）

1. 去掉标点符号再统计
2. 支持命令行参数：`python word_count.py sample.txt --top 5`
3. 把结果写到 `result.txt`
4. 统计总单词数、不同单词数

---

## 做完回答 3 个问题

1. 为什么用 `with open` 而不是 `open`？
2. `Counter` 是什么？它和普通字典有什么区别？
3. 文件名写相对路径时，是相对于哪个目录？

写在 `day02/README.md` 里。
