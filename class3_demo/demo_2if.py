# 嵌套if的使用

#例题： 先判断顾客是否有会员卡，有会员卡则打折，消费额小于100（不打折），消费额100-200（9折），消费额200以上（8折）



ans=str(input("请问您有会员卡吗？（请输入是/否）："))
if ans=="是":
    price = float(input("请输入您的消费金额："))
    if 100<=price<200:
        price *= 0.9
        print("会员折扣价格为：",price)
    elif 200<=price:
        price *= 0.8
        print("高级会员折扣价为：",price)
    else:
        print("消费额度不足，无折扣消费金额为：",price)
else:
    price = float(input("请输入您的消费金额："))
    print('您不是会员用户，消费金额为：',price)


