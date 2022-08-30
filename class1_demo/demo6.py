#常用的数据类型
#整数类型，可以表示正数，负数，零  int   98
n1 = 90
n2 = -76
n3 = 0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
#整数可以表示为二进制，十进制，八进制和十六进制
print('十进制',118)
#要让python理解二进制数据时，要在前面加上 0b
print('二进制',0b111100011)
#要让python理解八进制数据时，要在前面加上0o
#八进制数据由01234567组成
print('八进制',0o12546)
#要让python理解十六进制数据时，要在前面加上0x
#十六进制数据由0123456789ABCDEF组成
print('十六进制',0X5675424ABC)

#浮点数类型  float  3.1415926
#浮点数在进行运算的时候会导致不精确
a = 3.14159
print(a,type(a))
b1 = 1.1
b2 = 2.2
print(b1+b2)

from decimal import Decimal

print(Decimal('1.1')+Decimal('2.2'))
print(Decimal(b1)+Decimal(b2))
print(type(Decimal(1.1)))



#布尔类型    bool   true  false
#布尔值可以在转化为整数   true=1  false=0

f1 = True
f2 = False
print(type(f1))
print(type(f2))
print(f1+f2)   # True=1 false=0  0+1=1
print(f1+1)     # True=1  1+1=2
print(f2+1)     # False=0 0+1=1


#字符串类型  str   需要加上单引号或双引号或三引号  '人生苦短'   ”我用python“
#单引号，双引号定义的字符串必须在一行，三引号定义的字符串可以在多行显示

str1='人生苦短，我用python'
str2="人生苦短，我用python"
str3='''人生苦短，
我用python'''
str4="""人生苦短，
我用python"""
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))

