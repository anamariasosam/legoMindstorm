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
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import GyroSensor

# state constants
ON = True
OFF = False

def move():
    # motor_pair.on(steering=0, speed=10


def girarAngulo(tetha):
    tetha_grados = math.degrees(tetha)
    mover = gyro.value() - tetha_grados
    
    motor_pair.on_for_rotations(steering=-100, speed=50, rotations=0.5)
    motor_pair.on_for_rotations(steering=-100, speed=50, rotations=0.5)  
    

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
    

    

    persecucion()
    

if __name__ == '__main__':
    main()


def persecucion():
    Xob = 8
    Yob = 8
    v = 2

    x = 0
    y = 0.5

    tetha = 0
    L = 1

    xc = [0]
    yc = [0.5]

    motor = MoveSteering(OUTPUT_B, OUTPUT_C)
    gyro = GyroSensor()
    gyro.mode = GyroSensor.MODE_GYRO_ANG
    gyro.reset()

    while True:
        x = -v * math.sin(tetha) + x
         = v * math.cos(tetha) + y
        deltaX = (Xob - x) * math.cos(tetha) + (Yob - y) * math.sin(tetha)
        curvatura = -(2 * deltaX)/(L**2)
        tetha += v * curvatura
        girarAngulo(tetha)
        move(motor, gyro)
        xc.append(x)
        yc.append(y)
        print(deltaX,curvatura, math.degrees(tetha))
        if math.fabs(x) >= Xob or math.fabs(y) >= Yob:
            break

 
