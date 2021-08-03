import ssd1306
import machine
import time
import uos
import machine
import framebuf

print(uos.uname())
print("Freq: "  + str(machine.freq()) + " Hz")
print("128x64 SSD1306 I2C OLED on Raspberry Pi Pico")

WIDTH = 128
HEIGHT = 64

i2c = machine.I2C(0)

print("Available i2c devices: "+ str(i2c.scan()))
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

#oled.text("N:k3s-master-1", 0, 0)
#oled.text("I:192.168.85.150", 0, 10)
#oled.text("S:OK", 0, 20)
#oled.text("U:12h", 0, 30)
#fbuf = framebuf.FrameBuffer(bytearray(8 * 8 * 1), 8, 8, framebuf.MONO_VLSB)
#fbuf.line(0, 0, 60, 60, 1)
#oled.blit(fbuf, 10, 10, 0)


with open('tick_icon.pbm', 'rb') as f:
    f.readline() # magic number
    f.readline() # creator comment
    f.readline() # dimensions
    data = bytearray(f.read())

TICK_ICON = framebuf.FrameBuffer(data, 50, 27, framebuf.MONO_HLSB)

with open('cross_icon.pbm', 'rb') as f:
    f.readline() # magic number
    f.readline() # creator comment
    f.readline() # dimensions
    data = bytearray(f.read())

CROSS_ICON = framebuf.FrameBuffer(data, 50, 27, framebuf.MONO_HLSB)

left_indent = 10
top_indent = 0
box_width = 107
box_height = 62

icon_switch = True
while True:
    oled.fill(0)
    oled.rect(left_indent, top_indent, box_width, box_height, 1)
    oled.hline(left_indent, (31 + top_indent), box_width, 1)
    oled.vline((53 + left_indent), (31 + top_indent), 31, 1)
    oled.text("k3s-master-1", 15, 12)
    oled.text("150", 15, 42)
    if icon_switch == True:
        oled.blit(TICK_ICON, 65,33)
        icon_switch = False
    else:
        oled.blit(CROSS_ICON, 65,33)
        icon_switch = True
    oled.show()
    time.sleep_ms(1000)
