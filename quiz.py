print("Welcome to my computer quiz game")

answer = input("Do yo want to continue? ")

if answer.lower() != "yes":
    quit()

answer = input("What is CAPTCHA in full? ")
if answer.lower() == "completely automated public turing test to tell computers and humans apart":
    print("correct")
else:
    print("Incorrect")

answer = input("What is HTML in full? ")
if answer.lower() == "hypertext markup language":
    print("correct")
else:
    print("Incorrect")
