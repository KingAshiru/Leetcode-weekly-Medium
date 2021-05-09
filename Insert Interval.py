class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        insertFlag = False
        
        for i, interval in enumerate(intervals):
            if interval[0] >= newInterval[0]:
                intervals.insert(i, newInterval)
                insertFlag = True
                break
        
        if not insertFlag:
            intervals.append(newInterval)
            
        i, nxt = 0, 1
        while nxt < len(intervals):
            if intervals[i][1] >= intervals[nxt][0]:
                intervals[i][1] = max(intervals[i][1], intervals[nxt][1])
            else:
                i += 1
                intervals[i] = intervals[nxt]
            nxt += 1
        return intervals[:i+1]
