# Бот для автоматизации работы в ПК Универсальный механизм (УМ)
Целью проекта является автоматизация процессов выбора парметров при динамическом моделировании вагонов

## Структура проекта
 - get_position.py - скрипт, который определяет положение курсора на экране
 - start_app.py - скрипт для запуска УМ
 - bot_class.py - классы работы бота
 - main_bot.py - основной файлик, где выстроена логика работы бота
 - UM_params - папка с доп файлами для настройки УМ

## Результаты
В результате, написанный бот может самостоятельно рассчитать от 540 расчетов, при дефолтных настройках.
Бот умеет менять скорость, с которой движется вагон, макрогеометрию пути (прямая и кривые разных радиусов),
может менять профили колес, выбирать неисправности на поверхности катания, а также выбирать конфигурацию вагона т.е.
груженый или порожний.

## Окружение
```
pywinauto == 0.6.8
pyautogui == 2.21
loguru == 0.7.0
```
# Важно!
Проект работает на разрешении экрана Full HD и временые интервалы в работе бота установлены с учетом железа ЭВМ.
В конкретном примере процессор Intel Core I7-11800, а версия УМ 9.1.3.6

## Предварительная настройка ПК Универсальный механизм
ПК "Универсальный механизм" можно загрузить по ссылке http://www.umlab.ru/pages/index.php?id=3, после установки и получения лицензии
необходимо создать или загрузить уже готовые файлы конфигурации вагона. В папке `UM_params->Конфигурация вагонов` можно найти две версии полувагона на тележках 18-100,
их необходимо добавить в корневую папку моделей `...\UM Software Lab\Universal Mechanism\9\samples\Rail_Vehicles`, ВАЖНО скопировать полностью папку, а не отдельные файлы.

## Применение бота для автоматизации работы
...
