import os 
import map

welcome_message = r"""
            ____                                                  
           / __ \__  __ ___  ____  ___  ____  ____  _____         
          / / / / / / / __ \/ __ `/ _ \/ __ \/ __ \/ ___/         
         / /_/ / /_/ / / / / /_/ /  __/ /_/ / / / (__  )          
        /_____/\__,_/_/ /_/\__, /\___/\____/_/ /_/____/           
                          /____/  ____                                
                                 / __ \_____ ___  ____  ____  ____  _____             
                                / / / / ___/ __ `/ __ `/ __ \/ __ \/ ___/             
                               / /_/ / /  / /_/ / /_/ / /_/ / / / (__  )              
                              /_____/_/   \__,_/\__, /\____/_/ /_/____/               
                                               /____/                                 
"""
print("===========================================================================================================")

print(welcome_message)
print("-----------------------------------By Chaitali Ingle and Chaitali Nannore----------------------------------\n")
print("===========================================================================================================")

print("> Welcome To Dungeons And Dragons!")
print("> You are locked by Goblin in Dungeuns of an abondanded castle in the middle of dense woods and a howling night")
print("> You have to escaped the Dungeon, by finding the Secret Chest gaurded by the Goblin")
print("> Kill the Goblin, and get the Keys to escape from the Chest")
print("--Further Instruction loading soon. Enter any vowel for the Instructions.--")

print("===========================================================================================================")
ans='aeiou'
bb=input('>').strip()
if bb.lower() in ans:
    os.system('Clear')

    print("===========================================================================================================\n")
    print("In Dungeons and Dragons, you are supposed to:\n")

    print("> You will be provided with a Map of the rooms in the Dungeon available for you to navigate\nBut it will not stay with you through out the game. \nMake sure to observe it well.")
    print("> Navigate through a haunted Dungeon by the command 'go <direction>")
    print("> <direction> to navigate could be North, South, East or West")
    print("> When present in a room, you will be provided Information about the items present in the room for you to pick\nAnd the items in your inventory")
    print("> To pick an item and collect it in your inventory, you need the command 'get <item>' ")
    print("> You can not collect the items if you leave the room beforehand by the 'go <direction>' command")
    print("> You need to collect the Total of 6 Items in your inventory before arriving at the Boss Room.")
    print("> In the boss room you need to fight the Goblin gaurding a Secret Chest and open it with the item 'Chest Key' collected in your inventory")
    print("> To Kill the Goblin you need the item 'Rusty Sword' collected in your inventory")
    print("> Enter any vowel to start the game! (Map will appear!)\n")
    print("==========================================================================================================")

    mapp=input('>').strip()
    os.system("Clear")

    if mapp.lower() in ans:
        map.map()
    else:
        aa=input("You did not enter x :()\nEnter 1 If that was accidental and you wish to continue or enter 2 if you want to end \n>")
        if aa=='1':
            map.map()
        else:
            print("Bye!")


