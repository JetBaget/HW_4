Описание
---------
WSGI-совместимый нано веб-фреймворк Otus.

Возможности:
  - роутинг url-адресов к view
  - парсинг запроса
  - доступ к параметрам запроса из view

Установка
---------
Для использования фреймворка необходимо зайти в директорию, куда вы хотите выкачать файлы и выполнить команду:    

         git clone https://github.com/JetBaget/HW_4

После этого вы должны увидеть следующие файлы:
- wsgi_framework/__init__.py
- wsgi_framework/app.py
- wsgi_framework/otus.py
- README.md
- .gitignore

Зависимости
---------
Для запуска файла app.py необходимо, чтобы в системе было установлено приложение uWSGI.
Инструкция по установке uWSGI:
http://uwsgi.readthedocs.io/en/latest/Install.html

Помимо этого в виртуальном окружении проекта должен быть установлен pip-пакет uWSGI.
Для его установки выполните команду:

      pip install uwsgi
        
Быстрый старт:
---------
Перейдите в директорию с проектом.
После создания и активации виртуального окружения с установленным пакетом uWSGI, выполните:

      uwsgi --http :9090 --wsgi-file wsgi_framework/app.py
      
Затем откройте браузер и наберите в адресной строке:

      localhost:9090
      