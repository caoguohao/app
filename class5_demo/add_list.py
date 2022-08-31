'''
    列表生成式
        列表生成式简称--生成列表的公式
        语法结构
            [       i*i        for    i      in range(1,10)]
             产生列表元素的表达式     自定义变量        可迭代对象
        注意事项
            表示列表元素的表达式中通常包含自定义变量
'''

lst=[i for i in range(1,10)]
lst2=[i*i for i in range(1,10)]
print(lst)
print(lst2)