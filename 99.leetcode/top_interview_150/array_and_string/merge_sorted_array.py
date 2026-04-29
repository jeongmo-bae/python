# https://leetcode.com/problems/merge-sorted-array/submissions/1989019825/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for idx, num2 in enumerate(nums2):
            print(idx)
            nums1[idx+m] = num2
        nums1.sort()
        print(nums1)

    def merge_with_two_pointer(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0 :
            if i >= 0 and nums1[i] > nums2[j] :
                nums1[k] = nums1[i]
                i -= 1
            else :
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            print(nums1)


solu = Solution()
solu.merge_with_two_pointer([10,12,13,0,0,0], 3, [2,5,6], 3)
solu.merge_with_two_pointer([10], 1, [], 0)

