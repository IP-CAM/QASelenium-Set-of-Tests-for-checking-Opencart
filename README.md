# pythonqaselenoid

## Tests Set for OpenCart Check
- Helpers.py - Auxiliary Methods
- test_account_page.py - checking the display of page items for user registration
- test_admin_login_page.py - Check Administrator authorization form
- test_admin_product_page.py - checking the display page of the product configuration
- test_desktops_page.py - checking the Desktops section
- test_login_logout.py - Check F-La correct / incorrect authorization
- test_main_page.py - checking the display of elements of the landing page
- test_product_page.py - checking the display of page items with product

## Local launch OpenCart
1. Run the image download` Docker Pull Bitnami / OpenCart`

2. Install environment variables:
- `phpadmin_port` - port for phpmyAdmin
- `Local_IP` - IP address to start the OpenCart application

3. Download file `https: // gist.github.com / konflic / ECD93A4BF7666D97D62BCECBE2713E55`
and execute in the directory with the `docker-compose up -d`

4. To stop running `Docker Stop $ (Docker PS -Q)`

* - in case of errors when starting, etc. Try
Run:
`Docker Prune System --Volumes`

## Local launch selenoid
1. Install Docker
2. Download Actual Configuration Manager with Https resource: // Github.com / Aerokube / CM / Releases / `
3. Download`
4. Run CM: `./cm Selenoid Start --VNC` (Stop to stop)
5. Run SELENOID-UI: `./cm Selenoid-UI Start` (Stop to stop)

## Starting tests
`Pytest --Browser Opera -N 5 --LUREDIR = .. / Allure_results` - Run tests in the Opera browser in 5 threads with data generation for the Allure report.
- `--Browser` - Browser
- `-n` - indication of the number of streams with multithreaded tests
- `--Lelluredir = .. / Allure_results` - directory for allure files

## Report Allure.
1. Load allure `https: // github.com / allure-framework / allure2 / Releases`
2. Put the path to the Allure executable file in environment environment variables
3. After starting the tests indicating `--Lelluredir` and in the directory with allure data files, run` Allure Serve`

---------

# pythonQASelenoid

## Набор тестов для проверки opencart
- helpers.py - вспомогательные методы
- test_account_page.py - проверка отображения элементов страницы для регистрации пользователя
- test_admin_login_page.py - проверка формы авторизации администратора
- test_admin_product_page.py - проверка отображения страницы конфигурации продуктов
- test_desktops_page.py - проверка отображения раздела Desktops
- test_login_logout.py - проверка ф-ла корректной/некорректной авторизации
- test_main_page.py - проверка отображения элементов посадочной страницы
- test_product_page.py - проверка отображения элементов страницы с продуктом

## Локальный запуск opencart
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

## Локальный запуск selenoid
1. Установить Docker
2. Загрузить актуальный Configuration manager с ресурса `https://github.com/aerokube/cm/releases/`
3. Загрузить браузеры `./cm selenoid configure --browsers chrome;firefox;opera` (загрузится последняя и предпоследняя версии браузера)
4. Запустить cm: `./cm selenoid start --vnc`(stop для остановки)
5. Запустить selenoid-ui: `./cm selenoid-ui start`(stop для остановки)

## Запуск тестов
`pytest --browser opera -n 5 --alluredir=../allure_results` - запустить тесты в браузере Opera в 5 потоков с генерацией данных для отчета Allure
- `--browser` - браузер
- `-n` - указание количества потоков при многопоточном выполнении тестов
- `--alluredir=../allure_results` - директория для файлов Allure

## Отчет Allure
1. Загрузить Allure `https://github.com/allure-framework/allure2/releases`
2. Прописать путь к исполняемому файлу allure в переменных среды окружения
3. После запуска тестов с указанием `--alluredir` и в директории с файлами данных Allure запустить `allure serve`
