def init():
    # Size of the user's screen
    global screenSize
    screenSize = 1024

    # Multiplier for Dungeon to make the rooms larger than 1 by 1 pixels
    global dunMultiply
    dunMultiply = 4

    # Dungeon Area to Achieve
    global dunSize
    dunSize = 1250 * (dunMultiply * dunMultiply)


# To do
# Item                              | Difficulty    | Timeframe | Assigned  | Status
# Correct the push out spacing      | Medium        | 3/29      | Bobby     | Done
# Save Image if Expanding offscreen | Hard          | 3/29      | Bobby     | Done
# Implement Scaling                 | Easy          | 3/29      | Eric      | Done
# Implement Moving                  | Easy          | 3/29      | Eric      | Done
# Input Tiles                       | Medium        | 3/29      | Eric      | ----
# Green Dots on first room            | Easy          | 3/29    | Bobby     | Done 
# Red Dot in last room              | Easy          | 3/29      | Bobby     | Done
# Map in first room                 | Easy          | 4/5       | Eric      | 
# Can't Walk through walls          | Medium        | 4/5       | Bobby     | 
# Terrain only when Flashlight      | Medium        | 3/31      | Eric      | Done
# Menu                              | Easy          | 4/11      | Bobby     | ----
    # Restart
    # Quit
    # How To

