import turtle
import random
from func import*

wordFile = open("words.txt", "r")
fileData = wordFile.read()
words = fileData.splitlines()
word = random.choice(words)

length = 60
border = 7
startingX = -175
startingY = 200
numTries = 6
wordGuessed = False

bgColor = "#2c2b2e"
defaultColor = "#5c5c5e"
winningColor = "#77fafc"
colorAccuracy = [defaultColor, "#07fc03", "#068f1a"]
accuracy = ["red", "red", "red", "red", "red"]
allColors = [bgColor, defaultColor, accuracy]

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.bgcolor(bgColor)

board(t, startingX, startingY, length, border, defaultColor)

while not wordGuessed and numTries > 0:
  guess = "abc"

  while len(guess) != 5:
    guess = input("\nGuess a five letter word: ")

  if guess == word:

    print("\nYOU WIN!")
    for i in range(len(word)):
      accuracy[i] = winningColor
    wordGuessed = True

  else:

    numTries -= 1
    for i in range(len(word)):

      if guess[i] == word[i]:
        accuracy[i] = colorAccuracy[2]
      elif guess[i] in word:
        accuracy[i] = colorAccuracy[1]
      else:
        accuracy[i] = colorAccuracy[0]

  row(t, startingX, startingY, length, border, defaultColor, guess, bgColor, accuracy)
  startingY -= length + border

turtle.exitonclick()