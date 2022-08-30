#多分支结构，多选一进行执行
# if  elif   else
#例题：  判断学生的成绩区间 60，60-70，70-80，80-90，90-100
num=float(input('请输入学生的考试成绩：'))
if 60<= num <70:
    print('成绩为：',num,'恭喜你及格了！')
elif 70<= num <80:
    print('成绩为：',num,'您的成绩尚可，继续加油！')
elif 80<=  num <90:
    print('成绩为：', num, '您的成绩优良，继续加油！')
elif 90 <= num < 100:
    print('成绩为：', num, '您的成绩优秀，继续加油！')
elif num == 100 :
    print('成绩为：', num, '恭喜你获得了满分！')
elif num <0 or num >100:
    print("你输入的成绩数据错误！")
else:
    print("你的成绩是",num,"你的考试成绩不及格，请继续努力！")