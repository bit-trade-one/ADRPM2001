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
$ sudo python3 任意の名前.py
```

----

### GPIOオーディオ出力無効化(PWM使用時は無効化しないと動かない場合あり)

設定ファイル編集のため下記コマンドを入力
```
$ sudo mousepad /boot/config.txt
```
テキストファイルが開くので56行目辺りdtparam=audio=onの先頭に#をつけてコメント化
```
# dtparam=audio=on
```
再起動
```
$ sudo reboot
```


## プログラム
### mcp3002.py
ADコンバータMCP3002のライブラリです。 
### sled.py
シリアルLEDを任意の色で光らせます。
### sled_color.py
ボリュームの位置によりシリアルLEDの色を変えます。
### sled_move.py
シリアルLEDの色を一定間隔で変えて7色に点灯させます。
ボリュームで点灯時間を変えられます。
