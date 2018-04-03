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
# Map on Keybind + Red              | Medium        | 4/5       | Both      | 
# Win Condition on Blue             | Medium        | 4/5       | Both      |
# Can't walk through walls          | Medium        | 4/5       | Both      | 
# Instructions on startup && h      | Easy          | 4/5       | Bobby     |
# Battery Life                      | Medium        | 4/5       | Bobby     | 

