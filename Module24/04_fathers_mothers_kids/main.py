class Child():
    name = 'ADMIN'
    age = 4
    condition = False
    state_of_hunger = False

    def __init__(self, name, age, condition, state_of_hunger):
        self.name = name
        self.age = age
        self.condition = condition
        self.state_of_hunger = state_of_hunger

    def info(self):
        print('Name: {}\nAge: {}\nCondition: {}\nState of hunger: {}'.format(
            self.name, self.age, self.condition, self.state_of_hunger
        ))

class Parent():
    name = 'ADMIN'
    age = 20
    children = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def children_add(self, child):
        if isinstance(child, Child):
            if (self.age - Child.age) < 16:
                print("Error. The age of the child does not match the age of the parent'")
            else:
                self.children.append(child)

    def info(self):
        print('Name: {}\nAge: {}\nChildren: {}'.format(
            self.name, self.age, self.children
        ))

    def soothe(self, child):
        if isinstance(child, Child):
            child.condition = True

    def feed(self, child):
        if isinstance(child, Child):
            child.state_of_hunger = True

child_1 = Child('Petr Ivanov', 5, False, False)
parent_1 = Parent('Sveta Ivanova', 30)

parent_1.children_add(child_1) # Добавить ребенка
parent_1.info()
parent_1.soothe(child_1) # успокоить
parent_1.feed(child_1) # покормить
child_1.info()

