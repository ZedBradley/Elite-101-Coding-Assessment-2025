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
    for j in range(len(tables)):
        for i in range(len(tables[j])):
            if tables[i][j] == "o":
                freeTables.append(tables[i][0])
        if len(freeTables) > 0:
            print(f"Table {j} is available at time slot {freeTables}")
        freeTables.clear()
    return "yes"
       

 # Level 2
    # Returns the first table ID that can seat 'party_size' and is free,
    # or None if none found.  
def firstOpenWithSeating(tables, partySize):
    timeSlot = []
    capacity = 0
    i = 1
    while capacity < partySize:
        if i >= len(tables):
            print("None")
            return "none"
        tableSplit = tables[0][i].split("(")
        tableSplit2 = tableSplit[1].split(")")
        capacity = int(tableSplit2[0])
        if capacity < partySize:
            i+=1

    for j in range(len(tables)):
        if tables[j][i] == "o":
            timeSlot.append(tables[j][0])
            j+=1
    print(f"Table {i} can seat {capacity} and is available at time slots {timeSlot}")
    

# Level 3
    # Returns a list of all table IDs that can seat 'party_size' and are free.
def allOpenWithSeating(tables, partySize):
    timeSlot = []
    goodTable = 0
    i = 1
    count = 0
    for table in tables:
        if i >= len(tables):
            if count == 0:
                print("None")
                return "none"
        tableSplit = tables[0][i].split("(")
        tableSplit2 = tableSplit[1].split(")")
        goodTable = int(tableSplit2[0])
        if goodTable >= partySize:
            for j in range(len(tables)):
                if tables[j][i] == "o":
                    timeSlot.append(tables[j][0])
                    j+=1
                    count += 1
            print(f"Table {i} can seat {goodTable} and is available at time slots {timeSlot}")
            timeSlot.clear()
        i+=1

# Level 4
    # Returns a list of table or table combinations that can seat 'party_size'.
    # Adjacent combos are determined via the table's "neighbors" list.
def openTableCombos(tables, partySize):
    timeSlot = []
    i = 1
    left = i - 1
    right = i + 1
    count = 0
    for table in tables:
        if i == len(tables) - 1:
            if count == 0:
                print("none")
                return "none"
            return
        tableSplit = tables[0][i].split("(")
        tableSplit2 = tableSplit[1].split(")")
        goodTable = int(tableSplit2[0])
        
        rightTableSplit = tables[0][i+1].split("(")
        rightTableSplit2 = rightTableSplit[1].split(")")
        rightTableCap = int(rightTableSplit2[0])
        
        if (goodTable + rightTableCap) >= partySize:
            for j in range(len(tables)):
                if tables[j][i] == "o" and tables[j][i+1] == "o":
                    timeSlot.append(tables[j][0])
                    count += 1
                j+=1
            print(f"Tables {i} and {i + 1} can be pushed together to seat {goodTable + rightTableCap}, it is available at time slots {timeSlot}")
            timeSlot.clear()
        i += 1
        

# -----------------------------------------------------------------------------
# Example usage / testing:
if __name__ == "__main__":
    # Example data
    unittest.main()
    # getFreeTables(restaurant_tables2)
    # firstOpenWithSeating(restaurant_tables2, 2)
    # allOpenWithSeating(restaurant_tables2, 4)
    # openTableCombos(restaurant_tables2, 5)
