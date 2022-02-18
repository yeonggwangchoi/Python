import turtle as t

t.shape("circle")
# t.shape("turtle")이 실행이 안된다 이유는 아직 찾는중이다.
t.showturtle()

t.write("Welcome to Python")

#직선으로 100픽셀 만큼 그려라.
t.forward(100)
t.right(90)
t.color("red")
t.forward(100)
t.right(90)
t.color("yellow")
t.forward(100)
t.left(90)
t.color("green")
t.forward(100)