# Практика 1. Основы работы в командной строке

Работа выполняется в оболочке Bash.  
Запустить linux в браузере можно по данной ссылке: <https://bellard.org/jslinux/>  
Стрелка вверх позволяет напечатать предыдущую команду  
Нажатие TAB допишет имя файла или выведет несколько вариантов, если будет найдено несколько совпадений.  

* Команда **ls** позволяет вывести содержимое каталога
* Команда **dir** позволяет изменить текущий каталог
* Команда **cat** позволяет создавать, объединять, а также выводить содержимое файлов в командной строке или в другом файле
* Команды можно объединять при помощи различных операторов. Например оператор потока PIPE **|** направляет вывод первой команды на вход второй.
* Команда **grep** используется для поиска. Её можно использовать как отдельно, так и в качестве "фильтра" для других команд. Флаг **-o** (--only-matching) позволяет вывести только совпадающие части строки.

```bash
localhost:~# ls
bench.py hello.c hello.js readme.txt
localhost:~# ls | grep 'hello'
hello.c
hello.js
```

* Команда **sort** используется для сортировки по различным параметрам. Например флаг **-n** позволяет сравнивать по числовому значению, флаг **-r** изменить порядок сортировки. Так же можно, например, выбрать второй столбец для сортировки **-k2**. Флаги можно объединять **-nrk2**
* Команда **head** выводит начальные строчки из одного или нескольких документов. По умолчанию выводится первые 10 строк, для изменения кол-ва строк используется флаг **-n**. Вывод первых 7 строк: `head -n 7`
* Команда **awk** даёт доступ к мощному инструментов для обработки и фильтрации текста. Синтаксис можно изучить по данной ссылке:
<https://www.gnu.org/software/gawk/manual/gawk.html> В качестве простого примера, для вывода второго столбца команда будет следующая: `awk '{print $2}'`

## Задание 1. grep, sort

Вывести отсортированный в алфавитном порядке список имен пользователей в файле /etc/passwd  
Вывод должен получиться следующим:

```text
adm
at
bin
cron
cyrus
daemon
dhcp
ftp
games
guest
halt
lp
mail
man
news
nobody
ntp
operator
postmaster
root
shutdown
smmsp
squid
sshd
svn
sync
uucp
vpopmail
xfs
```

Решение:

```bash
cat /etc/passwd | sort | grep -o "^\w*"
```

## Задание 2. sort, head, awk

Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов.  
Вывод должен получиться примерно следующим:

```text
103 pim
98 encap
94 ipip
89 ospf
81 vmtp
```

Решение:

```bash
sort /etc/protocols -nrk2 | head -n 5 | awk '{print $2, $1}'
```
