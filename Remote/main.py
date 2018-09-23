#!/usr/bin/env python3
import os
import sys
from ev3dev2.motor import (MoveSteering, OUTPUT_B, OUTPUT_C)
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
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

def stop(motor_pair, sound):
    motor_pair.off()
    sound.beep()
    motor_pair.on_for_seconds(steering=0, speed=-20, seconds=2.5)
    motor_pair.off()
    sound.play('hasta_la_vista.wav')

def run(sound, motor_pair, touch_sensor_left, touch_sensor_right):
    motor_pair.on(steering=0, speed=30)

    if touch_sensor_left.is_pressed and touch_sensor_right.is_pressed:
        stop(motor_pair, sound)

    if touch_sensor_left.is_pressed:
        motor_pair.on_for_rotations(steering=-50, speed=15, rotations=0.5)
    
    if touch_sensor_right.is_pressed:
        motor_pair.on_for_rotations(steering=50, speed=15, rotations=0.5)

def constructor():
    sound = Sound()
    motor_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
    touch_sensor_left = TouchSensor(INPUT_1)
    touch_sensor_right = TouchSensor(INPUT_4)

    return sound, motor_pair, touch_sensor_left, touch_sensor_right

def main():
    reset_console()

    debug_print('Start program')

    sound, motor_pair, touch_sensor_left, touch_sensor_right, motor = constructor()
    sound.play('carstartgarage.wav')

    while True:
        run(sound, motor_pair, touch_sensor_left, touch_sensor_right)

if __name__ == '__main__':
    main()