class Elevator:
    source_floor = 1
    dest_floor = 0
    direction = "UP"
    saram_nums = 0

    def check_floor(self, source):
        previous_floor = self.dest_floor
        next_floor = source
        middle_direction = previous_floor - next_floor
        if middle_direction > 0:
            print("** DOWN **")
        elif middle_direction == 0:
            print("** PAUSE **")
        else:
            print("** UP **")

    def gotofloor(self, s, d, direct, num):
        self.check_floor(s)
        self.source_floor = s
        self.dest_floor = d
        self.direction = direct
        self.saram_nums = num

    def info(self):
        print("=======================================")
        print("%d 층 => %d 층 : %s : (%d 명)" % (self.source_floor, self.dest_floor, self.direction, self.saram_nums))
        print("=======================================")



def main():
    actions = [[1, 5, 'UP', 2], [3, 4, 'UP', 3], [5, 1, 'DOWN', 1], [2, 3, 'UP', 3]]

    e = Elevator()
    for action in actions:
        # print(action)
        e.gotofloor(action[0], action[1], action[2], action[3])
        e.info()


if __name__ == '__main__':
    main()