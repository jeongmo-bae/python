# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for idx, num in reversed(list(enumerate(nums))) :
            if num == val :
                nums.pop(idx)
            else :
                k += 1
                continue
        print(nums)
        return k

    # 제거하는 문제지만, 남길 것을 생각해주는 문제로 보면 이해가 쉽다.
    # mutable 이라 가능한거네
    def removeElementWithTwoPointer(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums :
            print(nums)
            if num != val :
                nums[k] = num
                k += 1
            else:
                continue

        return k

sol = Solution()
# print(sol.removeElement([5,2,5,4,5], 5))
print(sol.removeElementWithTwoPointer([5,2,5,4,5], 5))
print(sol.removeElementWithTwoPointer([3,2,2,3], 3))
