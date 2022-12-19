
result = []

num1 = input("input num1 :")
result.append(int(num1))
num2 = input("input num2 :")
result.append(int(num2))

maxnum = max(result)
print(maxnum)

if maxnum % 2 == 0:
    print("짝수")
else:
    print("홀수")


