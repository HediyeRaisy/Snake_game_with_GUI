from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")

snake = Snake()
food = Food()
score = Score()

game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.show()
    if snake.squares[0].distance(food) < 20:
        food.refresh()
        snake.extend()
        score.refresh()

    if snake.squares[0].xcor() > 280 or snake.squares[0].xcor() < -280 or snake.squares[0].ycor() > 280 or \
            snake.squares[0].ycor() < -280:
        # game_is_on = False
        for i in snake.squares:
            i.hideturtle()
        snake.reset()
        snake = Snake()
        print("1")
        score.reset()

    # snake collision
    for square in snake.squares[1::]:

        if snake.squares[0].distance(square) < 10:
            print("2")
            # game_is_on = False
            for i in snake.squares:
                i.hideturtle()
            snake.reset()
            snake = Snake()
            score.reset()

screen.exitonclick()
