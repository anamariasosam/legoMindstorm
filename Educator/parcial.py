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
from ev3dev2.motor import OUTPUT_D, MediumMotor
from ev3dev2.sound import Sound

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.
    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')

def run(sound, motor_pair, ts1, ts2, motor):
    while True:
        motor_pair.on(steering=0, speed=30)

        if ts1.is_pressed:
            motor_pair.on_for_rotations(steering=-50, speed=15, rotations=0.5)
        
        if ts2.is_pressed:
            motor_pair.on_for_rotations(steering=50, speed=15, rotations=0.5)

        if ts1.is_pressed and ts2.is_pressed:
            motor_pair.off()
            sound.beep()
            motor_pair.on_for_seconds(steering=0, speed=-20, seconds=2.5)
            motor_pair.off()
            sound.play('hasta_la_vista.wav')
            break 

def constructor():
    # color_sensor = ColorSensor()
    sound = Sound()
    motor_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
    # touch_sensor = TouchSensor()
    ts1 = TouchSensor(INPUT_1)
    ts2 = TouchSensor(INPUT_4)
    motor = MediumMotor(OUTPUT_D)

    return sound, motor_pair, ts1, ts2, motor

def main():
    # set the console just how we want it
    reset_console()

    # print something to the output panel in VS Code
    debug_print('Start program')

    sound, motor_pair, ts1, ts2, motor = constructor()
    sound.play('carstartgarage.wav')

    # while True:
    run(sound, motor_pair, ts1, ts2, motor)


        
if __name__ == '__main__':
    main()