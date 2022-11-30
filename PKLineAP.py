import json

import requests

# "line設定.json" 一定要改的地方～～
auth_token="R4XTGnlFzJ+hYSTA8mp47OyRGQbPR5hzXdAYDPaZXBsz7UDBQCHFeXLPpoG2WWsYfGq3HKAOrslaiAlKqix8+k2bk9xaOusBZKzLJMvJimMXEE6heI5Haou+EnW3sfRYow4QEK16p6ikuVL7y3aX2AdB04t89/1O/w1cDnyilFU="
YouruserID="U5f2b01b7ea1b9c122e7d4c7bb654be76"
userId="U5f2b01b7ea1b9c122e7d4c7bb654be76"



def Line_讀取設定檔(filename):
    global auth_token,YouruserID,userId
    # read a json file and return a dictionary
    with open(filename, 'r', encoding='utf-8') as f:
       dict1=json.load(f)
       auth_token=dict1.get('auth_token',"")
       YouruserID=dict1.get('YouruserID',"")
       userId=dict1.get('userId',"")




import uuid
def UUID_產生器():
    return  str(uuid.uuid4())

def Line_廣播推送(toID="",str1="hello"):
    message={
            "to": toID,
            "messages":[
                {
                    "type":"text",
                    "text":str1
                }
            ]
        }


    UUID=UUID_產生器()
    hed = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + auth_token,
           'X-Line-Retry-Key':UUID}
    url = 'https://api.line.me/v2/bot/message/push'
    response = requests.post(url, json=message, headers=hed)
    print(response)
