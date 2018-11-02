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


def caminar(ruedaDerecha, ruedaIzquierda, gyro):
    ruedaDerecha.run_timed(time_sp = 1000, speed_sp = 460)
    ruedaIzquierda.run_timed(time_sp = 1000, speed_sp = 460)
    angulo = gyro.value()


def girar(ang, tetha, ruedaDerecha, ruedaIzquierda, gyro):
    diferencia =  ang - tetha
    while math.fabs(math.fabs(ang) - math.fabs(tetha)) > 10:
        if diferencia > 0:
            ruedaDerecha.run_timed(time_sp = 40, speed_sp = -460)
            ruedaIzquierda.run_timed(time_sp = 40, speed_sp = 460)
        else:
            ruedaDerecha.run_timed(time_sp = 40, speed_sp = 460)
            ruedaIzquierda.run_timed(time_sp = 40, speed_sp =-460)
        ang = gyro.value()
        sleep(1)

def persecusionPura(tetha, x, y, v, Xob, Yob, l, movimientosX, movimientosY):
    x = -v * math.sin(tetha) + x
    y = v * math.cos(tetha) + y
    deltaX = (Xob - x) * math.cos(tetha) + (Yob - y) * math.sin(tetha)
    curvatura = -(2 * deltaX)/(l**2)
    tetha += v * curvatura
    movimientosX.append(x)
    movimientosY.append(y)
    return tetha,x,y


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

    Xob = 12
    Yob = 12
    v = 0.5
    x = 0
    y = 0
    tetha = 0
    l = 4
    movimientosX = [x]
    movimientosY = [y]

    ruedaDerecha = LargeMotor('outC')
    ruedaIzquierda = LargeMotor('outB')

    gyro = GyroSensor()
    gyro.mode = 'GYRO-RATE'
    gyro.mode = 'GYRO-ANG'
    sleep(1)
    while True:
        print(gyro.value())
        tetha,x,y = persecusionPura(tetha, x, y, v, Xob, Yob, l, movimientosX, movimientosY)
        tetha = math.degrees(tetha)
        ang = gyro.value()
        girar(ang, tetha, ruedaDerecha, ruedaIzquierda, gyro)
        caminar(ruedaDerecha, ruedaIzquierda, gyro)
        sleep(1)
        if math.fabs(x) >= Xob or math.fabs(y) >= Yob:
            break

    

if __name__ == '__main__':
    main()
