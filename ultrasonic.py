#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
from ev3dev2.motor import (
    MoveSteering, OUTPUT_B, OUTPUT_C)
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound

# state constants
ON = True
OFF = False

def reverse(motor_pair, sound, angle, rotations):

    # Stop moving forward
    motor_pair.off()
    sound.play('aw_crap.wav')

    # Reverse away from wall
    motor_pair.on_for_seconds(steering=0, speed=-10, seconds=2)
    for i in range(rotations):
        # Turn robot left 90 degrees
        sound.beep()
        motor_pair.on_for_rotations(steering=angle, speed=35, rotations=0.5)

def move(motor_pair, color_sensor, caminar, sound):
    ultrasonic_sensor = UltrasonicSensor()
    ts1 = TouchSensor(INPUT_1)
    ts2 = TouchSensor(INPUT_4)

    if color_sensor.color == 3:
        caminar = True
        
    while caminar:
        if color_sensor.color == 5:
            caminar = False
            motor_pair.off()
            sound.play('hasta_la_vista.wav')
            break
            
        motor_pair.on(steering=0, speed=60)

        if ts1.is_pressed and ts2.is_pressed:
            reverse(motor_pair, sound, 100, 3)

        if ts1.is_pressed:
            reverse(motor_pair, sound, -100, 2)
        if ts2.is_pressed:
            reverse(motor_pair, sound, 100, 2)
        if ultrasonic_sensor.distance_centimeters < 10:
            reverse(motor_pair, sound, 100, 3)

        
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
    
    sound = Sound()
    sound.play('internet7.wav')

    color_sensor = ColorSensor()
    motor_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
    andar = False
    while True:
        move(motor_pair, color_sensor, andar, sound)
         



if __name__ == '__main__':
    main()