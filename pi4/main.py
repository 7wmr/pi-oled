import time
import socket
import psutil
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi pin configuration:
RST = None #24
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
font = ImageFont.truetype('/repos/pi-oled/fonts/roboto/Roboto-Light.ttf', 14)


def display_box(name, value):
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Draw box.
    draw.rectangle((left_indent, top_indent, box_width, box_height), outline=1, fill=0)

    draw.line((left_indent, (31 + top_indent), box_width, (31 + top_indent)), fill=255)
    draw.line(((45 + left_indent), (31 + top_indent), (45 + left_indent), box_height), fill=255)

    host_name = socket.gethostname()

    draw.text((15, 12), host_name,  font=font, fill=255)
    draw.text((15, 42), name, font=font, fill=255) 
    draw.text((62, 42), value, font=font, fill=255) 

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(2)


while True:
    
    # Display Memory
    mem_usage = str(psutil.virtual_memory()[2]) + '%'

    display_box('MEM', mem_usage)

    # Display CPU
    cpu_usage = str(psutil.cpu_percent(4)) + '%'

    display_box('CPU', cpu_usage)

    # Display Disk
    disk_usage = str(round(psutil.disk_usage('/').percent, 1)) + '%'

    display_box('DSK', disk_usage)

    # Display Temperature
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temperature = f.readlines()
    
    temperature = temperature[0].replace('\n', '')
    degrees_c = int(temperature) / 1000
    degrees_c = str(round(degrees_c, 1)) + "ºC"

    display_box('TMP', degrees_c)



