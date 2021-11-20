





from time import sleep

from machine import Pin, SoftSPI, SoftI2C
import st7789py as st7789
from bmp180 import BMP180

#choose fonts

from romfonts import vga2_16x16 as font

i2c = SoftI2C (scl=Pin(22), sda=Pin(21))

bmp = BMP180(i2c)


spi = SoftSPI(
    boudrate=20000000,
    polarity=1,
    phase=0,
    sck=Pin(18),
    mosi=Pin(19),
    miso=Pin(13))

tft = st7789.ST7789(
    spi,
    135,
    240,
    reset=Pin(23, Pin.OUT),
    cs=Pin(5, Pin.OUT),
    dc=Pin(16, Pin.OUT),
    backlight=Pin(4, Pin.OUT),
    rotation=1)

#tft.vscrdef(40,240,40)

tft.fill(st7789.GREEN)
line = 0 
col = 0
while True:
    ausgabe = str(bmp.temperature)
    tft.text(font, ausgabe, 10, 10, st7789.BLUE, st7789.YELLOW)