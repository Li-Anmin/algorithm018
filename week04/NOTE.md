学习笔记

寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

本质就是旋转数组寻找最小值问题

代码：基于二分法

    class Solution:
    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]: i = m + 1
            elif numbers[m] < numbers[j]: j = m
            else: j -= 1
        return i+1
