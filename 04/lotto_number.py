import random

def lotto_number(max_choice):
    results = []
    for i in range(max_choice):
        random.shuffle(lotto_number_list)
        results.append(lotto_number_list.pop())
    print(results)

lotto_number_list = [i for i in range(1,46)]
lotto_number(6)





