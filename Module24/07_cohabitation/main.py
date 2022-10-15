import random

class House:
    food = 50
    money = 0

    def __init__(self, food, money):
        self.food = food
        self.money = money

    def info(self):
        print('FOOD: {}\nMONEY: {}'.format(self.food, self.money))

class People:
    name = 'ADMIN'
    satiety = 50
    house = 'No'

    def __init__(self, name, satiety, house):
        self.name = name
        self.satiety = satiety
        self.house = house

    def feed(self):
        self.satiety += 5
        self.house.food -= 5

    def work(self):
        self.satiety -= 10
        self.house.money += 20

    def play_games(self):
        self.satiety -= 5

    def go_store(self):
        self.house.food += 50
        self.house.money -= 50

    def info(self):
        print('NAME: {}\nSATIETY: {}'.format(self.name, self.satiety))



house_1 = House(50, 0)
people_1 = People('Sergey', 50, house_1)
people_2 = People('Kate', 50, house_1)

days = 0
while people_1.satiety > 0 or people_1.satiety > 0:
    print()
    people_1.info()
    people_1.house.info()
    print()
    people_2.info()
    people_2.house.info()
    if days == 365:
        print('Поздравляем, ты выжил')
        break
    number = random.randint(1, 6)
    for people in [people_1, people_2]:
        if people.satiety < 20:
            people.feed()
        elif people.house.food < 10:
            people.go_store()
        elif people.house.money < 50:
            people.work()
        elif number == 1:
            people.work()
        elif number == 2:
            people.feed()
        else:
            people.play_games()
    days += 1


