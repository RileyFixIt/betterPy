import turtle

class draw:
  def line(self, outline, pensize, angle, length):
    turtle.color(outline)
    turtle.pensize(pensize)
    turtle.right(angle)
    turtle.forward(length)
  def circle(self, outline, fill, pensize, size):
    turtle.color(outline, fill)
    sizer = size
    turtle.pensize(pensize)
    for i in range(72):
      turtle.forward(5 * sizer)
      turtle.right(5)
  def clear(self):
    turtle.clearscreen()
  def speed(self, num):
    turtle.speed(num)
  def regular_shape(num, pensize, length, outline, fill):
    turtle.color(outline, fill)
    turtle.pensize(pensize)
    for i in range(num):
      turtle.forward(length)
      turtle.right(360 / num)
