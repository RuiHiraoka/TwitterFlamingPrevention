
# coding: utf-8

# In[ ]:

from requests_oauthlib import OAuth1Session

CK = 'XXXXXXXXXXXXXXXXXXXXXX'                             # Consumer Key
CS = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'         # Consumer Secret
AT = 'XXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' # Access Token
AS = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'         # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"


def tweet(image,text):
    # ツイート本文
    files = {
        "status": text, "media[]": open(image, "rb")
    }
    
    # OAuth認証で POST method で投稿
    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.post(url, params = params)
    # レスポンスを確認
    if req.status_code == 200:
        return ("OK")
    else:
        return ("Error: %d" % req.status_code)

