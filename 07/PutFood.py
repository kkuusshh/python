import Fridge

lg = Fridge.Fridge()
apple = Fridge.Foods()
elephant = Fridge.Foods()

lg.open()
lg.put(apple)
lg.put(elephant)
print(lg.foods)
lg.close()
lg.put(apple)
lg.open()
lg.put(elephant)

