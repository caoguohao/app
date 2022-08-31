
# 判断对象在列表中是否存在
lstx=[10,20,'hello','word']
print(10 in lstx)
print(30 not in lstx)
print('---------------遍历列表中的元素-----------')
for item in lstx:
    print(item)

'''
列表元素的增加操作：
append()  lst.append('str') 在列表的末尾添加一个元素
                            无法用于列表的合并
extend() lst1.extend(lst2)  在列表的末尾至少添加一个元素（末尾添加多个，在往列表中插入列表时，可将被插入的列表中的元素拆分并插入到原列表中）
                            多用于列表的合并
insert() lst.insert(2)  在列表的任意位置添加一个元素（中间插入）
  切片 lst1[start:stop]=lst2      在列表的任意位置添加最少一个元素(覆盖添加)
'''
# 在列表的末尾添加一个元素
lst=[10,20,30]
print('添加元素之前：',lst,id(lst))
lst.append(100)
print('添加元素之后',lst,id(lst))

lst2=['hello','word']
lst.append(lst2)   #将lst2作为一个元素，添加到lst的末尾
#  [10, 20, 30, 100, ['hello', 'word']]
print(lst)
lst.extend(lst2)   #像列表的末尾一次性添加多个元素
#  [10, 20, 30, 100, ['hello', 'word'], 'hello', 'word']
print(lst)
lst.insert(1,90)   #在任意位置上插入一个元素，此时指定在索引位置1处插入元素90，原来位于索引1的元素索引变成了2
#  [10, 90, 20, 30, 100, ['hello', 'word'], 'hello', 'word']
print(lst)
lst3=[True,False,'hello','word']
print('原列表lst的id',id(lst))
lst[1:]=lst3        #切片添加，在任意位置上添加多个元素，这是一种覆盖添加
# 将lst3的列表内容覆盖到切片掉的位置，列表的id值不变
#   [10, True, False, 'hello', 'word']
print('切片添加后新列表的id',id(lst))
print(lst)
lst4=[]
lst[:1]=lst4
print(lst)
lst.extend(lst4)
print(lst)