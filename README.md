# Файл clicks

Данная программа принимает от пользователя ссылку, с помощью API сервиса bitly, сокращает ее, считает клики пользователей по укороченной ссылке, 
далее выводит информацию на экран. Если же пользователь ввел сразу укороченную ссылку, программа только посчитает клики и выведет данную информацию на экран. 
Если же пользователь введет некорректную ссылку, программа напишет об этом.

## shorten_link()

Принимает в качестве аргументов TOKEN и ссылку пользователя. С помощью post запроса обращается к API сервиса bitly и возвращает укороченную ссылку.

## count_clicks()

Принимает в качестве аргументов TOKEN и укороченную ссылку. С помощью get запроса обращается к API сервиса bitly и возвращает количетсво кликов за один день.

## is_bitlink()

Принимает в качестве аргумента ссылку пользователя и осуществляет проверку является ли ссылка пользователя уже сокращенным вариантом bitly или нет. 
Возвращает булевое значение. 

## Переменные среды

В данной программе используется переменная среды `BITLY_TOKEN`. В ней находится токен для подключения к API сервиса bitly. Создайте файл .env и пропишите в него свой токен, вот так: `BITLY_TOKEN=afnroeroinorf13jr94bg3fn`. Файл поместите в папку с проектом. Чтобы создать такой файл вам может понадобиться текстовый редактор. Для Windows это Notepad++, для macOS — CotEditor. 

## Как установить

1. Скачиваем проект из репозитория
1. Устанавливаем менеджер управления зависимостями и виртуальным окружением `pipenv`:  
`$ pip install --user pipenv`
1. Переходим в папку проекта:  
`$ cd project_folder`
1. Запускаем виртуальное окружение:  
`$ pipenv shell`
1. Устанавливаем зависимости из файла `requirements.txt`:  
`pipenv install -r requirements.txt`
1. Запускаем файл:  
`$ clicks.py`

## Пример запуска

![Как выглядит запущенная программа](/image_clicks.jpg)

