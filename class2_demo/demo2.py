#python 中的运算符
#标准运算符   加 +   减  -   乘 *   除  /   整除  //   取余运算  %   幂运算  **

print('加法运算结果：预期结果为3，实际结果为：',1+2)    #加法运算
print('减法运算结果：预期结果为2，实际结果为：',3-1)    #减法运算
print('乘法运算结果：预期结果为9，实际结果为：',3*3)    #乘法运算
print('除法运算结果：预期结果为3.0，实际结果为：',9/3.1,'计算结果的数据类型为：',type(9/3.1))    #除法运算
print('除法运算结果：预期结果为3.0，实际结果为：',1/3,'计算结果的数据类型为：',type(1/3))    #除法运算
print('整除法运算结果：预期结果为3.0，实际结果为：',12//3.111,'计算结果的数据类型为：',type(12//3.111))    #除法运算
print('整除法运算结果：预期结果为3.0，实际结果为：',1//3.111,'计算结果的数据类型为：',type(1//3.111))    #除法运算
print('除法运算结果：预期结果为3.0，实际结果为：',12/3,'计算结果的数据类型为：',type(12/3))    #除法运算
print('整除法运算结果：预期结果为3.0，实际结果为：',12//5,'计算结果的数据类型为：',type(12//5))    #除法运算
print(12/3)
print(type(12/3))

#除法取余运算符号  %
print("取余运算，13除以2得6余1，计算结果为1：",13%2)
print("表示2的3次方，2*2*2，计算结果为8：",2**3)

#一正一负的取余和整除

print(9//4)
print(-9//-4)
#一正一负的整除公式为  向下取整
print(9//-4)  #结果为-2.222 此时向下取整 所以结果为-3
print(-9//4)  #结果为-2.222 此时向下取整 所以结果为-3

#一正一负的整除要遵循公式：  余数=被除数-除数*商
print(9%-4)   #商为 9//-4的取整结果-3，故而结果为：9-（-4）*（-3）==-3
print(-9%4)   #商为 -9//4的取整结果-3，故而结果为：-9-（4）*（-3）==3
