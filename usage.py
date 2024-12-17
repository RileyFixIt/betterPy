import betterPy
import time

# This section of code is example usage for the draw class: it draws a circle and then a line.
drawer = betterPy.draw()
drawer.speed(100000000000000)
drawer.circle("black", "red", 10, 1)
time.sleep(1)
drawer.clear()
drawer.line("black", 10, 45, 100)
