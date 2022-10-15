def one_family(word, dict):
    for people in dict:
        if people[0] == word or people[0] == word + 'а' or people[0] == word[:-1]:
            print(people[0], people[1], dict[people])


families = {
    ('Сидоров', 'Антон') : 35,
    ('Сидорова', 'Татьяна') : 27,
    ('Сидоров', 'Фёдор') : 47,
    ('Петрова', 'Татьяна') : 20,
    ('Петров', 'Кирил') : 22,
    ('Коршунов', 'Сергей') : 7,
    ('Коршунов', 'Виктор') : 17,
    ('Коршунова', 'Екатерина') : 28
    }

fam = input('Введите фамилию: ')
one_family(fam, families)

