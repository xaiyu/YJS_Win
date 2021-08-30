import re
target = "膏 - Z5-1 制服短丝 [435P2V1.9G]"

print(re.search('大西瓜爱牙膏', target))

if not re.search('大西瓜爱牙膏', target):
    print('检测到')