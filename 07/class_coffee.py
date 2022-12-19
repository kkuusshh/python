import sys


class CoffeeMachine:
    total_amount = 10           # 총 커피 개수
    total_amount_price = 5000   # 총 보유 금액
    coffee_price = 300          # 커피 한개의 가격
    put_price = 0               # 사용자가 넣은 돈
    req_coffee_nums = 0         # 사용자가 원하는 커피 개수
    remaining_price = 0         # 사용자에게 줄 거스름돈

    def request(self):
        # input: None
        # output: None
        # function:
        # * 사용자의 커피 개수, 사용자의 돈 입력
        # self.put_price = int(input('[ INFO ] 돈을 입력하세요: '))
        # self.req_coffee_nums = int(input('[ INFO ] 원하는 커피 개수를 입력하세요: '))
        self.put_price = 800
        self.req_coffee_nums = 3
        # print(self.put_price, self.req_coffee_nums)

    def check_amount(self):
        # input: None
        # output: True|False
        # function:
        # * 자판기의 커피 개수가 부족하거나 또는 보유 금액이 부족한 경우를 점검합니다.
        if self.total_amount <= 0 or self.total_amount_price <= 0:
            return False
        else:
            return True

    def info(self):
        # input: None
        # output: None
        # function:
        # * 커피 자판기의 총 커피 개수와 총 보유금액을 출력한다.
        print("+--------------------------------------------")
        print("| 총 금액:", self.total_amount_price)
        print("| 총 개수:", self.total_amount)
        print("+--------------------------------------------")

    def get(self):
        # input: None
        # output: None
        # function:
        # * 1) 돈을 충분히 넣은 경우(커피개수: 2, 돈: 700)
        # * 2) 돈을 조금 부족하게 넣은 경우(커피개수: 2, 돈: 500)
        # * 3) 돈을 부족하게 넣은 경우(커피개수: 2, 돈: 200)
        price = self.req_coffee_nums * self.coffee_price
        # * 1) 돈을 충분히 넣은 경우(커피개수: 2, 돈: 700)
        if self.put_price >= price:
            print('[  OK  ] 커피 %d 개를 드립니다.' % self.req_coffee_nums)
            self.total_amount -= self.req_coffee_nums

            self.remaining_price = self.put_price - price
            print('[  OK  ] 거스름돈 %d 만큼 드립니다.' % self.remaining_price)
            self.total_amount_price -= self.remaining_price
        # * 2) 돈을 조금 부족하게 넣은 경우(커피개수: 3, 돈: 800,       커피: 2, 거스름돈: 200)
        elif price > self.put_price >= self.coffee_price:
            num = self.put_price // self.coffee_price
            print('[  OK  ] 커피 %d 개를 드립니다.' % num)
            self.total_amount -= num

            self.remaining_price = self.put_price - (self.coffee_price * num)
            print('[  OK  ] 거스름돈 %d 만큼 드립니다.' % self.remaining_price)
            self.total_amount_price -= self.remaining_price
        # * 3) 돈을 부족하게 넣은 경우(커피개수: 2, 돈: 200)
        else:
            print('[ FAIL ] 돈을 충분하게 넣지 않으셨습니다. 커피 한개도 못 드리겠네요.')
            print('[ INFO ] 넣은 돈 %d를 돌려 드립니다.' % self.put_price)


def main():
    c = CoffeeMachine()

    while True:
        # 1) 입력(커피개수, 돈입력)
        c.info()
        c.request()
        # 2) 커피자판기가 계산
        if c.check_amount():
            c.get()
        else:
            print('커피 자판기에 커피개수가 부족하거나 또는 보유 금액이 부족합니다.')
            sys.exit(1)
        # 3) 출력(커피개수, 거스름돈)
        c.info()
        input('Press any key ....')


if __name__ == '__main__':
    main()