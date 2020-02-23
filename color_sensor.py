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

#drive speed at 450 mm per second with 0 deg per second turn rate
robot.drive(450, 0)
while cs.color() != Color.RED:
    wait(50)
    print("color seen by the robot:", cs.color())

robot.stop(Stop.BRAKE)
brick.sound.beep()

robot.drive(500,0)
while cs.color() != Color.RED:
    wait(50)
    print("color seen by the robot:", cs.color())
    
robot.stop(Stop.BRAKE)
