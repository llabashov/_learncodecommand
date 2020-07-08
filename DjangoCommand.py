"""
pip install pylint-django - улучшение анализа кода Django

django-admin startproject *name* - создать проект джанго
python manage.py createsuperuser - создать админа для manage

python manage.py startapp *name* - создать приложение
python manage.py makemigrations *name* - создание миграции
python manage.py migrate - миграция
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




CSS бесплатные шаблоны
Для установки Bootstrap тебе нужно добавить следующие строки в <head> 
твоего .html файла (blog/templates/blog/post_list.html):

blog/templates/blog/post_list.html
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">


"""