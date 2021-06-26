class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.average = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.check_in:
            return "You can't begin another trip until you complete previous"
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.check_in:
            return "Trip not found!"
        end = stationName
        start, time = self.check_in[id]
        duration = t - time
        if (start, end) in self.average:
            self.average[(start, end)] = self.average[(start, end)][0] + duration, self.average[(start, end)][1] + 1
        else:
            self.average[(start, end)] = (duration, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ave, count = self.average[(startStation, endStation)]
        return ave / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
