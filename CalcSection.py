import Passengers
import random

#simulates boarding using a sort by section entrance method
def SectSim():
    numSeats = 195  #the total number of seats on board
    numCol = 33     #the total number of colums 
    numRow = 6      #the total number of rows
    manifest = []   #a list of all passengers

    #This will ensure that here are no double bookings and that we have a full flight
    def doubleBook(row, col):
        for seat in manifest:
            if (seat.getSeatRow() == row and seat.getSeatCol() == col):
                return True
        return False

    #function used to give each passenger their own unique seat
    def genRowCol(min, max):
        conflict = True
        coord = [0, 0] #list as [row, col]

        while(conflict):
            coord[0] = int(random.randint(1, 6)) #row
            coord[1] = int(random.randint(min, max)) #col

            #In row 4, 5, and 6 in col 1 don't exist. We can't have passengers there
            if (coord[0] > 3 and coord[1] == 1):
                conflict = True
                continue
            #check and correct any double bookings
            conflict = doubleBook(coord[0], coord[1])
        return (coord)

    def genNumBags():
        return random.randrange(1, 5, 1)

    #fill the flight manifest with passenger objects
    for x in range (66):
        manifest.append(Passengers.Passengers(genRowCol(23, 33), genNumBags()))
    for x in range(66):
        manifest.append(Passengers.Passengers(genRowCol(12, 22), genNumBags()))
    for x in range(63):
        manifest.append(Passengers.Passengers(genRowCol(1, 11), genNumBags()))
    
    #values to calculate the model
    tDist = 0.0     #time to walk to your seat (with no stops)
    tBaggage = 0.0  #time to put your carry ons into the overhead bin
    tSwap = 0.0     #time to allow people to enter a closer to window seat when there are people closer to the asile
    tWait = 0.0     #time to wait for the person in front of you to move

    #constants used in our calculations. Derived from experimentation and/or research
    avgWalkSpd = .4     #in meters/second
    planeLength = 67.0  #in meters 45 meter plane 22 meter walkway
    tBagUp = 10.25      #in seconds 

    for person in range(len(manifest)):
        tDist = ((manifest[person].getSeatCol() * planeLength) / 33) / avgWalkSpd
        tBaggage = manifest[person].getNumBags() * tBagUp

        # to get tSwap
        for prevPerson in range(person):
            if (manifest[person].getSeatRow() == 3 or manifest[person].getSeatRow() == 4):
                tSwap = 0
                break
            elif (manifest[person].getSeatCol() != manifest[prevPerson].getSeatCol()):
                tSwap += 0
                continue
            elif (manifest[person].getSeatRow() == 1 and (manifest[prevPerson].getSeatRow() == 2 or manifest[prevPerson].getSeatRow() == 3)):
                tSwap += tBagUp
            elif (manifest[person].getSeatRow() == 2 and manifest[prevPerson].getSeatRow() == 3):
                tSwap += tBagUp
            elif (manifest[person].getSeatRow == 5 and manifest[prevPerson].getSeatRow() == 4):
                tSwap += tBagUp
            elif (manifest[person].getSeatRow == 6 and (manifest[prevPerson].getSeatRow() == 4 or manifest[prevPerson].getSeatRow() == 5)):
                tSwap += tBagUp

        #to get tWait
        if (person == 0):
            tWait = 0
        f = person - 1
        while(f > 0):
            if (manifest[f].getSeatCol() <= manifest[person].getSeatCol()):
                tWait = manifest[f].getTotalTime()
                break
            f -= 1
        
        manifest[person].setTotalTime(tDist + tBaggage + 0 + tWait)
        
        #reset variables
        tDist = 0.0
        tBaggage = 0.0
        tSwap = 0.0
        tWait = 0.0
        
    max = 0
    for g in manifest:
        if(g.getTotalTime() > max):
            max = g.getTotalTime()
    return(max / 60.0) #return a time in minutes

#Do 5000 trails and output the average
trials = []
numTrials = 5000
for x in range(numTrials):
    trials.append(SectSim())
sum = 0
for num in trials:
    sum += num
print(sum / numTrials)
