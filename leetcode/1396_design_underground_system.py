
from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.person_database = {}
        self.time_database = defaultdict(lambda:defaultdict(lambda:[0,0]))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.person_database:
            self.person_database[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station = self.person_database[id][0]
        start = self.person_database[id][1]
        self.time_database[station][stationName][0]+=(t-start)
        self.time_database[station][stationName][1]+=1
        del self.person_database[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time = self.time_database[startStation][endStation][0]
        n = self.time_database[startStation][endStation][1]
        return total_time/n
        
        
