from random import random
import requests.utils
from lxml import etree
from get_session import run_get_session,reload_file
import time
import random
import re
from urllib.error import HTTPError
import pymysql

session = run_get_session()
db = pymysql.connect(host="155.94.184.173", port=3306, user="false", password="false123", db="YJinfo")

headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cache-contro': 'max-age=0',
        'referer': 'https://www.leshetu.com/other/yjs',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
        # 'user-agent': UserAgent(use_cache_server=False).chrome
     }

def get_response():
    '''
        get index response
    '''
    for i in range(23, 25):
        target_url ="https://www.leshetu.com/tag/12/page/"+str(i)
        print(target_url)
        response_data = requests.get(target_url, headers=headers)
        print('hello')
        parse_response(response_data)

def parse_response(response_data):
    '''
        parse url_list data
        return detail_list
    '''
    data = response_data.content.decode()
    with open('YJS.html','w') as f:
        f.write(data)
    xpath_data_ob = etree.HTML(data)
    xpath_data_list = xpath_data_ob.xpath('//div[@class="entry-media"]//a/@href')
    print("主页列表信息链接:\n", xpath_data_list)
    get_content_response(session=session, data_list=xpath_data_list)


def get_content_response(session, data_list):
    '''
    get download url
    return detail_ulr, detail_title
    '''
    if data_list == []:
        print('empty list')
        return
    for i in data_list:
        time.sleep(random.randint(0,10))
        content_res = session.get(i, headers=headers).content.decode()
        try:
            xpath_data_list = etree.HTML(content_res)
            tags = xpath_data_list.xpath('//div[@class="entry-tags"]/a/text()')
            print(tags)
            detail_url = xpath_data_list.xpath('//div[@class="pay-box"]/a[2]/@href')[0]
            detail_title = xpath_data_list.xpath("//h1/text()")[0]
            print(detail_title,detail_url)
            save_detail_data(detail_title=detail_title, detail_url=detail_url, session=session, index_url=i)
        except Exception as e:
            print('重载Cookie', e)
            if re.search('登录后购买', content_res).group():
                session = reload_file()
                return get_content_response(session,data_list)

def save_detail_data(detail_title, detail_url, session, index_url):
    '''
        get zip url
    '''
    try:
        file_url_data= session.get(detail_url, headers=headers).content.decode()
        file_url =  re.search('https://.+\.zip', file_url_data).group()
        print("资源链接：", file_url)
        # insert_db(title=detail_title, index_url=detail_url, file_url=index_url)
    except Exception as e:
        if isinstance(e, HTTPError):
            print(e)
            time.sleep(random.randint(900, 1200))
            save_detail_data(detail_title,  session)
    

def insert_db(title, index_url, file_url):

    cursor = db.cursor()
    sql = "insert into YJS_table(YJ_title,YJ_Page_url,YJ_tag1, YJ_tag2, YJ_file_url) values('%s','%s','%s');"%(title, index_url, file_url )
    cursor.execute(sql)
    db.commit()



if __name__ == '__main__':
    get_response()
    print('######################################')
