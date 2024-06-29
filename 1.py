# from typing import List
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in nums:
            num2 = target - num
            ind = len(nums)-1-nums[::-1].index(num)
            if num2 in nums and nums.index(num2) != ind:
                return [nums.index(num2),ind]
        #return nums[::-1]


    
# clone from solution, make good use of hashtable
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
    
print(Solution2)
