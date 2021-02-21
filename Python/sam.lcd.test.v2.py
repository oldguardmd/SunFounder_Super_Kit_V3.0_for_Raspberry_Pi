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

    #Common Hex Values for 1602 operations
    initialize_stage1 = 0x33
    initialize_stage2 = 0x32
    matrix = 0x28             # 2 line 5x7 Matrix
    cursor_off = 0x0C         # Cursor Off
    cursor_on = 0x0E          # Cursor On

    #Time
    onesecond = 1000000 # Number of microseconds in a second

    #Debugging Output
    debug = True

    def __init__(self):
        import RPi.GPIO as GPIO
        self.GPIO = GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.full_pin_list = {}
        self.full_pin_list['e'] = self.pin_e
        self.full_pin_list['rs'] = self.pin_rs
        self.full_pin_list['d4'] = self.lcd_d4
        self.full_pin_list['d5'] = self.lcd_d5
        self.full_pin_list['d6'] = self.lcd_d6
        self.full_pin_list['d7'] = self.lcd_d7
    
    def setAllPinsToOutput(self):
        for pin in self.full_pin_list:
            self.GPIO.setup(self.full_pin_list[pin], self.GPIO.OUT)
        return
    
    def clear4bits(self):
        #Basic house keeping to clear four bits to 0s before we set them.
        #This does not right the register. We assume enable is 0
        for name, pin in self.full_pin_list.items():
            if str(name).startswith('lcd'):
                self.GPIO.output(pin,False)
        return
    
    def write4bits(self,fourBits):
        if fourBits[0] == 1:
            print(f'Setting D4 to True') if self.debug==True else print(f'Setting D4 to False')
            self.GPIO.output(self.lcd_d4, True)
        if fourBits[1] == 1:
            print(f'Setting D5 to True') if self.debug==True else print(f'Setting D5 to False')
            self.GPIO.output(self.lcd_d5, True)
        if fourBits[2] == 1:
            print(f'Setting D6 to True') if self.debug==True else print(f'Setting D6 to False')
            self.GPIO.output(self.lcd_d6, True)
        if fourBits[3] == 1:
            print(f'Setting D7 to True') if self.debug==True else print(f'Setting D7 to False')
            self.GPIO.output(self.lcd_d7, True)
    
    def enableChange(self):
        # This sets the enable flag so that the 1602 reads the change
        self.GPIO.output(self.pin_e, False)
        sleep(1/self.onesecond) # Sleep one microsecond
        self.GPIO.output(self.pin_e, True)
        sleep(1/self.onesecond) # Sleep one microsecond
        self.GPIO.output(self.pin_e, False)
        sleep(1/self.onesecond) # Sleep one microsecond
        return

    def write8bits(self, hex_bits,mode):
        #to write 8 bits in 4 bit mode, we split the binary into 4 bits and send the sequentially
        sleep(3000/1000000) # Wait to ensure previous change is completed
        bin_bits = bin(hex_bits)[2:].zfill(8)   #Convert hex to a 8 bit binary number
        
        #we need to set either commands or data.
        self.GPIO.output(self.pin_rs, mode)

        #set all bits to false so they are off
        self.clear4bits()

        #Write high bits
        print(f'writing: {bin_bits[4:]}')
        self.write4bits(fourBits=bin_bits[4:])
        self.enableChange()
        #Write low bits
        print(f'writing: {bin_bits[:4]}')
        self.write4bits(fourBits=bin_bits[:4])
        self.enableChange()

        return

    def main(self):
        self.setAllPinsToOutput()
        self.write8bits(self.initialize_stage1, self.pin_rs_cmd)
        self.write8bits(self.initialize_stage2, self.pin_rs_cmd)
        self.write8bits(self.matrix, self.pin_rs_cmd)
        self.write8bits(self.cursor_off, self.pin_rs_cmd)

            


LCD().main()