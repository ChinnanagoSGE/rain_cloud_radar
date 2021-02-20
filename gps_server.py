# -*- coding: utf-8 -*-

import tkinter as tk
import socket
import serial
import micropyGPS
import threading
import sys
import asyncio
import websockets

#GPSの取得
gps=micropyGPS.MicropyGPS(9,'dd')

def rungps():
    s=serial.Serial('/dev/serial0',9600,timeout=10)#address
    s.readline()
    while True:
        sentence=s.readline().decode('utf-8')
        if(sentence==""):
            continue
        if (sentence[0]!='$'):
            continue
        for x in sentence:
            gps.update(x)
gpsthread1=threading.Thread(target=rungps,args=())
gpsthread1.daemon=True
gpsthread1.start()

root = tk.Tk()

# クライアント接続すると呼び出す。
async def accept(websocket, path):
    # 無限ループ
    while True:
        try:
            # 接続されたら緯度経度の情報を','で区切って少数9桁で送る
            mpoint = str('{:.9f}'.format(gps.latitude[0])) + ', ' + str('{:.9f}'.format(gps.longitude[0]))
            await websocket.send(mpoint)
        except:
            # 接続が切れたらpythonを終了する
            exit()

# WebSocketサーバー生成。ホストはlocalhost、ポート番号は10001に生成し，"amagumo.html"と通信。
start_server = websockets.serve(accept, "localhost", 10001)
# 非同期でサーバを待機する。
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

root.mainloop()
