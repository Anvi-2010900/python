#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
ev3.speaker.beep()

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
medium_left = Motor(Port.B)
medium_right = Motor(Port.C)
gs = GyroSensor (Port.S3)
csLeft = ColorSensor(Port.S1)
csMiddle = ColorSensor(Port.S2)
csRight = ColorSensor(Port.S4)
robot = DriveBase(left_motor, right_motor, axle_track = 104, wheel_diameter = 55.5)

def turnLeft(turn_angle):
    left_motor.hold()
    angle = gs.angle()
    gs.reset_angle(0)
    while(angle < turn_angle): 
        angle = gs.angle()        
        angle = abs(angle)
        print(angle)
        right_motor.run(300)

    right_motor.hold()

def turnRight(turn_angle):
    right_motor.hold()
    angle = gs.angle()
    gs.reset_angle(0)
    while(angle < turn_angle): 
        angle = gs.angle()        
        angle = abs(angle)
        print(angle)
        left_motor.run(300)

    left_motor.hold()

def StopAtWhiteLine():
    robot.drive(100, 0)
    while(csLeft.reflection() < 35):
        robot.drive(100, 0)
    
    robot.stop()

def StopAtWhiteLineBackwards():
    robot.drive(-100, 0)
    while(csLeft.reflection() < 35):
        robot.drive(100, 0)
    
    robot.stop()

def StopAtWhiteLineRightMotorBackwards():
    right_motor.run(-100)
    right_motor.stop()
    while(csLeft.reflection() < 35):
        robot.drive(100, 0)
    
    robot.stop()

def StopAtWhiteLineRight():
    robot.drive(100, 0)
    while(csRight.reflection() > 40):
        robot.drive(100, 0)
    
    robot.stop()

def StopAtBlackLineRight():
    robot.drive(100, 0)
    while(csRight.reflection() < 15):
        robot.drive(100, 0)
    
    robot.stop()
robot.settings(500, 600, 100, 600)

#Small Tire Flip
robot.straight(1000)
robot.stop()
robot.settings(250, 300, 100, 600)
StopAtWhiteLine()
robot.straight(175)
#robot turns toward the wall and reveres: 

robot.turn(-120)
robot.straight(-180)
#goes off the wall and turns to the wheel
robot.straight(200)
robot.turn(-65)
robot.stop()
#Goes foreward to flip the wheel
medium_left.run_time(-200, 5000)
robot.straight(80)
medium_left.run_time(150, 5000)
medium_left.stop()
#Large Tire Flip
#StopAtWhiteLineRightMotorBackwards()
robot.turn(30)
robot.straight(-50)
medium_left.run_time(-200, 4000)
robot.straight(110)
medium_left.run_time(150, 6500)

#back after both tire flip
robot.turn(20)
robot.straight(-550)
robot.straight(150)
robot.turn(-125)
robot.straight(300)
robot.stop()
StopAtWhiteLineRight()

gs.reset_angle(0)
#parrallel park
while(gs.angle() > -35):
    right_motor.run(300)
    left_motor.run(215)
    print(gs.angle())

robot.stop()


while(gs.angle() < 0):
    right_motor.run(215)
    left_motor.run(300)
    print(gs.angle())

robot.stop()

#pushes step counter
robot.straight(-500)
robot.stop()
right_motor.run_time(300, 4000)
robot.stop()
robot.straight(50)
robot.straight(-200)
robot.stop()
gs.reset_angle(0)
while (gs.angle() > -80):
    right_motor.run(200)
    left_motor.run(-200)
robot.stop()
robot.straight(130)
StopAtWhiteLine
robot.straight(-65)
robot.stop()
gs.reset_angle(0)
while (gs.angle() > -82):
    right_motor.run(200)
    left_motor.run(-200)
robot.stop()




robot.straight(400)
robot.stop()
medium_right.run_time(4000, 2000)
