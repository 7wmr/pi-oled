import time
import socket
import psutil
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

indicator_box = True

while True:
        
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Draw box.
    draw.rectangle((left_indent, top_indent, box_width, box_height), outline=1, fill=0)

    # Indicator box.
    if indicator_box == True:
        draw.rectangle(((left_indent + 1), (top_indent + 1), (left_indent + 3), (top_indent + 3)), outline=1, fill=1)
        indicator_box = False
    else:
        indicator_box = True

    draw.line((left_indent, (31 + top_indent), box_width, (31 + top_indent)), fill=255)
    draw.line(((50 + left_indent), (31 + top_indent), (50 + left_indent), box_height), fill=255)

    host_name = socket.gethostname()
    mem_usage = str(psutil.virtual_memory()[2]) + '%'
    cpu_usage = str(psutil.cpu_percent(4)) + '%'

    draw.text((15, 12), host_name,  font=font, fill=255)
    draw.text((15, 42), mem_usage, font=font, fill=255) 
    draw.text((68, 42), cpu_usage, font=font, fill=255) 

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(.1)