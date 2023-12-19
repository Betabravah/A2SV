class UndergroundSystem:

    def __init__(self):
        self.cur = defaultdict(list)
        self.ave = defaultdict(float)
        self.total = defaultdict(float)
        self.count = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cur[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prev_station, prev_t = self.cur[id]
        
        
        self.total[(prev_station, stationName)] +=  + t - prev_t
        self.count[(prev_station, stationName)] += 1
        average = self.total[(prev_station, stationName)] / self.count[(prev_station, stationName)]
        
        
        self.ave[(prev_station, stationName)] = average

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.ave[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)