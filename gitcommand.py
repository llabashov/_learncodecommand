"""
#git status - статус гита
#git add . - добавить все в коммиты
#git commit -m "" - комитить с сообщением
#git push - запушить на гитхаб комиты

#git branch - просмотр веток
#git branch --delete name - удалить + название файла который удалить
#git checkout master - перейти в ветку master
#git pull - запулить в локальный репозиторий с гитхаба
#git checkout -b имя-новой-ветки
git push origin --delete имя_ветки - удалить ветку на сервере

#git init - создать репо 
#git clone https://github.com/m0zgen/github-examle.git - клонирование С гитхаба на локалку
#git remote add origin https://github.com/<your-github-username>/<your-github-name-repo>.git - КЛОНИРОВАНИЕ НА РЕПО
#git push -u origin master - запушить клон кода на мастер
#git pull origin master - объеденяем репы
#git push origin master - отправить в гитхаб




#git config --global --list - просмотр данных

git reset имя_файла - отмена git add ДО КОММИТА

git commit --amend - можно рредактировать текст коммита если коммит не запушен
git reset --soft HEAD~1 - сохранить все, что сделали, но отмена последнего коммита
git reset --hard HEAD~1 - полная отмена последнего коммит. HEAD~1 означает один коммит до HEAD, т.е. до текущего положения. 

git branch -a - Клонировать все ветки с сервера


Создать новую ветку на сервере из текущей локальной ветки
git config --global push.default current
git push -u

Отменить все изменения, кроме тех, что уже добавлены в планируемый коммит
git checkout -- .

Перезаписать локальные файлы во время git pull
Вам снова поможет git reset:
git fetch --all
git reset --hard origin/master

Экспортирование исходников аналогично «svn export»
Используйте git archive, например, так:
git archive --format zip --output /путь/к/файлу/файл.zip master

Как разрешать конфликты слияния?
Используйте программу git mergetool, которая предоставляет удобный интерфейс для разрешения конфликтов.

Восстановить удалённый файл
Сначала нужно найти последний коммит, где файл ещё существует:
git rev-list -n 1 HEAD -- имя_файла
Потом восстановить этот файл:
git checkout найденный_коммит^ -- имя_файла

Заставить Git помнить пароль при работе с https
Для запоминания на 15 минут:
git config --global credential.helper cache
Можно настроить и более долгий период:
git config --global credential.helper "cache --timeout=XXXX"
"""