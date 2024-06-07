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
ColorSensor_1 = ColorSensor(Port.S2)
detected_color = ColorSensor_1.color()
prev_angle = Motor_Big.angle()
wheel_turns = 0
ev3 = EV3Brick()


def Turn_Right():
    Motor_Small.run_target(2000, 30)


def Turn_Left():
    Motor_Small.run_target(2000, -30)

while wheel_turns < 12:
    detected_color = ColorSensor_1.color()

    # Check for red color and turn left if detected
    if detected_color == Color.RED:
        Turn_Left()
        Motor_Big.run(200)
        
    # Check for green color and turn right if detected
    if detected_color == Color.GREEN:
        Turn_Right()
        Motor_Big.run(200)

    while UltraSonic_front.distance() > 165:
        Motor_Big.run(700)
        
        detected_color = ColorSensor_1.color()
        if detected_color == Color.RED:
            Motor_Big.run(200)
            Turn_Left()
            break
        if detected_color == Color.GREEN:
            Motor_Big.run(200)
            Turn_Right()
            break  # Exit the inner loop to check the condition again
        
        if UltraSonic_right.distance() < 400 or UltraSonic_left.distance() > 800:
            Turn_Right()
        if UltraSonic_left.distance() < 400 or UltraSonic_right.distance() > 800:
            Turn_Left()
        
    while UltraSonic_front.distance() < 100 and detected_color != Color.RED and detected_color != Color.GREEN:
        detected_color = ColorSensor_1.color()
        
        if detected_color == Color.RED:
            Motor_Big.run(200)
            Turn_Left()
            break 
        if detected_color == Color.GREEN:
            Motor_Big.run(200)
           Turn_Right()
            break  # Exit the inner loop to check the condition again
        
        if UltraSonic_left.distance() > UltraSonic_right.distance():
            wait(500)
            Motor_Big.run(-600)
            wait(1000)
            Turn_Right()
        if UltraSonic_left.distance() < UltraSonic_right.distance():
            wait(500)
            Motor_Big.run(-600)
            wait(1000)
            Turn_Left()
    
    # Check if the wheel has completed a full rotation
    current_angle = Motor_Big.angle()
    angle_diff = current_angle - prev_angle

    if angle_diff >= 360:
        wheel_turns += 1
        prev_angle = current_angle

    # Stop the robot after 4 wheel turns
    if wheel_turns >= 12:
        Motor_Big.stop()
        break 