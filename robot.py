from microbit import *
motorA1 = pin0
motorA2 = pin1
motorB1 = pin2
motorB2 = pin8

def stop():
    motorA1.write_digital(0)
    motorA2.write_digital(0)
    motorB1.write_digital(0)
    motorB2.write_digital(0)
    display.scroll("STOP")

def backward(speed):
    motorA1.write_analog(speed)
    motorA2.write_analog(0)
    motorB1.write_analog(0)
    motorB2.write_analog(speed)

def forward(speed):
    motorA1.write_analog(0)
    motorA2.write_analog(speed)
    motorB1.write_analog(speed)
    motorB2.write_analog(0)

def left(speed):
    motorA1.write_analog(0)
    motorA2.write_analog(speed)
    motorB1.write_analog(0)
    motorB2.write_analog(speed)

def right(speed):
    motorA1.write_analog(speed)
    motorA2.write_analog(0)
    motorB1.write_analog(speed)
    motorB2.write_analog(0)

stop()
forward(512)
sleep(3000)
backward(512)
sleep(3000)
left(512)
sleep(3000)
right(512)
sleep(3000)
stop()