
# 变量可以存储一个元素
# 而列表时一个‘大容器’，可以存储N多个元素
# 程序可以方便的对这些数据进行整体操作
# 列表相当于其他语言中的数组
a=['hello','word',2,3,1.1,2.34]
print(id(a))
print(type(a))
print(a)

# 创建列表的两种方式
lst1=['hello','word',98]    #第一中方式-->使用方括号
lst2=list(['hello','word',98])    #第二种方式，使用内置函数list()
print(type(lst1))
print(type(lst2))
print(id(lst1))
print(id(lst2))
print(lst1)
print(lst2)

'''
列表的特点：
1.列表元素按顺序有序排列
2.索引映射唯一一个数据
3.列表可以存储重复数据
4.任意数据类型数据可以混存
5.根据需要动态分配和回收内存
'''