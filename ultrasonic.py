#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
from ev3dev2.motor import (
    MoveSteering, MediumMotor, OUTPUT_B, OUTPUT_C)
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from time import sleep

# state constants
ON = True
OFF = False

def reverse(motor_pair):
    # Stop moving forward
    motor_pair.off()

    # Reverse away from wall
    motor_pair.on_for_seconds(steering=0, speed=-10, seconds=2)
    motor_pair.on_for_rotations(steering=-100, speed=15, rotations=0.5)
    motor_pair.on_for_rotations(steering=-100, speed=15, rotations=0.5)

def move():
    motor_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
    ultrasonic_sensor = UltrasonicSensor()
    touch_sensor = TouchSensor()

    # Start robot moving forward
    motor_pair.on(steering=0, speed=30)

    if ultrasonic_sensor.distance_centimeters < 10 or touch_sensor.is_pressed:
        reverse(motor_pair)
        
def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.
    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')


def set_cursor(state):
    '''Turn the cursor on or off'''
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')


def set_font(name):
    '''Sets the console font
    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)


def main():
    '''The main function of our program'''

    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')


    # print something to the output panel in VS Code
    debug_print('Hello VS Code!')
    
    while True:
        move()


if __name__ == '__main__':
    main()