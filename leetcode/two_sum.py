def two_sum(nums, target):
    # TODO: 两层循环，找出和为 target 的两个下标
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(two_sum([2, 7, 11, 15], 9))  # 期望 [0, 1]
print(two_sum([3, 2, 4], 6))       # 期望 [1, 2]
print(two_sum([3, 3], 6))          # 期望 [0, 1]


def two_sum_fast(nums, target):
    seen = {}                      # 值 -> 下标
    for i, num in enumerate(nums):
        need = target - num        # 还差多少
        if need in seen:           # TODO: 如果 need 在 seen 里，返回 [seen[need], i]
            return [seen[need], i]
        else:                      # TODO: 否则把 num 和 i 存进 seen
         seen[num] = i
           


print(two_sum_fast([2, 7, 11, 15], 9))  # 期望 [0, 1]
print(two_sum_fast([3, 2, 4], 6))       # 期望 [1, 2]
print(two_sum_fast([3, 3], 6))          # 期望 [0, 1]
