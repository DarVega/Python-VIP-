# 'https://music.163.com/weapi/copyright/pay_fee_message/config?csrf_token='
# 链接 "http://music.163.com/song/media/outer/url?id={}.mp3".format(music_id)

import requests

url = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="

var = requests.post(
    url,
    data={
       "params": "evtid+8JoVkpBfbItk8g3NbZR8pfOXn1QrrgjDpXbChLgnLFRcHxgAwh2mDLDvvKy4JGyXrheIq5XeGz81kqg7cLtX6P0dxsrSCMfDyj2bMmy0Zp+zLtR6mBeAeDPT3KRenAcWhky+xS3WMTGlQaBuyOPw7+OCuIkfBHyUMBbHhnkK70nSGexAa0zGsTTRwSMBaUfOv3fAWlLiGgUWlSkfS/DxTpXpJtmVhvohYd67L60PzJOpOxM2p4Emlp9hWNsN0k+NipgL38YBpXt+5WZr29VSEKlk0p6oGWz/wHdaqtnE6gKuznDCa2DGtDUK03",
       "encSecKey": "573c1b2c21346fcc23119e9113b2a10210d05da5cbdd5c0c9f5126b3f4c28a33d48ed5a9b374481ee43b30a1631f0b9229121d9072c0a97a8956c8fdf21c751f463e520e56b6b6606940983c6205dc43c04d52cf5a1ecfcc8d16b395afe43a9c8448fda08d1f97a0fa7d393ebf15d25ace550d8da065fbe70988c72eae4fadc7"
    }
).json()
item = var['result']['songs']
for i in item:
    name = i["name"]
    music_id = i["id"]
    urls = "http://music.163.com/song/media/outer/url?id={}.mp3".format(music_id)
    mp3 = requests.get(urls).content
    with open("music/" + name + ".mp3", "wb") as f:
        f.write(mp3)
    print(name, "下载完成！")
