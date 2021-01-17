Тестовое задание
=
Для выполнения тестового задания будут использованы framework aiohttp и БД SQLite3.

## Используемые библиотеки:
+ __aiohttp__ #Framework API
+ __json__ #Разбор формата JSon
+ __sqlite3__ #Для работы с БД
+ __emoji__ #Для кодирования emoji
+ __datetime__ #Для работы и преобразования к единому формату дат
+ __csv__ #Для парсинга и добавления изначальных данных в таблицу
+ __socket__ #Для опеределения своего локального IP
+ __requests__ #Для внесения тестовых данных через PUT метод к серверу

## Структура для проекта:
> 
>> __API__ #Хранилище скриптов для API
> >>    __api_main.py__ #Главный файл для API
>
> >__DB__ #Хранилище скриптов для БД
> > >__db_lite.db__ #База данных. При отсутствии будет создана автоматически
>>
>
> >__TEST__ #Хранилище скриптов для ТЕСТА
>>>__insert.py__ #Скрипт для загрузки тестовых данных в БД
>>
>>>__posts.csv__ #Тестовые данные
>>
>>>__test.py__ #Тест 3 методов в API
>
> >__main.py__  #Файл для инициализации и запуска сервера
>

>


### При отсутствии БД, будет автоматически создана БД, тестовая таблица и индекс на тестовую таблицу.
#### Таблица:
```sql
CREATE TABLE test_table (
    id           INTEGER PRIMARY KEY ON CONFLICT ROLLBACK AUTOINCREMENT
                         UNIQUE ON CONFLICT ROLLBACK
                         NOT NULL,
    rubrics      VARCHAR NOT NULL,
    text         VARCHAR NOT NULL,
    created_date DATE    NOT NULL
                         DEFAULT strftime('%d.%m.%Y %H:%M:%S','now','localtime')
);
```
#### Индекс:
```sql
CREATE UNIQUE INDEX test_index ON test_table (
    id ASC,
    text ASC
);
```
#### Создано два основных класса:
+ Class Aio_app с 4 методами: get, put, delete, start_app.
+ Class DB с 3 методами для работы с базой данных.

#### Для заполнения тестовыми данными из posts.csv, был написан скрипт insert.py с функцией insert_test_csv.
