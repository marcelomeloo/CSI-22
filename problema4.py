import turtle as tt
import time

window = tt.Screen()
tess = tt.Turtle()

def draw_crazy_figure(angle):
  for i in range(100):
    tess.forward(5*i)
    tess.right(angle)

draw_crazy_figure(90)
time.sleep(3)
tess.goto([0, 0])
tess.clear()
draw_crazy_figure(89)

window.mainloop()
