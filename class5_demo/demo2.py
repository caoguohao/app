'''
# 列表的查询操作
# 如果查询的元素不在列表中，则会抛出ValueError
获取列表中的单个元素
正向索引    从 0 --->  N-1    例如： lst[0]
逆向索引    从 -N --->  -1    例如： lst[-N]
指定索引不存在，抛出 indexError
'''
lst=['hello','word',98,'hello','word',89]
# 获取索引为2的元素
print(lst[2])
# 获取索引为-3的元素
print(lst[-3])
# 获取索引为10的元素
# print(lst[10])   IndexError: list index out of range



