class Cat:  
  width = 26
  age = 3
  hungry = 25
  fatigue = 50

  def __init__(self):
    print("heigt = 60")

  def get_older(self):
    self.age += 0.5

  def eat_Food(self):
    self.hungry += 75

  def go_sleep(self):
    self.fatigue += 50


my_cat = Cat()
print(my_cat.age)

my_cat.get_older()
print(my_cat.age)

my_cat.eat_Food()
print("yummy!", my_cat.hungry )

my_cat.go_sleep()
print("ZzZzZ", my_cat.fatigue)