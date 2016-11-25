

health = 10
power = 10

from random import randint

def statusbar():

   print("\n"*3)
   print ("********************************************************************************************************")
   print (" HEALTH:", health,        "========="          "POWER:", power)                                                         
   print ("********************************************************************************************************")
   print ("")
   
def room1():
    global health
    global power

    statusbar()

    print ("You awake in a cold, damp basement")
    print ("A. explore")
    print ("B. cry for help")
    answer = input ("what would you Do: ")

    if answer.lower() == "b":
        print ("suck it up and explore!")
        room1()

    elif answer.lower() == "a":
        print ("Let's go!")
        room2()


def room2():
    global health
    global power

    statusbar()

    print ("You enter a room, you hear a noise from a tunnel opening behind you")
    print ("A. Run back")
    print ("B. Go follow the noise")
    answer = input ("What would you do: ")

    if answer.lower() == "a":
        print ("you trip and fall on your arm")
        health = health - 1
        print("Health remaining:", health)
        room1()
   

    elif answer.lower() == "b":
        print ("theres 4 tunnels. Which one has the monster inside")
        room3()

def room3():
    global health
    global power

    statusbar()

    print ("1. Go into the tunnel on your right")
    print ("2. Go into into the tunnel on your left")
    print ("3. go into the tunnel behind you")
    print ("4. go into the tunnel infront of you")
    answer = input ("Choose one: ")

    if answer == "3":
        print ("you're in need of food")
        power = power = power - 1


        print ("find food")
        room4()


    else:
        print ("No entry")
        room3()


def room4():
    global health
    global power

    statusbar()

    print ("As you are eating you hear the noise again!")
    print ("Choose your option")
    print ("A. turn back")
    print ("B. investagate")
    answer = input ("which path will you take? :")

    if answer.lower() == "a":
        print ("too scary?")
        room1()

    elif answer.lower() == "b":
        print ("We need to find clues")
        room5()


def room5():
    global health
    global power

    statusbar()

    print ("you see a large box")
    print ("do you...")
    print ("A. open with caution")
    print ("B. yank it open")
    answer = input ("choose: ")

    if answer.lower() == "a":
        print ("the box opens")
        room6()

    elif answer.lower() == "b":
        print ("the box opens")
        room6()

def room6():
   global health
   global power

   statusbar()

   print ("You approach a locked door but you remember that there was a key in the box")
   print ("A. Grab the key")
   print ("B. look around for other clues -unnsuccesful-")
   answer = input ("Which option: ")

   if answer.lower()== "a":
      room7()

   elif answer.lower() == "b":
      room6()



def room7():
    global health
    global power

    statusbar()

    print ("the key fits the lock!")
    
    print ("A. ooooo!")
    print ("B. lets open the  door!")
    answer = input ("Which one: ")

    if answer.lower() == "a":
        print ("lets open the door shall we?")
        room8()

    elif answer.lower()== "b":
        print ("lets open the door then")
        room8()


def room8():
    global health
    global power

    statusbar()
            
    print ("oh no, the noise is coming from behind the door!")
    print ("A. quit game now and start from the beggining")
    print ("B. carry on with your mission and go in the door")
    
    answer = input ("Which one: ")

    if answer.lower() == "a":
               print ("Fair enough")
               room1()

    elif answer.lower() == "b":
               print ("lets carry on!")
               room9()

def room9():
    global health
    global power

    statusbar()

    print ("The monster jumps out from behind the door!")
    print ("A. Run!")
    print ("B. lets battle")
    answer = input ("Which one: ")

    if answer.lower() == "a":
        print ("Remember, you have only got limited health and power")
        room10()

    elif answer.lower() == "b":
        print ("Theres no choice now!")
        room10()


