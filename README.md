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
Далее необходимо запустить само приложение UM Simulation, в стартовом окне необходимо выбрать предварительно загруженные конфигурации вагонов, это можно сделать следующими шагами:
 1. В левом верхнем углу будет иконка ![Image_alt](https://github.com/daniilgorenkov/UM-Bot/blob/main/images/config_button.png)
 2. Потом необходимо выбрать конфигурацию вагона ![Image_alt](https://github.com/daniilgorenkov/UM-Bot/blob/main/images/loaded_empty.png)
 3. Вы должны будете увидеть предзагруженное стартовое окно ![Image_alt](https://github.com/daniilgorenkov/UM-Bot/blob/main/images/config_view.png)
 4. Далее заходим во вкладку начала интеграции ![Image_alt](https://github.com/daniilgorenkov/UM-Bot/blob/main/images/intergation_button.png)
 5. У вас откроется новое окно, в котором необходимо выбрать следующие вкладки для добавления профилей колес ![Image_alt](https://github.com/daniilgorenkov/UM-Bot/blob/main/images/add_profiles.png)
Все расписанные шаги делаются один раз перед запуском скрипта, для корректной работы бота
### Дополнительная информация по работе с ПК УМ http://www.umlab.ru/download/90/rus/gs_um_loco.pdf и http://www.umlab.ru/download/90/rus/04_um_simulation_program.pdf
## Применение бота для автоматизации работы
Для начала работы бота необходимо будет указать путь до исполняющего файла `umsimul.exe`  в файле `start_app.py`  в функцию `get_model_path()`,
также необходимо выбрать пути сохранения файлов и указать их в конструкторе класса `UM_bot`.
В файле `main_bot` уже выстроена логика работы бота, блок `проверки конфигурации вагона` нужен для того, чтобы бот не пытался при каждой новой итерации выбрать груженый или порожний вагон т.к. для этого необходимо закрывать окно моделирования.
## Дополнительная информация
Этот бот создавался для облегчения сбора результатов экспериментов для выполнения диссертационной работы, поэтому он не оптимален и скорее всего будет дорабатываться со временем и дополняться новыми функциями. Также стоит добавить, что в рамках поставленной задачи мне необходимо считать одну вертикальную силу в системе "колесо-рельс", поэтому если будете считать больше одной силы, то советую изменить функцию `start_integration()`.
