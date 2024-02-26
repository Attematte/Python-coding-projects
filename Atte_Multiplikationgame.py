
import random
print("WELCOME TO THE MULTIPLICATION GAME! :)")
print()
print("LET'S COUNT SOME MATH AND TEST YOUR MATH SKILLS!")
print()
print("BUT BEFORE WE START PLAYING THE MULTIPLICATION GAME, THERE ARE SOME RULES AND INSTRUCTIONS THAT NEEDS TO BE COVERED..")
print()
print("..AND VIOLATING THESE RULES IS STRICTLY FORBIDDEN! SO READ THE INSTRUCTIONS CAREFULLY AND ACT ACCORDINGLY!")
print()
print("RULE NUMBER ONE: DON'T USE CALCULATOR!")
print()
print("RULE NUMBER TWO: DON'T ASK HELP FROM ANYBODY ELSE!")
print()
print("INSTRUCTIONS:")
print()
print("REGARDING THE DIFFICULTY OF THE GAME YOU HAVE TWO OPTIONS:")
print()
print("AN EASY GAME WITH EASY QUESTIONS, OR A HARD GAME WITH DIFFICULT QUESTIONS. IF YOU CHOOSE THE HARD GAME AND ANSWER CORRECTLY ON THE DIFFICULT QUESTIONS..")
print()
print("YOU WILL BE ASKED EVEN MORE DIFFICULT QUESTION! WHO DOESN'T LIKE CHALLENGE ;)")
print()
print("OKAY OKAY! ENOUGH TALK, LET THE GAMES BEGIN! GOOD LUCK :)")
print()
print("Enter 1 to play EASY GAME.")
print("Enter 2 to play HARD GAME.")
print()
gamedecision = int(input("Enter your answer here: "))


def percentageCalcutor(totalcorrectanswers, totalamountQ):
    userpercentage = (totalcorrectanswers)/(totalamountQ)*100
    if userpercentage == 100:
        print()
        print("In percentages you answered 100% of all of the questions right! Congratulations!.")
        print()
        print("Your percentage was", userpercentage, "%")
        print()
        print("Are you a math genious?")
        print()
        return userpercentage
    elif userpercentage < 100 and userpercentage >= 80:
        print("In percentages you got 80 - 99% of all of the questions right.")
        print()
        print("Your percentage was", userpercentage, "%")
        return userpercentage
    elif userpercentage < 80 and userpercentage >= 70:
        print("In percentages you got 70 - 79% of all of the questions right.")
        print()
        print("Your percentage was", userpercentage, "%")
        return userpercentage
    elif userpercentage < 70 and userpercentage >= 60:
        print("In percentages you got 60 - 69% of all of the questions right.")
        print()
        print("Your percentage was", userpercentage, "%")
        return userpercentage
    elif userpercentage < 60:
        print("In percentages you got less than 60% of all of the questions right.")
        print()
        print("Your percentage was", userpercentage, "%")
        return userpercentage


def checkAnswer(answer, num5, num6):
    if answer == num5*num6:
        print()
        print("Correct answer!")
        print()
        return "correct"
    elif answer != num5*num6:
        print("Wrong answer!")
        print("The right answer is", num5*num6)
        print()
        return "false"


def easyGame(amountQ):
    correctans = 0
    for i in range(0, amountQ):
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        print("What is", num1, "*", num2, "?")
        print()
        useranswer = int(input("Enter your answer here: "))
        checkans = checkAnswer(useranswer, num1, num2)
        if checkans == "correct":
            correctans = correctans + 1
    print()
    print("Game over!")
    print("Your got", correctans, "questions right out of", amountQ, "questions :)")
    percentage = percentageCalcutor(correctans, amountQ)


