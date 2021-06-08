# 01LED
## 端子説明
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
###　JP3
接続するとADC1chでLEDにかかる電圧値を測定できます。　　
###　VOLT
LEDにかかる電圧値をテスタなどで測定できる端子です。　　

## プログラム
### LED‗bling.py
基板上のLED"D1"が点滅を繰り返します。　　

```
import pigpio #ライブラリのインポート
import time

LED_PIN = 14 #LED_PINに14を代入
LED_TIME ＝ 1 #LED_TIME に 1を代入
pi = pigpio.pi()　#GPIOにアクセスするためのインスタンスを作成

pi.set_mode( LED_PIN, pigpio.OUTPUT ) #LED_PINをアウトプットに設定

while True:　#以下無限ループ
	pi.write( LED_PIN, pigpio.LOW ) # LED_PIN出力ををオフにする
	time.sleep( LED_TIME ) # LED_TIMEの値秒待機
	pi.write( LED_PIN, pigpio.HIGH ) # LED_PIN出力ををオンにする
	time.sleep( LED_TIME ) # LED_TIMEの値秒待機
```

### led_off.py
LEDをオフにします　　
### led_on.py
LEDをオンにします　　
### led_pattern.py
三三七拍子でLEDが点滅します　　
