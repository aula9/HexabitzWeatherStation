#AulaJazmati
#Test
#Hexabitz Sensors Hub with Raspberry Pi Pico Test
from machine import UART, Pin , I2C
import time
from ssd1306 import SSD1306_I2C
import framebuf

uart = UART(0, baudrate= 921600, tx=Pin(0), rx=Pin(1))  # init with given baudrate
uart.init(921600, bits=8, parity=None, stop=1)          # init with given parameters
print('-- UART Serial Test --')
print('>', end='')
txData = b'\r'
uart.write(txData.decode('utf-8'))
time.sleep(1)
rxData = bytes()
WIDTH  = 128                                            # oled display width
HEIGHT = 32                                            # oled display height

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)       # Init I2C using pins GP8 & GP9 (default I2C0 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config


oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display


while uart.any() > 0:
    rxData = uart.read(12)
    w =rxData.decode('utf-8')
    print(w)
    oled.fill(0)
    oled.text("Temperature(C)&",5,4)
    oled.text("   Humidity %:",5,14)
    oled.text(w,44,23)
    oled.show()
    time.sleep(2)
