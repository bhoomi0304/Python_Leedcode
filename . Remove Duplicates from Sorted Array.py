class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # pointer for the place to insert the next unique number
        k = 1  

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # found a new unique element
                nums[k] = nums[i]
                k += 1

        return k
