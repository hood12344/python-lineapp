import urllib.request as httplib
import ssl

# 透過連結取得穩路上的文件 (xml/json/csv)
def http_get(url=''):
    ssl._create_default_https_context = ssl._create_unverified_context  # 因.urlopen發生問題，將ssl憑證排除
    url = url
    req = httplib.Request(url, data=None,
                          headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"})
    reponse = httplib.urlopen(req)              # 開啟連線動作
    if reponse.code == 200:                     # 當連線正常時
        contents = reponse.read()               # 讀取網頁內容
        contents = contents.decode("utf-8")     # 轉換編碼為 utf-8
    return contents