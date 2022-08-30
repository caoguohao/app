# if 表达式的简写

num_a= int(input('请输入第一个整数：'))
num_b= int(input('请输入第二个整数：'))
if num_a >= num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)
# 条件判断为true则执行之前的代码，---------这里是条件判断区间--------条件判断为false则执行之后的代码
print(str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b))