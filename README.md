# pi-oled


## Raspberry Pi Setup

```bash
sudo apt install -y python3-dev
sudo apt install -y python3-pil
sudo apt install -y python3-pip
sudo apt install -y python3-setuptools
sudo apt install -y python3-rpi.gpio
sudo apt install -y i2c-tools
sudo apt install -y python3-smbus
```

```bash
sudo pip3 install psutil
```

```bash
cd /repos
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python setup.py install
```

```bash
sudo pip3 install Adafruit-SSD1306
```

```bash
sudo python3 pi4/main.py
```

https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/
https://www.dafont.com/search.php?text=k3s-master-1
