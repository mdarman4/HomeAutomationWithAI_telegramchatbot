import RPi.GPIO as GPIO

#Set up GPIO
GPIO.setmode(GPIO.BCM)
gpio_pins=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
for pin in gpio_pins:
    GPIO.setup(pin,GPIO.OUT)

#Parent Bedroom
def p_bedroom_bulb_on():
    GPIO.output(1,GPIO.HIGH)
def p_bedroom_bulb_off():
    GPIO.output(1,GPIO.LOW)
def p_fan_on():
    GPIO.output(2,GPIO.HIGH)
def p_fan_off():
    GPIO.output(2,GPIO.LOW)
def p_AC_on():
    GPIO.output(3,GPIO.HIGH)
def p_AC_off():
    GPIO.output(3,GPIO.LOW)

#Child Bedroom

def c_bedroom_bulb_on():
    GPIO.output(4,GPIO.HIGH)
def c_bedroom_bulb_off():
    GPIO.output(4,GPIO.LOW)
def c_fan_on():
    GPIO.output(5,GPIO.HIGH)
def c_fan_off():
    GPIO.output(5,GPIO.LOW)
def c_AC_on():
    GPIO.output(6,GPIO.HIGH)
def c_AC_off():
    GPIO.output(6,GPIO.LOW)
def c_study_lamp_on():
    GPIO.output(7,GPIO.HIGH)
def c_study_lamp_off():
    GPIO.output(7,GPIO.LOW)

#Kitchen
def k_bulb_on():
    GPIO.output(8,GPIO.HIGH)
def k_bulb_off():
    GPIO.output(8,GPIO.LOW)

#Washroom
def w_bulb_on():
    GPIO.output(9,GPIO.HIGH)
def w_bulb_off():
    GPIO.output(9,GPIO.LOW)
def w_geyser_on():
    GPIO.output(10,GPIO.HIGH)
def w_geyser_off():
    GPIO.output(10,GPIO.LOW)
#Living Room

def l_bulb_on():
    GPIO.output(11,GPIO.HIGH)
def l_bulb_off():
    GPIO.output(11,GPIO.LOW)

def l_fan_on():
    GPIO.output(12,GPIO.HIGH)
def l_fan_off():
    GPIO.output(12,GPIO.LOW)
def l_AC_on():
    GPIO.output(13,GPIO.HIGH)
def l_AC_off():
    GPIO.ouput(13,GPIO.LOW)

#Motor Pump

def motor_on():
    GPIO.output(14,GPIO.HIGH)
def motor_off():
    GPIO.output(14,GPIO.LOW)

