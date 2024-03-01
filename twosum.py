class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            sol = target - nums[i]
            if sol in dict:
                return [dict[sol], i]
            else:
                dict[nums[i]] = i
