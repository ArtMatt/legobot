#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

servoMin = 150# Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
servoCustom = ()
y = 375

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

#def run
pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
y = raw_input("Yes?")
if y == "max":
  pwm.setPWM(1, 0, servoMax)
  ime.sleep(.5)
elif y == "min":
  pwm.setPWM(1, 0, servoMin)
  time.sleep(.5)
else:  
