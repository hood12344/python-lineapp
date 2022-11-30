# 技術文章
# https://developers.line.biz/en/docs/messaging-api/sending-messages/#methods-of-sending-message

# 一定要改的地方～～
auth_token="R4XTGnlFzJ+hYSTA8mp47OyRGQbPR5hzXdAYDPaZXBsz7UDBQCHFeXLPpoG2WWsYfGq3HKAOrslaiAlKqix8+k2bk9xaOusBZKzLJMvJimMXEE6heI5Haou+EnW3sfRYow4QEK16p6ikuVL7y3aX2AdB04t89/1O/w1cDnyilFU="
接收人的id=["U5f2b01b7ea1b9c122e7d4c7bb654be76"]

import requests
import json


# 請參考
# https://developers.line.biz/zh-hant/docs/messaging-api/sending-messages/#methods-of-sending-message
message = {
    "to": 接收人的id,
    "messages": [
                {
                    "type": "text",
                    "text": "1. 你好 \n  push資料"
                }
            ]
    }

# 資料回傳 到 Line 的 https 伺服器
hed = {'Authorization': 'Bearer ' + auth_token}
url = 'https://api.line.me/v2/bot/message/multicast'

t1=requests.post(url, json=message, headers=hed)      # 把資料HTTP POST送出去
print(t1)


"""
curl -v -X POST https://api.line.me/v2/bot/message/multicast \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
    "to": ["U4af4980629...","U0c229f96c4..."],
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