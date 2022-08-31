'''
获取列表中的多个元素  （列表的切片操作）
语法格式：   列表名【start:stop:step】   起始位置：结束位置：步长
切片的结果-->原列表片段的拷贝
切片的范围--> [start:stop]
start为正数时，切片起始位置从左往右数
start为负数时，切片起始位置从右往左数
step（步长）默认为1-->简写方法为【start:stop】
                 / -->[:stop:step] -->（不写start）切片的第一个元素默认是列表的第一个元素   \
step（步长）为正数/                                                                   \-->从start开始往后计算切片
               \   __>[start::step] -->（不写stop）切片的最后一个元素默认是列表的最后一个元素/
                / -->[:stop:step] -->（不写start）切片的第一个元素默认是列表的最后一个元素   \
step（步长）为负数/                                                                   \-->从start开始往前计算切片
               \   __>[start::step] -->（不写stop）切片的最后一个元素默认是列表的第一个元素/
'''

lst=[1,2,3,4,5,6,7,8]
print('-----------------步长 step 为正数--------------')
#start=1,stop=6,step=1
print(lst[1:6:1])
#start=1,stop=6,step默认
print(lst[1:6])     #不写step 默认步长为1
print(lst[1:6:])    #step为空 默认步长为1
print('原列表id：',id(lst))
lst2=lst[1:6:1]
print('切出的片段的id：',id(lst2))
#start=1,stop=6,step=2
print(lst[1:6:2])
#start=默认，stop=6,step=2
print(lst[:6:2])    #因为 start 不写/为空时，切片的第一个元素默认为列表的第一个元素
print(lst[0:6:2])
#start=1,stop=默认，step=2
print(lst[1::2])    #因为 stop 不写/为空时，切片的最后一个元素默认为列表的最后一个元素
print(lst[1:8:2])
print('-----------------步长 step 为负数--------------')
print("原列表：",lst)
#start=0,stop=n,step=-1
print(lst[::-1])
#start=7,stop=n,step=-1
print(lst[7::-1])
#start=n,stop=0,step=-1
print(lst[:-2:-1])
print(lst[-5:-1])
print(lst[-5:-6])
print(lst[:])