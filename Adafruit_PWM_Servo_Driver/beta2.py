#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address.
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMinn = 1  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
servoMid = 375
servoMaxx = 740
servoMaxxx = 760 
y = "yes"
m = 375


def setServoPulse(channel, pulse):
pulseLength = 1000000                   # 1,000,000 us per second
pulseLength /= 60                       # 60 Hz
print "%d us per period" % pulseLength
pulseLength /= 4096                     # 12 bits of resolution
print "%d us per bit" % pulseLength
pulse *= 1000
pulse /= pulseLength
pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

while y != "no":
print ">>>> M value is: ", m
s = int(raw_input(">>> Which Servo? >> "))
if s == 2
pwm.setPWM(2, 0, 400)
pwm.setPWM(2, 0, 300)
else
if m != "stop" and int(m) > 149 and int(m) < 601:
pwm.setPWM(s, 0, m) 
elif int(m) < 150:
m = 151
pwm.setPWM(s, 0, m) 
elif int(m) > 600:
m = 600
pwm.setPWM(s, 0, m) 
else:
y = "no"
print "murder she wrote"   

# END OF FILE 
