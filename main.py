# Filename: main.py (or any file of your choice)
# -----------------------------------------------------------------------------
# DISCLAIMER:
# This code is an EXAMPLE solution for reference/study purposes ONLY.
# Submitting it as your own may violate assignment rules against plagiarism
# or AI-generated solutions. Use it ethically and responsibly.
# -----------------------------------------------------------------------------
from restaurantTables import restaurant_tables

    
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
       

 # Level 2
    # Returns the first table ID that can seat 'party_size' and is free,
    # or None if none found.  
def firstOpenWithSeating(tables, partySize):
    timeSlot = []
    goodTable = 0
    i = 1
    while goodTable < partySize:
        if i >= len(tables):
            print("None")
            return
        tableSplit = tables[0][i].split("(")
        tableSplit2 = tableSplit[1].split(")")
        goodTable = int(tableSplit2[0])
        # if goodTable < partySize:
        #     i+=1
        #     print(f"{tableSplit[0]} can seat {goodTable} people")
    
    for j in range(len(tables)):
        if tables[j][i] == "o":
            timeSlot.append(tables[j][0])
            j+=1
    print(f"Table {i} can seat {goodTable} and is available at time slots {timeSlot}")


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
            return
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
    for table in tables:
        if i == len(tables) - 1:
            return
        tableSplit = tables[0][i].split("(")
        tableSplit2 = tableSplit[1].split(")")
        goodTable = int(tableSplit2[0])
        # print(f"main table {i}: {goodTable}")
        
        rightTableSplit = tables[0][i+1].split("(")
        rightTableSplit2 = rightTableSplit[1].split(")")
        rightTableCap = int(rightTableSplit2[0])
        # print(f"right neighbor: {rightTableCap}")
        
        if (goodTable + rightTableCap) >= partySize:
            for j in range(len(tables)):
                if tables[j][i] == "o" and tables[j][i+1] == "o":
                    timeSlot.append(tables[j][0])
                j+=1
            print(f"Tables {i} and {i + 1} can be pushed together to seat {goodTable + rightTableCap}, it is available at time slots {timeSlot}")
            timeSlot.clear()
        i += 1

# -----------------------------------------------------------------------------
# Example usage / testing:
if __name__ == "__main__":
    # Example data

    # getFreeTables(restaurant_tables)
    firstOpenWithSeating(restaurant_tables, 2)
    # allOpenWithSeating(restaurant_tables, 10)
    # openTableCombos(restaurant_tables, 7)
