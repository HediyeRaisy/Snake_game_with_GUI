from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        if rand_x <= 30 and rand_x >= -30 and rand_y >= 210 and rand_y <=300 :
            self.refresh()
        self.goto(rand_x, rand_y)
