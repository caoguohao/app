"""
列表元素的删除操作
                一次删除一个元素
remove()        重复元素只删除第一个
                元素不存在则抛出异常 ValueError

                删除一个指定索引位置上的元素
pop()           不指定索引，则删除列表中的最后一个元素
                指定索引不存在则抛出异常 Value Error
切片  lst[1:3]=[]                   此时在原列表中删除切片位置的元素，没有新列表的产生
clear()           清空列表中的所有元素
del               删除列表
"""
print('----------------lst.remove(\'str\')  删除列表元素------------')
lst=[10,20,30,40,50,60,30]
lst.remove(30)      #从列表中移除一个元素，如果有多个匹配，则移除第一个
print(lst)          # [10, 20, 40, 50, 60, 30]
#  lst.remove(100)  元素 100 在列表中不存在，此时会抛出异常ValueError
print('----------------lst.pop(2)  指定索引删除列表元素------------')
lst2=[10,20,30,40,50,60,30]
lst2.pop(2)         #从列表中删除索引2的元素
print(lst2)         # [10, 20, 40, 50, 60, 30]
lst2.pop()          #不指定要删除元素的索引，所以此时删除列表中的最后一个元素
print(lst2)         # [10, 20, 40, 50, 60]
#  lst.pop(20)         列表索引不存在，所以抛出异常Value Error

print('----------------lst[1:3]=[]  此时在原列表中删除切片位置的元素，没有新列表的产生------------')
print('原列表的id',lst,id(lst))
lst[1:3]=[]
print(lst[1])
print('新列表的id',lst,id(lst))
print('----------------lst.clear()  清楚列表中的所有元素-----------')
print('原列表的id',lst,id(lst))
lst.clear()
print('新列表的id',lst,id(lst))
print('----------------del lst  将列表对象删除-----------')
del lst
# print(lst)    NameError: name 'lst' is not defined. Did you mean: 'lst2'?  此时列表对象被删除了
