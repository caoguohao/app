

# 习题：要求计算 1-100之间的偶数之和

a = 1
b = 0

while a <= 100:
    if not bool(a%2):
    # if not a%2:
    # if a%2 == 0:
        b +=a
    else:
        pass
    a+=1

print(b)
