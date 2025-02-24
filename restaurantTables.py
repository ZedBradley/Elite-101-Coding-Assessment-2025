# ------------------------------------------------------------------------------------
# The following 2D lists mimic a restaurant seating layout, similar to a grid.
# 
# - Row 0 is a "header row":
#     - The first cell (index 0) is just a row label (0).
#     - The remaining cells are table labels with capacities in parentheses,
#       e.g., 'T1(2)' means "Table 1" has capacity 2.
#
# - Rows 1 through 6 each represent a distinct "timeslot" or "seating period":
#     - The first cell in each row (e.g., [1], [2], etc.) is that row's label (the timeslot number).
#     - Each subsequent cell shows whether the table (from the header row) is
#       free ('o') or occupied ('x') during that timeslot.
#
# In other words, restaurant_tables[row][column] tells you the status of a
# particular table (column) at a particular timeslot (row).
# ------------------------------------------------------------------------------------

# Shows the structure of the restaurant layout with all tables free ("o" = open).
restaurant_tables = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'o',      'o',      'o',      'o',      'o',      'o'],
    [2,        'o',      'o',      'o',      'o',      'o',      'o'],
    [3,        'o',      'o',      'o',      'o',      'o',      'o'],
    [4,        'o',      'o',      'o',      'o',      'o',      'o'],
    [5,        'o',      'o',      'o',      'o',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'o',      'o']
]

# ------------------------------------------------------------------------------------
# This second layout serves as a test case where some tables ('x') are already occupied.
# Use this for testing your logic to:
#   - Find free tables (marked 'o')
#   - Check if those tables meet a certain capacity (from the header row, e.g. 'T1(2)')
#   - Potentially combine adjacent tables if one alone isn't enough for a larger party.
# ------------------------------------------------------------------------------------



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
    
    # Level 3
    # Returns a list of all table IDs that can seat 'party_size' and are free.
    
    # Level 4
    # Returns a list of table or table combinations that can seat 'party_size'.
    # Adjacent combos are determined via the table's "neighbors" list.
    
    # Example output structure:
    # [(1,), (3,), (1,2), (3,5)]  # Each tuple is a single table or a pair.
  
    # Bonus:
    # Takes the combos from Level 4 (like [(1,), (2,), (1,2)]) and
    # prints a more user-friendly message about each result.

