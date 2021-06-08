### pigpio有効化

```
$ sudo systemctl enable pigpiod
$ sudo systemctl start pigpiod
```

### pigpio再起動

```
$ sudo systemctl restart pigpiod
```

### シリアルLEDライブラリ
管理者権限必須

```
$ sudo pip3 install adafruit-circuitipython-neopixel
```

#### 管理者権限でthonnyを起動

```
$ sudo thonny
```

### OLED関連ライブラリ
#### 日本語フォントインストール

```
$ sudo apt-get install fonts-takao
```

#### OLEDライブラリ

```
$ git clone https://github.com/adafruit/Adafuruit_python_SSD1306.git
$ cd Adafruit_python_SSD1306/
$ sudo python3 setup.py install
```

