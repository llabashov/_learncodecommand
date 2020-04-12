"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>    
</body>
</html>



/template/*name*.html
or
/*app*/template/*app*/*templatename*.html

!

{% load static %} - добавление статики (расположение файла css в /*app*/static/css/*name*.css)
<html>
    <head>
        <title>llabashov blogs</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"> - ссылки на bootstrap шаблоны css
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"> - ссылки на bootstrap шаблоны css
        <link rel="stylesheet" href="{% static 'css/blog.css' %}"> - указываем где в статиках у нас css
    </head>
    <body>
        <div>
            <h1><a href="/">llabashov blogs</a></h1>
        </div>
        
        {% for post in posts %}
             <div>
                <p>published: {{ post.published_date }}</p>
                <h1><a href="">{{ post.title }}</a></h1>
                <p>{{ post.text|linebreaksbr }}</p>
            </div>
        {% endfor %}
    </body>
</html>







"""