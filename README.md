# Flight_Boarding_Sim
Flight entrance simulator used for spring 2022 HIMCM competition.

### Overview
The model, developed by team 11844, computes the time to board a flight under the competition guidelines. I made this program in our five day window to execute our model as manually calculating this with enough trials for a representative average would have been impossible in the time frame. 

This simulation will test three different boarding methods as defined by the HIMCM competition and output the average time it takes each method to fill up a standard plane of 195 seats.

### Model
Our model computed this time using several smaller calculations to find the time it takes for individuals to get seated. **The total time it takes to board a flight is equal to the time to board the person that took the longest to get seated.** This is not necessarily the last person in line, but they will be toward the end. Time starts when the first person in line enters the jet bridge.

The simulator creates a flight manifest and assigns a list of passengers a seat in a full plane. It puts them in a 'line'. The order of the line is determined by the boarding method. It then fills up the plane one by one, keeping track of several measures for each person and determines who took the longest to get seated.

### Boarding methods
Random Boarding 
	-This is where the line order is entirely randomized

Sort by Seat
	-This is where the line is ordered by column. For example, the first group in line may be all those with the leftmost window seat. 
  
Sort by Section
-This is where the line is ordered by rows. For example, all those in rows 30-34 (the back section of the plane) are first  in line 

### Output
5000 simulations per method with data averaged.

Random boarding: 16.043 min

Sort by Seat: 14.795 min

Sort by Section: 27.603 min
