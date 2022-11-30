
import PKLineAP
import requests

"""
參考資料：
https://developers.line.biz/en/reference/messaging-api/#send-push-message

curl -v -X POST https://api.line.me/v2/bot/message/push \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-H 'X-Line-Retry-Key: {UUID}' \
-d '{
    "to": "U4af4980629...",
    "messages":[
        {
            "type":"text",
            "text":"Hello, world1"
        },
        {
            "type":"text",
            "text":"Hello, world2"
        }
    ]
}'
"""
PKLineAP.Line_讀取設定檔("line設定.json")
PKLineAP.Line_廣播推送(PKLineAP.userId,"你好 世界222")