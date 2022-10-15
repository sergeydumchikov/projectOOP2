user_name = input('Введите имя пользователя: ')
while True:
    print('1 - Посмотреть текущий текст чата.\n2 - Отправить сообщение')
    ques = input()
    if ques == '1':
        try:
            with open('chat.txt', 'r') as chat_file:
                mess = chat_file.readline()
                print(''.join(mess))
        except FileNotFoundError:
            print('Пока ничего нет')
    elif ques == '2':
        new_mess = input('Введите новое сообщение: ')
        with open('chat.txt', 'a') as chat_file:
            chat_file.write(f'{user_name} : {new_mess}\n')
    elif ques == 'stop':
        break
    else:
        print('Ошибка неверный ввод')