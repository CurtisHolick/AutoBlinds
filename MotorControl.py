#Tutorial link:
#https://tutorials-raspberrypi.com/how-to-control-a-stepper-motor-with-raspberry-pi-and-l293d-uln2003a/
#^Not using
#New tutorial:
#https://ben.akrin.com/?p=9768

#!/usr/bin/python3
import RPi.GPIO as GPIO
import time


class MotorControl:
    def __init__(self):
        self.in1 = 4
        self.in2 = 27
        self.in3 = 22
        self.in4 = 23

        # careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
        self.step_sleep = 0.002

        self.step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°

        self.direction = False # True for clockwise, False for counter-clockwise

        # defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
        self.step_sequence = [[1,0,0,1],
                         [1,0,0,0],
                         [1,1,0,0],
                         [0,1,0,0],
                         [0,1,1,0],
                         [0,0,1,0],
                         [0,0,1,1],
                         [0,0,0,1]]

        # setting up
        GPIO.setmode( GPIO.BCM )
        GPIO.setup( self.in1, GPIO.OUT )
        GPIO.setup( self.in2, GPIO.OUT )
        GPIO.setup( self.in3, GPIO.OUT )
        GPIO.setup( self.in4, GPIO.OUT )

        # initializing
        GPIO.output( self.in1, GPIO.LOW )
        GPIO.output( self.in2, GPIO.LOW )
        GPIO.output( self.in3, GPIO.LOW )
        GPIO.output( self.in4, GPIO.LOW )


        self.motor_pins = [self.in1,self.in2,self.in3,self.in4]
        self.motor_step_counter = 0


    def cleanup(self):
        GPIO.output( self.in1, GPIO.LOW )
        GPIO.output( self.in2, GPIO.LOW )
        GPIO.output( self.in3, GPIO.LOW )
        GPIO.output( self.in4, GPIO.LOW )
        GPIO.cleanup()


    def turnForward(self, numTurns):
        self.direction=True
        for turns in range(numTurns):
            self.turnOnce()
        #self.cleanup()??????

    def turnBackward(self, numTurns):
        self.direction=False
        for turns in range(numTurns):
            self.turnOnce()
        #self.cleanup()??????


    def turnOnce(self):
        try:
            i = 0
            for i in range(self.step_count):
                for pin in range(0, len(self.motor_pins)):
                    GPIO.output( self.motor_pins[pin], self.step_sequence[self.motor_step_counter][pin] )
                if self.direction==True:
                    self.motor_step_counter = (self.motor_step_counter - 1) % 8
                elif self.direction==False:
                    self.motor_step_counter = (self.motor_step_counter + 1) % 8
                else: # defensive programming
                    print( "uh oh... direction should *always* be either True or False" )
                    self.cleanup()
                    exit( 1 )
                time.sleep( self.step_sleep )

        except KeyboardInterrupt:
            self.cleanup()
            exit( 1 )

# turnForward(2)
# turnBackward(2)

# cleanup()
# exit( 0 )
