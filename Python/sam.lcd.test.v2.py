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
    LCD_initialize_stage1 = 0x33
    LCD_set_4bit_mode = 0x32
    LCD_matrix = 0x28             # 2 line 5x7 Matrix
    LCD_cursor_off = 0x0C         # Cursor Off
    LCD_cursor_on = 0x0E          # Cursor On
    LCD_shift_cursor_right = 0x06
    LCD_clear_display = 0x01

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
    
    def write4bits(self, bits, mode):
        self.clear4bits()
        fourBits = bin(bits)[2:].zfill(4)   #Convert hex to a 8 bit binary number

        #we need to set either commands or data.
        self.GPIO.output(self.pin_rs, mode)

        print('\t\tStarting 4 bit write process')
        if self.debug: print(f'\t\tD4 value is {fourBits[3]}')
        if int(fourBits[3]) == 1:
            if self.debug : print(f'\t\tSetting D4 to True')
            self.GPIO.output(self.lcd_d4, True)
        else:
            if self.debug : print(f'\t\tSetting D4 to False')
        if self.debug: print(f'\t\tD5 value is {fourBits[2]}')
        if int(fourBits[2]) == 1:
            if self.debug : print(f'\t\tSetting D5 to True')
            self.GPIO.output(self.lcd_d5, True)
        else:
            if self.debug : print(f'\t\tSetting D5 to False')
        if self.debug: print(f'\t\tD6 value is {fourBits[1]}')
        if int(fourBits[1]) == 1:
            if self.debug : print(f'\t\tSetting D6 to True')
            self.GPIO.output(self.lcd_d6, True)
        else:
            if self.debug : print(f'\t\tSetting D6 to False')
        if self.debug: print(f'\t\tD7 value is {fourBits[0]}')
        if int(fourBits[0]) == 1:
            if self.debug : print(f'\t\tSetting D7 to True')
            self.GPIO.output(self.lcd_d7, True)
        else:
            if self.debug : print(f'\t\tSetting D7 to False')
    
    def enableChange(self):
        # This sets the enable flag so that the 1602 reads the change
        self.GPIO.output(self.pin_e, False)
        sleep(0.0005)
        #sleep(1/self.onesecond) # Sleep one microsecond
        self.GPIO.output(self.pin_e, True)
        sleep(0.0005)
        #sleep(1/self.onesecond) # Sleep one microsecond
        self.GPIO.output(self.pin_e, False)
        sleep(0.0005)
        #sleep(1/self.onesecond) # Sleep one microsecond
        return

    def main(self):
        #These are parameters to start up the LCD
        self.setAllPinsToOutput()
        
        #if self.debug: print('Initializing Stage 1')
        #self.write8bits(self.LCD_initialize_stage1, self.pin_rs_cmd)

        #if self.debug: print('Setting 4 Bit Mode')
        #self.write8bits(self.LCD_set_4bit_mode, self.pin_rs_cmd)

        #if self.debug: print('Setting matrix size')
        #self.write8bits(self.LCD_matrix, self.pin_rs_cmd)

        #if self.debug: print('Setting Cursor visibilty')
        #self.write8bits(self.LCD_cursor_on, self.pin_rs_cmd)

        #if self.debug: print('Shifting Cursor to the Right')
        #self.write8bits(self.LCD_shift_cursor_right, self.pin_rs_cmd)

        #if self.debug: print('Clearing the display')
        #self.write8bits(self.LCD_clear_display, self.pin_rs_cmd)

        self.write4bits(0x03, self.pin_rs_cmd)
        self.write4bits(0x03, self.pin_rs_cmd)
        self.write4bits(0x03, self.pin_rs_cmd)
        self.write4bits(0x02, self.pin_rs_cmd)
        
        self.write4bits(0x02, self.pin_rs_cmd)
        #self.write4bits(0x03, self.pin_rs_cmd)

        self.write4bits(0x00, self.pin_rs_cmd)
        self.write4bits(0x06, self.pin_rs_cmd)

        self.write4bits(0x05, self.pin_rs_data)
        self.write4bits(0x03, self.pin_rs_data)


        sleep(.0005)
        # Everything after this is what you want to display 
        

            


LCD().main()
