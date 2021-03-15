import math


def salary_increase():
    flage = True
    salary = int(input('工资:'))
    if (salary < 0):
        print("工资输入错误")
        flage = False
    year = int(input('工龄:'))
    if year < 0:
        print("工龄输入错误")
        flage = False
    increase = 0

    if year < 1:
        increase = 200
    elif year < 3:
        increase = 500
    elif year < 5:
        increase = 1000
    elif year < 10:
        increase = 2500
    elif year < 15:
        increase = 5000
    else:
        increase = 5000
    if (flage):
        print("您目前工作了{0}年，基本工资为{1}员，应涨工资为{2}元，涨后工资{3}元".format(year, salary, increase, increase + salary))


def how_many_time(start):
    count = 0
    while start < 8848:
        start *= 2
        count += 1
    print("you need to flod {0} times.".format(count))


def double_list(init_list):
    my_map = map(lambda x: x * 2, init_list)
    print(list(my_map))


class Monkey:
    def __init__(self, mark, next_mk=None):
        self.mark = mark
        self.next_mk = next_mk


def Creat_Mk(num):
    first_Mk = None
    current_Mk = None
    for i in range(num):
        monkey_temp = Monkey(i)
        if not first_Mk:
            first_Mk = monkey_temp
            current_Mk = monkey_temp
        else:
            current_Mk.next_mk = monkey_temp
            current_Mk = monkey_temp
    current_Mk.next_mk = first_Mk
    return first_Mk


def King(num):
    first_Mk = Creat_Mk(num)
    current_Mk = first_Mk
    count = 0
    while True:
        current_Mk = current_Mk.next_mk
        count += 1
        if count == 2:
            temp = current_Mk.next_mk
            current_Mk.next_mk = temp.next_mk
            temp.next_mk = None
            count = 0
        if current_Mk.next_mk == current_Mk:
            break
    print(current_Mk.mark)


def big_year(start, end):
    start
    count = 0
    while start <= end:
        if (((start % 4 == 0) & (start % 100 != 0)) | (start % 400 == 0)):
            count += 1
            print(start)
            start += 1
        else:
            start += 1
    print("There are {0} big_years.".format(count))


def target(year):
    String = str(year)
    if String == String[::-1]:
        return True
    else:
        return False


def target_n(grade):
    count = 0
    left = int(math.pow(10, grade - 1))
    right = int(math.pow(10, grade))
    for i in range(left, right):
        if (target(i)):
            count += 1
            i += 1
        else:
            i += 1
    return count


def diff(num1, num2):
    print("相差{0}个回文数：".format(abs(target_n(num1) - target_n(num2))))


def gongyinshu(a, b):
    while True:
        if (a > b):
            big = a
            small = b
        else:
            big = b
            small = a
        if big % small == 0:
            break
        else:
            a = b
            b = big % small
    return small


def gongbeishu(a, b):
    return a * b / gongyinshu(a, b)


class Fenshu:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        if isinstance(other,Fenshu):
            beishu = gongbeishu(self.den,other.den)
            numa = self.num*(beishu/self.den)
            numb = other.num * (beishu/other.den)
            rnum = numa + numb
            rden = beishu
            result = Fenshu(rnum,rden)
            yinshu = gongyinshu(result.num, result.den)
            result.num /= yinshu
            result.den /= yinshu
            return result
        else:
            print("类型不同，无法相加")

def add_fenshu(num):
    fibonaqie = [0, 1, 1]
    sum = None
    for i in range(2,num+4):
        fibonaqie.append(fibonaqie[-1] + fibonaqie[-2])
    for i in range(num):
        if not sum:
            sum = Fenshu(fibonaqie[i+3],fibonaqie[i+2])
            i += 1
        else:
            sum += Fenshu(fibonaqie[i+3],fibonaqie[i+2])
            i += 1
    print("{0} / {1}".format(sum.num,sum.den))


