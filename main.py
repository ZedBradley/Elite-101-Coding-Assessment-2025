# Filename: main.py (or any file of your choice)
# -----------------------------------------------------------------------------
# DISCLAIMER:
# This code is an EXAMPLE solution for reference/study purposes ONLY.
# Submitting it as your own may violate assignment rules against plagiarism
# or AI-generated solutions. Use it ethically and responsibly.
# -----------------------------------------------------------------------------
from restaurantTables import restaurant_tables
from restaurantTables import restaurant_tables2
import unittest

class testTableMethods(unittest.TestCase):
    def testLevel1(self):
        self.assertEqual(getFreeTables(restaurant_tables), "yes")

    def testLevel2(self):
        self.assertEqual(firstOpenWithSeating(restaurant_tables, 33), "none")

    def testLevel3(self):
        self.assertEqual(allOpenWithSeating(restaurant_tables, 33), "none")

    def testLevel4(self):
        self.assertEqual(openTableCombos(restaurant_tables, 33), "none")

    
 # Level 1
    # Returns a list of table IDs (or entire objects) that are currently free.
 
def getFreeTables(tables):
    freeTables = []
    # loop through time slots
    for j in range(len(tables)): #j - column
        for i in range(len(tables[j])): #i - row
            if tables[i][j] == "o": 
                freeTables.append(tables[i][0]) #add time to new list
        if len(freeTables) > 0: #make surethere are times
            print(f"Table {j} is available at time slot {freeTables}")
        freeTables.clear() #make room for next tables times
    return "yes" #for unit testing
       

 # Level 2
    # Returns the first table ID that can seat 'party_size' and is free,
    # or None if none found.  
def firstOpenWithSeating(tables, partySize):
    timeSlot = []
    capacity = 0
    i = 1 #skip restaurant_tables[0][0]
    while capacity < partySize:
        if i >= len(tables): #keep in bounds
            print("None")
            return "none" #for unit test
        tableSplit = tables[0][i].split("(") #isolate capacity
        tableSplit2 = tableSplit[1].split(")") #isolate capacity
        capacity = int(tableSplit2[0]) #convert capacity to int
        if capacity < partySize: #check if cap meets party size
            i+=1

    for j in range(len(tables)): #loop throught list
        if tables[j][i] == "o": #use variable i for column to keep table from above
            timeSlot.append(tables[j][0]) #add time if available
            j+=1
    print(f"Table {i} can seat {capacity} and is available at time slots {timeSlot}")
    

# Level 3
    # Returns a list of all table IDs that can seat 'party_size' and are free.
def allOpenWithSeating(tables, partySize):
    timeSlot = []
    capacity = 0
    i = 1 #skip restaurant_tables[0][0]
    count = 0 #print none if count == 0
    for table in tables:
        if i >= len(tables):
            if count == 0: #print none if count == 0
                print("None")
                return "none" #for unit testing
            return #end loop
        tableSplit = tables[0][i].split("(") #isolate capacity
        tableSplit2 = tableSplit[1].split(")") #isolate capacity
        capacity = int(tableSplit2[0]) #convert capacity to int 
        if capacity >= partySize: #check if cap meets party size
            for j in range(len(tables)): #loop through list
                if tables[j][i] == "o": #use variable i as column to keep table from above
                    timeSlot.append(tables[j][0]) #add time if available
                    j+=1 #next time slot
                    count += 1 
            print(f"Table {i} can seat {capacity} and is available at time slots {timeSlot}")
            timeSlot.clear() #prep for next table 
        i+=1 #next table

# Level 4
    # Returns a list of table or table combinations that can seat 'party_size'.
    # Adjacent combos are determined via the table's "neighbors" list.
def openTableCombos(tables, partySize):
    timeSlot = []
    i = 1 #skip restaurant_tables[0][0]
    right = i + 1 #get rightside neighbor, only right to avoid duplicates
    count = 0 #make sure to print none is nothing available
    for table in tables: #loop through list
        if i == len(tables) - 1: #stop before out of range
            if count == 0: #check if any available tables
                print("none")
                return "none" #for unit testing
            return #end loop
        tableSplit = tables[0][i].split("(") #isolate capacity
        tableSplit2 = tableSplit[1].split(")") #isolate capacity
        tableCap = int(tableSplit2[0]) #convert capacity to int
        
        rightTableSplit = tables[0][right].split("(") #isolate neighbor capacity
        rightTableSplit2 = rightTableSplit[1].split(")") #isolate neighbor capacity
        rightTableCap = int(rightTableSplit2[0]) #convert neighbor capacity to int
        
        if (tableCap + rightTableCap) >= partySize: #check if cap meets party size
            for j in range(len(tables)): #loop through list
                if tables[j][i] == "o" and tables[j][right] == "o": #check if both tables free
                    timeSlot.append(tables[j][0]) #add time slot
                    count += 1 
                j+=1 #next time slot
            print(f"Tables {i} and {i + 1} can be pushed together to seat {tableCap + rightTableCap}, it is available at time slots {timeSlot}")
            timeSlot.clear() #prep for next table
        i += 1
        

# -----------------------------------------------------------------------------
# Example usage / testing:
if __name__ == "__main__":
    # Example data
    # unittest.main() #get familiar with testing
    getFreeTables(restaurant_tables2)
    firstOpenWithSeating(restaurant_tables2, 2)
    allOpenWithSeating(restaurant_tables2, 4)
    openTableCombos(restaurant_tables2, 10)
