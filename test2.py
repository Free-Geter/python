import re

import chardet   #需要导入这个模块，检测编码格式


# "(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]"

f = open('nike.txt','rb')
str = f.read()
encode_type = chardet.detect(str)
str = str.decode(encode_type['encoding'])
# print(str)

f.close()
result = re.finditer(r'https://img.alicdn.com/imgextra/i\d/890482188/[A-Za-z0-9-!_]*?.jpg_430x430q90.jpg',str, re.M|re.I)
for match in result:
    print(match.group())
print(re.findall(r'cloud.video.taobao.com/play/u/890482188/p/\d/e/6/t/MLP_Handwriting_numbers/[0-9]*.mp4',str,re.M|re.I))




# cloud.video.taobao.com/play/u/890482188/p/2/e/6/t/MLP_Handwriting_numbers/249265602501.mp4
# cloud.video.taobao.com/play/u/890482188/p/MLP_Handwriting_numbers/e/6/t/MLP_Handwriting_numbers/295197894623.mp4
