import turtle, tkinter, time, random

class draw:
  def line(self, outline, pensize, angle, length):
    turtle.color(outline)
    turtle.pensize(pensize)
    turtle.right(angle)
    turtle.forward(length)
  def circle(self, outline, fill, pensize, size):
    turtle.color(outline, fill)
    turtle.begin_fill()
    sizer = size
    turtle.pensize(pensize)
    for i in range(72):
      turtle.forward(0.5 * sizer)
      turtle.right(5)
    turtle.end_fill()
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

class GUI:
  def __init__(self, title):
    window = tkinter.Tk()
    window.title(title)
    return window
