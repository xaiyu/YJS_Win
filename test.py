# # from get_session import run_get_session
# import brotli
# import chardet
# import wget
# import requests
# import zipfile
# from io import BytesIO
import random


print(type(random.randint(900, 1200)))
# def get_detail():
#     headers = {
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
#         'cache-contro': 'max-age=0',
#         # 'cookie': 'X_CACHE_KEY=1415806422c66871915101902384599e; Hm_lvt_4f83e18b7d484b57d9790c167a548728=1627377536; _ga=GA1.2.62030650.1627377536; _gid=GA1.2.723468768.1627377536; Hm_lpvt_4f83e18b7d484b57d9790c167a548728=1627378189',
#         'referer': 'https://www.leshetu.com/other/yjs',
#         'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-fetch-dest': 'document',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'same-origin',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
#     }
#     url = 'https://pan.156135784.xyz/show/WLJ15/QLFkaYWaek1.zip'
#     r = requests.get(url, stream=True)
#     print(r.content)
#     z = zipfile.ZipFile(BytesIO(r.content))
#     z.extractall()

# def decode_res():
#     with open('./1.html', 'rb') as f:
#         while True:
#             line = f.readline()
#             if not line:
#                 break
#             else:
#                 try:
#                     # print(line.decode('utf8'))
#                     line.decode('utf8')
#                     # 为了暴露出错误，最好此处不print
#                 except:
#                     print(str(line))

# def test():
#     with open('cookie_save.txt', 'a+') as f:
#         f.seek(0)
#         print(f.read())
#         print('kongde', f.read())
#         if f.read()=='':
#             print('有东西')
#         else:
#             print('没东西')
            
# def wget_file():
#     wget.download('https://pan.156135784.xyz/show/WLJ15/QLFkaYWaek1.zip','1.zip')
#     requests.

# if __name__ == '__main__':
#     # session = run_get_session()
#     get_detail()
#     # # decode_res()
#     # # test()
#     # wget_file()

# from data_filter import filter_data
#
# filter_data('https://www.leshetu.com/go?post_id=17730')
# filter_data.next()