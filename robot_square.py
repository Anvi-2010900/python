#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

motorA = Motor(Port.A)
motorD = Motor(Port.D)
robot = DriveBase(motorA, motorD, 56, 114)
cs = ColorSensor(Port.S1)
gs = GyroSensor(Port.S3)
x = 0

#Drive the rob ot for 500 mm/s, 0 turn rate and for 2 seconds
while x < 4:
    robot.drive_time(500, 0, 2000)
    robot.stop(stop_type = Stop.BRAKE)
    wait(500)
    print("Robot moved forward.Square side count = ", x+1)

    #Reset Gyro Angle befor starts to turn
    gs.reset_angle(0)
    print("Gyro Angle :", gs.angle())

    #Make the robot to turn
    motorA.run(-75)
    motorD.run(75)


    while gs.angle() >=-75:
        wait(0.5)
        print("Gyro Angle :", gs.angle())

        if gs.angle() <= -75:
            robot.stop(Stop.BRAKE)

    robot.stop(Stop.BRAKE)

    x = x+1
