# def foo(num):
#     print("starting...")
#     while num<10:
#         num=num+1
#         yield num
# for n in foo(0):
#     print(n)
# import datetime
#
# import pymysql
#
# db = pymysql.connect(host='localhost', user='root', password='200046m..', database='stock')
# dt = datetime.date.today() - datetime.timedelta(0)
# select_sql = "SELECT increase_rate FROM stock.info where symbol = '"+ 'sz000001' + "' and date = '"+ '2021-03-11' +"';"
# cursor = db.cursor()
# cursor.execute(select_sql)
# db.commit()
# result = cursor.fetchall()
# print(result[0][0])

from datetime import datetime


week = datetime.strptime('2021-03-07', "%Y-%m-%d").weekday()
print(week)

print(week)