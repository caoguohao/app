#转移字符使用
#  换行：\n 回车(相当于光标回到行首位置)：\r  水平制表符：\t   退格: \b
#\  +转义字符首字母  n == newline 表示换行
print("hello\nword")

print('hello\nword')  #换行操作
#水平指标符 \t 从起始位置到结束位置共使用4个字符位置，取决于是否占满了4个字符位置，占满了重新开一个制表位，否则就不重新开
#  \t 是水平指示符   意为开始到结束期间增加一个4字符间距的缩进，取决于上一位置是否占满了4个字符位置，如：上一个位置占了2个字符位置，则\t占据2个字符位置
# 若上一个位置刚好占满了4个字符位置，则重新开一个4字符位置的间距
print("hello\tword")
print('helloo\tword')
print('hellooo\tword')
print('helloooo\tword')
#回车(相当于光标回到行首位置)/覆盖：\r
print('hello\rword')  #程序先输出了 hello  但是由于输入光标移动到了行首位置，则程序在该行重新输入了word，此时程序结果为 word
print('hello\rword')
#退格(向前删除一位),每一个退一格: \b
# \b 为退格（删除）操作，一个\b则为向前删除1位字符，依次类推
print('hello\b\b\bword')  #此时程序在输出hello之后，进行了3次退格删除的动作，则程序输出为：  heword
print('hello\bword')
print('hello\b\bword')
#输出反斜线\\
# 因为在python中的反斜线多用于字符转义操作，当需要输出反斜线的时候，需要在反斜线后再加一个反斜线
print('http:\baidu.com')   #当只有一个反斜线是，因为后面的字母b，导致程序认为是进行\b转义操作，则程序向前缩进了一格
print('http:\\baidu.com')  # 当有两个反斜线时， \\转义为\  故而输出了一条反斜线
print('这里是三个反斜线','http:\\\baidu.com')  # 当有三条反斜线时，最后一个反斜线和字母b组成了\b的操作，则将第二个反斜线删除了，此时为\\b,程序再次删除了一个反斜线并完成了\b 的操作，所以输出了 http:aidu.com
print('这里是四个反斜线','http:\\\\baidu.com')
#当有四条反斜线存在时，当视作两个\\的转义操作，各自转义成一条反斜线，故而输出  http:\\baidu.com
#输出单引号和双引号：  \'   \"
#再python中 英文格式的单引号和双引号用于定义字符串，不能直接输出，需要加上转义符号\
print('老师说：\'你好\'')   # 此时输出结果为 老师说：’你好‘
print('老师说：“你好”')  # 由于中文格式的单引号和双引号再python中没有操作用处，故而可以直接输出
print('老师说：’你好‘')  # 由于中文格式的单引号和双引号再python中没有操作用处，故而可以直接输出
print('老师说：\"你好\"')
#原字符，就是在字符串之前加上r或R，不希望字符串中的转义字符生效
#注意事项：最后一个字符不能是反斜线（会报错）,但这里可以是偶数个反斜线
print("hello\nword")
print('hello\\nword')
print(r'hello\nword')
print(R'hello\nword')
#print(R'hello\nword\')
print(R'hello\nword\\')
print(R'hello\nword\\\\')
print(r'hello\\word')  #\\为反斜线的转义，但是再字符串前加了r，所以不执行转义
print(r'hello\tword')  #\t为加上指示器向后缩进
print(r'hello\bword')  #\b为向前缩进一格
print(r"hello\'word\'")#\' 为单引号的转义
print(r"hello\nword")  # \n 为换行操作
print(r"hello\tword")  #\t 为加上4个空格
print(r'hello\rword')  #\r 为将输入位置重置到行首
