

#open方法需要指定正确的文件夹，a+为对文件的操作方法，如果文件不存在就创建文件，如果存在就在文件末尾处新增内容
#写入内容的时候，需要通过file=fq为执行操作指定对应的文件名
fq=open('D:/test/text.txt','a+')
print("hello word",file=fq)
fq.close()

fp=open('D:/test/text2.txt','a+')
print('hello word',file=fp)
fp.close()
#在操作文件时，需要记住有始有终，打开一个文件后，操作完成之后要记住关闭该文件

