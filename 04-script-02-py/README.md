# Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"

## Обязательная задача 1

Есть скрипт:
```python
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b
```

### Вопросы:
| Вопрос  | Ответ                                                                                             |
| ------------- |---------------------------------------------------------------------------------------------------|
| Какое значение будет присвоено переменной `c`?  | `unsupported operand type(s) for +: 'int' and 'str'`, так как переменные `a` и `b` имеют разные типы |
| Как получить для переменной `c` значение 12?  | `c = str(a) + b`                                                                                                 |
| Как получить для переменной `c` значение 3?  | `c = a + int(b)`                                                                                             |

## Обязательная задача 2
Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?

```python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
```

### Ваш скрипт:
```python
#!/usr/bin/env python3

import os

bash_command = ["cd ./", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()

for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)

```

### Вывод скрипта при запуске при тестировании:
```
04-script-01-bash/README.md
```

## Обязательная задача 3
1. Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

### Ваш скрипт:
```python
import os
import sys

import os, sys

gitDir = sys.argv[1]
bash_command = [f'cd {gitDir}', "git status"]
result_os = os.popen(' && '.join(bash_command)).read()

for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(f'{gitDir}/{prepare_result}')

```

### Вывод скрипта при запуске при тестировании:
```

/Users/yakimov/DevOps/HW/yakimov778/netology-hw/03-sysadmin-01-terminal/README.md
/Users/yakimov/DevOps/HW/yakimov778/netology-hw/README.md
```

## Обязательная задача 4
1. Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: `drive.google.com`, `mail.google.com`, `google.com`.

### Ваш скрипт:
```python
import socket
import time

service_addr = {
    'drive.google.com': '0',
    'mail.google.com': '0',
    'google.com': '0'
}

for item in service_addr:
    initial_addr = socket.gethostbyname(item)
    service_addr[item] = initial_addr


while True:
    for item in service_addr:
        old_addr = service_addr[item]
        new_addr = socket.gethostbyname(item)
        if new_addr != old_addr:
            service_addr[item] = new_addr
            print("[ERROR] "+item+" IP mismatch: old IP "+old_addr+", new IP "+new_addr)
        print(item + " - " + service_addr[item])
    print("***")
    time.sleep(5)

```

### Вывод скрипта при запуске при тестировании:
```
/usr/local/bin/python3.10 /Users/yakimov/DevOps/HW/yakimov778/netology-hw/04-script-02-py/script.py 
drive.google.com - 74.125.205.194
mail.google.com - 216.58.209.165
google.com - 216.58.210.174
######################################
drive.google.com - 74.125.205.194
mail.google.com - 216.58.209.165
google.com - 216.58.210.174
######################################
```