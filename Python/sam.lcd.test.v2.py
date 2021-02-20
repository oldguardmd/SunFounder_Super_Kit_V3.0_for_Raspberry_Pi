from time import sleep

#We are using GPIO port numbers instead of pin numbers.

class LCD:
    def __init__(self, pin_e=15, pin_rs=13, pin_list=[22,18,16,12]):
        import RPi.GPIO as GPIO
        self.GPIO = GPIO
        GPIO.setmode(GPIO.BOARD)
        self.pin_rs = pin_rs
        self.pin_e = pin_e
        self.pin_list = pin_list

        self.full_pin_list = self.pin_list[:]
        self.full_pin_list.append(self.pin_e)
        self.full_pin_list.append(self.pin_rs)

        print (self.full_pin_list)

LCD()





