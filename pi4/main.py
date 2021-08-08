import time
import socket
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)


left_indent = 10
top_indent = 0
box_width = 107
box_height = 62

# Fonts.
font = ImageFont.truetype('fonts/roboto/Roboto-Light.ttf', 14)

while True:
        
    # Draw a black filled box to clear the image.
    draw.rectangle((left_indent, top_indent, box_width, box_height), outline=1, fill=0)
    # draw.hline(left_indent, (31 + top_indent), box_width, 1)
    # draw.vline((53 + left_indent), (31 + top_indent), 31, 1)
    draw.line((left_indent, (31 + top_indent), box_width, (31 + top_indent)), fill=255)
    draw.line(((53 + left_indent), 31, box_height, (31 + top_indent)), fill=255)

    draw.text((15, 12), socket.gethostname(),  font=font, fill=255)
    draw.text((25, 42), '150', font=font, fill=255) # 15, 42

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(1000)