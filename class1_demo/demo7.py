name='张三'
age=20
print("age的数据类型：",type(age))
age2=str(20)
print("age2的数据类型：",type(age2))
print(type(name),type(age))
#print('我叫'+name+'今年'+age+'岁')   # 当str类型与int类型进行链接时会报错，需要进行类型转接

print('我叫'+name+'今年'+str(age)+'岁')   #将int类型通过str()转换成了str类型再进行连接

#数据类型转换的方法：   str()  int()  float()

print('--------str()将其他类型的数据转成str类型------------')
a=10
b=197.67
c=False
print('a的数据类型',a,type(a))
print('b的数据类型',b,type(b))
print('c的数据类型',c,type(c))


print('a的数据类型',str(a),type(str(a)))
print('a的数据类型',str(b),type(str(b)))
print('a的数据类型',str(c),type(str(c)))

print('--------------int()将其他数据类型转成int类型')
s1='124'
s2=98.62
s3='78.87'
s4=True
s5="hello word"
print('s1的数据类型',s1,type(s1))
print('s2的数据类型',s2,type(s2))
print('s3的数据类型',s3,type(s3))
print('s4的数据类型',s4,type(s4))
print('s5的数据类型',s5,type(s5))

print('s1的数据类型',int(s1),type(int(s1)))  #将str转换成int类型，字符串为数字串
print('s2的数据类型',int(s2),type(int(s2)))  #将float转换成int类型，会截取整数部分，舍掉小数部分
#print('s3的数据类型',int(s3),type(int(s3)))  #将str转换成int类型，报错，因为字符串为小数串
print('s4的数据类型',int(s4),type(int(s4)))  #将bool转换成int类型，true=1 false=0
#print('s5的数据类型',int(s5),type(int(s5)))  #将str转换成int类型，字符串必须为数字串，非数字串不允许转换


print('--------------float()将其他数据类型转成float类型')
#文字类无法转换成整数
#整数转换成浮点，末尾会加上.0


s1='124.67'
s2=98
s3='78'
s4=True
s5="hello word"
print('s1的数据类型',s1,type(s1))
print('s2的数据类型',s2,type(s2))
print('s3的数据类型',s3,type(s3))
print('s4的数据类型',s4,type(s4))
print('s5的数据类型',s5,type(s5))


print('s1的数据类型',float(s1),type(float(s1)))
print('s2的数据类型',float(s2),type(float(s2)))
print('s3的数据类型',float(s3),type(int(s3)))
print('s4的数据类型',float(s4),type(float(s4)))
#print('s5的数据类型',float(s5),type(float(s5)))  #字符串中的数据为非数字串，报错，不允许进行转换