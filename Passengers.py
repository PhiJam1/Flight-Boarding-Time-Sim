class Passengers(object):

    #a constructor used to set values for the attributes to each passenger object with totalTime defaulting to 0
    def __init__(self, _SeatRowCol, _numBags, _totalTime = 0):
        self.seatRow = _SeatRowCol[0]
        self.seatCol = _SeatRowCol[1]
        self.numBags = _numBags
        self.totalTime = _totalTime

    
    #some basic getters
    def getSeatRow(self):
        return self.seatRow
    
    def getSeatCol(self):
        return self.seatCol
    
    def getNumBags(self):
        return self.numBags
    
    def getTotalTime(self):
        return self.totalTime
    
    def setTotalTime(self, time):
        self.totalTime = time
