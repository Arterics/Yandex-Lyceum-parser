# Парсер Яндекс лицея
Скачивание всех заданий с платформы Яндекс лицей

1. Для работы селениума, вам нужно будет скачать драйвер вашего браузера. 
Подробный гайд установки есть в этом видео ролике: https://www.youtube.com/watch?v=kpNhT1fm1pk
таймкод: 6:26 до 13:31


2. Прописываем данную команду в терминале (файл requirements.txt должен быть в папке с проектом)
pip install all -r requirements.txt

3. Скачиваем файл parser.py и config.py
В конфиге определяем все параметры

4. В 12 строке кода, написано driver = webdriver.Chrome()
Вам нужно вместо Chrome, вписать название вашего браузера (с большой буквы)
В случае, если библиотека говорит, что такого браузера нет или появляется ошибка, установите браузер в списке селениума (например Chrome)

5. Запускаем и ждём окончания!
