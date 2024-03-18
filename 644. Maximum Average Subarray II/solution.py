from typing import (
    List,
)
'''
Description:
Given an array with positive and negative numbers, find the maximum average subarray which length should be greater or equal to given length k.

Example
Input:
[1,12,-5,-6,50,3]
3
Output:
15.667
Explanation:
 (-6 + 50 + 3) / 3 = 15.667
'''

class Solution:
    def max_average(self, nums: List[int], k: int) -> float:
        # write your code here