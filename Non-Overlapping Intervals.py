class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: x[0])
        count = 0
        i, nxt = 0, 1
      
        while nxt < len(intervals):
            if intervals[i][1]<=intervals[nxt][0]: #Non overlapping
                i = nxt
                
            elif intervals[i][1]<=intervals[nxt][1]: #partial overlapping
                count+=1
                
            elif intervals[i][1]>=intervals[nxt][1]: #full overalapping
                i = nxt
                count+=1
            nxt += 1
        return count
                
                
