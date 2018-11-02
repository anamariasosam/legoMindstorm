#!/usr/bin/env python3

import os
import sys
from ev3dev2.sensor import INPUT_1, INPUT_4
from time import sleep
from ev3dev2.motor import (MoveSteering, OUTPUT_B, OUTPUT_C)
from ev3dev2.sensor.lego import GyroSensor
import math

Xob = 12
Yob = 12
v = .5
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

def avanzar():
	motor_pair.on_for_seconds(steering=0, speed=50, seconds=1)
	angle = gy.value()
	print(str(angle))

def girar(tetha):
	tetha = math.degrees(tetha)
	ang = gy.value()
	print(str(tetha) + " - " + str(ang))
	diferenciaDeAngulos = ang - tetha

	while math.fabs(math.fabs(ang) - math.fabs(tetha)) > 10:
			motor_pair.on_for_rotations(steering=20, speed=10, rotations=0.5)
			ang = gy.value()
			print(str(tetha) + " - " + str(ang))
			sleep(1)
    
while True:
	x = -v * math.sin(tetha) + x
	y = v * math.cos(tetha) + y
	deltaX = (Xob - x) * math.cos(tetha) + (Yob - y) * math.sin(tetha)
	curvatura = -(2 * deltaX)/(l**2)
	tetha += v * curvatura
	xc.append(x)
	yc.append(y)    
	girar(tetha)
	avanzar()
	sleep(1)
	if math.fabs(x) >= Xob or math.fabs(y) >= Yob:
			break
