#python 中的布尔运算符

#  and     or     not      in      not in

a,b=1,2
# and 运算符   同真则真，有假则假
print('---------------------and 并且--------------------')
print(a==1 and b==2)  # true    true and true  --> true
print(a==1 and b<2)   # false   true and false --> false
print(a!=1 and b==2)  # false   false and true --> false
print(a!=1 and b!=2)  # true    false and false --> false

print('----------------------or 或者-------------------------')
print(a==1 or b==2)   # true true or true -->true
print(a==1 or b<2)    # true  true or false -->true
print(a!=1 or b==2)   # true   false or true -->true
print(a!=1 or b!=2)   # false   false or false -->fasle

print('-----------------------not 对bool类型数据进行取反-----------------------------')
f1=True
f2=False
print(not f1)    #false
print(not f2)    #true

print('----------------in 和 not in-------------------------------------')
s='helloword'
print('w' in s)         #true   w 在 s的值中存在
print('k' in s)         #false  k 在 s的值中不存在
print('w' not in s)     #false  w 在 s的值中存在，不构成not in
print('k' not in s)     #true   k 在 s的值中不存在，构成not in

# true ==1  false ==0   大于0的数字都是true
# 在使用not 方法时，0 或 空（字符串，列表，元组，字典，集合） 都是标识的False    此时not False == True
print('aaa:',not ())
print(int(True))
print(int(False))