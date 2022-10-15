import random

class Warrior:
    name = 'unit'
    soundness = 100
    hit = 20

    def __init__(self, name):
        self.name = name

    def min_soundness(self):
        self.soundness -= self.hit

    def info(self):
        print('Оставшиеся количество здоровья {}: {}\n'.format(self.name, self.soundness))


war_1 = Warrior('Unit_1')
war_2 = Warrior('Unit_2')


while True:
    users = [war_1, war_2]
    what_enemy = random.choice(users)
    users.remove(what_enemy)
    print('Атакует {} по {}'.format(users[0].name, what_enemy.name))
    what_enemy.min_soundness()
    if what_enemy.soundness <= 0:
        print('Победил {}'.format(what_enemy.name))
        break
    what_enemy.info()
