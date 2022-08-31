'''
    列表元素的修改
        为指定索引的元素赋予一个新值
        为指定的切片赋予一个新值
'''

lst=[10,20,30,40]
# 一次修改一个值
lst[2]=100
print(lst)
# 使用切片方式修改列表
lst[1:3:1]=[100,200,300,400]    # lst[1:3]=[]  当右侧列表为空时，这就是一个切片删除的操作
print(lst)
# 此时是将 [100，200，300，400] 替换到 切片lst[1:3]的位置上
# [10, 100, 200, 300, 400, 40]