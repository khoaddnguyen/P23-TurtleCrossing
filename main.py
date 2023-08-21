# 1. Move the turtle with keypress
# 2. Create and move cars
# 3. Detect collision with car
# 4. Detect when turtle reaches other side
# 5. Create scoreboard


import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.bgcolor("black")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()

# 1. Move the turtle with keypress
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

# 2. Create and move cars
    car_manager.create_car()
    car_manager.move_cars()

# 3. Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()