import turtle

class draw:
  def line(self, outline, pensize, angle, length):
    turtle.color(outline)
    turtle.pensize(pensize)
    turtle.right(angle)
    turtle.forward(length)

def wait():
  input()
