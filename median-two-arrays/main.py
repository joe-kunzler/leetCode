class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        else:
            return nums[len(nums) // 2]