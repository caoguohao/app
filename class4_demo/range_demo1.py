
# range()的三种创建方式

#第一种创建方式. 只有一个参数（括号中中给了一个数字）
r=range(10)  #生成[0,1,2,3,4,5,6,7,8,9],默认从0开始，默认相差为1（称为步长为1）
print(r)   #range(0,10)    返回了一个迭代器，创建了一个0-10之间的整数序列，步长为1
print(list(r))  #用于查看 range对象中的整数序列   list表示的是列表
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#第二种创建方式，给了两个参数（小括号中给了两个数）
s=range(1,10)   #指定了起始值1，从1开始到10结束（不包括10），默认步长为1
print(list(s))   #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#第三种创建方式，给了三个参数（小括号中给了三个数，这三个数分别是起始值，结束值，相差值/步长）

f=range(1,10,2)   #指定了起始值为1，结束值为10，步长为2
print(list(f))  #[1, 3, 5, 7, 9]

#判断指定的整数是否在序列中存在,可以使用in  或者 not in

print(10 in f)  #False
print(9 in f)   #True
print(8 in f)   #False

print(10 not in f)  #True
print(9 not in f)   #False
print(8 not in f)   #True


#总结 使用range()函数的优点
# 不管range对象表示的数列有多长，所有range对象占用的内存空间都是相同的
# 即为，所有的range对象，只需要存储start(起始值)，stop(结束值)，step(步长)
# 只有当使用到range对象时，才回去计算序列中的相关元素

n=range(-10,int(True))   #从-10开始，到1结束，步长为1  aaaaa
print(list(n))
print(int(False))