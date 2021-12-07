

from time import sleep                                  # alle 10 Sekunden die Temperatur messen
from machine import Pin, SoftSPI, SoftI2C               # Pin , SoftSPI (TFT), SoftI2C (BMP180)
import st7789py as st7789                               # TFT Display
from bmp180 import BMP180                               # BMP180 Temperatursensor
from bh1750 import BH1750                               # BH1750 Lichtsensor
from htu2x import HTU21D

#choose fonts

from romfonts import vga2_16x16 as font                 # Schriftart laden


i2c = SoftI2C (scl=Pin(22), sda=Pin(21))                # I2C (BMP180)

bmp = BMP180(i2c)                                       # Objekt bmp instanzieren
bh = BH1750(i2c)                                        # Objekt bh instanzieren
ht = HTU21D(22,21)

ledgruen = Pin(25, Pin.OUT)                             # Objekt ledgruen instanzieren
ledgelb = Pin(26, Pin.OUT)                              # Objekt ledgelb instanzieren
ledrot = Pin(27, Pin.OUT)                               # Objekt ledrot instanzieren

spi = SoftSPI(                                          # Objekt spi instanzieren
    baudrate=20000000,                                  # Kummunikationsgeschwindigkeit
    polarity=1,                                         
    phase=0,
    sck=Pin(18),
    mosi=Pin(19),
    miso=Pin(13))

tft = st7789.ST7789(                                    # Objekt tft instanzieren
    spi,                                                # Schnittstelle
    135,                                                # Pixel x-Achse (hochkant)
    240,                                                # Pixel y-Achse
    reset=Pin(23, Pin.OUT),
    cs=Pin(5, Pin.OUT),
    dc=Pin(16, Pin.OUT),
    backlight=Pin(4, Pin.OUT),
    rotation=1)                                         # Querformat


#----------------------------Initialisierung Ende-------------------------------------------------

tft.fill(st7789.BLACK)                                  # Hintergrundfarbe Grün
line = 0                                                # Textbeginn Zeile
col = 0                                                 # Textbeginn Spalte
while True:

    #led nach Temperatur anzeigen
    if bmp.temperature <= 24:                           
        ledgruen.value(1)
        ledgelb.value(0)
        ledrot.value(0)
    elif bmp.temperature >25:
        ledrot.value(1)
        ledgelb.value(0)
        ledgruen.value(0)
    else:
        ledgelb.value(1)
        ledrot.value(0)
        ledgruen.value(0) 
    # Text ausgabe                                        
    temp = str(round(bmp.temperature,1))             # Objekt ausgabe wird deklariert und wird als String ausgegeben
    druck = str(round(bmp.pressure/100,1))           # Objekt druck initialisieren
    licht = str(round(bh.luminance(BH1750.CONT_HIRES_1)))
    luft = str(round(ht.humidity))
    temperatur = str(round(ht.temperature))
    tft.text(font,'Temp:'+temp+'\xf8c', 10, 10, st7789.GREEN, st7789.BLACK)
    tft.text(font,'L:'+druck+'hPa', 10, 30, st7789.GREEN, st7789.BLACK)       
    tft.text(font,'Licht:'+licht+'lux', 10, 50, st7789.GREEN, st7789.BLACK)
    tft.text(font,'Luft:'+luft+'%', 10, 70, st7789.GREEN, st7789.BLACK)
    tft.text(font,'Temp:'+temperatur+'\xf8c', 10, 90, st7789.GREEN, st7789.BLACK)
    sleep(1)