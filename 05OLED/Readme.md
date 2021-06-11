# 05OLED
## 部品説明
### 有機ELディスプレイ(Organic Light Emitting Diode → OLED)
128*32のディスプレイです。I²Cで通信しています。  
### 360°サーボモータ
連続回転可能なサーボモータです。黄色いシールが貼ってあります。  

## ライブラリ
### 日本語フォント

```
$ sudo apt install fonts-takao
```

### OLEDライブラリ

```
$ git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
$ cd Adafruit_Python_SSD1306/
$ sudo python3 setup.py install
```
## プログラム
### con_servo.py
可変抵抗の電圧値を取得し、それに合わせてサーボの速度・回転方向を変更します。  ターミナルに取得した電圧値と出力するパルスを表示します。  
### mcp3002.py
ADコンバータMCP3002のライブラリです。  
### menu_servo.py
速度選択、回転方法選択、パルス幅表示メニューを有機ELディスプレイ上に表示しSWを使い選択するとサーボを制御できるプログラムです。  
![Servo1](https://raw.githubusercontent.com/bit-trade-one/ADRPM2001/main/image/Servo.jpg?token=AUMSAR65GKWV4AT272FMUYLAYMRBG)  

### OLED_text.py
有機ELディスプレイに 以下の文を表示します。

```
基本パーツ  
配線済みボード  
```

