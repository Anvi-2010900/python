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


def turnLeftRun1(turn_angle):
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

def turnRightRun1(turn_angle):
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

def StopAtWhiteLineRun1():
    robot.drive(100, 0)
    while(csLeft.reflection() < 35):
        robot.drive(100, 0)
    
    robot.stop()


def StopAtWhiteLine():
    robot.drive(100, 0)
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


while True:
    ev3.screen.clear()
    ev3.screen.draw_text(30, 25, "Up-1, Down-2")

    # Wait until any Brick Button is pressed.
    while not any(ev3.buttons.pressed()):
        wait(10)

    # Check whether Up Button is pressed, and 
    if Button.UP in ev3.buttons.pressed():
        robot.settings(500, 600, 100, 600)

        robot.straight(1350)
        #Stop at the white line before treadmill
        StopAtWhiteLineRun1()
        robot.straight(-70) 
        gs.reset_angle(0)
        robot.stop()
        # turn and backing up against wall
        turnLeftRun1(80)
        robot.settings(250, 300, 100, 600)
        robot.straight(-300)
        robot.straight(105)
        robot.stop()
        gs.reset_angle(0)
        #turn to face the treadmill
        turnRightRun1(87)
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
        turnLeftRun1(80)
        robot.stop()
        robot.settings(250, 300, 100, 600)
        robot.straight(-300)
        #moving off the wall
        robot.straight(100)
        gs.reset_angle(0)
        turnRightRun1(80)
        StopAtWhiteLineRun1()
        robot.straight(-75)
        gs.reset_angle(0)
        turnLeftRun1(35)

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
        turnLeftRun1(25)
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
        medium_left.run_time(150, 2000, wait=True, then=Stop.BRAKE)
        #backing against wall
        robot.straight(-150)
        robot.straight(230)
        #turning to go back
        robot.turn(125)
        robot.straight(1000)
        gs.reset_angle(0)
        turnLeftRun1(50)
        robot.straight(1300)

    # Check whether Down Button is pressed, and decrease the steps
    # variable by 1 if it is.
    elif Button.DOWN in ev3.buttons.pressed():
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
        medium_right.run_time(4000, 2000, then=Stop.BRAKE)
    # If the Center Button is pressed, break out of the loop.
    elif Button.CENTER in ev3.buttons.pressed():
        break

