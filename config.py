def init():
    # Size of the user's screen
    global screenSize
    screenSize = 1000

    # Multiplier for Dungeon to make the rooms larger than 1 by 1 pixels
    global dunMultiply
    dunMultiply = 5

    # Dungeon Area to Achieve
    global dunSize
    dunSize = 1000 * (dunMultiply * dunMultiply)