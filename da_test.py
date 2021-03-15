import datetime
import json
import time

import pymysql
import requests

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=10',
    'cookie': 'U_TRS1=00000086.87813d1c.5dedb3dc.b1e0ea1b; SINAGLOBAL=10.79.231.185_1575859165.858265; UOR=,blog.sina.com.cn,; Qs_lvt_335601=1599296191; Qs_pv_335601=4289120960897087000%2C15709800655511562%2C2947809733759635000%2C1411156326722380300%2C4097618829650471400; MONEY-FINANCE-SINA-COM-CN-WEB5=; Apache=218.199.186.85_1615532598.506572; ULV=1615532614605:2:1:1:218.199.186.85_1615532598.506572:1587030318295; rotatecount=1; U_TRS2=00000055.19eed66.604b1321.e317221f',
    # 可以把自己浏览器里面的cookie填进去
    'upgrade-insecure-requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}

def get_Data_form_Web(page=1,num=100):
    url = 'http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=' + str(page) +'&num='+str(num)+'&node=sh_a'
    getResponse = requests.get(url, headers=headers, params=None)
    html = getResponse.text
    return html

def write_into_file(str = 'C:/Users/DELL/Desktop/stock_symbol.txt'):
    p = 1
    while True:
        html = get_Data_form_Web(page=p)
        if html == '[]':
            break
        print(p)
        with open(str, 'a', encoding='utf8') as f:
            f.write(html)
            f.write('\n')
        time.sleep(3)
        p += 1
    print("end")


def insert_into_db(str = 'C:/Users/DELL/Desktop/temp_data.txt'):
    # 打开数据库连接
    db = pymysql.connect(host='localhost', user='root', password='200046m..', database='stock')
    with open(str,'r',encoding='utf8')as f:
        htmls = f.readlines()
    for ht in htmls:
        objects = json.loads(ht)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        for obj in objects:
            # print(obj['code'],obj['symbol'],obj['name'])
            time = datetime.datetime.strftime(datetime.datetime.now(),'%y-%m-%d %H:%M:%S')
            sql = "INSERT INTO symbol SET code = '" + obj['code'] + "',symbol = '" + obj['symbol'] + "',name = '" + obj['name'] + "',gmt_create = '" + time + "'ON DUPLICATE KEY UPDATE name='" + obj['name'] +"',gmt_update='"+ time+"';"
            print(sql)
            cursor.execute(sql)
        db.commit()
    db.close()

def get_stock_code():
    select_sql = 'SELECT symbol FROM stock.symbol;'
    db = pymysql.connect(host='localhost', user='root', password='200046m..', database='stock')
    cursor = db.cursor()
    cursor.execute(select_sql)
    stock_code_list = cursor.fetchall()
    db.commit()
    db.close()
    return stock_code_list

def get_deal_info(stock_code_list,day=20):
    db = pymysql.connect(host='localhost', user='root', password='200046m..', database='stock')
    for stock_code in stock_code_list:
        url = 'https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newfqkline/get?_var=kline_dayqfq&param={0},day,,,{1},qfq'.format(stock_code[0],day+1)
        getResponse = requests.get(url, headers=headers, params=None)
        html = getResponse.text
        html = html[13:]
        result = json.loads(html)
        print(result)
        for i in range(day):
            dict = {'日期': result['data'][stock_code[0]]['qfqday'][i][0],
                    '开盘价格': result['data'][stock_code[0]]['qfqday'][i][1],
                    '收盘价格': result['data'][stock_code[0]]['qfqday'][i][2],
                    '最高价格': result['data'][stock_code[0]]['qfqday'][i][3],
                    '最低价格': result['data'][stock_code[0]]['qfqday'][i][4],
                    '成交量': result['data'][stock_code[0]]['qfqday'][i][5],
                    'symbol': stock_code[0],
                    '增长率':((float(result['data'][stock_code[0]]['qfqday'][i][2])-float(result['data'][stock_code[0]]['qfqday'][i+1][2]))/float(result['data'][stock_code[0]]['qfqday'][i+1][2])*100)}
            cursor = db.cursor()
            time_now = datetime.datetime.strftime(datetime.datetime.now(), '%y-%m-%d %H:%M:%S')
            insert_sql = "INSERT INTO stock.info SET symbol = '" + dict['symbol'] + "',date = '" + dict['日期'] + "',kaipan = '" + dict['开盘价格'] + "',shoupan = '" + dict['收盘价格'] + "', max ='" + dict['最高价格'] + "',min ='" + dict['最低价格'] + "',chengjiaoliang = '" + dict['成交量'] + "',increase_rate = '" + str(dict['增长率']) + "',gmt_create = '" + time_now + "';"
            print(insert_sql)
            cursor.execute(insert_sql)
            db.commit()
        print("完成:", dict['symbol'])
        time.sleep(1)
    db.close()


def find_stock(day = 5):
    stock_code_list = get_stock_code()
    db = pymysql.connect(host='localhost', user='root', password='200046m..', database='stock')
    increase_list = []
    decrease_list = []
    for code in stock_code_list:
        ir = 0
        dt = datetime.date.today() - datetime.timedelta(4)
        for i in range(day):
            week = datetime.datetime.strptime(str(dt), "%Y-%m-%d").weekday()
            if week == 6:
                dt -= datetime.timedelta(2)
            elif week == 5:
                dt -= datetime.timedelta(1)
            select_sql = "SELECT increase_rate FROM stock.info where symbol = '"+ code[0] + "' and date = '"+ str(dt) +"';"
            cursor = db.cursor()
            rows = cursor.execute(select_sql)
            if rows == 0:
                break
            else:
                db.commit()
                result = cursor.fetchall()
                # print(dt, code)
                # print(result[0][0])
                ir += result[0][0]
            dt = dt - datetime.timedelta(1)
        if ir > 20:
            increase_list.append(code[0])
        elif ir < -20:
            decrease_list.append(code[0])
    print("在近{0}天，跌幅达到20%以上的股票".format(day),decrease_list)
    print("在近{0}天，增幅达到20%以上的股票".format(day),increase_list)


if __name__ == '__main__':
    # stock_code_list = get_stock_code()
    # print(len(stock_code_list))
    # html = get_deal_info(stock_code_list)
    find_stock()
