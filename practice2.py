
# name = input("name:")
# address = input("address:")
# hobby = input("hobby:")
# info = """
# "敬爱可爱的%s，最喜欢在%s地方%s"
# """ % (name, address, hobby)
# print(info)

# year = int(input("year:"))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(year,"年是闰年")
# else:
#     print(year,"年不是闰年")

# 一年期定期利率为3.25%，计算需要过多少年，1万元的一年定期存款连本带利能翻番

money = 10000
rate = 0.0325
years = 0
while money <= 20000:
 years += 1
 money = money*(1+rate)
print(str(years))
