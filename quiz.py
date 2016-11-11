# Our quiz!



score = 0
name = ""




def quiz():
    global score
    global name

    name = input ("Enter your name: ")

    question1()
    question2()
    question3()
    question4()
    question5()
    question6()
    question7()
    question8()
    question9()



def question1():
    global score

    print (name, "Who is the lead singer of The1975")
    print ("A. Vann McCann")
    print ("B. Matthew Healy")
    print ("C. Patrick Stump")
    answer = input("Select an option: ")

    if answer.lower() == "b":    #this makes sure it's case insentitive 
        score = score + 1

    print("Score:", score)

def question2():
    global score 

    print ("How many albums has The1975 released")
    print ("A. 1")
    print ("B. 4")
    print ("C. 2")
    answer = input("Select an option: ")

    if answer.lower() == "c":
        score = score + 1    # this is the score added for each question 

    print ("Score:", score)

def question3():
    global score 

    print (name , "What is the lead singer of Arctic Monkeys")
    print ("A. Alex Turner")
    print ("B. Matthew Healy")
    print ("C. Oliver Sykes")
    answer = input("Select an option: ")

    if answer.lower() == "a":
        score = score + 1

    print ("Score:", score)

def question4():
    global score 

    print ("Have I got any pets")
    print ("A. No")
    print ("B. you hate animals")
    print ("C. yes")
    answer = input("Select an option: ")

    if answer.lower() == "c":
        score = score + 1

    print ("Score:", score)     #prints the score for the user 

def question5():
    global score 

    print ("ROUND TWO")
    print (name , "This game is going to get harder now!")
    print ("What is the answer to 15 x 15")
    print ("A. 2225")
    print ("B. 225")
    print ("C. 257")
    answer = input("Select an option: ")

    if answer.lower() == "b":
        score = score + 1

    print ("Score:" , score)

def question6():
    global score 

    print ("What is the name of a standard computer keyboard")
    print ("A. Qwerty keyboard")
    print ("B. Apple Keyboard")
    print ("C. Standard keyboard")
    answer = input("Select an option: ")

    if answer.lower() == "a":
        score = score + 1

    print ("Score:" , score)


def question7():
    global score 

    print (name , "How many rabbits have I got")
    print ("A. 4")
    print ("B. 3")
    print ("C. You don't have any")
    print ("D. 2")
    answer = input("Select an option: ")     # this gives the user an input option 

    if answer.lower() == "d":
        score = score + 1

    print ("Score:" , score)

    print ("Well done, you have completed the first 2 rounds! Round of applause!")


def question8():
    global score 

    print ("What colour theme is my room")
    print ("A. yellow")
    print ("B. green")
    print ("C. blue")
    answer = input("Select an option: ")

    if answer.lower() == "b":
        score = score + 1

    print ("Score:" , score)


    print ("Who has recently been elected for president" , name)
    print ("A. Donald Trump, unfortunatley")
    print ("B. Hilary Clinton")
    print ("C. Bernie Sanders")
    amswer = input("Select an option: ")

    if answer.lower() == "a":
        score = score + 1

    print ("Score:" , score)


def question9():
    global score

    print ("How many terms does a United States president serve")
    print ("A. 4")
    print ("B. 2")
    print ("C. 1")
    answer = input("Select an option: ")

    if answer.lower() == "b":
        score = score + 1

    print ("Score:" , score)


def question10():
    global score

    print ("How did you feel about this quiz!")
    print ("A. amazing")
    print ("B. Ok")
    print ("C. Bad")
    answer = input ("Select an option: ")

    if answer.lower() == "a":
        score = score + 1

    print ("Score:" , score, "Thankyou")



# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
