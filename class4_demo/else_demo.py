# else语句同样可以搭配while  和  for  循环语句进行使用
# 在循环正常结束是执行else内的代码
# 在循环语句中，没有碰到break是执行else

#练习题： 输入密码问题  3次验证

'''
a=0
while a<3:
    pwd=int(input("请输入密码："))
    if pwd==8888:
        print("密码正确")
        break
    else:
        print("密码错误")
    a += 1    #改变变量要放在循环体中
else:   #循环正常结束，执行else中的代码
    print("对不起，密码连续三次输入错误")

'''
for item in range(3):
    pwd=int(input('请输入密码：'))
    if pwd==8888:
        print("密码正确")
        break
    else:
        print("密码错误")
else:    #循环正常结束，执行else中的代码
    print("对不起三次密码均输入错误")



