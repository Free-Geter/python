#sort()用于对列表进行排序，调用该方法会改变原来的列表
a=[11,20,13,34,5,36,17]
a.sort()
print(a)
print('正序：',a)
a.sort(reverse=True)
print('逆序：',a)

#sorted 用于对列表进行排序，生成新列表，不改变原来的列表
print('-'*5,'sorted 排序','-'*5)
a=[11,20,13,34,5,36,17]
b=sorted(a)
print('a 列表：',a) #原来列表不会被修改
print('正序 a 列表：',b)
b=sorted(a, reverse=True)
print('逆序 a 列表：',b)