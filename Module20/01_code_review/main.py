
students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)
def data(dict):
    interests = []
    count = 0
    for key, val in dict.items():
        interests += (val['interests'])
        count += len(val['surname'])
    return count, interests

pairs = [(ind, val['age']) for ind, val in students.items()]

print('Список пар "ID студента - Возраст":', pairs)
print('Полный список интересов всех студентов:', data(students)[1])
print('Общая длина всех фамилий студентов:', data(students)[0])