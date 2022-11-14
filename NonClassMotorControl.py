#Tutorial link:
#https://tutorials-raspberrypi.com/how-to-control-a-stepper-motor-with-raspberry-pi-and-l293d-uln2003a/
#^Not using
#New tutorial:
#https://ben.akrin.com/?p=9768

#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

in1 = 4
in2 = 27
in3 = 22
in4 = 23

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002

step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°

direction = False # True for clockwise, False for counter-clockwise

# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]

# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )

# initializing
GPIO.output( in1, GPIO.LOW )
GPIO.output( in2, GPIO.LOW )
GPIO.output( in3, GPIO.LOW )
GPIO.output( in4, GPIO.LOW )


motor_pins = [in1,in2,in3,in4]
motor_step_counter = 0 ;


def cleanup():
    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    GPIO.cleanup()


def turnForward(numTurns):
    global direction
    direction=True
    for turns in range(numTurns):
        turnOnce()

def turnBackward(numTurns):
    global direction
    direction=False
    for turns in range(numTurns):
        turnOnce()


def turnOnce():
    global motor_pins, step_sequence, motor_pins, motor_step_counter, direction, step_count, step_sleep
    try:
        i = 0
        for i in range(step_count):
            for pin in range(0, len(motor_pins)):
                GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
            if direction==True:
                motor_step_counter = (motor_step_counter - 1) % 8
            elif direction==False:
                motor_step_counter = (motor_step_counter + 1) % 8
            else: # defensive programming
                print( "uh oh... direction should *always* be either True or False" )
                cleanup()
                exit( 1 )
            time.sleep( step_sleep )

    except KeyboardInterrupt:
        cleanup()
        exit( 1 )

turnForward(2)
turnBackward(2)

cleanup()
exit( 0 )
