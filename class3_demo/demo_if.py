#单分支结构
money=1000   # 这是你的余额
s=float(input('请输入你的取款金额：'))
if money>=s:
    money-=s
    print('成功取款：',s,"您的余额为：",money)
#else:
#    print('您的余额不足！')