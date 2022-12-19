import Person

class Student(Person.Person):
    def study(self):
        print('열공...')

lee = Student()
print(lee.mouth)
lee.eat()
lee.study()

kim = Student()
print(lee.mouth)
kim.eat()
kim.study()