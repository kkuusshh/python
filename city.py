citys = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan']

citys_num = [len(city) for city in citys]
print(citys_num)
citys_long_num=max(citys_num)
citys_short_num=min(citys_num)
print(citys_long_num,citys_short_num)

citys_long = []
citys_short = []
for city in citys:
    if len(city) == citys_long_num:
        citys_long.append(city)
    if len(city) == citys_short_num:
        citys_short.append(city)

#print(citys_long,citys_short)
print("Long Name City: ", ' '.join(citys_long))
print("Short Name City: ", ' '.join(citys_short))

