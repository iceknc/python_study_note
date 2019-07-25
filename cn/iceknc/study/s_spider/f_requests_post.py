# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/23
# @Desc  : 
import requests


def main():
    post_url = "https://fanyi.baidu.com/sug"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/12.0 Mobile/15A372 Safari/604.1"}

    post_data = {
        "kw": "床前明月光",
    }

    response = requests.post(post_url, headers=headers, data=post_data)
    print(response.content.decode())


if __name__ == "__main__":
    main()
