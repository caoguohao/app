# 多层嵌套循环中 break 和 continue 的用法
# 多重循环中的 break 和 continue 用于控制本层循环
# 练习题：循环输出1-10中的奇数或偶数

'''
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            break   # 当循环第一次时，j=1，此时输出j=1,
                    # 当循环第二次时，j=2,此时满足j%2==0,执行了break，此时内层循环结束，开始进行第二次外层循环
                    # 每次每层循环走到第二次时，都会立即结束当前的内循环，所以程序的输出结果为 1，1，1，1，1
        else:
            print(j)

for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        else:
            print(j,end='\t')
    print()
'''

a=1
while a<6:
    b = 1
    while b<11:
        b += 1
        if b % 2 == 0:
            continue
        else:
            print(b, end='\t')
    print()
    a += 1