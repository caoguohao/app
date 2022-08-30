#python中的比较运算符

#比较运算符，比较运算符的结果为bool类型
a,b=20,30
print("a>b吗？",a>b)  #False
print("a<b吗？",a<b)  #True
print("a>=b吗？",a>=b)    #False
print("a<=b吗？",a<=b)    #True
print("a==b吗？",a==b)    #False
print("a!=b吗？",a!=b)    #True

#一个 = 称为赋值运算符,   == 称为比较运算符
#一个变量由三部分组成：标识（内存id），类型（type）,值（value）
#  == 比较的是值
#  比较标识用的是  is

a=10
b=10
c=5+5
print(id(a))
print(id(b))
print(id(c))
print(a==b)    #True 说明 a和b 的Value相等
print(a is b)  #True 说明 a和b 的标识也相等
print(a is not b)  #True 说明 a和b 的标识不相等
list1=[11,22,33,44]
list2=[11,22,33,44]
print(id(list1))
print(id(list2))
print(list1 == list2)
print(list1 is list2)
print(list1 is not list2)