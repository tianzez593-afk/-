# 实验 A · CSV 统计感受

1. 最顺手的一步：写第一个函数 `read_scores`，用 `DictReader` 把 CSV 读成字典
2. 最烦的一步：算平均分和写 CSV 的两个函数
   - `averages[subject] = total / len(rows)` 一开始不理解
   - `DictWriter` / `writeheader()` / `writerows()` 三个方法不熟
3. 有没有「还想再做点别的」的冲动：暂时没有，但知道可以按总分排序、加平均分列
4. 这次学到的：Python 自带的 `csv` 模块——`DictReader` 读、`DictWriter` 写
5. 下次想试：给结果按总分排序，或者在 CSV 里加一列平均分
