def move(N, start, aux, finish):
    if N == 1:
        print('Переложить диск 1 со стержня номер {} на стержень номер {}'.format(start, finish))
        return
    move(N - 1, start, finish, aux)
    print('Переложить диск {num} со стержня номер {st} на стержень номер {end}'.format(num=N,
                                                                                       st=start,
                                                                                       end=finish))
    move(N - 1, aux, start, finish)


number = int(input('Введите кол-во дисков: '))
num_steps = move(number, '1', '2', '3')


