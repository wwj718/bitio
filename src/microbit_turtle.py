#!/usr/bin/env python
# encoding: utf-8

# https://gist.github.com/wwj718/9449dd4730bd6232b1d241cce52dcc15

import microbit
import turtle
import time


def do_action(action):
    if action == "f":
        turtle.forward(2)
    if action == "b":
        turtle.backward(2)
    if action == "l":
        turtle.left(90)
    if action == "r":
        turtle.right(90)


while True:
    # http://microbit-challenges.readthedocs.io/en/latest/tutorials/accelerometer.html
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    # import IPython;IPython.embed()

    # gesture = microbit.accelerometer.get_gestures()
    print(x,y)
    # print("gesture:",gesture)
    if x < -300:
        print("left")
        action = "l"
        do_action(action)
    elif x > 300:
        print("right")
        action = "r"
        do_action(action)

    if y < -300:
        print("forward") # 需要整块板子朝前 竖起来
        action = "f"
        do_action(action)
    elif y > 300:
        print("backward")
        action = "b"
        do_action(action)


    time.sleep(0.5)

