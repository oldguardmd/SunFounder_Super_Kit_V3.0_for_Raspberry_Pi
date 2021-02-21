from time import sleep

#We are using GPIO port numbers instead of pin numbers.

class LCD:
    pin_rs_cmd = False  # Equivelent of zero or off for register select.
    pin_rs_data = True  # Equivelent of 1 or on for register select.

    def __init__(self, pin_e=15, pin_rs=13, pin_list=[22,18,16,12]):
        import RPi.GPIO as GPIO
        self.GPIO = GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        self.pin_rs = pin_rs    #GPIO 27
        self.pin_e = pin_e      #GPIO 22
        self.pin_list = pin_list    #GPIO 25, 24, 23, 18

        self.full_pin_list = self.pin_list[:]
        self.full_pin_list.append(self.pin_e)
        self.full_pin_list.append(self.pin_rs)
    
    def resetAllPins(self):
        for pin in self.full_pin_list:
            self.GPIO.setup(pin, self.GPIO.OUT)
            sleep(.5)
        return

    def main(self):
        self.resetAllPins()
            


LCD().main()