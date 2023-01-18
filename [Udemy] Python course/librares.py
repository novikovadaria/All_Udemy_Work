# .........Path
# import random
import webbrowser
# from pathlib import pathlib
# import sqlite3
# import json
# import csv
# from hashlib import new
# from os import scandir
# from zipfile import ZipFile
# import shutil
# from pathlib import Path

# from isort import place_module_with_reason
# path = Path('C:\\Program Files\\Python 3')
# print(path)

# # Relative path
# path = Path('users/__init__.py')
# print(path)

# # current folder
# path = Path()

# # combining
# path_2 = Path('Some_path')/Path('users')
# print(path_2)
# # combining with a string
# path_2 = Path('Some_path') / 'users'
# print(path_2)

# # Getting home directory
# print(Path.home())

# # Exesting
# path = Path('social/audio')
# path3 = Path('social/images/__init__.py')
# path2 = Path('users')
# print(path.exists())
# print(path2.exists())

# # if is a file
# print(path.is_file())
# print(path2.is_file())

# # if is a directory
# print(path.is_dir())
# print(path2.is_dir())

# # the file name
# print(path.name)
# print(path2.name)

# # the file name ectension
# print(path.suffix)
# print(path2.suffix)

# # parent
# print(path.parent)
# print(path2.parent)

# # file name changed
# path3 = path2.with_name('__init__.txt')
# print(path3)

# # the absolute path
# print(path3.absolute())

# # changing the extension
# print(path3.with_suffix('.js'))

# # ......................Directories...........
# my_directory = Path('real_estate')
# new_directory = Path('social')

# # exists()
# # mkdir()
# # my_directory.mkdir()
# # my_directory.rmdir()

# # rename()
# # my_directory.rename('smt')

# # iterdir()
# print(my_directory.iterdir())
# for data in my_directory.iterdir():
#     print(data)

# # getting only the files
# social_data = [data for data in my_directory.iterdir()]
# print(social_data)

# # is_file()
# path = [data for data in my_directory.iterdir() if data.is_file()]
# print(path)

# # is_dir()
# path = [data for data in my_directory.iterdir() if data.is_dir()]
# print(path)

# # searching (*)
# path = [data for data in my_directory.iterdir() if data.is_dir()]

# python_files = [data for data in my_directory.glob("*.py")]
# print(path)
# print(python_files)

# # rglob()
# python_files = [data for data in my_directory.rglob("*.*")]
# print(python_files)

# # ....................................Files..................
# # exists()
# # rename()
# # unlink() /removing
# # stat() / returns data about the file

# # Opening and closing files
# # read_bytes()
# # read_text()
# # write_bytes() (b'print('Hello from the Sun')')
# # write_text()

# # coping a file to another location

# target_dir = Path('astronomy')
# shutil.copy(my_directory, target_dir)

# # ............................Zip Files..............

# # creating
# all_z = ZipFile('zip_dir/all.zip', 'w')
# py_z = ZipFile('zip_dir/py.zip', 'w')

# # adding files
# for path in Path('socail_media').rglob('*.*'):
#     all_z.write(path)
# all_z.close()

# # .........................CSV Files.............

# # Topic 1
# # opening
# with open('users_info/isers.csv', 'w', newline='') as users_date:
#     CSV_writer_data = csv.writer(users_date)

#     # raw 1
#     CSV_writer_data.writerow(['User Nmae', 'User ID', 'Status'])

#     # raw 2
#     CSV_writer_data.writerow('cool666', 111, 'online')

# # Topic 2
# with open('users_info/users.csv') as users_date:
#     CSV_writer_data = csv.reader(users_date)
#     # print(list(CSV_writer_data))

#     for data_row in CSV_writer_data:
#         print(data_row)

# # ....................JSON Files...................
# l = [1, 2, 3, 4, 5]
# l_d = json.dump(l)
# print(l_d)

# # writing
# Path('ecommerse/products.json').write_text(l_d)

# # reading
# json_data = Path('ecommerse/products.json').read_text()
# print(json_data)
# readable_data = json.loads(json_data)
# print(readable_data)

# # .............................SQLite Database..............

# prod = json.loads(Path('ecommerce/products.json').read_text())

# # writing
# with sqlite3.connect('roducts-db.sqlite3') as connection:
#     command = 'INSERT INTO prod VALUES(?,?,?)'

#     for product in prod:
#         connection.execute(command, tuple(product.values()))

#     connection.commit()

# # reading
# with sqlite3.connect('products-db.sqlite3') as connection:
#     command = 'SELECT * FROM Prod'
#     cursor = connection.execute(command)
#     for data_row in cursor:
#         print(data_row)


# # ......................Randow values............

# # 0 and 1
# print(random.random())

# # two numbers
# print(random.randint(1, 50))

# # randomly choisinig
# # multipli (.choices([], k=n))
# # snuffling a list (snuffle())

# ..........................Workimg with Browser...............
webbrowser.open('https://www.google.com/search?q=cats+photo&oq=cats+photo&aqs=chrome..69i57j0i512l2j0i22i30j0i10i22i30j0i22i30l5.3156j0j15&sourceid=chrome&ie=UTF-8#imgrc=o1DBy1C_tJGHtM')
