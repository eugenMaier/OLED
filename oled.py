

from time import sleep                                  #aus Uhren funktionen wirt sleep importiert
from machine import Pin, SoftSPI, SoftI2C               #es werden die Pins und die Ansteuerungs Buse von dem Chip abgelsen
import st7789py as st7789                               #Bibliothek st7789py wird zu st7789 umgewandelt
from bmp180 import BMP180                               #aus der Bibliothek bmp180 wird die Klasse BMP180 importiert

#choose fonts

from romfonts import vga2_16x16 as font                 #Schirftart wird ausgewählt


i2c = SoftI2C (scl=Pin(22), sda=Pin(21))                #wird angegeben unter welchen Pins der I2C Bus angesteuert wird

bmp = BMP180(i2c)                                       #Objekt bmp wird werstellt und BMP180 wird i2c zugewiesen


spi = SoftSPI(                                          #Variablen für den SoftSPI Bus werden festgelegt
    baudrate=20000000,
    polarity=1,
    phase=0,
    sck=Pin(18),
    mosi=Pin(19),
    miso=Pin(13))

tft = st7789.ST7789(                                    #Variablen für den Display werden festgelegt
    spi,
    135,
    240,
    reset=Pin(23, Pin.OUT),
    cs=Pin(5, Pin.OUT),
    dc=Pin(16, Pin.OUT),
    backlight=Pin(4, Pin.OUT),
    rotation=0)

#tft.vscrdef(40,240,40)

tft.fill(st7789.GREEN)                                  #Hintergrundfarbe
line = 0                                                #Anfangsparameter
col = 0                                                 #Anfangsparameter
while True:                                             #Schleife wird eingebaut
    ausgabe = str(bmp.temperature)                      #Objekt asugabe wird deklariert und wir als String ausgegeben
    tft.text(font, ausgabe, 10, 10, st7789.BLUE, st7789.YELLOW) #Text ausgabe 