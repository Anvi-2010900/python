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
    angle = gs.angle()
    gs.reset_angle(0)
    robot.stop()
    while(angle < turn_angle): 
        angle = gs.angle()        
        angle = abs(angle)
     
        #print(angle)
        left_motor.run(-200)
        right_motor.run(200)

    right_motor.hold()

def turnRight(turn_angle):
    angle = gs.angle()
    gs.reset_angle(0)
    robot.stop()
    while(angle < turn_angle): 
        angle = gs.angle()        
        angle = abs(angle)
        
        #print(angle)
        left_motor.run(200)
        right_motor.run(-200)

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

robot.straight(1350)
#Stop at the white line before treadmill
StopAtWhiteLine()
robot.straight(-70) 
gs.reset_angle(0)
robot.stop()
# turn and backing up against wall
turnLeft(80)
robot.settings(250, 300, 100, 600)
robot.straight(-300)
robot.straight(105)
robot.stop()
gs.reset_angle(0)
#turn to face the treadmill
turnRight(87)
robot.stop()
#going on treadmill

robot.straight(250)
robot.stop()
#left_motor.run_angle(200, 360)
#spinning treadmill
right_motor.run_time(300, 6000)
robot.stop()
#getting down from treadmill
robot.straight(-300)
robot.stop()
#backing up against wall
gs.reset_angle(0)
turnLeft(80)
robot.stop()
robot.settings(250, 300, 100, 600)
robot.straight(-300)
#moving off the wall
robot.straight(100)
gs.reset_angle(0)
turnRight(80)
StopAtWhiteLine()
robot.straight(-75)
gs.reset_angle(0)
turnLeft(35)

#aproching pulley thing
robot.straight(120)
robot.stop()
medium_left.run_time(-90, 3000, then=Stop.HOLD, wait=True) #3750
robot.stop()
#Go Closer to Pulley
robot.straight(50)
robot.stop()
medium_left.run_time(-90, 800, then=Stop.HOLD, wait=True)
#pulling happens
robot.straight(-100)
medium_left.run_time(200, 2000, wait=True)
robot.straight(-225)
gs.reset_angle(0)
turnLeft(25)
robot.stop()
#hitting wall @ weight machine
robot.straight(-200)
robot.straight(1200)
robot.stop()
#moving back and pivoting
robot.straight(-100)
robot.stop()
gs.reset_angle(0)
while (gs.angle() < 80):
    right_motor.run(-300)
    left_motor.run(2)

robot.stop()
#tipping puller
robot.straight(15)

medium_left.run_time(-120, 3500, wait=True)
wait(500)
robot.straight(-15)

#turning away from weight machine
robot.straight(15)
robot.stop()
robot.turn(122)
medium_left.run_time(150, 2000, wait=True)
#backing against wall
robot.straight(-150)
robot.straight(230)
#turning to go back
robot.turn(125)
robot.straight(1000)
gs.reset_angle(0)
turnLeft(50)
robot.straight(1300)
