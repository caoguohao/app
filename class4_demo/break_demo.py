
#练习题：录入密码，最多3次，如果正确就结束循环
#break 用于结束当前循环，通常与分支结构if一起使用
for i in range(3):
    pwd=int(input("请输入密码："))
    if pwd == 8888:
        print("密码正确")
        break
    else:
        print("密码错误，请重新输入")
a=0
while a<3:
    pwd=int(input("请输入密码："))
    if pwd==8888:
        print("密码正确")
        break
    else:
        print("密码错误，请重新输入")
    a+=1
