print(f"Hello! I have a cute story about a Teacup Piglet.  I am excited to tell it!  ")
print(f"Before the story gets started, I have several questions for you to answer. ")
print(f"After typing your answer, please be sure to press the enter key. ")
input(f"\nPress the enter key to continue... ")

keepPlaying = "y" 
while keepPlaying.lower() == "y":

    pigletName = input("\nWhat is the Teacup Piglet's name? ")
    
    while len(pigletName) == 0:
        pigletName = input(f"Please enter a name:  ")
    room = input("\nWhat room is the Teacup Piglet's pen in? ")
    
    while len(room) == 0:
        room = input(f"Please enter a room: ")
    toy = input("\nWhat is the Teacup Piglet's favorite toy? ")
    
    while len(toy) == 0:
        toy = input(f"Please enter a toy: ")
    nap = input("\nHow many minutes is the Teacup Piglet's nap? ")
    
    while not nap.isdigit():
        nap = input(f"Value not recognized. Please enter a numeric value: ")
    yourName = input("\nWhat is your name? ")
    
    while len(yourName) == 0:
        yourName = input(f"Please enter your name: ")

    print(f"\nLet's go!! ")
    print(f"Once there was a beautiful Teacup Piglet named {pigletName}. ")
    print(f"The piglet was taking a {nap} minute nap and wants to get free from it's pen. ")
    print(f"{pigletName} notices it's pen is open. Here is the chance to be mischievious! ")
    print(f"{pigletName} runs out of it's pen and sees a basket of it's toys. It squeals with excitment! ")
    print(f"It sees its favorite toy {toy} in it's basket of toys! ")

    knockOverBasket = input(f"\nShould {pigletName} knock over it's basket of toys? Type yes or no: ")
    while knockOverBasket.lower() != "yes" and knockOverBasket.lower() != "no":
        knockOverBasket = input("Please type yes or no: ")
    if knockOverBasket == "yes":
        print(f"\n{pigletName} knocks over the basket of toys to play with the {toy}.")
        print(f"\nWhen it grabs it's toy, it squeals with joy. Weee weeee weeee! ")
        print(f"\nIt rolls around in {room} and has a fun time away from the pen!")
    else:
        print(f"\n{pigletName} decides that the {room} is already clean and does not want")
        print(f"\nto risk messing up the room that it's human, {yourName}, worked so hard to clean up!")
        print(f"\nUnfortunately, there is nothing else to do in the {room}.")
        print(f"\n{pigletName} decides to walk the home and exit the {room}.  ")

    walkThroughDoggieDoor = input(f"\nShould {pigletName} go through the opened doggie door? Type yes or no: ")
    while walkThroughDoggieDoor.lower() != "yes" and walkThroughDoggieDoor.lower() != "no":
        walkThroughDoggieDoor = input(f"PLease type yes or no:  ")

    if walkThroughDoggieDoor == "yes":
        print(f"\n{pigletName} walks up to the doggie door!  It's unlocked and open. It walks through!")
        print(f"\nIt is muddy outside. {pigletName} squeals with anticipation of rolling around in the mud!")
        print(f"\nIt jumps up and down and rolls all around in the mud. {pigletName} loves splashing in the mud!")
    else:
        print(f"\nIt decides not to go through the door. The piglet sees {yourName} and is too afraid to go outside")
        print(f"\nto get all muddy because it would have to take a bath to get cleaned up. It turns around and")
        print(f"\n{yourName} picks {pigletName} up!")

    if knockOverBasket == "yes" and walkThroughDoggieDoor == "yes":
        print(f"\nAfter spending the afternoon sneaking out of it's pen, knocking over it's basket of toys to play,")
        print(f"\nand splashing around in the mud, it is happy, tired, muddy little piglet.  {yourName} picks it up")
        print(f"\nand gives {pigletName} a bath and puts it to bed in it's pen!")
    elif knockOverBasket == "no"and walkThroughDoggieDoor == "no":
        print(f"\n{pigletName} spent the day walking around the house. It made good decisions and did not get into")
        print(f"\nany trouble. {pigletName} gets to cuddle with it's human parent {yourName}!")
    else:
        print(f"\nAfter spending the day having some fun, {pigletName} gets fed it's dinner, and has a bath.")
        print(f"\n{yourName} places {pigletName} into it's pen for bedtime.")
    print("\nThe End")
    
    keepPlaying = input("Do you want to play again? Enter y or n:  ")
    while keepPlaying.lower() not in ["y", "n"]:
        keepPlaying = input("Please type y or n:  ")
