
j = []
j = input("주민등록번호를 입력하세요: ")
jm = int(j.split('-')[-1][0])
print(jm)
if jm == 1 == 3:
    print("성별: 남자")
else:
    print("성별: 여자")

if 0 <= int(j.split('-')[1][1:3]) <= 8: print("서울사람입니다.")
elif 9 <= int(j.split('-')[1][1:3]) <= 12: print("부산 사람입니다.")
elif 16 <= int(j.split('-')[1][1:3]) <= 25: print("경기도 사람입니다.")
elif 56 <= int(j.split('-')[1][1:3]) <= 64: print("전라남도 사람입니다.")
else: print("범위를 벗어남")

first = int(j[0])*2 + int(j[1])*3 + int(j[2])*4 + \
        int(j[3])*5 + int(j[4])*6 + int(j[5])*7 + \
        int(j[7])*8 + int(j[8])*9 + int(j[9])*2 + \
        int(j[10])*3+ int(j[11])*4+ int(j[12])*5
second = first % 11
last = 11 - second
if last == int(j[13]):
    print("유효한 주민번호 입니다.")
else:
    print("유효하지 않은 주민번호 입니다.")
