from datetime import datetime
import time


class Logwork:
    def __init__(self, path, mode='rt'):
        self.file = open(path, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Я работаю секретарем и мне постоянно приходят различные документы.
# Я должен быть очень внимателен чтобы не потерять ни один документ.
# Каталог документов хранится в следующем виде:


documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
  {"type": "Exception", "number": "1000345", "name": "Еписков первый"}
]

# Перечень полок, на которых находятся документы хранится в следующем виде:
directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

# Необходимо реализовать пользовательские команды,
# которые будут выполнять следующие функции


def people():
  """
  p – people – команда, которая спросит номер документа и выведет имя человека,
   которому он принадлежит;
  """
  marker = 1
  number_doc = input("Введите номер документа :")
  for doc in documents:
    if doc['number'] == number_doc:
      print(doc['name'])
      marker = 0
    else:
      continue
  if marker:
    print(f"Документа {number_doc} не обнаружено")


def listing():
  """
  l– list – команда, которая выведет список всех документов в формате passport
   "2207 876234" "Василий Гупкин"
  """
  print("Все документы: ")
  for doc in documents:
    print(f"{doc['number']} {doc['name']}")


def shelf():
  """
  s – shelf – команда, которая спросит номер документа и выведет номер полки,
   на которой он находится;
  """
  marker = 1
  number_doc = input("Введите номер документа :")
  for directory, docs in directories.items():
    for doc in docs:
      if doc == number_doc:
        print(f"Номер полки {directory}")
        marker = 0
      else:
        continue
  if marker:
    print(f"Документа {number_doc} не обнаружено")


def add():
  """
  a – add – команда, которая добавит новый документ в каталог и в перечень
  полок, спросив его номер, тип, имя владельца и номер полки,
  на котором он будет храниться.
  """
  number = input("Введите номер документа :")
  type_doc = input("Введите тип документа :")
  owner = input("Введите имя владельца :")
  number_shelf = input("Введите номер полки :")
  new_doc = {"type": type_doc, "number": number, "name": owner}
  documents.append(new_doc)
  marker = 1
  for directory, docs in directories.items():
    if directory == number_shelf:
      docs.append(number)
      marker = 0
  if marker:
    directories[number_shelf] = [number]
  print(directories)
  print(documents)


def add_shelf():
  """
  as – add shelf – команда, которая спросит номер новой полки и
  добавит ее в перечень;
  """
  marker = 1
  number_shelf = input("Введите номер номер новой полки :")
  for directory, docs in directories.items():
    if directory == number_shelf:
      marker = 0
  if marker:
    directories[number_shelf]=[]
  else:
    print(f"Полка с номером {number_shelf} уже существует")
  print(directories)


def name_list():
  """
  nl - name list - команда, выводящяя имена всех владельцев документов
  """
  for doc in documents:
    try:
      print(f"{doc['name']}")
    except KeyError:
      pass


def main():
  """
  Ввод команд пользователем
  """
  print("Доступные вам команды:\n l – list – команда, которая выведет список \
  всех документов в формате passport \
   '2207 876234' 'Василий Гупкин'\n p – people – команда, которая спросит \
   номер документа и выведет имя человека, \
   которому он принадлежит\n s – shelf – команда, которая спросит номер \
   документа и выведет номер полки, на которой \
   он находится\n a – add – команда, которая добавит новый документ в каталог \
   и в перечень полок, спросив его номер,\
   тип, имя владельца и номер полки, на котором он будет храниться\n as – \
   add shelf – команда, которая спросит номер \
   новой полки и добавит ее в перечень\n nl - name list - команда, \
   выводящяя имена всех владельцев документов")

  user_command = input("\nВведите вашу команду: ")
  if user_command == "a":
    add()
  elif user_command == "l":
    listing()
  elif user_command == "s":
    shelf()
  elif user_command == "p":
    people()
  elif user_command == "as":
    add_shelf()
  elif user_command == "nl":
    name_list()
  else:
    print("Извините, такой команды не предусмотрено")

# Внимание: p, s, l, a - это пользовательские команды, а не названия функций.
# Функции должны иметь выразительное название, передающие её действие.


with Logwork ("log.txt", "w") as file:
    start_time = datetime.now()
    file.write(f"Время начала работы {start_time}\n")
    print(f"Время начала работы {start_time}\n")
    main()
    print("Трёхсекундная пауза, чтобы было интереснее")
    time.sleep(3)
    stop_time = datetime.now()
    file.write(f"Время окончания работы {stop_time}\n")
    print(f"Время окончания работы {stop_time}\n")
    calc_time = stop_time - start_time
    file.write(f"Общее время работы скрипта {calc_time}\n\n")
    print(f"Общее время работы скрипта {calc_time}\n\n")

