from time import sleep

#We are using GPIO port numbers instead of pin numbers.

class LCD:
    pin_rs_cmd = False  # Equivelent of zero or off for register select.
    pin_rs_data = True  # Equivelent of 1 or on for register select.

    #Control Pins
    pin_rs = 13
    pin_e = 15

    #Data Pin Assignments
    lcd_d4 = 22
    lcd_d5 = 18
    lcd_d6 = 16
    lcd_d7 = 12

    def __init__(self):
        import RPi.GPIO as GPIO
        self.GPIO = GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.full_pin_list = {}
        self.full_pin_list['e]'] = self.pin_e
        self.full_pin_list['rs'] = self.pin_rs
        self.full_pin_list['d4'] = self.lcd_d4
        self.full_pin_list['d5'] = self.lcd_d5
        self.full_pin_list['d6'] = self.lcd_d6
        self.full_pin_list['d7'] = self.lcd_d7
        print(self.full_pin_list)
        exit()
    
    def setAllPinsToOutput(self):
        for pin in self.full_pin_list:
            self.GPIO.setup(pin, self.GPIO.OUT)
        return

    def resetAllPins(self):
        for pin in self.full_pin_list:
            #
            sleep(.5)
        return

    def main(self):
        self.setAllPinsToOutput()
            


LCD().main()