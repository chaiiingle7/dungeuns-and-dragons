import os
import navigation

def map(): 
    print("=================================================================================")
    print("   _____________                               _____________      _____________")
    print("  |             |                             |             |    |             |")
    print("  |   Armory    |                             |   Library   |====|    Study    |")
    print("  |_____________|                             |_____________|    |_____________|")

    # Vertical Paths
    print("        ||                                          ||")
    print("        ||                                          ||")

    # Row 2
    print("   _____________         _____________         _____________      _____________")
    print("  |             |       |             |       |             |    |             |")
    print("  | Prison Cell |=======|  Grand Hall |=======|   Shrine    |====|  Boss Room  |")
    print("  |_____________|       |_____________|       |_____________|    |_____________|")

    # Vertical Paths
    print("        ||                    ||                                       ||")
    print("        ||                    ||                                       ||")

    # Row 3
    print("   _____________         _____________                            _____________")
    print("  |             |       |             |                          |             |")
    print("  | Ancient Tomb|       |   Pantry    |                          |    Foyer    |")
    print("  |_____________|       |_____________|                          |_____________|")

    # Exit Path
    print("                                                                       ||")
    print("                                                                       \\/")
    print("                                                                     EXIT!!")
    print("=================================================================================")
    print("Here is the Map, observe well! Enter x when you're ready to start the game!")
    print("==================================================================================")
    enter=input('>').strip()
    ans='x'
    if enter.lower()==ans:
           os.system("Clear")
           navigation.nav('Prison Cell', 0)
    else:
          print('You were supposed to print x!')

    


