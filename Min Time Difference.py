class Solution:
    def findMinDifference(self, timePoints):

        timelist = []
        for time in timePoints:
            minutes = int(time[0:2])*60 + int(time[3:5])
            minutes2 = minutes+24*60
            timelist.append(minutes2)
            timelist.append(minutes)
        timelist.sort()
        diff = 24*60+1
        for i in range(len(timelist)-1):
            diff = min(diff, timelist[i+1]-timelist[i])
        return diff
