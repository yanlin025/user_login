# 查询
def find(code1):
    count = 0
    index = code1.index("where")  # 获取where的索引值
    require = code1[index + 1:]  # 截取条件
    # print("require:", require)
    if require[0] in index_columns:
        global index_column
        index_column = index_columns.index(require[0])  # 获取字段索引
    for k in info_dic:
        if require[1] == ">":
            if info_dic[k][int(index_column)] > require[2]:
                if code1[1] == "*":  # 输入*号，则打印整条记录
                    print(info_dic[k])
                else:
                    items = code1[1].strip().split(",")  # 否则，字符串转为列表
                    info = []  # 存储符合条件的值
                    for v in items:
                        if v in index_columns:  # 列表元素在字段列表中
                            index_items = index_columns.index(v)  # 获取相应的索引值
                            info.append(info_dic[k][index_items])
                    print(info)
                count += 1
        elif require[1] == "<":
            if info_dic[k][int(index_column)] < require[2]:
                if code1[1] == "*":  # 输入*号，则打印整条记录
                    print(info_dic[k])
                else:
                    items = code1[1].strip().split(",")  # 否则，字符串转为列表
                    info = []  # 存储符合条件的值
                    for v in items:
                        if v in index_columns:  # 列表元素在字段列表中
                            index_items = index_columns.index(v)  # 获取相应的索引值
                            info.append(info_dic[k][index_items])
                    print(info)
                count += 1
        elif require[1] == "=":
            if info_dic[k][int(index_column)] == require[2]:
                if code1[1] == "*":  # 输入*号，则打印整条记录
                    print(info_dic[k])
                else:
                    items = code1[1].strip().split(",")  # 否则，字符串转为列表
                    info = []  # 存储符合条件的值
                    for v in items:
                        if v in index_columns:  # 列表元素在字段列表中
                            index_items = index_columns.index(v)  # 获取相应的索引值
                            info.append(info_dic[k][index_items])
                    print(info)
                count += 1
        elif require[1] == "like":
            if require[2] in info_dic[k][int(index_column)]:
                if code1[1] == "*":  # 输入*号，则打印整条记录
                    print(info_dic[k])
                else:
                    items = code1[1].strip().split(",")  # 否则，字符串转为列表
                    info = []  # 存储符合条件的值
                    for v in items:
                        if v in index_columns:  # 列表元素在字段列表中
                            index_items = index_columns.index(v)  # 获取相应的索引值
                            info.append(info_dic[k][index_items])
                    print(info)
                count += 1
    print("to find {} items".format(count))  # 统计查询记录


# 新建
def add(code2):
    a = True
    add_con = code[2:]
    add_con = " ".join(add_con)
    add_con = add_con.strip().split(",")
    # print("add_con:", add_con)
    max_id = len(info_dic)  # 获取字典长度作为新增值得id
    for k in info_dic:
        if add_con[2] in info_dic[k]:  # 以phone唯一键
            a = False
            print("The employee has already existed，fail to change")
    if a:
        info_dic[str(max_id)] = [max_id, add_con[0], add_con[1], add_con[2], add_con[3], add_con[4]]  # 字典新增key-value
        print("add successfully!")
    else:
        pass


# 删除
def del_info(code3):
    del_id = code3[-1]  # 截取id
    del info_dic[del_id]  # 删除记录
    len_info = len(info_dic)  # 删除后字典长度
    for k in range(int(del_id), len_info):
        info_dic[str(k)] = info_dic[str(k + 1)]  # 修改删除后的字典key值
        info_dic[str(k)][0] = str(k)
        del info_dic[str(k + 1)]  # 删除多余的记录
    print("delete successfully!")


# 更改
def change(code4):
    count = 0
    index1 = code4.index("WHERE")  # 获取where的索引值
    old = code4[index1 + 1:]  # 旧内容
    # print("old:", old)
    index2 = code4.index("SET")  # 获取set的索引值
    new = code4[index2 + 1:index1]  # 新内容
    # print("new:", new)
    if old[0] in index_columns:
        global index_column
        index_column = index_columns.index(old[0])  # 获取字段索引
    if new[0] in index_columns:
        global index_set
        index_set = index_columns.index(new[0])
    for k in info_dic:
        if " ".join(old[2:]) in info_dic[k]:
            info_dic[k][index_set] = " ".join(new[2:])  # 更改
            count += 1
    print("changed\033[33;1m %s\033[0m items." % count)
    # print(info_dic)


# 写入文件
def write():
    f1 = open("user_3", "w", encoding="utf-8")
    for k in info_dic:
        record = ",".join(info_dic[str(k)][1:])  # 连接字符串
        record = k + "," + record
        f1.write(record)
        f1.write("\n")
    f1.close()


# 读取文件信息存入字典
f = open("user_3", 'r', encoding="utf-8")
data = f.readlines()
info_dic = {}
for line in data:
    line = line.strip().split(",")  # 去掉首尾空格，记录转为列表
    info_dic[line[0]] = line  # 写入字典
print(info_dic)
f.close()

# 主程序
index_columns = ['id', 'name', 'age', 'phone', 'dept', 'enroll_date']
code = input("input request:")  # 输入命令,以空格间隔字符
# print(code, type(code))
code = code.strip().split()  # 字符串转为列表
# print(code, type(code))
if code[0] == "find":  # 查询
    find(code)
elif code[0] == "add":  # 新建
    add(code)
    write()
elif code[0] == "del":  # 删除
    del_info(code)
    write()
elif code[0] == "UPDATE":  # 更新
    change(code)
    write()

