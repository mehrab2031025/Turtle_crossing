import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
screen.onkeypress(key="Up", fun=player.Move_forward)
screen.onkeypress(key="Down", fun=player.Move_backward)

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()

    car.create_cars()
    car.move_cars()

    for i in car.cars:
        if player.distance(i) < 20:
            score.GAME_OVER()
            game_is_on = False

    if player.reached_finish_line():
        score.increase_score()
        car.car_speedup()
        player.goto_start()

screen.exitonclick()
