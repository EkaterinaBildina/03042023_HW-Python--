def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def add_data() -> None:
    '''Добавляет информацию в справочник'''
    fio = input('Введите ФИО: ')
    tel_num = input('Введите номер тел.: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_num}')


def find_data() -> None:
    '''Осуществляет поиск по справочинкам'''
    find = input('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    result = search(tel_book, find)
    print(result)


def search(book: str, info: str) -> str:
    '''Находит в строке записи по определенному критерию поиска'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])

def delete_data() -> None:
    objects = []
    with open('book.txt', 'r+', encoding='utf-8') as f:
        delete_fio = str(input('Введите ФИО для удаления: '))
        for i in f.readlines():
            #fio = fio(from_line = i)
            objects.append(i)
        print(objects)
        for object in objects:
            if object == delete_fio:
                f.write(object.__str__())



def change_data() -> None:
    '''Ищем по значению все данные из справочника и вносим изменения в нужное'''

    find = input('Введите данные для поиска изменяемого контакта: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    result = search(tel_book, find)
    b = (result)
    print(b)
    
    tel_book = [tel_book]
    b = [b]
    tel_book[tel_book.index(b)] = changing(b)
    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write('\n tel_book')
     
    #with open('book.txt', 'w', encoding='utf-8') as f:
    #    f.write(f'\n{tel_book.index(obj_indx)}')


def changing(text: str) -> str:
    '''Вносит изменения'''
    fio = input(
        'Внесите новые данные ФИО (или Enter - оставить текущие данные): ')
    tel_num = input(
        'Введите новый номер тел (или Enter - оставить текущие данные): ')
    if len(fio) == 0:
        fio = text.split(' | ')[0]
    if len(tel_num) == 0:
        tel_num = text.split(' | ')[1]
    return (f'{fio} | {tel_num}')


