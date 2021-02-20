# written by Mazen Osama for Rpi-Model3B
# this is just to simplify some things with handling text
# ---------------------------------------------------------
# from this line up to the line saying: disp.begin()
# These are the neccessary lines in order to start writing your code
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import ST7735 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI




def DisplayInit():

    WIDTH = 128
    HEIGHT = 160
    SPEED_HZ = 4000000

    # Raspberry Pi configuration.
    DC = 24
    RST = 25
    SPI_PORT = 0
    SPI_DEVICE = 0

    # Create TFT LCD display class.
    disp = TFT.ST7735(
        DC,
        width=WIDTH,
        height=HEIGHT,
        rst=RST,
        spi=SPI.SpiDev(
            SPI_PORT,
            SPI_DEVICE,
            max_speed_hz=SPEED_HZ))

    # Initialize display.
    disp.begin()
    # Get a PIL Draw object to start drawing on the display buffer.
    draw = disp.draw()
    disp.clear()
    font = ImageFont.load_default()




# Define a function to create rotated text.  Unfortunately PIL doesn't have good
# native support for rotated fonts, but this function can be used to make a
# text image and rotate it so it's easy to paste in the buffer.
def DisplayRotatedText(image, text, position, angle, fill=(255,255,255)):
    global font
    # Get rendered font width and height.
    draw = ImageDraw.Draw(image)
    width, height = draw.textsize(text, font=font)
    # Create a new image with transparent background to store the text.
##    textimage = Image.new('RGBA', (width, height), (0,0,0,0))
    textimage = Image.new('RGBA', (WIDTH, HEIGHT), (0,0,0,0))
    # Render the text.
    textdraw = ImageDraw.Draw(textimage)
    textdraw.text((0,0), text, font=font, fill=fill)
    # Rotate the text image.
    rotated = textimage.rotate(angle, expand=1)
    # Paste the text into the image, using it as a mask for transparency.
    image.paste(rotated, position, rotated)

