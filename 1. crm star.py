from turtle import *
color('black', 'blue')
begin_fill()

while True:
    forward(100)
    backward(100)
    right(100)
    forward(80)
    left(100)
    forward(100)
    left(100)
    right(100)
    left(50)
    right(100)
    if abs(pos()) < 1:
        break
    speed(10000000)
    position()

end_fill()
done()