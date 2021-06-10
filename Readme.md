# ADRPM2001
「基本パーツ配線済みボード」はRaspberry PiでI/O制御を学ぶための学習ボード。
LEDや抵抗から、サーボモータや有機ELディスプレイまで8種類の電子部品をラズパイで制御できます。
配線やシルク印字を工夫して、電子工作初心者の方にも簡単に様々なパーツを扱えるよう設計しました。
ラズパイマガジン2020年夏号では付録として基版がついてくるほか、記事内にて本ボードを徹底解説。
付録基板の組み立て方法から各種機能の取り扱い方まで網羅しています。
ラズパイx電子工作の入門にぴったりの基本パーツ配線済みボードで、シングルボードコンピュータの世界に足を踏み入れてみませんか。  

## 製品の特徴
・ラズパイマガジン連動！記事と読み合せて様々なパーツを実験・学習！
ラズパイマガジン2020年夏号にて強力特集記事が掲載！
基板へのはんだ付けから各部の使用法まで丁寧に解説。
8種類の電子パーツを搭載し、多方面の学習が可能です。  
・GPIOやPWM、I2C、SPI、アナログ入力で実験が可能！
ラズベリーパイで利用できる様々なI/Oに対応。 GPIO/PWM/I2C/SPI/アナログ入力をそれぞれの電子パーツで使用可能。様々な部品に合わせた適切な使用方法を学べます。  
・わかりやすさに太鼓判！細かいシルク印刷で簡単スピーディーな実験が可能！
姉妹製品「主要パーツ試せるボード」で好評をいただいた、シルク印字マーキングを今回も採用。信号の流れを視覚的にとらえることができる学習しやすいボードになりました。  

基本仕様
【対応機種】Raspberry Pi B+ / 2B / 3B / 3B+ / 4
【実験用搭載部品】タクトスイッチ x2 / ボリューム x1 / 128×32 OLEDパネルx1 / フルカラーシリアルLED x2
【外部接続端子】 外部LEDソケット x1 / 外部抵抗ソケット x1 / 外部LED電圧測定端子 x1 / 外部LED電流測定端子 x1 / 14pinGPIO x1 / 4pin I2C x1 / 6pin SPI x1 / カラーセンサ用端子 x1 / 3pinアナログ端子 x1 / 3pinシリアルLED(NeoPixelシリーズ)出力端子 x1 / サーボモータ接続端子 x2
【実験用同梱部品】カラーセンサ x1 / 単色LED x3(赤・緑・青）/ 抵抗各種 x11 / サーボモータ180° x1 / サーボモータ360° x1 / テスター接続用みの虫クリップ-バナナプラグケーブル x2(赤・黒)
【外形寸法】H20xW65xD56mm（突起部除く）.
【重量】 組立済基板単体：約35g (基板+外部パーツ一式：約120g)
【動作環境】 温度0～45℃、湿度10～60％(結露なきこと）
【生産国】Made in Japan
【保証期間】お買い上げから1年間 (組立済みのみ）
【付属品】ネジセット一式 保証書1部（キット版には付属しません）
（＊Raspberry Pi本体及びケース、ケーブル類は付属致しません。）  

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

