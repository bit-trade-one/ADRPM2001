# 06Collar sensor
## 部品説明
### カラーセンサー
OLEDとかぶらないようColor_Sensorのソケットにカラーセンサー本体を外側に向けて接続します。I²Cで通信しています。  

## プログラム
### cls381.py
カラーセンサのライブラリです。  
### color.py
カラーセンサから計測値を取得しターミナルに表示します。  
### color_paper.py
カラーセンサ基板上のLEDを点灯し自ら発光しない物の色を計測できます。対象物から1cmほど離して使用します。  

<img src="https://github.com/bit-trade-one/ADRPM2001/blob/main/images/CollarSensor.jpg" width = "720px" >

### normalize.py
色の度合いを補正する際に使います。実行すると10回測定するので白い紙などを測り、その中で最も大きな値をdisc_color.py内8行目辺りの「NORM_RED」「NORM_GREEN」「NORMA_BLUE」に代入してください。
### README.txt
上記のノーマライズの方法、輝度の高い光の測り方が記載されています。  