def room10():
    global health
    global power

    statusbar()

    print ("He runs at you...")
    print ("A. dodge")
    print ("B. hit")
    answer = input ("Attack or defence: ")

    if answer.lower()== "a":
        print ("You dodge succesfully")
        room11()

    elif answer.lower()== "b":

        hit = randint(1, 2)
        if hit == 1:
            print ("you missed and he hit you!")
            health = health - 1
            power = power - 1
        else:
             print("You hit the monster")         
          
        room11()


def room11():
   global health
   global power

   statusbar()

   print ("You have some health remaining, try and take down the monster")
   print ("A. punch him in the face")
   print ("B. Dodge him as he leans in for a punch")
   answer = input ("Quick: ")

   if answer.lower()== "a":
       print ("you punched him and he's on his last leg")
       room12()

   elif answer.lower()== "b":
        print ("UNSUCCESSFUL")
        health = health -1
        power = power - 1
        room12()

def room12():
    global health
    global power

    statusbar()

    print ("As the monster is looking quite frazzled, I think you should attack once more")
    print ("A. a massive blow to the stomach!")
    print ("B. a massive blow to the head!")
    answer = input ("Hurry while he's still frazzled: ")

    if answer.lower()== "a":
        print ("He falls! You can quickly escape")
        room13()

    elif answer.lower()== "b":
        print ("He falls and cries, you feel bad but should move on!")
        room13()
        
    


def room13():

   
    global power
    global health

    statusbar()

    print ("You run out of the door that awaits you at the end of the room!But...")
    print ("The monster has awaken and he's lookng for you!")
    print ("A. Look for clues to help you escape him once more")
    print ("B. See if your key helps you find out what he wants")
    answer = input ("Choose: ")

    if answer.lower()== "a":
        print ("you then go to through the door, there is a large chest with some locks")
        room14()

    elif answer.lower()== "b":
        print ("you go back to the room, but, he want's a fight")
        room9()

def room14():
    global power
    global health

    statusbar()

    print ("you try the key from the locked door in on of the pad locks and it opens one, but, others have number lock")
    print ("Can you remember what answer you chose for question 3, that may be the first number...")
    print ("A. 2")
    print ("B.3")
    print ("C. 7")
    answer = input ("How good is your memory: ")

    if answer.lower()== "b":
       print ("you remembered,you put the first number into the lock")
       room15()

    else:
      print ("Wrong, try again")
      room14()
      

def room15():
    global health
    global power

    statusbar()

    print ("now you have the first number, the second and third number is the amount of questions there are")
    print ("Can you remember how many questions there are SO FAR")
    print ("A. 13")
    print ("B. 16")
    print ("C. 15")
    answer = input ("Can you remember: ")

    if answer.lower()== "c":
       print ("correct, the key code is:     315")
       room16()

    else:
      print ("Try again")
      room15()

def room16():
   global health
   global power

   statusbar()

   print ("You try all the locks, they're the same code")
   print ("Inside the box, theres a letter")
   print ("it reads")
   print ("\n")
   print ("DEAR WHOEVER OPENED THIS BOX, WELCOME, NOW,YOU NEED TO CONCERNTRATE IN NOT LOOSING ALL HEALTH AND POWER")
   print ("USE THE KEY, INSIDE THIS LETTER, AND OPEN THE SECOND DOOR TO YOUR LEFT AND FIND TH NEXT CLUE")
   print ("\n")
   print ("A. go and open the first door on your left")
   print ("B. go and open the second door on your left")
   answer = input ("Memnory games: ")

   if answer.lower()== "b":
      print ("Enter the door")
      print ("you get a pain")
      health = health - 3
      room17()

   elif answer.lower()== "a":
      health = health - 2
      power = power - 2
      room17()

def room17():
    global health
    global power

    statusbar()

    print ("a voice plays on a speaker in the room")
    print ("\n")
    print ("YOU HAVE LIMITED HEALTH,IF YOU HEALTH IS LOWER THAN 6, YOU DIE")

    statusbar()

    if health < 6:
       print ("YOU DIE")

    elif health > 6:
      print ("YOU LIVE")

      

   

    
        















if __name__ == "__main__":
    room1()
