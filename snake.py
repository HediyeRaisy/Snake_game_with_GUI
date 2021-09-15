from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake :


    def __init__(self ):
        self.squares = []

        self.make_snake()


    def move(self):
        for square in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square - 1].xcor()
            new_y = self.squares[square - 1].ycor()
            self.squares[square].goto(new_x, new_y)
        self.squares[0].forward(20)

    def make_snake(self):
        s = 0
        for i in range(0, 3):
            self.squares.append(Turtle(shape="square"))
            self.squares[i].penup()
            self.squares[i].color("white")
            self.squares[i].setx(s)

            s += -20

    def up(self):
        if self.squares[0].heading() != DOWN:
            self.move()
            self.squares[0].setheading(90)
            self.move()


    def down(self):
        if self.squares[0].heading() != UP:
            self.move()
            self.squares[0].setheading(270)
            self.move()

    def right(self):
        if self.squares[0].heading() != LEFT:
            self.move()
            self.squares[0].setheading(0)
            self.move()

    def left(self):
        if self.squares[0].heading() != RIGHT:
            self.move()
            self.squares[0].setheading(180)
            self.move()

    # def collision(self):
    #     for i in self.squares:
    #         for j in self.squares:
    #             if not i == j:
    #                 if i.xcor() == j.xcor() and i.ycor() == j.ycor():
    #                     return True

    def extend(self):
        i = len(self.squares)
        x = self.squares[-1].xcor()
        y = self.squares[-1].ycor()
        seg = Turtle()
        seg.color("white")
        seg.penup()
        seg.shape("square")
        seg.goto(x, y)

        self.squares.append(seg)

    def reset(self):
        for i in self.squares:
            i.clear()

        self.squares.clear()
            # self.squares.remove(i)
