
Tree menu in Django           


## Приложение для отрисовки меню с помощью templatetag

### Содержание:
+ [Краткое описание](#краткое-описание)
+ [Requirements](#requirements)
+ [Сборка и запуск проекта](#сборка-и-запуск)        




### Краткое описание:
Простое Django приложение для отрисовки древовидного меню, реализованное через templatetag. Меню и его элементы создаются и редактируются в админ панели Django. С помощью тега {% draw_menu 'menu_name' %} меню можно расположить на любой странице приложения.






### Requirements:
+ Django==2.2.7
+ pytz==2019.3
+ sqlparse==0.3.0       




### Сборка и запуск:
! Для корректного отображения меню при запуске следует сначала создать его а так-же добавить в него элементы в админ панели Django.
```bash
git clone git@github.com:iliazhigalev/django-menu.git
cd test_project_1
python3 -m venv djvenv
source .\djvenv\Scripts\activate
pip install -r requirements.txt
cd myproject
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
