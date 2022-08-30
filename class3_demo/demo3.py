#python中所有的对象都有一个布尔值
# 使用 bool() 方法来查看布尔值
# 下列对象的布尔值均为 false
#以下对象的布尔值均为false
# False
# 数值0
# None
# 空字符串
# 空列表
# 空元组
# 空字典
# 空集合
print('--------------以下对象的布尔值为False-------------')
print(bool(False))      #False
print(bool(0))          #False
print(bool(0.0))        #False
print(bool(None))       #False
print(bool(''))         #False
print(bool(""))         #False
print(bool([]))         #False 空列表
print(bool(list()))     #False 空列表
print(bool(()))         #False 空元组
print(bool(tuple()))    #False 空元组
print(bool({}))         #False 空字典
print(bool(dict()))     #False 空字典
print(bool(set()))      #False 空集合
print('---------------其他对象的布尔值均为True---------------')
print(not None)
print('----------------not None的值--------------')

#应用场景，可以直接将对象当作布尔值进行判断

age=int(input('请输入您的年龄：'))
if age:   #此时的对象age，同时也能当作布尔值判断进行使用，可以认为是 age>0
    print(age)
else:
    print('您的年龄为：',age)

if age > 0:
    print(age)
else:
    print('您的年龄为：',age)

