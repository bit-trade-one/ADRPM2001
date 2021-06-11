# ADRPM2001 基本パーツ配線済みボード
「基本パーツ配線済みボード」はRaspberry PiでI/O制御を学ぶための学習ボード。  
LEDや抵抗から、サーボモータや有機ELディスプレイまで8種類の電子部品をラズパイで制御できます。  
配線やシルク印字を工夫して、電子工作初心者の方にも簡単に様々なパーツを扱えるよう設計しました。  
ラズパイマガジン2020年夏号では付録として基版がついてくるほか、記事内にて本ボードを徹底解説。  
付録基板の組み立て方法から各種機能の取り扱い方まで網羅しています。  
ラズパイx電子工作の入門にぴったりの基本パーツ配線済みボードで、シングルボードコンピュータの世界に足を踏み入れてみませんか。  
  
![pin1](https://bit-trade-one.co.jp/wp/wp-content/uploads/2020/04/deff4bca4a0d42b4332a5f1be77e123c.jpg)

### [製品の詳細はこちら(HPリンク)](https://bit-trade-one.co.jp/adrpm2001/)

## 制作例
### [LED制御](https://github.com/bit-trade-one/ADRPM2001/tree/main/01LED)   
### [スイッチ入力](https://github.com/bit-trade-one/ADRPM2001/tree/main/02Switch)   
### [180°サーボ制御、アナログ入力](https://github.com/bit-trade-one/ADRPM2001/tree/main/03Servo)  
![Servo1](https://raw.githubusercontent.com/bit-trade-one/ADRPM2001/main/image/Servo.jpg?token=AUMSAR65GKWV4AT272FMUYLAYMRBG)
### [フルカラーシリアルLED](https://github.com/bit-trade-one/ADRPM2001/tree/main/04Serial%20LED)  
### [有機ELディスプレイ、360°サーボ制御](https://github.com/bit-trade-one/ADRPM2001/tree/main/05OLED)  
### [カラーセンサー](https://github.com/bit-trade-one/ADRPM2001/tree/main/06Collar%20sensor)  
---

## セットアップ

### I2C/SPI有効化

![setting1](https://bit-trade-one.co.jp/wp/wp-content/uploads/2020/04/setting1.png)
![setting2](https://bit-trade-one.co.jp/wp/wp-content/uploads/2020/04/setting2.png)

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
