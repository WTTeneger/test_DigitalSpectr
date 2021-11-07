# Документация к тестовому заданию
____
## Запуск кода

для запуска кода в папке **_mysite_** нужно выполнить команду (предворительно скачав докер)

```docker-compose build```

и

```docker-compose up```

____

## Основные ссылки

[Страница вывода всей информации](http://localhost/users/) - `http://localhost/users/`

[Страница добавления пользователей](http://localhost/users/add) - `http://localhost/users/add`

[admin панель](http://localhost/admin/) - `http://localhost/admin/` 

login - `root`

password - `pass`

____
## Апи запросы

### запрос на фильтрацию работает через рест апи ссылку
http://localhost/users/api/filter/
которая принимает аргументы такие как
#

####Поиск по майлу
`search_value:str` - принимает email

`http://localhost/users/api/filter/?search_value=asdaw@mail.ru`
#
####Фильтрация
`field:str` - принимает название поля из бд

`to_:str` - принимает направление фильтрации (up, down, none)


`http://localhost/users/api/filter/?field=email&to_=up`
____
###использовались библиотеки:
Django

docker

psycopg2-binary

gunicorn

djangorestframework

markdown

django-filter
____
Логами не обкладовал, есть принты
