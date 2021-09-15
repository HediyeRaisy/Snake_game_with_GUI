from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.mark = 0

        c = 0
        self.color("white")
        self.penup()
        with open("data.txt" , mode="r") as file:
            self.highscore = int(file.read())



    def show(self):
        self.clear()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score: {self.mark} , High Score : {self.highscore}", move=False, align="center", font=("Arial",24, "normal"))

    def refresh(self):
        self.mark += 1
        self.show()

    def reset(self) :
        if self.mark > self.highscore:
            self.highscore = self.mark
            with open("data.txt", mode= "w") as file:
                file.write(str(self.highscore))
        self.mark = 0
    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write("GAME OVER", move=False, align="center", font=("Arial", 24, "normal"))
