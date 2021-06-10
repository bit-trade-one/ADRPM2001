## 部品・端子説明
### JP1
3.3V側にジャンパを接続すると3.3V端子から電源を引っ張りLEDが常時点灯するため、抵抗選定時などに使用します。
反対側にジャンパを接続するとGPIO14と接続し制御が可能になります。  
### Resistor
抵抗をコの字型に曲げて5つ穴のある端子の両端に接続します。横にある100Ω抵抗と直列につながり、LEDの電流値を決めることができます。  
### LED
Aと書いてある方にLEDのアノードを接続します。  
### JP2
左側に接続するとGNDとつながり、右側に接続するとCURRENT端子からテスタなどで測定
ができます。  
### CURRENT
上記JP2に記載
### JP3
接続するとADC1chでLEDにかかる電圧値を測定できます。　　
### VOLT
LEDにかかる電圧値をテスタなどで測定できる端子です。

### SW1
スイッチのボタンを押すとGPIO17と3.3Vが導通します。  
### SW2
スイッチのボタンを押すとGPIO4とGNDが導通します。 

### ボリューム(可変抵抗)
つまみで指定した電圧をADコンバータへ入力します。 
### 180°サーボモータ
指定した角度にホーンが動きます。白いシールが貼ってあります。  
### Servo_A(J4)
サーボモータの橙色の信号線を▼印のある方に合わせて接続します。GPIO5で制御可能です。  
### Servo_B(J5)
サーボモータの橙色の信号線を▼印のある方に合わせて接続します。GPIO6で制御可能です。  


### D1,D2
シリアルLED(フルカラー) GPIO18から制御します。 使用する際はSW3をONにします。
### SW3
上記による。   


### 有機ELディスプレイ
128*32のディスプレイです。I²Cで通信しています。  
### 360°サーボ
連続回転可能なサーボモータです。黄色いシールが貼ってあります。  

### カラーセンサー
OLEDとかぶらないようColor＿Sensorのソケットにに本体
を外側に向けて接続します。I²Cで通信しています。  

---
## 使用コマンド
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

