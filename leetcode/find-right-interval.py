class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        d = {}
        for i, j in  enumerate(intervals):
            d[j[0]] = i
        left = sorted(list(d.keys()))
        ans = [-1] * len(intervals)
        for i, j in enumerate(intervals):
            ind = bisect_left(left, j[1])
            if ind != len(intervals):ans[i] = d[left[ind]]
        return ans



        