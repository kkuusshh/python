left_coffee = 5     # 남은 커피 수
left_money = 2000   # 남은 돈
coffee_price = 300  # 커피 한개의 가격
needs = 0           # 사용자가 커피를 살 때 필요한 돈

while True:
    input_money = int(input("돈을 넣으세요. : "))
    input_coffee_num = int(input("커피 개수를 입력하세요.: "))

    needs = coffee_price * input_coffee_num
    # 1) 커피 살 돈을 충분히 넣은 경우
    if input_money >= needs:
        # 거스름 돈 = 입력한 돈 - 필요한 돈
        output_left_money = input_money - needs
        # 줄 커피 개수 = 고객이 입력한 거피 개수
        output_coffee = input_coffee_num

        # 커피 자판기에 남은 커피 개수 = 남은 커피 개수 - 고객이 요청한 커피 개수
        left_coffee = left_coffee - input_coffee_num
        # 커피 자판기에 남은 돈 = 남은 돈 - 커피 살 돈
        left_money = left_money - output_left_money

    # 2) 커피 살 돈을 부족하게 넣은 경우
    elif input_money < needs:
        lack_of_money = needs - input_money
        print("커피 살 돈이 부족합니다. %d 만큼 더 넣어 주세요.\n" % lack_of_money)
        continue

    # 커피 자판기의 남은 돈이나 남은 커피의 양이 부족한 경우 몽땅 돌려주기
    if left_money < 0 or left_coffee < 0:
        print("+---------------------------------------------------")
        print("| 커피 자판기에는 남은 돈이 없거나 남은 커피가 없습니다.")
        print("| 관리자에게 문의 하세요.")
        print("+----------------------------------------------------")
        print("넣은 돈을 몽땅 돌려 드릴께요. : %d" % input_money)
        break

    # 사용자에게 주어야 하는 부분
    print("커피를 %d개 줍니다. 그리고 거스름 돈은 %d입니다." % (output_coffee, output_left_money))

    # 자판기의 상태를 나타내는 부분
    print("+--------------------------------")
    print("| 남은 커피 수량: %d" % left_coffee)
    print("| 남은 돈: %d" % left_money)
    print("+---------------------------------\n")