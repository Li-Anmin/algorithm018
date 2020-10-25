from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 12]
    target = 9
    way = Solution()
    result = way.twoSum(nums, target)
    print(result)
