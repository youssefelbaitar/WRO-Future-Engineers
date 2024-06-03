#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

Motor_Big = Motor(Port.D)
Motor_Small = Motor(Port.B)

UltraSonic_front = UltrasonicSensor(Port.S1)
UltraSonic_right = UltrasonicSensor(Port.S3)
UltraSonic_left = UltrasonicSensor(Port.S4)
GyroSensor_1 = GyroSensor(Port.S2)
Wheel_Turn = 0

GyroSensor_1.reset_angle(0)
# Initialize the EV3 brick'à
ev3 = EV3Brick()

def Turn_Right():
    Motor_Small.run_target(2000, 25)


def Turn_Left():
    Motor_Small.run_target(2000, -25)
while True:
    while UltraSonic_front.distance() > 165:
        Motor_Big.run(500)
        if UltraSonic_right.distance() < 160 or UltraSonic_left.distance()> 1700:
            Turn_Right()
        if UltraSonic_left.distance() <160 or UltraSonic_right.distance()>1700:
            Turn_Left()
        if GyroSensor_1.angle() >= 90:
            Turn_Right()
            GyroSensor_1.reset_angle(0)
        if GyroSensor_1.angle() <= -90 :
            Turn_Left()
            GyroSensor_1.reset_angle(0)
    while UltraSonic_front.distance() < 165:
        if UltraSonic_left.distance() > UltraSonic_right.distance() :
            Motor_Big.run(-600)
            wait(1000)
            Turn_Right()
            
        if UltraSonic_right.distance() > UltraSonic_left.distance() :
            Motor_Big.run(-600)
            wait(1000)
            Turn_Left()
            
    
        
        
        
