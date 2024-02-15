import random
topRange = input("Enter a number: ")

if topRange.isdigit():
    topRange = int(topRange)
    if topRange<= 0:
        print("Enter a number larger than zero")
        quit()
else:
        print("Enter a number next time")
        quit()
random_number = random.randint(0, topRange)
guess_number =0
while True:
     guess_number+=1
     guesss = input("make a guess ")
     if guesss.isdigit():
        guesss = int(guesss)
     else:
          print("Enter a number next time")
          continue
     if guesss==random_number:
          print("you got it!")
          break
     else:
          print("you got it wrong!")

print("you got it after", guess_number,"attempts")

    