class Solution:
    def moveZeroes(self,nums):
        if not nums:
            return 0
        j=0
        for i in range(len(nums)):
            if nums[i]:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
        print(nums)

if __name__ == '__main__':
    nums=[0,1,0,3,12,18]
    print(nums)
    way=Solution()
    result = way.moveZeroes(nums)


