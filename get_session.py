import requests
import configparser
from requests.utils import dict_from_cookiejar
import json
from fake_useragent import UserAgent
from requests import sessions
from requests.sessions import session

def  get_login_info():
    con = configparser.ConfigParser()
    con.read('./userInfo.ini', encoding="utf-8")
    try:
        username = con.get('UserInfo', 'username')
        password = con.get('UserInfo','password')
        print(username,password)
    except Exception as e:
        username = input("Please InputYour UserName")
        password = input("Please Input Your PassWord")
    return username,password



def get_session_object(username, password):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cache-contro': 'max-age=0',
        'cookie': 'X_CACHE_KEY=1415806422c66871915101902384599e; Hm_lvt_4f83e18b7d484b57d9790c167a548728=1627377536; _ga=GA1.2.62030650.1627377536; _gid=GA1.2.723468768.1627377536; Hm_lpvt_4f83e18b7d484b57d9790c167a548728=1627378189',
        'referer': 'https://www.leshetu.com/other/yjs',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }
    url = "https://www.leshetu.com/wp-admin/admin-ajax.php"
    form_data = {
        "action": "user_login",
        "username": username,
        "password":	password,
    }
    session_ob = requests.session()
    with open('cookie_save.json', 'a+') as f:
        f.seek(0)
        file_load = f.read()
        if not file_load:
            res = session_ob.post(url=url, headers=headers, data=form_data)
            print('request session:', res.cookies)
            f.write(json.dumps(requests.utils.dict_from_cookiejar(res.cookies)))
            return session_ob
        else:
            print(file_load)
            session_ob.cookies = requests.utils.cookiejar_from_dict(json.loads(file_load))
            print('load session:', session_ob.cookies)
            return session_ob

def reload_file():
    with open('cookie_save.json', 'w') as f:
        f.close()
    return run_get_session()

def run_get_session():
    username, password = get_login_info()
    session = get_session_object(username, password)
    return session


if __name__ == '__main__':
    run_get_session()