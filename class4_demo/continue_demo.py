
# continue语句，用于结束当前循环，进入下一次循环，常与分支结构if一起使用
# 练习题：要求输出1-50之间所有5的倍数的值
'''
for i in range(1,51):
    if i%5!=0:
        continue
    print(i)
'''

s=0
while s<51:
    s += 1
    if s%5!=0:
        continue
    print(s)
