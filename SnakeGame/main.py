from turtle import Screen
from snake import Snake
from Food import Food
from scoreboard import ScoreBoard
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()

food=Food()

score_board=ScoreBoard()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.score_count()

    #Detect collision wit wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        score_board.reset()
        snake.reset()

    #Detect collision with tail.
    for segment in snake.segments:
        if segment==snake.snake_head:
            pass
        elif snake.snake_head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()