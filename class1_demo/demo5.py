#变量的使用

#变量在多次复制之后，变量名会指向新的空间

name="玛丽亚"
print(name)
name="楚留香"
print(name)
name2="玛丽亚"
name3="楚留香"
name3="张孝全"
print('name的id:',id(name))
print("name2的id:",id(name2))
print("name3的id:",id(name3))
print("name4的id:",id(name3))  #