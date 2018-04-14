# username = "seven"
# password = "123"
# _username = input("name:")
# _password = input("password:")
# if _username == username and _password == password:
#     print("welcome")
# else:
#     print("wrong username or password")

# username1 = "seven"
# username2 = "Alex"
# password = "123"
# count = 0
# while count < 3:
#     _username = input("name:")
#     _password = input("password:")
#     if _username == username1 or _username == username2 and _password == password:
#         print("welcome")
#         break
#     else:
#         print("wrong username or password")
#     count += 1

# count = 2
# count1 = 0
# while count <= 100:
#     if count % 2 == 0:
#         count1 += count
#     else:
#         count1 -= count
#     count += 1
# print("the result of 2-3+4-5...+100 is:",count1)

# count = 1
# while count <= 12:
#     if count == 6 or count == 10:
#         pass
#     else:
#         print(count)
#     count += 1

count = 100
while count > 50:
    print(count)
    count -= 1
    if count == 50:
        print(count)
        count = 1
        while count <= 50:
            print(count)
            count += 1
        break


# count = 1
# print("1-100之间的偶数：")
# while count <= 100:
#     if count % 2 == 0:
#         print(count)
#     count += 1

count = 1
print("1-100之间的奇数：")
while count <= 100:
    if count % 2 != 0:
        print(count)
    count += 1
