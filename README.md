# rain_cloud_radar

## この雨雲レーダーシステムについて
　GPIOピンにGPSモジュールを接続したRaspberry Piで利用可能．Yahoo! JavaScriptマップAPIを使用．  
 **Yahoo! JavaScriptマップAPIが2020年10月31日(土)に提供終了．一応動作するが，動作は保証されない．(2020年12月8日時点)**
 
## 環境
　動作に必要なライブラリを記す．バージョンは動作確認済みのもの．
 - Python 3.7
 - pySerial 3.0
 - websockets 8.1
 - micropyGPS
 
## 使用方法
 1. "gps_server.py"を実行．
 2. "amagumo.html"を開く．
