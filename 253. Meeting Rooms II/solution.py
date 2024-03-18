from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''
Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)


Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
'''

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        n = len(start)
        ans = 0
        usingRoom = 0

        p1 = p2 = 0

        while p1 < n:
            while p1 < n and start[p1] < end[p2]:
                usingRoom += 1
                p1+=1
            ans = max(ans, usingRoom)
            p2+=1
            usingRoom-=1

        return ans