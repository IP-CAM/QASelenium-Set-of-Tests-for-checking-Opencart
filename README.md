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

##Локальный запуск opencart
1. Выполнить загрузку образа `docker pull bitnami/opencart`

2. Установить переменные среды:
- `PHPADMIN_PORT` - порт для PHPMyAdmin
- `LOCAL_IP` - IP адрес для запуска приложения OpenCart

3. Загрузить файл `https://gist.github.com/konflic/ecd93a4bf7666d97d62bcecbe2713e55`
и выполнить в директории с файлом `docker-compose up -d`

4. Для остановки выполнить `docker stop $(docker ps -q)`

*-В случае возникновения ошибок при запуске и т.п. попробовать
выполнить:
`docker prune system --volumes`

##Локальный запуск selenoid
1. Установить Docker
2. Загрузить актуальный Configuration manager с ресурса `https://github.com/aerokube/cm/releases/`
3. Загрузить браузеры `./cm selenoid configure --browsers chrome;firefox;opera` (загрузится последняя и предпоследняя версии браузера)
4. Запустить cm: `./cm selenoid start --vnc`(stop для остановки)
5. Запустить selenoid-ui: `./cm selenoid-ui start`(stop для остановки)

##Запуск тестов
`pytest --browser opera -n 5` - запустить тесты в браузере Opera в 5 потоков
- `--browser` - браузер
- `-n` - указание количества потоков при многопоточном выполнении тестов
