# 升级需求：可以支持多个用户登录 (提示，通过列表存多个账户信息),用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）

list_info = [
    ["lucy", "123"],
    ["lily", "321"],
    ["张三", "456"],
    ["李斯", "456"],
]

count = 0
lock_file = open('lock_file', 'r')  # 读取文件
name = lock_file.read()
lock_file.close()
while count < 3:
    username = input("name:")
    password = input("password:")
    if username in name:  # 判断输入的用户名是否在黑名单中
        print("The user is remain locking!")
        break
    else:
        for i in range(0, len(list_info)):
            if list_info[i] == [username, password]:  # 判断输入的信息是否与list中的匹配
                print("Welcome ", username)
                count = 3
                break
        else:
            print("wrong username or password")
            count += 1
            record = open('lock_file', 'a')  # 写入黑名单
            record.write('%s\n' % username)
            record.close()

