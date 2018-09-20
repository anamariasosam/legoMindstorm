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


def main():
    '''The main function of our program'''

    # set the console just how we want it
    reset_console()


    # print something to the output panel in VS Code
    debug_print('Start program')

         
if __name__ == '__main__':
    main()