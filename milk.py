milk_orders = {'101': {'milk': 1, 'yogurt': 5},
               '102': {'milk': 2},
               '103': {'milk': 1, 'yogurt': 10},
               '104': {'yogurt': 15}}

for addr in milk_orders:
    milk_order_num = milk_orders[addr].get('milk')
    if milk_order_num is not None:
        print('%s 호 우유: %s개' %(addr, milk_orders[addr].get('milk')))