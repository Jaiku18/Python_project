from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
user_Input = True


def toggle_input_on():
    global user_Input

    user_Input = True


def toggle_input_off():
    global user_Input

    user_Input = False


def medium_level():
    game_is_on = True
    snake.box()
    while game_is_on:

        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall.
        if snake.head.xcor() > 250 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
            game_is_on = False

            scoreboard.game_over()

            return  screen.textinput('****', 'Wanna to continue the game type Y else type N')

        # Detect collision with tail.
        for segment in snake.segments[1:]:

            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

                return screen.textinput('****', 'Wanna to continue the game type Y else type N')


def easy_level():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect end of the wall.
        if snake.head.xcor() > 280:
            new_x = -275
            new_y = snake.head.ycor()
            snake.head.goto(new_x, new_y)
        if snake.head.xcor() < -280:
            new_x = 275
            new_y = snake.head.ycor()
            snake.head.goto(new_x, new_y)
        if snake.head.ycor() > 280:
            new_y = -275
            new_x = snake.head.xcor()
            snake.head.goto(new_x, new_y)
        if snake.head.ycor() < -280:
            new_y = 275
            new_x = snake.head.xcor()
            snake.head.goto(new_x, new_y)

        # Detect collision with tail.
        for segment in snake.segments[1:]:

            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

                return screen.textinput('****', 'Wanna to continue the game type Y else type N')


while user_Input:
    screen = Screen()
    screen.clear()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(toggle_input_on, 'y')
    screen.onkey(toggle_input_off, 'n')

    user_level = int(screen.textinput('Select Level', 'Type 1 for easy 2 for hard level'))
    print(user_level)
    if user_level == 1:
        screen.listen()
        text = easy_level()

    else:
        screen.listen()
        text = medium_level()
    if text == 'y':
        user_Input = True
    else:
        user_Input = False

screen.exitonclick()