def hardGame(startamountQ):
    correctans = 0
    plus_extra_Q = 0
    minus_extra_Q = 0
    for i in range(0, startamountQ):
        num3 = random.randint(10, 20)
        num4 = random.randint(10, 20)
        print("What is", num3, "*", num4, "?")
        print()
        hardanswer = int(input("Give your answer here: "))
        checkans = checkAnswer(hardanswer, num3, num4)
        if checkans == "correct":
            correctans = correctans + 1
            num7 = random.randint(20, 30)
            num8 = random.randint(20, 30)
            print("Time for a harder question! what is", num7, "*", num8)
            extraanswer = int(input("Enter your answer here: "))
            if extraanswer == num7*num8:
                print()
                print("CORRECT answer to the extra question!")
                print()
                plus_extra_Q += 1
            elif extraanswer != num7*num8:
                print()
                print("This time your answer was WRONG..")
                print("The correct answer is:", num7*num8)
                print()
                minus_extra_Q += 1
                print("Try again!")
        elif checkans == "false":
            print("Try again!")
    total_amount_extraQ = plus_extra_Q + minus_extra_Q
    totalcorrectanswers = correctans + plus_extra_Q
    totalamountQ = startamountQ + total_amount_extraQ
    print()
    print("GAME OVER!")
    print()
    print("RESULTS:")
    print()
    print("The initial amount of questions you entered was",
          startamountQ, "of which you answered", correctans, "right")
    print("And you answered", plus_extra_Q, " extra question(s) right out of the",
          total_amount_extraQ, "extra question(s)!")
    print("So in total, you answered", totalcorrectanswers,
          "question(s) right out of", totalamountQ, "question(s) :)")
    print()
    percentage = percentageCalcutor(totalcorrectanswers, totalamountQ)


def chooseGame(gamedecision):
    if gamedecision == 1:
        print()
        print("To how many questions do you want to answer?")
        print()
        rounds = int(
            input("Enter the number of questions you want to answer here: "))
        easyGame(rounds)
    elif gamedecision == 2:
        print()
        print("To how many questions do you want to answer?")
        print()
        print("Remember that if you answer correctly to these questions you will be challenged with a harder questions!")
        print()
        rounds = int(
            input("Enter the intial number of questions you want to answer here: "))
        print()
        hardGame(rounds)


chooseGame(gamedecision)


# # def outputAge(nameBirth):
# #     numberlist = []
# #     numberlist = [19] + list(range(0, 99))
# #     for name in nameBirth:
# #         if str(numberlist) in nameBirth:
# #             ageof = 2011 - int(numberlist)
# #             print(ageof)


# # first = ["John", "James", "Bill", "Arnold",
# #          "Lisa", "Ann", "Kimberly", "Monica"]
# # last = ["Smith", "Jones", "Williams", "Brown", "Wilson", "Taylor", "Johnson"]

# # for i in range(3):
# #     name = random.choice(first) + " " + random.choice(last)
# #     nameAge = name + ", 19" + str(random.randint(0, 99))
# #     print("Name and b.year:", nameAge)
# #     print("Age:", end="")
# #     outputAge(nameAge)

# # s = "My new car is Blue"
# # print(len(s))

# # myString = "abcde"
# # print(myString[1: len(myString) - 1])

# # a = "result:" + str(1 + 2)

# # print(len(a)
# #     if lst[i] < lst[i+1]:
# #         lista1 += lst[i]
# #     else:
# #             lista2 += lst[i]


# # n = [1, 2, 3, 4, 5]
# # s = 0
# # for i in range(1, len(n)):
# #     s = s + n[i]


# # n = [1, 2, 3, 4, 5]
# # m = [5, 4, 3, 2, 1]
# # i = 0
# # while n[i] < m[i]:
# #     print(n[i] * m[i])
# #     i = i + 1


# # b = range(1, 10)
# # a = [x * 2 for x in b]
# # print(a[3])

# import random
# from fractions import Fraction


# def getNumbers(listOfFractions):
#     a = []
#     b = []
#     for c in listOfFractions:
#         d = c.numerator
#         e = c.denominator
#         d in listOfFractions
#         a += [d]
#         e in listOfFractions
#         b += [e]
#     numden = a, b
#     return numden


# frac = []
# for i in range(random.randint(10, 15)):
#     f = Fraction(random.randint(1, 5), random.randint(2, 8))
#     frac.append(f)

# print("List of fractions:", frac)
# num, den = getNumbers(frac)
# print("Numerators:", num)
# print("Denominators:", den)

# a = [Fraction(4, 8), Fraction(3, 8), Fraction(2, 8), Fraction(5, 8)]
# print(a[0].numerator)
# print(a[0].denominator)
