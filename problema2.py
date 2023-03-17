import turtle as tt

window = tt.Screen()
tess = tt.Turtle()

def draw_poly(t, n, sz):
  for i in range(n):
    t.fd(sz)
    t.left(360/n)

draw_poly(tess, 8, 50)
window.mainloop()