# pythonQASelenium

##Набор тестов для проверки opencart

- helpers.py - вспомогательные методы
- test_account_page.py - проверка отображения элементов страницы для регистрации пользователя
- test_admin_login_page.py - проверка формы авторизации администратора
- test_admin_product_page.py - проверка отображения страницы конфигурации продуктов
- test_desktops_page.py - проверка отображения раздела Desktops
- test_login_logout.py - проверка ф-ла корректной/некорректной авторизации
- test_main_page.py - проверка отображения элементов посадочной страницы
- test_product_page.py - проверка отображения элементов страницы с продуктом

##Настройка opencart
Установить переменные среды:
PHPADMIN_PORT - порт для PHPMyAdmin
LOCAL_IP - IP адрес для запуска приложения OpenCart

Для запуска в директории opencart выполнить команду:
`docker-compose up -d`

Для остановки выполнить:
`docker stop $(docker ps -q)`

В случае возникновения ошибок при запуске и т.п. попробовать
выполнить:
`docker prune system --volumes`