def registration(line):
    bad_file = open('registrations_bad.log', 'a')
    good_file = open('registrations_good.log', 'a')
    try:
        if len(line.split()) < 3:
            raise IndexError
        if line.split()[0].isalpha() == False:
            raise NameError
        if '@' not in line.split()[1] and '.' not in line.split()[1]:
            raise SyntaxError
        if int(line.split()[2]) < 10 and int(line.split()[2]) > 99:
            raise ValueError

    except IndexError:
        string = f'{line[:len(line)-2]}       Строка не содержит 3 составляющие\n'
        bad_file.write(string)
    except NameError:
        string = f'{line[:len(line)-2]}       Поле имя содержит цифры\n'
        bad_file.write(string)
    except SyntaxError:
        string = f'{line[:len(line)-2]}       Поле email введено некорректно\n'
        bad_file.write(string)
    except ValueError:
        string = f'{line[:len(line)-2]}       Возраст находится вне допустимого диапазона (от 10 до 99)\n'
        bad_file.write(string)
    else:
        good_file.write(line)
    finally:
        bad_file.close()
        good_file.close()

with open('registrations.txt', 'r', encoding='utf-8') as bas_user:
    for i_line in bas_user:
        registration(i_line)
