#!/usr/bin/env python3
heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
        }
all_done = False
while not all_done:
    name_done = False 
    while not name_done:
        char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz)")
        char_name = char_name.lower()
        if heroes.get(char_name) == None :
            print(f"You entered {char_name} which in a valid option, please try again")
        else :
            name_done = True
    name_done = False 
    while not name_done:
        char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")
        char_stat = char_stat.lower()
        if heroes[char_name].get(char_stat) == None :
            print(f"You entered {char_stat} which in a valid option, please try again")
        else :
            name_done = True
    print(f"{char_name.title()}'s {char_stat.title()} is: {heroes[char_name][char_stat]}")
    print()
    done_ans = input("Wolud you line to try again (Y/N) ")
    if done_ans.upper() != 'Y' :
        print("thanks for using this app, good bye!")
        all_done = True
    
