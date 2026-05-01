import random 
import os

rooms={
              'Armory':{'South':'Prison Cell','Item': 'Rusty Sword'},
              'Library':{'South':"Shrine", 'East':'Study Room', "Item":'Manuscript'},
              'Shrine':{'North':'Library', 'East':"Boss Room", 'West':'Grand Hall', 'Item':"A Broken Idol"},
              'Ancient Tomb': {'North':'Prison Cell', 'Item':'A Skull'},
              'Prison Cell':{'North':'Armory', 'East':"Grand Hall", 'South':'Ancient Tomb', 'Item':'Chainsaw'},
              'Pantry':{'North':'Grand Hall'},
              'Boss Room': {'South':'Foyer', 'West':'Shrine', 'Boss':"Dragon", 'Secret':"Chest"},
              'Study Room':{'West':'Library', 'Item':'Chest Key'},
              'Grand Hall':{'South':'Pantry', 'East':'Shrine', 'West':'Prison Cell'},
              'Foyer':{'South':"Exit"}
       }


# inventory=[]
# vowel='aeiou'
# current_room='Prison Cell'
# strength=0


def nav(current_room, strength):
       inventory=[]
       vowel='aeiou'
       # current_room='Prison Cell'
       # strength=0

       
       run=True
       while run and current_room!='Foyer' and current_room!='Boss Room':
                     print("======================================================================")
                     print(f"You are in {current_room}")
                     print(f"Inventory: {inventory}")
                     print(f"Strength points: {strength}")
                     if 'Item' in (rooms[current_room]).keys():
                            print(f"{current_room} has the item: {rooms[current_room]['Item']}")
                     else:
                            print("This room has No Items")

                     print("Enter any non-vowel to roll a dice")

                     print("======================================================================")


                     cc=input('>').strip()
                     if cc.lower() not in vowel:
                            point=random.randint(1,20)
                            print(f"Dice says: {point}")
                            strength=strength+point
                            print(f"Total Strength point: {strength}")

                     
              
                     ans=input("Enter a command\n>").split(' ', 1)

                     if ans[0]=='get':
                                   if 'Item' not in (rooms[current_room]).keys():
                                          print("There are no Items here")
                                   elif ans[1] not in rooms[current_room]['Item']:
                                          print("No such item exists here")
                                   else:
                                          if ans[1] not in inventory:
                                                 inventory.append(ans[1])
                                                 print(f"You have acquired {rooms[current_room]['Item']}")
                                          else:
                                                 print(f"You already have {rooms[current_room]['Item']} in your inventory")
                                          

                     elif ans[0]=='go':
                            if ans[1] in rooms[current_room].keys():
                                   current_room=rooms[current_room][ans[1]]

                            else:
                                   print("No room in that direction")
                            
                     elif ans[0]=='exit':
                                   print("Bye, see you again")
                                   run=False
                     else:
                                   print("You are allowed only get, go and exit command")

                     print("======================================================================")
                            #aa=input('Enter 0 to continue').strip()
                            #if aa=='0':
                     os.system('clear')
              

       
       else:
              if current_room=='Boss Room':
                     print("======================================================================")
                     print(f"You are in {current_room}")
                     print(f"Inventory: {inventory}")
                     print(f"Strength points: {strength}")
                     print("This room contains the Secret Chest with the mystical key to escape, and the Goblin ready to kill you!")
                     print("---------------------------------------Beware!--------------------------------------")
                     print("Goblin has spotted you! You need to kill the Goblin with the item 'Rusty sword' and 99 strenth points\nto open the chest with the item 'Secret Key' and finally escape the foyer using 19 more points \nif you have all the 6 items in the inventory")
                     print("------------------------------------------------------------------------------------")
              
                     if len(inventory)==6 and 'Rusty Sword' in inventory and strength>=99:
                            
                            print("Enter the smallest armstrong number to kill the Goblin!")
                            ss=input(">").strip()
                            os.system("Clear")
                            if ss=='0':
                                   print("==============================================================================================")
                                   inventory.remove("Rusty Sword")
                                   strength=strength-99
                                   print(f"You are in {current_room}")
                                   print(f"Inventory: {inventory}")
                                   print(f"Strength points: {strength}")
                                   print("That was an intense battle! You have a bad wound on your knee but you slayed the Goblin!")
                                   
                            
                                   print(r"                             ,      ,")
                                   print(r'                            /(.-""-.)\ ')
                                   print(r"                        |\  \/      \/  /|  ")            
                                   print(r"                        | \ / =.  .= \ / |    ")          
                                   print(r"                        \( \   o\/o   / )/     ")                                      
                                   print(r"                         \_, '-/  \-' ,_/ ")
                                   print(r"                           /   \__/   \  ")
                                   print(r"                           \ \__/\__/ /")
                                   print(r"                         ___\ \|--|/ /___")
                                   print(r"                       /`    \      /    `\ ")
                                   print(r"                      /       '----'       \ ")
                                   print("You need to sacrifice 19 strength point and knowledge from the manuscript to first aid your wound")
                                   print("Enter last letter in alphabet to sacrifice")
                                   print("==============================================================================================")
                                   ans=input(">").strip()
                                   os.system("Clear")
                                   if ans.lower()=='z' and strength>=19:
                                          strength-=20
                                          inventory.remove("Manuscript")
                                          print(f"You are in {current_room}")
                                          print(f"Inventory: {inventory}")
                                          print(f"Strength points: {strength}")
                                          print("That was impressive! You can finally stand up and hopefully can walk too.\nWait.. Do you see that? The Chest! \nIt's right there! Let's open it and escape this Dungeon once and for all!")
                                          print("Enter SS to use the item Chest key from your inventory to open the chest!")
                                          
                                          print("==========================================================================================================")
                                          ans=input(">").strip()
                                          os.system("Clear")
                                          if ans.lower()=='ss':
                                                 print("==========================================================================================================")
                                                 inventory.remove("Chest Key")
                                                 print(f"You are in {current_room}")
                                                 print(f"Inventory: {inventory}")
                                                 print(f"Strength points: {strength}")
                                                 print("THE CHEST HAS THE MYSTICAL KEYS, LETS GO RUN.\nFind the Foyer and hence the Exist through the 'go <direction>' command")
                                                 run=True
                                                 while run:
                                                               ans=input("Enter a go command\n>").strip()
                                                               print("===========================================================================================================")
                                                               if ans=='go South':
                                                                      print("You're in the Foyer, yay!!")
                                                                      current_room='Foyer'
                                                                      run=False

                                                               else:
                                                                      print("Foyer is'nt in that direction, try again")
                                                               
                                                 # else:
                                                 #        print("You were supposed to enter a go command. Bye!")
                                                 #        nav("Shrine", strength)
                                                        
                                                  
                                          else:
                                                 print("You were supposed to enter the mentioned command! Now bye!")
                                   else:
                                          print("Insuffient strenth points or wrong command, you are back to the previous room!")
                                          nav("Shrine", strength)
                            
                            
                     else:
                            print("You are not eligible to Kill the goblin! You will be returned back to you previous room!")
                            nav("Shrine", strength)
                     
     
              if current_room=='Foyer':
                     print("YOU DID IT! NOW FINALLY, FIND THE EXIT USING GO COMMAND AGAIN!")
                     run=True
                     while run:
                                                               ans=input("Enter a go command\n>").split(' ', 1)
                                                               print("===========================================================================================================")
                                                               if ans[1]=='South':
                                                                      print("YOU ESCAPED AND WON!! YAY")
                                                                      print("You are the true legend ffrfrffrf")
                                                               
                                                                      run=False

                                                               else:
                                                                      print("You're so close yar, try again!")
                                                                      
