#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
from ev3dev2.sensor import INPUT_1, INPUT_4
from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import GyroSensor
import math

# state constants
ON = True
OFF = False

def avanzar(motor_pair, gy):
    motor_pair.on_for_seconds(steering=0, speed=50, seconds=1)
	angle = gy.value()

def girar(tetha, gy, ang, motor_pair):
	tetha = math.degrees(tetha)
	ang = gy.value()
	diferenciaDeAngulos = ang - tetha

	while math.fabs(math.fabs(ang) - math.fabs(tetha)) > 10:
        motor_pair.on_for_rotations(steering=5, speed=10, rotations=0.5)
        ang = gy.value()
        sleep(1)

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

    Xob = 8
    Yob = 8
    v = 1
    x = 0
    y = 0
    tetha = 0
    l = 4
    xc = [x]
    yc = [y]

    motor_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

    gy = GyroSensor()
    gy.mode = 'GYRO-RATE'
    gy.mode = 'GYRO-ANG'

    units = gy.units

    angle = gy.value()
    print(str(angle))
    sleep(1)

    while True:
        x = -v * math.sin(tetha) + x
        y = v * math.cos(tetha) + y
        deltaX = (Xob - x) * math.cos(tetha) + (Yob - y) * math.sin(tetha)
        curvatura = -(2 * deltaX)/(l**2)
        tetha += v * curvatura
        xc.append(x)
        yc.append(y)    
        girar(tetha, gy, ang, motor_pair)
        avanzar(motor_pair, gy)
        sleep(1)
        print(str(x) + " - " + str(y))
        if math.fabs(x) >= Xob or math.fabs(y) >= Yob:
            break

if __name__ == '__main__':
    main()
