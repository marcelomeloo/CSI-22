import turtle as tt

window = tt.Screen()
turtle = tt.Turtle()

def drawSquare(t, side):
  for i in range(4):
    turtle.fd(side)
    turtle.left(90)

for i in range(5):
  side = 20 * (i+1)
  drawSquare(turtle, side)
  turtle.up()
  turtle.goto(-side / 2, -side / 2)
  turtle.down()

window.mainloop()