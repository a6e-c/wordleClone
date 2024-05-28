import turtle

def square(t, x, y, length, color):
  t.penup()
  t.goto(x,y)
  t.color(color)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
    t.fd(length)
    t.rt(90)
  t.end_fill()

def animate(t, x, y, length, bgColor, oldColor, newColor):
  oneSixth = length/6
  a = turtle.Turtle()
  a2 = turtle.Turtle()
  a.hideturtle()
  a2.hideturtle()
  a.speed(0)
  a2.speed(0)

  square(t, x, y, length + 1, bgColor)
  square(a2, x, y, length + 1, oldColor)

  a.color(oldColor)
  a.penup()
  a.begin_fill()
  a.goto(x, y - oneSixth)
  a.goto(x + length, y - oneSixth)
  a.goto(x + length, y - oneSixth * 5)
  a.goto(x, y - oneSixth * 5)
  a.goto(x, y - oneSixth)
  a.end_fill()
  a2.clear()

  a2.color(oldColor)
  a2.penup()
  a2.begin_fill()
  a2.goto(x, y - oneSixth * 2)
  a2.goto(x + length, y - oneSixth * 2)
  a2.goto(x + length, y - oneSixth * 4)
  a2.goto(x, y - oneSixth * 4)
  a2.goto(x, y - oneSixth * 2)
  a2.end_fill()
  a.clear()

  a.color(newColor)
  a.penup()
  a.goto(x, y - oneSixth * 3)
  a.pendown()
  a.goto(x + length, y - oneSixth * 3)
  a2.clear()

  a2.color(newColor)
  a2.penup()
  a2.begin_fill()
  a2.goto(x, y - oneSixth * 2)
  a2.goto(x + length, y - oneSixth * 2)
  a2.goto(x + length, y - oneSixth * 4)
  a2.goto(x, y - oneSixth * 4)
  a2.goto(x, y - oneSixth * 2)
  a2.end_fill()
  a.clear()

  a.color(newColor)
  a.penup()
  a.begin_fill()
  a.goto(x, y - oneSixth)
  a.goto(x + length, y - oneSixth)
  a.goto(x + length, y - oneSixth * 5)
  a.goto(x, y - oneSixth * 5)
  a.goto(x, y - oneSixth)
  a.end_fill()
  a2.clear()

  square(t, x, y, length, newColor)
  a.clear()
  del a
  del a2

def row(t, x, y, length, border, defaultColor = None, 
        word = "     ", bgColor = None, accuracyColors = None):
  for i in range(5):
    square(t, x, y, length, defaultColor)

    if accuracyColors is not None:
      t.penup()
      t.pendown()
      t.color("white")
      animate(t, x, y, length, bgColor, defaultColor, accuracyColors[i])
      t.goto(x + length/3.35, y - (length * (9/10)))
      t.color("white")
      t.write(word[i], font = ("Times New Roman", int(length/2), "normal"))

    x += length + border

def board(t, x, y, length, border, defaultColor):
  for _ in range(6):
    row(t, x, y, length, border, defaultColor)
    y -= length + border