'''
    列表元素的排序操作
        一、调用 sort() 方法，列表中所有元素默认按照从小到大的顺序进行排序
            可以指定 recerse=True 进行降序排序（由大到小），不会产生新列表，原列表不发生改变
        二、调用内置函数 new_list=sorted(order_list)，可以指定 recerse=True,进行降序排序，会产生一个新的列表，原列表不发生改变
'''

lst=[3,5,1,2,7,6,9,5,3,46,7,98]
print('原列表的id',id(lst))
lst.sort()
print('排序后列表的id',id(lst))
print(lst)
lst.sort(reverse=True)
print(lst)
lst.sort(reverse=False)
print(lst)

print('------------new_list=sorted(order_list)，原列表不发生改变----------')

lst2=[3,5,1,2,7,6,9,5,3,46,7,98]
new_lst=sorted(lst2)
print('原列表lst2',lst2,id(lst2))
print('升序新列表new_lst',new_lst,id(new_lst))
# recerse=True 进行降序排序
new_lst2=sorted(lst2,reverse=True)
print('降序新列表new_lst',new_lst2,id(new_lst2))