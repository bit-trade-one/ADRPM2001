# 04Serial LED
## 部品説明
### D1,D2
シリアルLED(フルカラー) GPIO18から制御します。 使用する際はSW3をONにします。
### SW3
上記による。   
## ライブラリ
### シリアルLEDライブラリ
管理者権限で実行する必要があります。

```
$ sudo pip3 install adafruit-circuitpython-neopixel
```

thonnyでプログラムを管理者権限で作成する場合

```
$ sudo thonny
```

プログラムを管理者権限で実行する場合

```
$ sudo python3 sled.py
```

## プログラム
### mcp3002.py
ADコンバータMCP3002のライブラリです。 
