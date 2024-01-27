import os
import sys
import shutil



def action():
    #функция выводит главное меню главное меню
    directory = os.getcwd()
    try:
        print('_______________')
        action = int(input('   Действия:\n'
                           '1 - Указать абсолютный путь\n'
                           '2 - Перейти в родительскую директорию\n'
                           '3 - Перейти в папку из текущей директории\n'
                           '4 - Создать папку\n'
                           '5 - Выделить папку или файл\n'
                           '6 - Выход\n'))
        match action:
            case 1:
                while True:
                    directory = input('Укажите директорию: ')
                    if os.path.isdir(directory):
                        get_dir(directory)
                        break
                    else:
                        print('Директория не дуществует, попробуйте еще раз!')
            case 2:
                os.chdir('../')
                get_dir(directory)
            case 3:
                while True:
                    fold = input('Укажите имя папки: ')
                    if os.path.isdir(fold):
                        os.chdir(fold)
                        get_dir(directory)
                        break
                    else:
                        print('Папки нет!')
            case 4:
                while True:
                    new_fold = input('Укажите название новой папки: ')
                    if not os.path.exists(new_fold):
                        os.mkdir(new_fold)
                        get_dir(directory)
                        break
                    else:
                        print(f'Файл с именем "{new_fold}" уже существует! Укажите другое имя!')
            case 5:
                while True:
                    select = input('Укажите имя папки или файла: ')
                    #проверка существования файла/папки
                    if os.path.exists(select):
                        action_select(select)
                        break
                    else:
                        dir = os.getcwd()
                        print(f'Файл с именем "{select}" не существует в директории {dir}')
            case 6:
                sys.exit()
            case _:
                print('Вы указали некорректное число. Попробуйте еще!')
                get_dir(directory)

    except ValueError:
        print('Вы указали недопустимое значение!')
        get_dir(directory)


def action_select(select):
    #функция выводит меню для выделенного файла/папки
    directory = os.getcwd()
    try:
        print('________________')
        print(f'Выделен файл "{select}" в директории {os.getcwd()}')
        print('----------------')
        action = int(input('   Действия:\n'
                           '1 - Удалить\n'
                           '2 - Переместить\n'
                           '3 - Копировать\n'
                           '4 - Выход\n'))
        match action:
            case 1:
                if os.path.isdir(select):
                    os.rmdir(select)
                    print(f'Папка "{select}" удалена!')
                else:
                    os.remove(select)
                    print(f'Файл "{select}" удален!')
                get_dir(directory)
            case 2:
                while True:
                    dst = input(f'Введите путь директории, куда переместить {select}: ')
                    if os.path.isdir(dst):
                        shutil.move(select, dst)
                        get_dir(directory)
                        break
                    else:
                        print('Директории не существует!')
            case 3:
                if os.path.isfile(select):
                    while True:
                        dst = input(f'Введите путь директории, куда скопировать {select}: ')
                        if os.path.isdir(dst):
                            shutil.copy2(select, dst)
                            get_dir(directory)
                            break
                        else:
                            print('Директории не существует!')
                else:
                    print('Скопировать папку нельзя. Только файл.')
                    get_dir(directory)
            case 4:
                get_dir(directory)
            case _:
                print('Вы указали некорректное число. Попробуйте еще!')
                action_select(select)

    except ValueError:
        print('Вы указали недопустимое значение!')
        action_select(select)


def get_dir(dir = os.getcwd()):
    #функция получает текущий путь и
    #вызывает функуию get_files()
    directory = dir
    get_files(directory)
    return directory


def get_files(directory):
    #Функция получает текущий путь и
    #выводит список файлов
    # Выводим текущий путь
    print(f'Текущая директоря: {directory}')
    # Получаем список файлов
    files = os.listdir(directory)
    print('____________________')
    print('   Папки и файлы:   ')
    # Выводим список файлов
    for i in files:
        print(i)
    action()


#запуск программы
if __name__ == '__main__':
    directory = get_dir()