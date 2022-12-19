class Fridge:
    isOpend = False
    foods = []

    def open(self):
        self.isOpend = True
        print('냉장고 문이 열렸습니다.')

    def put(self, thing):
        if self.isOpend  == True:
            self.foods.append(thing)
            print('[ok] %s 음식을 넣었습니다.' % thing)
        else:
            print('[ fail ] 냉장고 문이 닫혀있습니다.')

    def close(self):
        self.isOpend = False
        print('[ info ] 냉장고 문을 닫았습니다.')


class Foods:
    pass
