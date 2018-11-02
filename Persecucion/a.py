#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
from ev3dev2.motor import (MoveSteering, OUTPUT_B, OUTPUT_C)
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.
    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')

def constructor():
    # color_sensor = ColorSensor()

    motor_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

    return motor_pair

def color(color_sensor, sound):
    color = color_sensor.color
    text = ColorSensor.COLORS[color]
    sound.speak(text)

def turnLeft(motor_pair):
    motor_pair.on_for_rotations(steering=-100, speed=50, rotations=0.5)
    motor_pair.on_for_rotations(steering=-100, speed=50, rotations=0.5)
    motor_pair.on_for_rotations(steering=-100, speed=50, rotations=0.5)
    motor_pair.on_for_rotations(steering=-100, speed=50, rotations=0.5)
    motor_pair.on_for_rotations(steering=-80, speed=50, rotations=0.5)

def square(motor_pair):
  motor_pair.on_for_seconds(steering=0, speed=50, seconds=1)


        
def run(motor_pair, ultrasonic_sensor):
    while True:
        motor_pair.on(steering=0, speed=60)

        if ultrasonic_sensor.distance_centimeters < 10:
            motor_pair.off()
            motor_pair.on_for_seconds(steering=0, speed=-10, seconds=2)
            motor_pair.on_for_rotations(steering=-100, speed=5, rotations=0.5)
            motor_pair.on_for_rotations(steering=-45, speed=5, rotations=0.5)

def move(motor_pair, touch_sensor, ultrasonic_sensor):
    # Start robot moving forward
    motor_pair.on(steering=0, speed=50)

    # Wait until robot touches wall
    touch_sensor.wait_for_pressed()

    # Stop moving forward
    motor_pair.off()

    # Reverse away from wall
    motor_pair.on_for_seconds(steering=0, speed=-50, seconds=2)


def main():
    # set the console just how we want it
    reset_console()

    # print something to the output panel in VS Code
    debug_print('Start program')

    motor_pair = constructor()

    # color(color_sensor, sound)
    # run(motor_pair, ultrasonic_sensor)
    # move(motor_pair, touch_sensor)

    square(motor_pair)

        
if __name__ == '__main__':
    main()
