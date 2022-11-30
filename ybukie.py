"""
桃園 youbike Q2
取得的網址=%E4%B8%AD%E5%A4%AE%E5%A4%A7%E5%AD%B8%E5%9C%96%E6%9B%B8%E9%A4%A8
problem at line52, how to decode string?
"""

from subprocess import Popen, PIPE
import os
import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import urlparse
import json
import myfun
import subprocess
import urllib.parse
encodedStr = 'Hell%C3%B6%20W%C3%B6rld%40Python'
t1=urllib.parse.unquote(encodedStr)    # URLdecode (解碼)
auth_token="R4XTGnlFzJ+hYSTA8mp47OyRGQbPR5hzXdAYDPaZXBsz7UDBQCHFeXLPpoG2WWsYfGq3HKAOrslaiAlKqix8+k2bk9xaOusBZKzLJMvJimMXEE6heI5Haou+EnW3sfRYow4QEK16p6ikuVL7y3aX2AdB04t89/1O/w1cDnyilFU="
YouruserID="U5f2b01b7ea1b9c122e7d4c7bb654be76"
userId="U5f2b01b7ea1b9c122e7d4c7bb654be76"

class MyHandler(RequestHandler):          # 物件導向OOP
    def do_GET(self):                     # GET 的方法
        t1 = urlparse(self.path)
        path = urlparse(self.path).path  # 取得路徑
        if path != '/':  # 後面加檔案名，可開啟同個路徑的其他檔案
            # 其他  例如：http://127.0.0.1:8888/1.jpg
            super(MyHandler, self).do_GET()  # 呼叫父類別的方法
        else:
            dict1={}
            t1=urlparse(self.path)
            # get path and file name
            t2=urlparse(self.path).path
            query = urlparse(self.path).query  # 取得和解析網路完整的URL
            if query != "":
                # ?sna=a
                a,b = query.split("=")
                b = urllib.parse.unquote(b)       # URL decode (解碼)
                print(a," = ",b)


            # 定義網路的資料型態
            self.send_response(200)           # 回傳200 網路定義
            self.send_header("Content-type", "text/html; charset=utf-8")  # 回傳 資料型態HTML
            self.end_headers()
            str1=""
            if a=="sna":
                # str1 = ybdata(b)
                exe2="python youbike.py "+b
                import os
                html1=""
                with Popen(exe2,
                           stdout=PIPE, stderr=PIPE) as p:
                    output, errors = p.communicate()
                list1 = output.decode('utf-8').splitlines()
                for str1 in list1:
                    html1=html1+str1



            html1=str1.encode("utf-8")               # 把字串 轉成 bytes
            self.wfile.write(html1)           # 把資料 回傳到  瀏覽器

socketserver.TCPServer.allow_reuse_address = True    # 可以重複使用IP
httpd = socketserver.TCPServer(('0.0.0.0', 8000), MyHandler)  # 啟動WebServer
try:
    httpd.serve_forever()                          # 等待用戶使用 WebServer
except:
    print("Closing the server.")
    httpd.server_close()                           # 關閉 WebServer