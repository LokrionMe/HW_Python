# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

from collections import namedtuple

Folder = namedtuple('Folder', ['name', 'parent_directory'])
File = namedtuple('File', ['name', 'expansion', 'parent_directory'])


class Walker:

    def __init__(self) -> None:
        self.list_files = []
        self.list_folders = []

    def __str__(self) -> str:
        f_str = ''
        if self.list_files != []:
            f_str += 'Files:\n'
            for i in self.list_files:
                f_str += str(i) + '\n'
        if self.list_folders != []:
            f_str += 'Folders:\n'
            for i in self.list_folders:
                f_str += str(i) + '\n'
        if self.list_folders == [] and self.list_files == []:
            f_str = 'Empty'
        return f_str

    def search_path(self, path: str):
        import logging
        from os import walk
        logging.basicConfig(level=logging.INFO, filename=f"{path}\py_log.log", filemode="w")
        print(f'Create py_log.log in {path}')
        for root, directs, files in walk(path, topdown=False):
            if files != []:
                for file in files:
                    self.list_files.append(File(file.rsplit('.', 1)[0], file.rsplit(
                        '.', 1)[1], root.rsplit('\\', 1)[1]))
                    logging.info(f"Add file: {file.rsplit('.', 1)[0]}")
            for direct in directs:
                self.list_folders.append(
                    Folder(direct.rsplit('.', 1)[0], root.rsplit('\\', 1)[1]))
                logging.info(f"Add direct: {direct.rsplit('.', 1)[0]}")
        return self

walker = Walker()
print(walker.search_path(input('Input path: ')))
