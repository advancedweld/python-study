a = 0; b = 1
count = 0
while count < 10:
    sum = a + b
    # print('fibbor:',sum, "count", count)
    a, b = b, a+b
    count += 1


def append_hello(list):
    list.append('hello')
    return list

lt = ['xiang', 'shang', 'zhi']
lt1 = append_hello(lt)
print('lt=====',lt)
print('lt1=====',lt1)
print(lt1 == lt)



def modify_value(x):
    x = x + 10
    print("函数内:", x)

num = 5
modify_value(num)
print("函数外:", num)  # 输出: 函数外: 5