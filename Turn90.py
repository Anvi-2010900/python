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
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)

DriveBase = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

ts = TouchSensor(Port.S4)
cs = ColorSensor(Port.S3)
gs = GyroSensor(Port.S1)

ev3.speaker.beep()


gs.reset_angle(0)
while gs.angle() < 75:
    DriveBase.drive(50, 100)

DriveBase.stop()
wait(1500)
print(gs.angle())

wait(2000)
ev3.speaker.beep()

gs.reset_angle(0)
DriveBase.turn(90)
wait(1500)
print(gs.angle())
