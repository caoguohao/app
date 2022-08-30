
#嵌套循环
#练习题：输出一个三行4列的矩形

'''
for i in range(4):
    for j in range(5):
        print("*",end='\t')
        # end='\t' 用于设置不换行输出，且每个输出之间加一个缩进
        # end 用于设置print函数的结尾，可设置为空字符串 end='' 或者 end="",这是python中标准的不换行做法
        # 如果不手动设置end,则 end='\n',故而print默认是换行输出
    print()
'''

#如何打印一个4x5的中空矩形


'''
for i in range(4):
    if i==0 or i==3:
        for j in range(5):
            print('*',end="\t")
    else:
        for j in range(5):
            if j==0 or j==4:
                print('*',end='\t')
            else:
                print(end='\t')
    print()
'''
'''
# 打印一个直角三角形
for i in range(1,10):
    for j in range(i):
        print((j+1)*i, end='\t')
    print()
print(list(range(1,10)))

for i in range(1,10):
    for j in range(1,i+1):
        print(j*i, end='\t')
    print()
'''

i=1
while i<10:
    j=1
    while j<i+1:
        print(i*j,end='\t')
        j+=1
    print()
    i+=1