import sys
import os 
from time import sleep
from bot_class import UM_bot
import keyboard
from start_app import get_model_path, start_app, is_running
from loguru import logger


running = is_running() # Проверка на то была ли программа запущена ранее

if running == True:
    pass

elif running == False:
    PATH = get_model_path() # получение пути до файла umsimul.exe
    start_app(PATH)

sleep(4)

wagons = ["empty","loaded"]
way_type = ["straight", "curve_350", "curve_650"]
faults = ["normal", "polzun15","ellips10"]
profiles = ["newwagonw", "greb_26", "gost","greb_28", "greb_30", "greb_24"]  #CHANGE PROFILE , "greb_26", "gost","greb_28", "greb_30"
speeds = [i for i in range(10,110,10)]   # Поменять скорости так как неравномерный прокат с тонким гребнем сходит в кривой на 110 км/ч

# Подсчет количества файлов результатов в одной папке
l_way_type = len(way_type)
l_faults = len(faults)
l_profiles = len(profiles)
l_speeds = len(speeds)

num_results_folder = l_way_type*l_faults*l_profiles*l_speeds

# Переменные для контроля типа вагона и счетчик выполненных результатов
empty = 0
loaded = 0
general_count = 0

for wagon in range(len(wagons)):                 # прохожусь по всем видам вагонов
    for way in range(len(way_type)):             # прохожусь по всем типам пути
        for fault in range(len(faults)):         # прохожусь по всем видам неисправностей на колесе
            for profile in range(len(profiles)): # прохожусь по всем профилям колес
                for speed in range(len(speeds)): # прохожусь по всем скоростям
                    
                    if keyboard.is_pressed("f5") == True: # если нажата f5, то скрипт прерывается
                        sys.exit(1)

                    # Экземпляр класса
                    helper = UM_bot(wagons[wagon],way_type[way],faults[fault],speeds[speed],profiles[profile])

                    saved_files = len(os.listdir(f"{helper.path_to_save}"))

                    # Проверка есть ли уже выполненные расчеты с такими же именами
                    if_exist = helper.if_result_exist()
                    
                    if if_exist == True:
                        logger.info(f"{helper.name} существует")
                        general_count += 1
                        if general_count == num_results_folder:  # обновление переменной для перехода в новую папку
                            general_count = 0
                        continue

                    elif if_exist == False:
                        logger.info(f"{helper.name} не существует")
                        pass

                    logger.info(f"всего расчетов сделано {general_count}")
                    logger.info(f"расчетов сохранено {saved_files}")

                    if general_count != saved_files:              # Проверка работает ли программа
                        if general_count - saved_files == 1:
                            raise ValueError("Программа не отвечает")
                        
                    
                    
                    # Проверка на конфигурацию вагона

                    if wagons[wagon] == "empty" and empty == 0:
                        if wagons[wagon] == "loaded" and loaded != 0:
                            helper.exit_model_integration()
                            logger.info(f"Выход из моделирования, {wagons[wagon]}")
                            
                        helper.choose_config()
                        logger.info(f"Выбрана конфигурация вагона {wagons[wagon]}")
                        empty += 1
                    
                    elif wagons[wagon] == "empty" and empty != 0:
                        pass

                    elif wagons[wagon] == "loaded" and loaded == 0:
                        if wagons[wagon] == "empty" and empty != 0:
                            helper.exit_model_integration()
                            logger.info(f"Выход из моделирования, {wagons[wagon]}")
                        
                        helper.choose_config()
                        logger.info(f"Выбрана конфигурация вагона {wagons[wagon]}")
                        loaded += 1

                    elif wagons[wagon] == "loaded" and loaded != 0:
                        pass

                    helper.change_speed()            # изменение скорости
                    helper.change_time_integration() # изменение времени интеграции
                    helper.change_way_type()         # изменение типа макрогеометрии
                    helper.change_fault(True)        # изменение неисправностей на поерхности катания
                                                     # True означает, что ползун вновь образованный
                    helper.change_wheel_profile()    # изменение профиля колеса
                    helper.start_integration(0.5,"side")       # начало расчета
                    helper.clear_speed()             # очистка ячейки скорости

                    general_count += 1

print("Расчет окончен")
