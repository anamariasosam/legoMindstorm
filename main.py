#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C

from ev3dev2.sensor.lego import ColorSensor
from time import sleep
from ev3dev2.sound import Sound

# state constants
ON = True
OFF = False

def colorSensor():
    color_sensor = ColorSensor()
    sound = Sound()

    while True:
        color = color_sensor.color
        text = ColorSensor.COLORS[color]
        sound.speak(text)

def reverse():
    motor_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
    touch_sensor = TouchSensor()

    # Start robot moving forward
    motor_pair.on(steering=0, speed=60)

    # Wait until robot touches wall
    touch_sensor.wait_for_pressed()

    # Stop moving forward
    motor_pair.off()

    # Reverse away from wall
    motor_pair.on_for_seconds(steering=0, speed=-10, seconds=2)
    motor_pair.on_for_rotations(steering=-100, speed=15, rotations=0.5)
    motor_pair.on_for_rotations(steering=-100, speed=15, rotations=0.5)

def touchLeds():
    ts = TouchSensor()
    leds = Leds()

    print("Press the touch sensor to change the LED color!")

    while True:
        if ts.is_pressed:
            leds.set_color("LEFT", "GREEN")
            leds.set_color("RIGHT", "GREEN")
        else:
            leds.set_color("LEFT", "RED")
            leds.set_color("RIGHT", "RED")

def square():
    motor_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

    for i in range(4):
        # Move robot forward for 3 seconds
        motor_pair.on_for_seconds(steering=0, speed=50, seconds=3)
        # Turn robot left 90 degrees (adjust rotations for your particular robot)
        motor_pair.on_for_rotations(steering=-100, speed=15, rotations=0.5)

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

    # colorSensor()
    reverse()
    # touchLeds()


if __name__ == '__main__':
    main()