coffee = 50           # 자판기의 커피 개수
coffee_price = 300
while True:
    if not coffee:      # 커피가 없으면
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
    money = int(input("돈을 넣어 주세요: "))
    if money >= 300:
        if money % 300 == 0:
            print("커피를 줍니다.")
        coffee -= 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee -= 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")

    print("남은 커피의 양은 %d개 입니다." % coffee)