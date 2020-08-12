"""
pip install pylint-django - улучшение анализа кода Django
pip freeze > requirements.txt - создаст txt документ со всеми установленными и необходимыми программные пакеты
pip install -r requirements.txt - Установка всех пакетов по списку 

django-admin startproject *name* - создать проект джанго
python manage.py createsuperuser - создать админа для manage

python manage.py startapp *name* - создать приложение
python manage.py makemigrations *name* - создание миграции
python manage.py migrate - миграция
python manage.py check - это проверяет наличие каких-либо проблем в ваш проект без выполнения миграций или прикосновения к базе данных.
python manage.py sqlmigrate servisrecruting 0001 - посмотреть миграцию



python manage.py shell - в консоли ORM Django (работ с БД)
Команды БД
a = *name*.objects.all() - привязать к переменной "а" все объекты *name*
a = *name*.objects.filter(id=1) - показать в переменной "а" все объекты *name* с id=1
a = *name*.objects.get(id=2) - привязать к переменной "а" все объекты *name* с id=2
a.id - показать id переменной "а"
a.*name*_set.all() - показать все объекты привязаные (ForingKey привязкой) к *name* (например все комментарии к статье)
a.*name*_set.count() - показать количество 
a.*name*_set.filter( author_name__startswith = "Дж" ) - показать имена авторов статей, имя которых начинаются на "Дж"
a.*name*_set.create ( author_name = "Джек", comment_text = "ZBS" ) - создать запить в БД (в данном случает создать комментарий ZBS автора Джек к статье)
a.delete() - удалить все, что в переменной "а"
a.save() - обновить/сохранить то, что было в переменной "а" в БД
a.objects.get(*slug*__iexact='*slug_name*') - *__exact* убирает чувствительность к регистру.
a.objects.get(*slug*__contains='*slug_name*') - *__contains* - должен содержать 
get - возвращает 1 объект
filter - возвращает querySet



CSS бесплатные шаблоны
Для установки Bootstrap тебе нужно добавить следующие строки в <head> 
твоего .html файла (blog/templates/blog/post_list.html):

blog/templates/blog/post_list.html
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">


CharField - поля для input

"""